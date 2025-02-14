# SNMP MIB module (ASTARO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASTARO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:53 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

astaro = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9789)
)
astaro.setRevisions(
        ("2016-05-06 00:00",
         "2008-12-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Notification_ObjectIdentity = ObjectIdentity
notification = _Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9789, 1500)
)
_Debug_ObjectIdentity = ObjectIdentity
debug = _Debug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 0)
)
_Info_ObjectIdentity = ObjectIdentity
info = _Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1)
)
_Warn_ObjectIdentity = ObjectIdentity
warn = _Warn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2)
)
_Crit_ObjectIdentity = ObjectIdentity
crit = _Crit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 3)
)
_NotificationGroup_ObjectIdentity = ObjectIdentity
notificationGroup = _NotificationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9789, 1501)
)

# Managed Objects groups


# Notification objects

sophosUTMNotificationINFO000 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 0)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO000.setStatus(
        "current"
    )

sophosUTMNotificationINFO005 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 5)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO005.setStatus(
        "current"
    )

sophosUTMNotificationINFO006 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 6)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO006.setStatus(
        "current"
    )

sophosUTMNotificationINFO007 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 7)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO007.setStatus(
        "current"
    )

sophosUTMNotificationINFO010 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 10)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO010.setStatus(
        "current"
    )

sophosUTMNotificationINFO011 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 11)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO011.setStatus(
        "current"
    )

sophosUTMNotificationINFO020 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 20)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO020.setStatus(
        "current"
    )

sophosUTMNotificationINFO021 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 21)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO021.setStatus(
        "current"
    )

sophosUTMNotificationINFO022 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 22)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO022.setStatus(
        "current"
    )

sophosUTMNotificationINFO040 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 40)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO040.setStatus(
        "current"
    )

sophosUTMNotificationINFO050 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 50)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO050.setStatus(
        "current"
    )

sophosUTMNotificationINFO051 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 51)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO051.setStatus(
        "current"
    )

sophosUTMNotificationINFO053 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 53)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO053.setStatus(
        "current"
    )

sophosUTMNotificationINFO062 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 62)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO062.setStatus(
        "current"
    )

sophosUTMNotificationINFO063 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 63)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO063.setStatus(
        "current"
    )

sophosUTMNotificationINFO065 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 65)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO065.setStatus(
        "current"
    )

sophosUTMNotificationINFO080 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 80)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO080.setStatus(
        "current"
    )

sophosUTMNotificationINFO081 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 81)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO081.setStatus(
        "current"
    )

sophosUTMNotificationINFO083 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 83)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO083.setStatus(
        "current"
    )

sophosUTMNotificationINFO090 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 90)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO090.setStatus(
        "current"
    )

sophosUTMNotificationINFO091 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 91)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO091.setStatus(
        "current"
    )

sophosUTMNotificationINFO092 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 92)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO092.setStatus(
        "current"
    )

sophosUTMNotificationINFO093 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 93)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO093.setStatus(
        "current"
    )

sophosUTMNotificationINFO094 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 94)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO094.setStatus(
        "current"
    )

sophosUTMNotificationINFO095 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 95)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO095.setStatus(
        "current"
    )

sophosUTMNotificationINFO105 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 105)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO105.setStatus(
        "current"
    )

sophosUTMNotificationINFO106 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 106)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO106.setStatus(
        "current"
    )

sophosUTMNotificationINFO107 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 107)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO107.setStatus(
        "current"
    )

sophosUTMNotificationINFO108 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 108)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO108.setStatus(
        "current"
    )

sophosUTMNotificationINFO109 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 109)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO109.setStatus(
        "current"
    )

sophosUTMNotificationINFO110 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 110)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO110.setStatus(
        "current"
    )

sophosUTMNotificationINFO111 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 111)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO111.setStatus(
        "current"
    )

sophosUTMNotificationINFO112 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 112)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO112.setStatus(
        "current"
    )

sophosUTMNotificationINFO114 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 114)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO114.setStatus(
        "current"
    )

sophosUTMNotificationINFO115 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 115)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO115.setStatus(
        "current"
    )

sophosUTMNotificationINFO116 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 116)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO116.setStatus(
        "current"
    )

sophosUTMNotificationINFO117 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 117)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO117.setStatus(
        "current"
    )

sophosUTMNotificationINFO118 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 118)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO118.setStatus(
        "current"
    )

sophosUTMNotificationINFO119 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 119)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO119.setStatus(
        "current"
    )

sophosUTMNotificationINFO120 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 120)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO120.setStatus(
        "current"
    )

sophosUTMNotificationINFO121 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 121)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO121.setStatus(
        "current"
    )

sophosUTMNotificationINFO122 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 122)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO122.setStatus(
        "current"
    )

sophosUTMNotificationINFO123 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 123)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO123.setStatus(
        "current"
    )

sophosUTMNotificationINFO124 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 124)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO124.setStatus(
        "current"
    )

