from datetime import date
from models import *

hardware = TechCategory(
    entries=[
        Tech(
            condensed=False, name="HP(E) Apollo, ProLiant, 9000, and Integrity servers"
        ),
        Tech(condensed=False, name="HP BladeSystem"),
        Tech(condensed=False, name="IBM RS6000/System p/Power servers"),
        Tech(condensed=False, name="Dell servers and disk enclosures"),
    ]
)

operating_systems = TechCategory(
    entries=[
        Tech(condensed=False, name="Red Hat Enterprise Linux (and clones) 3 – 8"),
        Tech(condensed=False, name="Fedora 4 – 35"),
        Tech(condensed=False, name="HP-UX 11.0, 11.11, 11.23, and 11.31"),
        Tech(condensed=False, name="AIX 5L and V6"),
    ]
)

applications = TechCategory(
    entries=[
        Tech(condensed=False, name="PTPv2/IEEE 1588-2008"),
        Tech(condensed=False, name="Chef"),
        Tech(condensed=False, name="Puppet"),
        Tech(condensed=False, name="Foreman"),
        Tech(condensed=False, name="Solarflare OpenOnload"),
        Tech(condensed=False, name="Docker"),
    ]
)


oneup_pos = Job(
    title="Network Administrator",
    dates=[
        DateRange(
            start_date=date(year=2003, month=5, day=1),
            end_date=date(year=2004, month=8, day=1),
        ),
        DateRange(
            start_date=date(year=2005, month=5, day=1),
            end_date=date(year=2005, month=8, day=1),
        ),
    ],
    summary="Administered network equipment and servers for a company providing web presence solutions to small publishing companies.",
    highlights=[
        JobHighlight(
            text="Migrated customer-facing servers from in-office server room to collocation center"
        ),
        JobHighlight(
            text="Overhauled backup systems and strategies to cope with rapidly growing capacity demands"
        ),
    ],
)
oneup = Employer(
    name="1up! Software",
    city_st="Kokomo, IN",
    positions=[
        oneup_pos,
    ],
)

chopper_pos = Job(
    title="Linux Administrator",
    dates=[
        DateRange(
            start_date=date(year=2012, month=6, day=1),
            end_date=date(year=2015, month=2, day=1),
        ),
    ],
    summary="Managed hundreds of Linux servers in a latency-sensitive high frequency trading environment across dozens of geographic locations",
    highlights=[
        JobHighlight(
            text="Implemented Active Directory authentication on Linux machines using pure krb5 and ldap"
        ),
        JobHighlight(
            text="Developed, tested, and implemented sub-millisecond time synchronization across geographically- distant data centers"
        ),
    ],
)
chopper = Employer(
    name="Chopper Trading",
    city_st="Chicago, IL",
    positions=[
        chopper_pos,
    ],
)

purdue = Degree(
    college="Purdue University",
    city_st="West Lafayette, IN",
    dates=[
        DateRange(
            start_date=date(year=2004, month=8, day=1),
            end_date=date(year=2007, month=5, day=1),
        ),
    ],
    major="Psychology",
    degree="Bachelor of Arts",
)

course1 = Course(
    name="HP BladeSystem Administration course", date=date(year=2012, month=1, day=1)
)
course2 = Course(
    name="VERITAS NetBackup 6.5 Fundamentals course",
    date=date(year=2008, month=11, day=1),
)
course3 = Course(
    name="Red Hat Enterprise Clustering and Storage Management course",
    date=date(year=2008, month=10, day=1),
)


resume = Resume(
    hardware=hardware,
    operating_systems=operating_systems,
    applications=applications,
    experience=[oneup, chopper],
    courses=[course1, course2, course3],
    education=[
        purdue,
    ],
)

resume.yaml()