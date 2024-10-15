# SNMP MIB module (ZyXEL-COE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZyXEL-COE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:23:23 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zyxel_ObjectIdentity = ObjectIdentity
zyxel = _Zyxel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1)
)
_Prestige_ObjectIdentity = ObjectIdentity
prestige = _Prestige_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2)
)
_Mtu_ObjectIdentity = ObjectIdentity
mtu = _Mtu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 3)
)
_Aes_100_ObjectIdentity = ObjectIdentity
aes_100 = _Aes_100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 3, 1)
)
_Pes_100_ObjectIdentity = ObjectIdentity
pes_100 = _Pes_100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 3, 2)
)
_Ves_100_ObjectIdentity = ObjectIdentity
ves_100 = _Ves_100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 3, 3)
)
_Shes_100_ObjectIdentity = ObjectIdentity
shes_100 = _Shes_100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 3, 4)
)
_P1600_ObjectIdentity = ObjectIdentity
p1600 = _P1600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 3, 5)
)
_P1400_ObjectIdentity = ObjectIdentity
p1400 = _P1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 3, 6)
)
_P2100_ObjectIdentity = ObjectIdentity
p2100 = _P2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 3, 7)
)
_Aes_100_1_ObjectIdentity = ObjectIdentity
aes_100_1 = _Aes_100_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 3, 8)
)
_Dslam_ObjectIdentity = ObjectIdentity
dslam = _Dslam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 4)
)
_Zysam_1000_ObjectIdentity = ObjectIdentity
zysam_1000 = _Zysam_1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 4, 1)
)
_Zysam_1100_ObjectIdentity = ObjectIdentity
zysam_1100 = _Zysam_1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 4, 2)
)
_Zysam_1200_ObjectIdentity = ObjectIdentity
zysam_1200 = _Zysam_1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 4, 3)
)
_Zysam_2000_ObjectIdentity = ObjectIdentity
zysam_2000 = _Zysam_2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 4, 4)
)
_SystemTraps_ObjectIdentity = ObjectIdentity
systemTraps = _SystemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 999)
)
_ProblemCause_Type = DisplayString
_ProblemCause_Object = MibScalar
problemCause = _ProblemCause_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 999, 1),
    _ProblemCause_Type()
)
problemCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    problemCause.setStatus("mandatory")
_SystemTemperature_Type = DisplayString
_SystemTemperature_Object = MibScalar
systemTemperature = _SystemTemperature_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 999, 2),
    _SystemTemperature_Type()
)
systemTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTemperature.setStatus("mandatory")

# Managed Objects groups


# Notification objects

reboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 0, 1)
)
reboot.setObjects(
    ("ZyXEL-COE-MIB", "problemCause")
)
if mibBuilder.loadTexts:
    reboot.setStatus(
        ""
    )

systemShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 0, 2)
)
systemShutdown.setObjects(
    ("ZyXEL-COE-MIB", "problemCause")
)
if mibBuilder.loadTexts:
    systemShutdown.setStatus(
        ""
    )

overheat = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 0, 3)
)
overheat.setObjects(
    ("ZyXEL-COE-MIB", "systemTemperature")
)
if mibBuilder.loadTexts:
    overheat.setStatus(
        ""
    )

overheatOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 0, 4)
)
overheatOver.setObjects(
    ("ZyXEL-COE-MIB", "systemTemperature")
)
if mibBuilder.loadTexts:
    overheatOver.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZyXEL-COE-MIB",
    **{"DisplayString": DisplayString,
       "zyxel": zyxel,
       "reboot": reboot,
       "systemShutdown": systemShutdown,
       "overheat": overheat,
       "overheatOver": overheatOver,
       "products": products,
       "prestige": prestige,
       "mtu": mtu,
       "aes-100": aes_100,
       "pes-100": pes_100,
       "ves-100": ves_100,
       "shes-100": shes_100,
       "p1600": p1600,
       "p1400": p1400,
       "p2100": p2100,
       "aes-100-1": aes_100_1,
       "dslam": dslam,
       "zysam-1000": zysam_1000,
       "zysam-1100": zysam_1100,
       "zysam-1200": zysam_1200,
       "zysam-2000": zysam_2000,
       "systemTraps": systemTraps,
       "problemCause": problemCause,
       "systemTemperature": systemTemperature}
)