sophosUTMNotificationINFO125 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 125)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO125.setStatus(
        "current"
    )

sophosUTMNotificationINFO126 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 126)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO126.setStatus(
        "current"
    )

sophosUTMNotificationINFO127 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 127)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO127.setStatus(
        "current"
    )

sophosUTMNotificationINFO128 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 128)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO128.setStatus(
        "current"
    )

sophosUTMNotificationINFO129 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 129)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO129.setStatus(
        "current"
    )

sophosUTMNotificationINFO130 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 130)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO130.setStatus(
        "current"
    )

sophosUTMNotificationINFO131 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 131)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO131.setStatus(
        "current"
    )

sophosUTMNotificationINFO132 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 132)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO132.setStatus(
        "current"
    )

sophosUTMNotificationINFO133 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 133)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO133.setStatus(
        "current"
    )

sophosUTMNotificationINFO134 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 134)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO134.setStatus(
        "current"
    )

sophosUTMNotificationINFO135 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 135)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO135.setStatus(
        "current"
    )

sophosUTMNotificationINFO136 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 136)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO136.setStatus(
        "current"
    )

sophosUTMNotificationINFO138 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 138)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO138.setStatus(
        "current"
    )

sophosUTMNotificationINFO139 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 139)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO139.setStatus(
        "current"
    )

sophosUTMNotificationINFO140 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 140)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO140.setStatus(
        "current"
    )

sophosUTMNotificationINFO141 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 141)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO141.setStatus(
        "current"
    )

sophosUTMNotificationINFO142 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 142)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO142.setStatus(
        "current"
    )

sophosUTMNotificationINFO143 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 143)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO143.setStatus(
        "current"
    )

sophosUTMNotificationINFO144 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 144)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO144.setStatus(
        "current"
    )

sophosUTMNotificationINFO145 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 145)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO145.setStatus(
        "current"
    )

sophosUTMNotificationINFO146 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 146)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO146.setStatus(
        "current"
    )

sophosUTMNotificationINFO147 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 147)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO147.setStatus(
        "current"
    )

sophosUTMNotificationINFO148 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 148)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO148.setStatus(
        "current"
    )

sophosUTMNotificationINFO149 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 149)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO149.setStatus(
        "current"
    )

sophosUTMNotificationINFO150 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 150)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO150.setStatus(
        "current"
    )

sophosUTMNotificationINFO152 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 152)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO152.setStatus(
        "current"
    )

sophosUTMNotificationINFO153 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 153)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO153.setStatus(
        "current"
    )

sophosUTMNotificationINFO154 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 154)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO154.setStatus(
        "current"
    )

sophosUTMNotificationINFO163 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 163)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO163.setStatus(
        "current"
    )

sophosUTMNotificationINFO164 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 164)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO164.setStatus(
        "current"
    )

sophosUTMNotificationINFO170 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 170)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO170.setStatus(
        "current"
    )

sophosUTMNotificationINFO171 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 171)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO171.setStatus(
        "current"
    )

sophosUTMNotificationINFO172 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 172)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO172.setStatus(
        "current"
    )

sophosUTMNotificationINFO173 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 173)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO173.setStatus(
        "current"
    )

sophosUTMNotificationINFO175 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 175)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO175.setStatus(
        "current"
    )

sophosUTMNotificationINFO176 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 176)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO176.setStatus(
        "current"
    )

sophosUTMNotificationINFO177 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 177)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO177.setStatus(
        "current"
    )

sophosUTMNotificationINFO178 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 178)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO178.setStatus(
        "current"
    )

sophosUTMNotificationINFO179 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 179)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO179.setStatus(
        "current"
    )

sophosUTMNotificationINFO180 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 180)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO180.setStatus(
        "current"
    )

sophosUTMNotificationINFO181 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 181)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO181.setStatus(
        "current"
    )

sophosUTMNotificationINFO182 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 182)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO182.setStatus(
        "current"
    )

sophosUTMNotificationINFO183 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 183)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO183.setStatus(
        "current"
    )

sophosUTMNotificationINFO184 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 184)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO184.setStatus(
        "current"
    )

sophosUTMNotificationINFO185 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 185)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO185.setStatus(
        "current"
    )

sophosUTMNotificationINFO186 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 186)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO186.setStatus(
        "current"
    )

sophosUTMNotificationINFO187 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 187)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO187.setStatus(
        "current"
    )

sophosUTMNotificationINFO188 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 188)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO188.setStatus(
        "current"
    )

sophosUTMNotificationINFO189 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 189)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO189.setStatus(
        "current"
    )

sophosUTMNotificationINFO190 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 190)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO190.setStatus(
        "current"
    )

sophosUTMNotificationINFO191 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 191)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO191.setStatus(
        "current"
    )

sophosUTMNotificationINFO192 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 192)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO192.setStatus(
        "current"
    )

sophosUTMNotificationINFO193 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 193)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO193.setStatus(
        "current"
    )

