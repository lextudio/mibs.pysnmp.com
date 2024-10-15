# SNMP MIB module (FORTINET-FORTISWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FORTINET-FORTISWITCH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:35 2024
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

(fnSysSerial,
 fortinet) = mibBuilder.importSymbols(
    "FORTINET-CORE-MIB",
    "fnSysSerial",
    "fortinet")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

fnFortiSwitchMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106)
)
fnFortiSwitchMib.setRevisions(
        ("2011-09-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsModel_ObjectIdentity = ObjectIdentity
fsModel = _FsModel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 1)
)
_FsTraps_ObjectIdentity = ObjectIdentity
fsTraps = _FsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2)
)
_FsTrapPrefix_ObjectIdentity = ObjectIdentity
fsTrapPrefix = _FsTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 0)
)
_FsTrunkMemPrefix_ObjectIdentity = ObjectIdentity
fsTrunkMemPrefix = _FsTrunkMemPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 3)
)


class _FsTrunkMember_Type(DisplayString):
    """Custom type fsTrunkMember based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 82),
    )


_FsTrunkMember_Type.__name__ = "DisplayString"
_FsTrunkMember_Object = MibScalar
fsTrunkMember = _FsTrunkMember_Object(
    (1, 3, 6, 1, 4, 1, 12356, 106, 3, 1),
    _FsTrunkMember_Type()
)
fsTrunkMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTrunkMember.setStatus("current")
_FsSystem_ObjectIdentity = ObjectIdentity
fsSystem = _FsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 4)
)
_FsSystemInfo_ObjectIdentity = ObjectIdentity
fsSystemInfo = _FsSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 4, 1)
)


class _FsSysVersion_Type(DisplayString):
    """Custom type fsSysVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FsSysVersion_Type.__name__ = "DisplayString"
_FsSysVersion_Object = MibScalar
fsSysVersion = _FsSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 106, 4, 1, 1),
    _FsSysVersion_Type()
)
fsSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSysVersion.setStatus("current")


class _FsSysCpuUsage_Type(Gauge32):
    """Custom type fsSysCpuUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsSysCpuUsage_Type.__name__ = "Gauge32"
_FsSysCpuUsage_Object = MibScalar
fsSysCpuUsage = _FsSysCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 106, 4, 1, 2),
    _FsSysCpuUsage_Type()
)
fsSysCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSysCpuUsage.setStatus("current")
_FsSysMemUsage_Type = Gauge32
_FsSysMemUsage_Object = MibScalar
fsSysMemUsage = _FsSysMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 106, 4, 1, 3),
    _FsSysMemUsage_Type()
)
fsSysMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSysMemUsage.setStatus("current")
_FsSysMemCapacity_Type = Gauge32
_FsSysMemCapacity_Object = MibScalar
fsSysMemCapacity = _FsSysMemCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 106, 4, 1, 4),
    _FsSysMemCapacity_Type()
)
fsSysMemCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSysMemCapacity.setStatus("current")
_FsSysDiskUsage_Type = Gauge32
_FsSysDiskUsage_Object = MibScalar
fsSysDiskUsage = _FsSysDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 106, 4, 1, 5),
    _FsSysDiskUsage_Type()
)
fsSysDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSysDiskUsage.setStatus("current")
_FsSysDiskCapacity_Type = Gauge32
_FsSysDiskCapacity_Object = MibScalar
fsSysDiskCapacity = _FsSysDiskCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 106, 4, 1, 6),
    _FsSysDiskCapacity_Type()
)
fsSysDiskCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSysDiskCapacity.setStatus("current")
_FsSoftware_ObjectIdentity = ObjectIdentity
fsSoftware = _FsSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 4, 2)
)


class _FsDirverVersion_Type(DisplayString):
    """Custom type fsDirverVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FsDirverVersion_Type.__name__ = "DisplayString"
_FsDirverVersion_Object = MibScalar
fsDirverVersion = _FsDirverVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 106, 4, 2, 1),
    _FsDirverVersion_Type()
)
fsDirverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDirverVersion.setStatus("current")
_FsMibConformance_ObjectIdentity = ObjectIdentity
fsMibConformance = _FsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 100)
)

# Managed Objects groups

fsSystemObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 106, 100, 2)
)
fsSystemObjectGroup.setObjects(
      *(("FORTINET-FORTISWITCH-MIB", "fsSysVersion"),
        ("FORTINET-FORTISWITCH-MIB", "fsSysCpuUsage"),
        ("FORTINET-FORTISWITCH-MIB", "fsSysMemUsage"),
        ("FORTINET-FORTISWITCH-MIB", "fsSysMemCapacity"),
        ("FORTINET-FORTISWITCH-MIB", "fsSysDiskUsage"),
        ("FORTINET-FORTISWITCH-MIB", "fsSysDiskCapacity"),
        ("FORTINET-FORTISWITCH-MIB", "fsDirverVersion"))
)
if mibBuilder.loadTexts:
    fsSystemObjectGroup.setStatus("current")

fsTrunkObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 106, 100, 3)
)
fsTrunkObjectGroup.setObjects(
    ("FORTINET-FORTISWITCH-MIB", "fsTrunkMember")
)
if mibBuilder.loadTexts:
    fsTrunkObjectGroup.setStatus("current")


# Notification objects

fsTrapHBFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 0, 701)
)
fsTrapHBFail.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTISWITCH-MIB", "fsTrunkMember"))
)
if mibBuilder.loadTexts:
    fsTrapHBFail.setStatus(
        "current"
    )

fsTrapHBReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 0, 702)
)
fsTrapHBReceived.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTISWITCH-MIB", "fsTrunkMember"))
)
if mibBuilder.loadTexts:
    fsTrapHBReceived.setStatus(
        "current"
    )

fsTrapMemberDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 0, 703)
)
fsTrapMemberDown.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTISWITCH-MIB", "fsTrunkMember"))
)
if mibBuilder.loadTexts:
    fsTrapMemberDown.setStatus(
        "current"
    )

fsTrapMemberUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 0, 704)
)
fsTrapMemberUp.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTISWITCH-MIB", "fsTrunkMember"))
)
if mibBuilder.loadTexts:
    fsTrapMemberUp.setStatus(
        "current"
    )


# Notifications groups

fsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12356, 106, 100, 1)
)
fsNotificationGroup.setObjects(
      *(("FORTINET-FORTISWITCH-MIB", "fsTrapHBFail"),
        ("FORTINET-FORTISWITCH-MIB", "fsTrapHBReceived"),
        ("FORTINET-FORTISWITCH-MIB", "fsTrapMemberDown"),
        ("FORTINET-FORTISWITCH-MIB", "fsTrapMemberUp"))
)
if mibBuilder.loadTexts:
    fsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12356, 106, 100, 100)
)
if mibBuilder.loadTexts:
    fsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORTINET-FORTISWITCH-MIB",
    **{"fnFortiSwitchMib": fnFortiSwitchMib,
       "fsModel": fsModel,
       "fsTraps": fsTraps,
       "fsTrapPrefix": fsTrapPrefix,
       "fsTrapHBFail": fsTrapHBFail,
       "fsTrapHBReceived": fsTrapHBReceived,
       "fsTrapMemberDown": fsTrapMemberDown,
       "fsTrapMemberUp": fsTrapMemberUp,
       "fsTrunkMemPrefix": fsTrunkMemPrefix,
       "fsTrunkMember": fsTrunkMember,
       "fsSystem": fsSystem,
       "fsSystemInfo": fsSystemInfo,
       "fsSysVersion": fsSysVersion,
       "fsSysCpuUsage": fsSysCpuUsage,
       "fsSysMemUsage": fsSysMemUsage,
       "fsSysMemCapacity": fsSysMemCapacity,
       "fsSysDiskUsage": fsSysDiskUsage,
       "fsSysDiskCapacity": fsSysDiskCapacity,
       "fsSoftware": fsSoftware,
       "fsDirverVersion": fsDirverVersion,
       "fsMibConformance": fsMibConformance,
       "fsNotificationGroup": fsNotificationGroup,
       "fsSystemObjectGroup": fsSystemObjectGroup,
       "fsTrunkObjectGroup": fsTrunkObjectGroup,
       "fsMIBCompliance": fsMIBCompliance}
)