sophosUTMNotificationINFO301 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 301)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO301.setStatus(
        "current"
    )

sophosUTMNotificationINFO302 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 302)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO302.setStatus(
        "current"
    )

sophosUTMNotificationINFO306 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 306)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO306.setStatus(
        "current"
    )

sophosUTMNotificationINFO310 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 310)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO310.setStatus(
        "current"
    )

sophosUTMNotificationINFO320 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 320)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO320.setStatus(
        "current"
    )

sophosUTMNotificationINFO321 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 321)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO321.setStatus(
        "current"
    )

sophosUTMNotificationINFO322 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 322)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO322.setStatus(
        "current"
    )

sophosUTMNotificationINFO601 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 601)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO601.setStatus(
        "current"
    )

sophosUTMNotificationINFO700 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 700)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO700.setStatus(
        "current"
    )

sophosUTMNotificationINFO710 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 710)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO710.setStatus(
        "current"
    )

sophosUTMNotificationINFO720 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 720)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO720.setStatus(
        "current"
    )

sophosUTMNotificationINFO721 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 721)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO721.setStatus(
        "current"
    )

sophosUTMNotificationINFO722 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 722)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO722.setStatus(
        "current"
    )

sophosUTMNotificationINFO723 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 723)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO723.setStatus(
        "current"
    )

sophosUTMNotificationINFO724 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 724)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO724.setStatus(
        "current"
    )

sophosUTMNotificationINFO725 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 725)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO725.setStatus(
        "current"
    )

sophosUTMNotificationINFO726 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 726)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO726.setStatus(
        "current"
    )

sophosUTMNotificationINFO727 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 727)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO727.setStatus(
        "current"
    )

sophosUTMNotificationINFO728 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 728)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO728.setStatus(
        "current"
    )

sophosUTMNotificationINFO729 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 729)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO729.setStatus(
        "current"
    )

sophosUTMNotificationINFO850 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 850)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO850.setStatus(
        "current"
    )

sophosUTMNotificationINFO852 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 1, 852)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationINFO852.setStatus(
        "current"
    )

sophosUTMNotificationWARN005 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 5)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN005.setStatus(
        "current"
    )

sophosUTMNotificationWARN006 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 6)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN006.setStatus(
        "current"
    )

sophosUTMNotificationWARN007 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 7)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN007.setStatus(
        "current"
    )

sophosUTMNotificationWARN025 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 25)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN025.setStatus(
        "current"
    )

sophosUTMNotificationWARN030 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 30)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN030.setStatus(
        "current"
    )

sophosUTMNotificationWARN031 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 31)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN031.setStatus(
        "current"
    )

sophosUTMNotificationWARN032 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 32)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN032.setStatus(
        "current"
    )

sophosUTMNotificationWARN033 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 33)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN033.setStatus(
        "current"
    )

sophosUTMNotificationWARN040 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 40)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN040.setStatus(
        "current"
    )

sophosUTMNotificationWARN052 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 52)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN052.setStatus(
        "current"
    )

sophosUTMNotificationWARN061 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 61)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN061.setStatus(
        "current"
    )

sophosUTMNotificationWARN070 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 70)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN070.setStatus(
        "current"
    )

sophosUTMNotificationWARN080 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 80)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN080.setStatus(
        "current"
    )

sophosUTMNotificationWARN090 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 90)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN090.setStatus(
        "current"
    )

sophosUTMNotificationWARN094 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 94)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN094.setStatus(
        "current"
    )

sophosUTMNotificationWARN129 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 129)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN129.setStatus(
        "current"
    )

sophosUTMNotificationWARN136 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 136)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN136.setStatus(
        "current"
    )

sophosUTMNotificationWARN160 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 160)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN160.setStatus(
        "current"
    )

sophosUTMNotificationWARN161 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 161)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN161.setStatus(
        "current"
    )

sophosUTMNotificationWARN162 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 162)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN162.setStatus(
        "current"
    )

sophosUTMNotificationWARN201 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 201)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN201.setStatus(
        "current"
    )

sophosUTMNotificationWARN501 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 501)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN501.setStatus(
        "current"
    )

sophosUTMNotificationWARN531 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 531)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN531.setStatus(
        "current"
    )

sophosUTMNotificationWARN711 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 711)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN711.setStatus(
        "current"
    )

sophosUTMNotificationWARN715 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 715)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN715.setStatus(
        "current"
    )

sophosUTMNotificationWARN726 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 726)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN726.setStatus(
        "current"
    )

sophosUTMNotificationWARN727 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 727)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN727.setStatus(
        "current"
    )

sophosUTMNotificationWARN728 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 728)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN728.setStatus(
        "current"
    )

sophosUTMNotificationWARN729 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 729)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN729.setStatus(
        "current"
    )

sophosUTMNotificationWARN850 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 850)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN850.setStatus(
        "current"
    )

sophosUTMNotificationWARN852 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 852)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN852.setStatus(
        "current"
    )

sophosUTMNotificationWARN856 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 2, 856)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationWARN856.setStatus(
        "current"
    )

sophosUTMNotificationCRIT025 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 3, 25)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationCRIT025.setStatus(
        "current"
    )

sophosUTMNotificationCRIT026 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 3, 26)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationCRIT026.setStatus(
        "current"
    )

sophosUTMNotificationCRIT027 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 3, 27)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationCRIT027.setStatus(
        "current"
    )

sophosUTMNotificationCRIT028 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 3, 28)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationCRIT028.setStatus(
        "current"
    )

sophosUTMNotificationCRIT054 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 3, 54)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationCRIT054.setStatus(
        "current"
    )

sophosUTMNotificationCRIT060 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 3, 60)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationCRIT060.setStatus(
        "current"
    )

sophosUTMNotificationCRIT065 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 3, 65)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationCRIT065.setStatus(
        "current"
    )

sophosUTMNotificationCRIT080 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 3, 80)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationCRIT080.setStatus(
        "current"
    )

sophosUTMNotificationCRIT081 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 3, 81)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationCRIT081.setStatus(
        "current"
    )

sophosUTMNotificationCRIT082 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 3, 82)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationCRIT082.setStatus(
        "current"
    )

sophosUTMNotificationCRIT090 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 3, 90)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationCRIT090.setStatus(
        "current"
    )

sophosUTMNotificationCRIT091 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 3, 91)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationCRIT091.setStatus(
        "current"
    )

sophosUTMNotificationCRIT092 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 3, 92)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationCRIT092.setStatus(
        "current"
    )

sophosUTMNotificationCRIT310 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 3, 310)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationCRIT310.setStatus(
        "current"
    )

sophosUTMNotificationCRIT311 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 3, 311)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationCRIT311.setStatus(
        "current"
    )

sophosUTMNotificationCRIT712 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 3, 712)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationCRIT712.setStatus(
        "current"
    )

sophosUTMNotificationCRIT850 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 3, 850)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationCRIT850.setStatus(
        "current"
    )

sophosUTMNotificationCRIT852 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 3, 852)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationCRIT852.setStatus(
        "current"
    )

sophosUTMNotificationCRIT861 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9789, 1500, 3, 861)
)
if mibBuilder.loadTexts:
    sophosUTMNotificationCRIT861.setStatus(
        "current"
    )


# Notifications groups

sophosUTMNotificationsBASE = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9789, 1501, 0)
)
sophosUTMNotificationsBASE.setObjects(
      *(("ASTARO-MIB", "sophosUTMNotificationCRIT025"),
        ("ASTARO-MIB", "sophosUTMNotificationCRIT026"),
        ("ASTARO-MIB", "sophosUTMNotificationCRIT054"),
        ("ASTARO-MIB", "sophosUTMNotificationCRIT060"),
        ("ASTARO-MIB", "sophosUTMNotificationCRIT065"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO000"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO005"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO006"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO007"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO010"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO011"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO020"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO021"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO022"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO040"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO050"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO051"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO053"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO062"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO063"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO065"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO094"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO095"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO601"),
        ("ASTARO-MIB", "sophosUTMNotificationWARN005"),
        ("ASTARO-MIB", "sophosUTMNotificationWARN006"),
        ("ASTARO-MIB", "sophosUTMNotificationWARN007"),
        ("ASTARO-MIB", "sophosUTMNotificationWARN025"),
        ("ASTARO-MIB", "sophosUTMNotificationWARN030"),
        ("ASTARO-MIB", "sophosUTMNotificationWARN031"),
        ("ASTARO-MIB", "sophosUTMNotificationWARN032"),
        ("ASTARO-MIB", "sophosUTMNotificationWARN033"),
        ("ASTARO-MIB", "sophosUTMNotificationWARN040"),
        ("ASTARO-MIB", "sophosUTMNotificationWARN052"),
        ("ASTARO-MIB", "sophosUTMNotificationWARN061"),
        ("ASTARO-MIB", "sophosUTMNotificationWARN070"),
        ("ASTARO-MIB", "sophosUTMNotificationWARN094"),
        ("ASTARO-MIB", "sophosUTMNotificationWARN136"),
        ("ASTARO-MIB", "sophosUTMNotificationWARN201"),
        ("ASTARO-MIB", "sophosUTMNotificationWARN531"))
)
if mibBuilder.loadTexts:
    sophosUTMNotificationsBASE.setStatus(
        "current"
    )

sophosUTMNotificationsSELFMON = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9789, 1501, 1)
)
sophosUTMNotificationsSELFMON.setObjects(
      *(("ASTARO-MIB", "sophosUTMNotificationINFO105"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO106"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO107"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO108"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO109"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO110"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO111"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO112"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO114"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO115"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO116"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO117"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO118"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO119"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO120"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO121"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO122"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO123"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO124"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO125"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO126"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO127"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO128"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO129"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO130"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO131"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO132"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO133"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO134"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO135"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO136"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO138"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO139"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO140"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO141"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO142"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO143"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO144"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO145"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO146"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO147"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO148"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO149"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO150"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO152"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO153"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO154"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO163"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO164"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO170"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO171"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO172"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO173"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO175"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO176"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO177"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO178"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO179"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO180"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO181"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO182"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO183"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO184"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO185"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO186"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO187"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO188"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO189"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO190"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO191"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO192"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO193"),
        ("ASTARO-MIB", "sophosUTMNotificationWARN129"),
        ("ASTARO-MIB", "sophosUTMNotificationWARN160"),
        ("ASTARO-MIB", "sophosUTMNotificationWARN161"),
        ("ASTARO-MIB", "sophosUTMNotificationWARN162"))
)
if mibBuilder.loadTexts:
    sophosUTMNotificationsSELFMON.setStatus(
        "current"
    )

sophosUTMNotificationsUP2DATE = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9789, 1501, 2)
)
sophosUTMNotificationsUP2DATE.setObjects(
      *(("ASTARO-MIB", "sophosUTMNotificationCRIT310"),
        ("ASTARO-MIB", "sophosUTMNotificationCRIT311"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO301"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO302"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO306"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO310"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO320"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO321"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO322"))
)
if mibBuilder.loadTexts:
    sophosUTMNotificationsUP2DATE.setStatus(
        "current"
    )

sophosUTMNotificationsREPORTING = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9789, 1501, 4)
)
sophosUTMNotificationsREPORTING.setObjects(
      *(("ASTARO-MIB", "sophosUTMNotificationCRIT712"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO700"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO710"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO720"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO721"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO722"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO723"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO724"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO725"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO726"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO727"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO728"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO729"),
        ("ASTARO-MIB", "sophosUTMNotificationWARN711"),
        ("ASTARO-MIB", "sophosUTMNotificationWARN715"),
        ("ASTARO-MIB", "sophosUTMNotificationWARN726"),
        ("ASTARO-MIB", "sophosUTMNotificationWARN727"),
        ("ASTARO-MIB", "sophosUTMNotificationWARN728"),
        ("ASTARO-MIB", "sophosUTMNotificationWARN729"))
)
if mibBuilder.loadTexts:
    sophosUTMNotificationsREPORTING.setStatus(
        "current"
    )

sophosUTMNotificationsIPS = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9789, 1501, 5)
)
sophosUTMNotificationsIPS.setObjects(
      *(("ASTARO-MIB", "sophosUTMNotificationCRIT850"),
        ("ASTARO-MIB", "sophosUTMNotificationCRIT852"),
        ("ASTARO-MIB", "sophosUTMNotificationCRIT861"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO850"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO852"),
        ("ASTARO-MIB", "sophosUTMNotificationWARN850"),
        ("ASTARO-MIB", "sophosUTMNotificationWARN852"),
        ("ASTARO-MIB", "sophosUTMNotificationWARN856"))
)
if mibBuilder.loadTexts:
    sophosUTMNotificationsIPS.setStatus(
        "current"
    )

sophosUTMNotificationsHA = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9789, 1501, 6)
)
sophosUTMNotificationsHA.setObjects(
      *(("ASTARO-MIB", "sophosUTMNotificationCRIT027"),
        ("ASTARO-MIB", "sophosUTMNotificationCRIT028"),
        ("ASTARO-MIB", "sophosUTMNotificationCRIT080"),
        ("ASTARO-MIB", "sophosUTMNotificationCRIT081"),
        ("ASTARO-MIB", "sophosUTMNotificationCRIT082"),
        ("ASTARO-MIB", "sophosUTMNotificationCRIT090"),
        ("ASTARO-MIB", "sophosUTMNotificationCRIT091"),
        ("ASTARO-MIB", "sophosUTMNotificationCRIT092"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO080"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO081"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO083"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO090"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO091"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO092"),
        ("ASTARO-MIB", "sophosUTMNotificationINFO093"),
        ("ASTARO-MIB", "sophosUTMNotificationWARN080"),
        ("ASTARO-MIB", "sophosUTMNotificationWARN090"))
)
if mibBuilder.loadTexts:
    sophosUTMNotificationsHA.setStatus(
        "current"
    )

sophosUTMNotificationsEPP = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9789, 1501, 7)
)
sophosUTMNotificationsEPP.setObjects(
    ("ASTARO-MIB", "sophosUTMNotificationWARN501")
)
if mibBuilder.loadTexts:
    sophosUTMNotificationsEPP.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASTARO-MIB",
    **{"astaro": astaro,
       "notification": notification,
       "debug": debug,
       "info": info,
       "sophosUTMNotificationINFO000": sophosUTMNotificationINFO000,
       "sophosUTMNotificationINFO005": sophosUTMNotificationINFO005,
       "sophosUTMNotificationINFO006": sophosUTMNotificationINFO006,
       "sophosUTMNotificationINFO007": sophosUTMNotificationINFO007,
       "sophosUTMNotificationINFO010": sophosUTMNotificationINFO010,
       "sophosUTMNotificationINFO011": sophosUTMNotificationINFO011,
       "sophosUTMNotificationINFO020": sophosUTMNotificationINFO020,
       "sophosUTMNotificationINFO021": sophosUTMNotificationINFO021,
       "sophosUTMNotificationINFO022": sophosUTMNotificationINFO022,
       "sophosUTMNotificationINFO040": sophosUTMNotificationINFO040,
       "sophosUTMNotificationINFO050": sophosUTMNotificationINFO050,
       "sophosUTMNotificationINFO051": sophosUTMNotificationINFO051,
       "sophosUTMNotificationINFO053": sophosUTMNotificationINFO053,
       "sophosUTMNotificationINFO062": sophosUTMNotificationINFO062,
       "sophosUTMNotificationINFO063": sophosUTMNotificationINFO063,
       "sophosUTMNotificationINFO065": sophosUTMNotificationINFO065,
       "sophosUTMNotificationINFO080": sophosUTMNotificationINFO080,
       "sophosUTMNotificationINFO081": sophosUTMNotificationINFO081,
       "sophosUTMNotificationINFO083": sophosUTMNotificationINFO083,
       "sophosUTMNotificationINFO090": sophosUTMNotificationINFO090,
       "sophosUTMNotificationINFO091": sophosUTMNotificationINFO091,
       "sophosUTMNotificationINFO092": sophosUTMNotificationINFO092,
       "sophosUTMNotificationINFO093": sophosUTMNotificationINFO093,
       "sophosUTMNotificationINFO094": sophosUTMNotificationINFO094,
       "sophosUTMNotificationINFO095": sophosUTMNotificationINFO095,
       "sophosUTMNotificationINFO105": sophosUTMNotificationINFO105,
       "sophosUTMNotificationINFO106": sophosUTMNotificationINFO106,
       "sophosUTMNotificationINFO107": sophosUTMNotificationINFO107,
       "sophosUTMNotificationINFO108": sophosUTMNotificationINFO108,
       "sophosUTMNotificationINFO109": sophosUTMNotificationINFO109,
       "sophosUTMNotificationINFO110": sophosUTMNotificationINFO110,
       "sophosUTMNotificationINFO111": sophosUTMNotificationINFO111,
       "sophosUTMNotificationINFO112": sophosUTMNotificationINFO112,
       "sophosUTMNotificationINFO114": sophosUTMNotificationINFO114,
       "sophosUTMNotificationINFO115": sophosUTMNotificationINFO115,
       "sophosUTMNotificationINFO116": sophosUTMNotificationINFO116,
       "sophosUTMNotificationINFO117": sophosUTMNotificationINFO117,
       "sophosUTMNotificationINFO118": sophosUTMNotificationINFO118,
       "sophosUTMNotificationINFO119": sophosUTMNotificationINFO119,
       "sophosUTMNotificationINFO120": sophosUTMNotificationINFO120,
       "sophosUTMNotificationINFO121": sophosUTMNotificationINFO121,
       "sophosUTMNotificationINFO122": sophosUTMNotificationINFO122,
       "sophosUTMNotificationINFO123": sophosUTMNotificationINFO123,
       "sophosUTMNotificationINFO124": sophosUTMNotificationINFO124,
       "sophosUTMNotificationINFO125": sophosUTMNotificationINFO125,
       "sophosUTMNotificationINFO126": sophosUTMNotificationINFO126,
       "sophosUTMNotificationINFO127": sophosUTMNotificationINFO127,
       "sophosUTMNotificationINFO128": sophosUTMNotificationINFO128,
       "sophosUTMNotificationINFO129": sophosUTMNotificationINFO129,
       "sophosUTMNotificationINFO130": sophosUTMNotificationINFO130,
       "sophosUTMNotificationINFO131": sophosUTMNotificationINFO131,
       "sophosUTMNotificationINFO132": sophosUTMNotificationINFO132,
       "sophosUTMNotificationINFO133": sophosUTMNotificationINFO133,
       "sophosUTMNotificationINFO134": sophosUTMNotificationINFO134,
       "sophosUTMNotificationINFO135": sophosUTMNotificationINFO135,
       "sophosUTMNotificationINFO136": sophosUTMNotificationINFO136,
       "sophosUTMNotificationINFO138": sophosUTMNotificationINFO138,
       "sophosUTMNotificationINFO139": sophosUTMNotificationINFO139,
       "sophosUTMNotificationINFO140": sophosUTMNotificationINFO140,
       "sophosUTMNotificationINFO141": sophosUTMNotificationINFO141,
       "sophosUTMNotificationINFO142": sophosUTMNotificationINFO142,
       "sophosUTMNotificationINFO143": sophosUTMNotificationINFO143,
       "sophosUTMNotificationINFO144": sophosUTMNotificationINFO144,
       "sophosUTMNotificationINFO145": sophosUTMNotificationINFO145,
       "sophosUTMNotificationINFO146": sophosUTMNotificationINFO146,
       "sophosUTMNotificationINFO147": sophosUTMNotificationINFO147,
       "sophosUTMNotificationINFO148": sophosUTMNotificationINFO148,
       "sophosUTMNotificationINFO149": sophosUTMNotificationINFO149,
       "sophosUTMNotificationINFO150": sophosUTMNotificationINFO150,
       "sophosUTMNotificationINFO152": sophosUTMNotificationINFO152,
       "sophosUTMNotificationINFO153": sophosUTMNotificationINFO153,
       "sophosUTMNotificationINFO154": sophosUTMNotificationINFO154,
       "sophosUTMNotificationINFO163": sophosUTMNotificationINFO163,
       "sophosUTMNotificationINFO164": sophosUTMNotificationINFO164,
       "sophosUTMNotificationINFO170": sophosUTMNotificationINFO170,
       "sophosUTMNotificationINFO171": sophosUTMNotificationINFO171,
       "sophosUTMNotificationINFO172": sophosUTMNotificationINFO172,
       "sophosUTMNotificationINFO173": sophosUTMNotificationINFO173,
       "sophosUTMNotificationINFO175": sophosUTMNotificationINFO175,
       "sophosUTMNotificationINFO176": sophosUTMNotificationINFO176,
       "sophosUTMNotificationINFO177": sophosUTMNotificationINFO177,
       "sophosUTMNotificationINFO178": sophosUTMNotificationINFO178,
       "sophosUTMNotificationINFO179": sophosUTMNotificationINFO179,
       "sophosUTMNotificationINFO180": sophosUTMNotificationINFO180,
       "sophosUTMNotificationINFO181": sophosUTMNotificationINFO181,
       "sophosUTMNotificationINFO182": sophosUTMNotificationINFO182,
       "sophosUTMNotificationINFO183": sophosUTMNotificationINFO183,
       "sophosUTMNotificationINFO184": sophosUTMNotificationINFO184,
       "sophosUTMNotificationINFO185": sophosUTMNotificationINFO185,
       "sophosUTMNotificationINFO186": sophosUTMNotificationINFO186,
       "sophosUTMNotificationINFO187": sophosUTMNotificationINFO187,
       "sophosUTMNotificationINFO188": sophosUTMNotificationINFO188,
       "sophosUTMNotificationINFO189": sophosUTMNotificationINFO189,
       "sophosUTMNotificationINFO190": sophosUTMNotificationINFO190,
       "sophosUTMNotificationINFO191": sophosUTMNotificationINFO191,
       "sophosUTMNotificationINFO192": sophosUTMNotificationINFO192,
       "sophosUTMNotificationINFO193": sophosUTMNotificationINFO193,
       "sophosUTMNotificationINFO301": sophosUTMNotificationINFO301,
       "sophosUTMNotificationINFO302": sophosUTMNotificationINFO302,
       "sophosUTMNotificationINFO306": sophosUTMNotificationINFO306,
       "sophosUTMNotificationINFO310": sophosUTMNotificationINFO310,
       "sophosUTMNotificationINFO320": sophosUTMNotificationINFO320,
       "sophosUTMNotificationINFO321": sophosUTMNotificationINFO321,
       "sophosUTMNotificationINFO322": sophosUTMNotificationINFO322,
       "sophosUTMNotificationINFO601": sophosUTMNotificationINFO601,
       "sophosUTMNotificationINFO700": sophosUTMNotificationINFO700,
       "sophosUTMNotificationINFO710": sophosUTMNotificationINFO710,
       "sophosUTMNotificationINFO720": sophosUTMNotificationINFO720,
       "sophosUTMNotificationINFO721": sophosUTMNotificationINFO721,
       "sophosUTMNotificationINFO722": sophosUTMNotificationINFO722,
       "sophosUTMNotificationINFO723": sophosUTMNotificationINFO723,
       "sophosUTMNotificationINFO724": sophosUTMNotificationINFO724,
       "sophosUTMNotificationINFO725": sophosUTMNotificationINFO725,
       "sophosUTMNotificationINFO726": sophosUTMNotificationINFO726,
       "sophosUTMNotificationINFO727": sophosUTMNotificationINFO727,
       "sophosUTMNotificationINFO728": sophosUTMNotificationINFO728,
       "sophosUTMNotificationINFO729": sophosUTMNotificationINFO729,
       "sophosUTMNotificationINFO850": sophosUTMNotificationINFO850,
       "sophosUTMNotificationINFO852": sophosUTMNotificationINFO852,
       "warn": warn,
       "sophosUTMNotificationWARN005": sophosUTMNotificationWARN005,
       "sophosUTMNotificationWARN006": sophosUTMNotificationWARN006,
       "sophosUTMNotificationWARN007": sophosUTMNotificationWARN007,
       "sophosUTMNotificationWARN025": sophosUTMNotificationWARN025,
       "sophosUTMNotificationWARN030": sophosUTMNotificationWARN030,
       "sophosUTMNotificationWARN031": sophosUTMNotificationWARN031,
       "sophosUTMNotificationWARN032": sophosUTMNotificationWARN032,
       "sophosUTMNotificationWARN033": sophosUTMNotificationWARN033,
       "sophosUTMNotificationWARN040": sophosUTMNotificationWARN040,
       "sophosUTMNotificationWARN052": sophosUTMNotificationWARN052,
       "sophosUTMNotificationWARN061": sophosUTMNotificationWARN061,
       "sophosUTMNotificationWARN070": sophosUTMNotificationWARN070,
       "sophosUTMNotificationWARN080": sophosUTMNotificationWARN080,
       "sophosUTMNotificationWARN090": sophosUTMNotificationWARN090,
       "sophosUTMNotificationWARN094": sophosUTMNotificationWARN094,
       "sophosUTMNotificationWARN129": sophosUTMNotificationWARN129,
       "sophosUTMNotificationWARN136": sophosUTMNotificationWARN136,
       "sophosUTMNotificationWARN160": sophosUTMNotificationWARN160,
       "sophosUTMNotificationWARN161": sophosUTMNotificationWARN161,
       "sophosUTMNotificationWARN162": sophosUTMNotificationWARN162,
       "sophosUTMNotificationWARN201": sophosUTMNotificationWARN201,
       "sophosUTMNotificationWARN501": sophosUTMNotificationWARN501,
       "sophosUTMNotificationWARN531": sophosUTMNotificationWARN531,
       "sophosUTMNotificationWARN711": sophosUTMNotificationWARN711,
       "sophosUTMNotificationWARN715": sophosUTMNotificationWARN715,
       "sophosUTMNotificationWARN726": sophosUTMNotificationWARN726,
       "sophosUTMNotificationWARN727": sophosUTMNotificationWARN727,
       "sophosUTMNotificationWARN728": sophosUTMNotificationWARN728,
       "sophosUTMNotificationWARN729": sophosUTMNotificationWARN729,
       "sophosUTMNotificationWARN850": sophosUTMNotificationWARN850,
       "sophosUTMNotificationWARN852": sophosUTMNotificationWARN852,
       "sophosUTMNotificationWARN856": sophosUTMNotificationWARN856,
       "crit": crit,
       "sophosUTMNotificationCRIT025": sophosUTMNotificationCRIT025,
       "sophosUTMNotificationCRIT026": sophosUTMNotificationCRIT026,
       "sophosUTMNotificationCRIT027": sophosUTMNotificationCRIT027,
       "sophosUTMNotificationCRIT028": sophosUTMNotificationCRIT028,
       "sophosUTMNotificationCRIT054": sophosUTMNotificationCRIT054,
       "sophosUTMNotificationCRIT060": sophosUTMNotificationCRIT060,
       "sophosUTMNotificationCRIT065": sophosUTMNotificationCRIT065,
       "sophosUTMNotificationCRIT080": sophosUTMNotificationCRIT080,
       "sophosUTMNotificationCRIT081": sophosUTMNotificationCRIT081,
       "sophosUTMNotificationCRIT082": sophosUTMNotificationCRIT082,
       "sophosUTMNotificationCRIT090": sophosUTMNotificationCRIT090,
       "sophosUTMNotificationCRIT091": sophosUTMNotificationCRIT091,
       "sophosUTMNotificationCRIT092": sophosUTMNotificationCRIT092,
       "sophosUTMNotificationCRIT310": sophosUTMNotificationCRIT310,
       "sophosUTMNotificationCRIT311": sophosUTMNotificationCRIT311,
       "sophosUTMNotificationCRIT712": sophosUTMNotificationCRIT712,
       "sophosUTMNotificationCRIT850": sophosUTMNotificationCRIT850,
       "sophosUTMNotificationCRIT852": sophosUTMNotificationCRIT852,
       "sophosUTMNotificationCRIT861": sophosUTMNotificationCRIT861,
       "notificationGroup": notificationGroup,
       "sophosUTMNotificationsBASE": sophosUTMNotificationsBASE,
       "sophosUTMNotificationsSELFMON": sophosUTMNotificationsSELFMON,
       "sophosUTMNotificationsUP2DATE": sophosUTMNotificationsUP2DATE,
       "sophosUTMNotificationsREPORTING": sophosUTMNotificationsREPORTING,
       "sophosUTMNotificationsIPS": sophosUTMNotificationsIPS,
       "sophosUTMNotificationsHA": sophosUTMNotificationsHA,
       "sophosUTMNotificationsEPP": sophosUTMNotificationsEPP}
)
