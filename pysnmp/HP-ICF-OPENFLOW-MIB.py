# SNMP MIB module (HP-ICF-OPENFLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-OPENFLOW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:54 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(VidList,) = mibBuilder.importSymbols(
    "HP-ICF-TC",
    "VidList")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfOpenFlowMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89)
)
hpicfOpenFlowMIB.setRevisions(
        ("2017-07-16 00:00",
         "2017-06-18 00:00",
         "2017-04-28 00:00",
         "2016-10-25 00:00",
         "2016-10-05 00:00",
         "2016-08-06 00:00",
         "2016-07-31 00:00",
         "2016-04-21 00:00",
         "2015-12-10 00:00",
         "2015-09-29 00:00",
         "2015-01-11 00:00",
         "2014-06-04 00:00",
         "2012-10-01 00:00",
         "2012-02-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfOpenFlowNotifications_ObjectIdentity = ObjectIdentity
hpicfOpenFlowNotifications = _HpicfOpenFlowNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 0)
)
_HpicfOpenFlowObjects_ObjectIdentity = ObjectIdentity
hpicfOpenFlowObjects = _HpicfOpenFlowObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1)
)


class _HpicfOpenFlowStatus_Type(Integer32):
    """Custom type hpicfOpenFlowStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("disableWithClearConfig", 3),
          ("enable", 1))
    )


_HpicfOpenFlowStatus_Type.__name__ = "Integer32"
_HpicfOpenFlowStatus_Object = MibScalar
hpicfOpenFlowStatus = _HpicfOpenFlowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 1),
    _HpicfOpenFlowStatus_Type()
)
hpicfOpenFlowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOpenFlowStatus.setStatus("current")
_HpicfOpenFlowInstanceTable_Object = MibTable
hpicfOpenFlowInstanceTable = _HpicfOpenFlowInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceTable.setStatus("current")
_HpicfOpenFlowInstanceEntry_Object = MibTableRow
hpicfOpenFlowInstanceEntry = _HpicfOpenFlowInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1)
)
hpicfOpenFlowInstanceEntry.setIndexNames(
    (0, "HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceName"),
)
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceEntry.setStatus("current")


class _HpicfOpenFlowInstanceName_Type(SnmpAdminString):
    """Custom type hpicfOpenFlowInstanceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpicfOpenFlowInstanceName_Type.__name__ = "SnmpAdminString"
_HpicfOpenFlowInstanceName_Object = MibTableColumn
hpicfOpenFlowInstanceName = _HpicfOpenFlowInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 1),
    _HpicfOpenFlowInstanceName_Type()
)
hpicfOpenFlowInstanceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceName.setStatus("current")


class _HpicfOpenFlowInstanceAdminStatus_Type(Integer32):
    """Custom type hpicfOpenFlowInstanceAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HpicfOpenFlowInstanceAdminStatus_Type.__name__ = "Integer32"
_HpicfOpenFlowInstanceAdminStatus_Object = MibTableColumn
hpicfOpenFlowInstanceAdminStatus = _HpicfOpenFlowInstanceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 2),
    _HpicfOpenFlowInstanceAdminStatus_Type()
)
hpicfOpenFlowInstanceAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceAdminStatus.setStatus("current")


class _HpicfOpenFlowInstanceListenPortCfg_Type(TruthValue):
    """Custom type hpicfOpenFlowInstanceListenPortCfg based on TruthValue"""


_HpicfOpenFlowInstanceListenPortCfg_Object = MibTableColumn
hpicfOpenFlowInstanceListenPortCfg = _HpicfOpenFlowInstanceListenPortCfg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 3),
    _HpicfOpenFlowInstanceListenPortCfg_Type()
)
hpicfOpenFlowInstanceListenPortCfg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceListenPortCfg.setStatus("current")


class _HpicfOpenFlowInstanceListenPort_Type(InetPortNumber):
    """Custom type hpicfOpenFlowInstanceListenPort based on InetPortNumber"""
    defaultValue = 6633


_HpicfOpenFlowInstanceListenPort_Object = MibTableColumn
hpicfOpenFlowInstanceListenPort = _HpicfOpenFlowInstanceListenPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 4),
    _HpicfOpenFlowInstanceListenPort_Type()
)
hpicfOpenFlowInstanceListenPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceListenPort.setStatus("current")


class _HpicfOpenFlowInstanceListenPortIsOobm_Type(TruthValue):
    """Custom type hpicfOpenFlowInstanceListenPortIsOobm based on TruthValue"""


_HpicfOpenFlowInstanceListenPortIsOobm_Object = MibTableColumn
hpicfOpenFlowInstanceListenPortIsOobm = _HpicfOpenFlowInstanceListenPortIsOobm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 5),
    _HpicfOpenFlowInstanceListenPortIsOobm_Type()
)
hpicfOpenFlowInstanceListenPortIsOobm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceListenPortIsOobm.setStatus("current")


class _HpicfOpenFlowInstanceMode_Type(Integer32):
    """Custom type hpicfOpenFlowInstanceMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_HpicfOpenFlowInstanceMode_Type.__name__ = "Integer32"
_HpicfOpenFlowInstanceMode_Object = MibTableColumn
hpicfOpenFlowInstanceMode = _HpicfOpenFlowInstanceMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 6),
    _HpicfOpenFlowInstanceMode_Type()
)
hpicfOpenFlowInstanceMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceMode.setStatus("current")


class _HpicfOpenFlowInstanceFlowLocationMode_Type(Integer32):
    """Custom type hpicfOpenFlowInstanceFlowLocationMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardwareAndSoftware", 2),
          ("hardwareOnly", 1))
    )


_HpicfOpenFlowInstanceFlowLocationMode_Type.__name__ = "Integer32"
_HpicfOpenFlowInstanceFlowLocationMode_Object = MibTableColumn
hpicfOpenFlowInstanceFlowLocationMode = _HpicfOpenFlowInstanceFlowLocationMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 7),
    _HpicfOpenFlowInstanceFlowLocationMode_Type()
)
hpicfOpenFlowInstanceFlowLocationMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceFlowLocationMode.setStatus("current")


class _HpicfOpenFlowConnectionInterruptionMode_Type(Integer32):
    """Custom type hpicfOpenFlowConnectionInterruptionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failSecure", 1),
          ("failStandalone", 2))
    )


_HpicfOpenFlowConnectionInterruptionMode_Type.__name__ = "Integer32"
_HpicfOpenFlowConnectionInterruptionMode_Object = MibTableColumn
hpicfOpenFlowConnectionInterruptionMode = _HpicfOpenFlowConnectionInterruptionMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 8),
    _HpicfOpenFlowConnectionInterruptionMode_Type()
)
hpicfOpenFlowConnectionInterruptionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOpenFlowConnectionInterruptionMode.setStatus("current")
_HpicfOpenFlowInstanceHwRateLimit_Type = Integer32
_HpicfOpenFlowInstanceHwRateLimit_Object = MibTableColumn
hpicfOpenFlowInstanceHwRateLimit = _HpicfOpenFlowInstanceHwRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 9),
    _HpicfOpenFlowInstanceHwRateLimit_Type()
)
hpicfOpenFlowInstanceHwRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceHwRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceHwRateLimit.setUnits("kilobits per second")


class _HpicfOpenFlowInstanceSwRateLimit_Type(Integer32):
    """Custom type hpicfOpenFlowInstanceSwRateLimit based on Integer32"""
    defaultValue = 100


_HpicfOpenFlowInstanceSwRateLimit_Object = MibTableColumn
hpicfOpenFlowInstanceSwRateLimit = _HpicfOpenFlowInstanceSwRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 10),
    _HpicfOpenFlowInstanceSwRateLimit_Type()
)
hpicfOpenFlowInstanceSwRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceSwRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceSwRateLimit.setUnits("packets per second")
_HpicfOpenFlowInstanceDatapathID_Type = Counter64
_HpicfOpenFlowInstanceDatapathID_Object = MibTableColumn
hpicfOpenFlowInstanceDatapathID = _HpicfOpenFlowInstanceDatapathID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 11),
    _HpicfOpenFlowInstanceDatapathID_Type()
)
hpicfOpenFlowInstanceDatapathID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceDatapathID.setStatus("current")
_HpicfOpenFlowInstanceNumOfHwFlows_Type = Counter64
_HpicfOpenFlowInstanceNumOfHwFlows_Object = MibTableColumn
hpicfOpenFlowInstanceNumOfHwFlows = _HpicfOpenFlowInstanceNumOfHwFlows_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 12),
    _HpicfOpenFlowInstanceNumOfHwFlows_Type()
)
hpicfOpenFlowInstanceNumOfHwFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceNumOfHwFlows.setStatus("current")
_HpicfOpenFlowInstanceNumOfSwFlows_Type = Counter64
_HpicfOpenFlowInstanceNumOfSwFlows_Object = MibTableColumn
hpicfOpenFlowInstanceNumOfSwFlows = _HpicfOpenFlowInstanceNumOfSwFlows_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 13),
    _HpicfOpenFlowInstanceNumOfSwFlows_Type()
)
hpicfOpenFlowInstanceNumOfSwFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceNumOfSwFlows.setStatus("current")


class _HpicfOpenFlowInstanceOperStatus_Type(Integer32):
    """Custom type hpicfOpenFlowInstanceOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_HpicfOpenFlowInstanceOperStatus_Type.__name__ = "Integer32"
_HpicfOpenFlowInstanceOperStatus_Object = MibTableColumn
hpicfOpenFlowInstanceOperStatus = _HpicfOpenFlowInstanceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 14),
    _HpicfOpenFlowInstanceOperStatus_Type()
)
hpicfOpenFlowInstanceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceOperStatus.setStatus("current")


class _HpicfOpenFlowInstanceMaxBackOffInterval_Type(Unsigned32):
    """Custom type hpicfOpenFlowInstanceMaxBackOffInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_HpicfOpenFlowInstanceMaxBackOffInterval_Type.__name__ = "Unsigned32"
_HpicfOpenFlowInstanceMaxBackOffInterval_Object = MibTableColumn
hpicfOpenFlowInstanceMaxBackOffInterval = _HpicfOpenFlowInstanceMaxBackOffInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 15),
    _HpicfOpenFlowInstanceMaxBackOffInterval_Type()
)
hpicfOpenFlowInstanceMaxBackOffInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceMaxBackOffInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceMaxBackOffInterval.setUnits("seconds")
_HpicfOpenFlowInstanceRowStatus_Type = RowStatus
_HpicfOpenFlowInstanceRowStatus_Object = MibTableColumn
hpicfOpenFlowInstanceRowStatus = _HpicfOpenFlowInstanceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 16),
    _HpicfOpenFlowInstanceRowStatus_Type()
)
hpicfOpenFlowInstanceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceRowStatus.setStatus("current")


class _HpicfOpenFlowInstanceProbeInterval_Type(Unsigned32):
    """Custom type hpicfOpenFlowInstanceProbeInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_HpicfOpenFlowInstanceProbeInterval_Type.__name__ = "Unsigned32"
_HpicfOpenFlowInstanceProbeInterval_Object = MibTableColumn
hpicfOpenFlowInstanceProbeInterval = _HpicfOpenFlowInstanceProbeInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 17),
    _HpicfOpenFlowInstanceProbeInterval_Type()
)
hpicfOpenFlowInstanceProbeInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceProbeInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceProbeInterval.setUnits("seconds")


class _HpicfOpenFlowInstanceProtoVersion_Type(Integer32):
    """Custom type hpicfOpenFlowInstanceProtoVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1dot0", 1),
          ("v1dot3", 2))
    )


_HpicfOpenFlowInstanceProtoVersion_Type.__name__ = "Integer32"
_HpicfOpenFlowInstanceProtoVersion_Object = MibTableColumn
hpicfOpenFlowInstanceProtoVersion = _HpicfOpenFlowInstanceProtoVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 18),
    _HpicfOpenFlowInstanceProtoVersion_Type()
)
hpicfOpenFlowInstanceProtoVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceProtoVersion.setStatus("current")


class _HpicfOpenFlowInstanceProtoVersionOnly_Type(TruthValue):
    """Custom type hpicfOpenFlowInstanceProtoVersionOnly based on TruthValue"""


_HpicfOpenFlowInstanceProtoVersionOnly_Object = MibTableColumn
hpicfOpenFlowInstanceProtoVersionOnly = _HpicfOpenFlowInstanceProtoVersionOnly_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 19),
    _HpicfOpenFlowInstanceProtoVersionOnly_Type()
)
hpicfOpenFlowInstanceProtoVersionOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceProtoVersionOnly.setStatus("current")


class _HpicfOpenFlowInstanceNumOfSwFlowTable_Type(Unsigned32):
    """Custom type hpicfOpenFlowInstanceNumOfSwFlowTable based on Unsigned32"""
    defaultValue = 1


_HpicfOpenFlowInstanceNumOfSwFlowTable_Object = MibTableColumn
hpicfOpenFlowInstanceNumOfSwFlowTable = _HpicfOpenFlowInstanceNumOfSwFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 20),
    _HpicfOpenFlowInstanceNumOfSwFlowTable_Type()
)
hpicfOpenFlowInstanceNumOfSwFlowTable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceNumOfSwFlowTable.setStatus("current")


class _HpicfOpenFlowInstanceOperStatusReason_Type(Integer32):
    """Custom type hpicfOpenFlowInstanceOperStatusReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("controllerVLANNotConfigured", 6),
          ("disabled", 8),
          ("enableFailedInHardware", 7),
          ("hardwareResourcesUnavailable", 2),
          ("memberVLANNotConfigured", 3),
          ("memberVLANRemoved", 4),
          ("noValidPortsInMemberVLAN", 5),
          ("notApplicable", 1))
    )


_HpicfOpenFlowInstanceOperStatusReason_Type.__name__ = "Integer32"
_HpicfOpenFlowInstanceOperStatusReason_Object = MibTableColumn
hpicfOpenFlowInstanceOperStatusReason = _HpicfOpenFlowInstanceOperStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 21),
    _HpicfOpenFlowInstanceOperStatusReason_Type()
)
hpicfOpenFlowInstanceOperStatusReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceOperStatusReason.setStatus("current")
_HpicfOpenFlowInstanceEgressOnlyPorts_Type = PortList
_HpicfOpenFlowInstanceEgressOnlyPorts_Object = MibTableColumn
hpicfOpenFlowInstanceEgressOnlyPorts = _HpicfOpenFlowInstanceEgressOnlyPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 22),
    _HpicfOpenFlowInstanceEgressOnlyPorts_Type()
)
hpicfOpenFlowInstanceEgressOnlyPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceEgressOnlyPorts.setStatus("current")


class _HpicfOpenFlowInstanceCapabilities_Type(Bits):
    """Custom type hpicfOpenFlowInstanceCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("blockPorts", 5),
          ("flowStatistics", 0),
          ("groupStatistics", 3),
          ("meterStatistics", 4),
          ("portStatistics", 2),
          ("tableStatistics", 1))
    )

_HpicfOpenFlowInstanceCapabilities_Type.__name__ = "Bits"
_HpicfOpenFlowInstanceCapabilities_Object = MibTableColumn
hpicfOpenFlowInstanceCapabilities = _HpicfOpenFlowInstanceCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 23),
    _HpicfOpenFlowInstanceCapabilities_Type()
)
hpicfOpenFlowInstanceCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceCapabilities.setStatus("current")
_HpicfOpenFlowInstanceHwTableMissCount_Type = Counter64
_HpicfOpenFlowInstanceHwTableMissCount_Object = MibTableColumn
hpicfOpenFlowInstanceHwTableMissCount = _HpicfOpenFlowInstanceHwTableMissCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 24),
    _HpicfOpenFlowInstanceHwTableMissCount_Type()
)
hpicfOpenFlowInstanceHwTableMissCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceHwTableMissCount.setStatus("current")


class _HpicfOpenFlowInstanceTableModel_Type(Integer32):
    """Custom type hpicfOpenFlowInstanceTableModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("customPipeline", 5),
          ("ipControlWithPolicyEngineAndSoftware", 4),
          ("none", 1),
          ("policyEngineAndSoftware", 3),
          ("singleTable", 2))
    )


_HpicfOpenFlowInstanceTableModel_Type.__name__ = "Integer32"
_HpicfOpenFlowInstanceTableModel_Object = MibTableColumn
hpicfOpenFlowInstanceTableModel = _HpicfOpenFlowInstanceTableModel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 25),
    _HpicfOpenFlowInstanceTableModel_Type()
)
hpicfOpenFlowInstanceTableModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceTableModel.setStatus("current")
_HpicfOpenFlowInstanceMembers_Type = VidList
_HpicfOpenFlowInstanceMembers_Object = MibTableColumn
hpicfOpenFlowInstanceMembers = _HpicfOpenFlowInstanceMembers_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 26),
    _HpicfOpenFlowInstanceMembers_Type()
)
hpicfOpenFlowInstanceMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceMembers.setStatus("current")


class _HpicfOpenFlowInstancePipelineModel_Type(Integer32):
    """Custom type hpicfOpenFlowInstancePipelineModel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("customPipeline", 3),
          ("ipcontrolTable", 2),
          ("none", 0),
          ("standardMatch", 1))
    )


_HpicfOpenFlowInstancePipelineModel_Type.__name__ = "Integer32"
_HpicfOpenFlowInstancePipelineModel_Object = MibTableColumn
hpicfOpenFlowInstancePipelineModel = _HpicfOpenFlowInstancePipelineModel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 27),
    _HpicfOpenFlowInstancePipelineModel_Type()
)
hpicfOpenFlowInstancePipelineModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstancePipelineModel.setStatus("current")


class _HpicfOpenFlowInstanceDatapathDesc_Type(DisplayString):
    """Custom type hpicfOpenFlowInstanceDatapathDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfOpenFlowInstanceDatapathDesc_Type.__name__ = "DisplayString"
_HpicfOpenFlowInstanceDatapathDesc_Object = MibTableColumn
hpicfOpenFlowInstanceDatapathDesc = _HpicfOpenFlowInstanceDatapathDesc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 28),
    _HpicfOpenFlowInstanceDatapathDesc_Type()
)
hpicfOpenFlowInstanceDatapathDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceDatapathDesc.setStatus("current")


class _HpicfOpenFlowInstanceSourceMacGrpTable_Type(Integer32):
    """Custom type hpicfOpenFlowInstanceSourceMacGrpTable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HpicfOpenFlowInstanceSourceMacGrpTable_Type.__name__ = "Integer32"
_HpicfOpenFlowInstanceSourceMacGrpTable_Object = MibTableColumn
hpicfOpenFlowInstanceSourceMacGrpTable = _HpicfOpenFlowInstanceSourceMacGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 29),
    _HpicfOpenFlowInstanceSourceMacGrpTable_Type()
)
hpicfOpenFlowInstanceSourceMacGrpTable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceSourceMacGrpTable.setStatus("current")


class _HpicfOpenFlowInstanceDestMacGrpTable_Type(Integer32):
    """Custom type hpicfOpenFlowInstanceDestMacGrpTable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HpicfOpenFlowInstanceDestMacGrpTable_Type.__name__ = "Integer32"
_HpicfOpenFlowInstanceDestMacGrpTable_Object = MibTableColumn
hpicfOpenFlowInstanceDestMacGrpTable = _HpicfOpenFlowInstanceDestMacGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 30),
    _HpicfOpenFlowInstanceDestMacGrpTable_Type()
)
hpicfOpenFlowInstanceDestMacGrpTable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceDestMacGrpTable.setStatus("current")


class _HpicfOpenFlowInstanceMissRuleDefaultAction_Type(Integer32):
    """Custom type hpicfOpenFlowInstanceMissRuleDefaultAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ctrl", 3),
          ("drop", 1),
          ("none", 0),
          ("normal", 2))
    )


_HpicfOpenFlowInstanceMissRuleDefaultAction_Type.__name__ = "Integer32"
_HpicfOpenFlowInstanceMissRuleDefaultAction_Object = MibTableColumn
hpicfOpenFlowInstanceMissRuleDefaultAction = _HpicfOpenFlowInstanceMissRuleDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 31),
    _HpicfOpenFlowInstanceMissRuleDefaultAction_Type()
)
hpicfOpenFlowInstanceMissRuleDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceMissRuleDefaultAction.setStatus("current")


class _HpicfOpenFlowInstanceOverrideProtocol_Type(Bits):
    """Custom type hpicfOpenFlowInstanceOverrideProtocol based on Bits"""
    namedValues = NamedValues(
        *(("bonjour", 10),
          ("dldp", 9),
          ("dot1x", 4),
          ("gvrp", 1),
          ("lacp", 3),
          ("loopprotect", 6),
          ("mvrp", 2),
          ("pvst", 7),
          ("smartlink", 8),
          ("stp", 0),
          ("traditionalPipeline", 11),
          ("udld", 5))
    )

_HpicfOpenFlowInstanceOverrideProtocol_Type.__name__ = "Bits"
_HpicfOpenFlowInstanceOverrideProtocol_Object = MibTableColumn
hpicfOpenFlowInstanceOverrideProtocol = _HpicfOpenFlowInstanceOverrideProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 32),
    _HpicfOpenFlowInstanceOverrideProtocol_Type()
)
hpicfOpenFlowInstanceOverrideProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceOverrideProtocol.setStatus("current")


class _HpicfOpenFlowInstancePktInVlanTagging_Type(Integer32):
    """Custom type hpicfOpenFlowInstancePktInVlanTagging based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("inputForm", 1),
          ("tagAlways", 2),
          ("untagAlways", 3))
    )


_HpicfOpenFlowInstancePktInVlanTagging_Type.__name__ = "Integer32"
_HpicfOpenFlowInstancePktInVlanTagging_Object = MibTableColumn
hpicfOpenFlowInstancePktInVlanTagging = _HpicfOpenFlowInstancePktInVlanTagging_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 4, 1, 33),
    _HpicfOpenFlowInstancePktInVlanTagging_Type()
)
hpicfOpenFlowInstancePktInVlanTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstancePktInVlanTagging.setStatus("current")
_HpicfOpenFlowInstanceMembershipTable_Object = MibTable
hpicfOpenFlowInstanceMembershipTable = _HpicfOpenFlowInstanceMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 5)
)
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceMembershipTable.setStatus("deprecated")
_HpicfOpenFlowInstanceMembershipEntry_Object = MibTableRow
hpicfOpenFlowInstanceMembershipEntry = _HpicfOpenFlowInstanceMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 5, 1)
)
hpicfOpenFlowInstanceMembershipEntry.setIndexNames(
    (0, "HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceName"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceMembershipEntry.setStatus("deprecated")
_HpicfOpenFlowInstanceMembershipRowStatus_Type = RowStatus
_HpicfOpenFlowInstanceMembershipRowStatus_Object = MibTableColumn
hpicfOpenFlowInstanceMembershipRowStatus = _HpicfOpenFlowInstanceMembershipRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 5, 1, 2),
    _HpicfOpenFlowInstanceMembershipRowStatus_Type()
)
hpicfOpenFlowInstanceMembershipRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceMembershipRowStatus.setStatus("deprecated")
_HpicfOpenFlowControllerTable_Object = MibTable
hpicfOpenFlowControllerTable = _HpicfOpenFlowControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 6)
)
if mibBuilder.loadTexts:
    hpicfOpenFlowControllerTable.setStatus("current")
_HpicfOpenFlowControllerEntry_Object = MibTableRow
hpicfOpenFlowControllerEntry = _HpicfOpenFlowControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 6, 1)
)
hpicfOpenFlowControllerEntry.setIndexNames(
    (0, "HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowControllerID"),
)
if mibBuilder.loadTexts:
    hpicfOpenFlowControllerEntry.setStatus("current")


class _HpicfOpenFlowControllerID_Type(Integer32):
    """Custom type hpicfOpenFlowControllerID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfOpenFlowControllerID_Type.__name__ = "Integer32"
_HpicfOpenFlowControllerID_Object = MibTableColumn
hpicfOpenFlowControllerID = _HpicfOpenFlowControllerID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 6, 1, 1),
    _HpicfOpenFlowControllerID_Type()
)
hpicfOpenFlowControllerID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfOpenFlowControllerID.setStatus("current")
_HpicfOpenFlowControllerInetAddressType_Type = InetAddressType
_HpicfOpenFlowControllerInetAddressType_Object = MibTableColumn
hpicfOpenFlowControllerInetAddressType = _HpicfOpenFlowControllerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 6, 1, 2),
    _HpicfOpenFlowControllerInetAddressType_Type()
)
hpicfOpenFlowControllerInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOpenFlowControllerInetAddressType.setStatus("current")
_HpicfOpenFlowControllerInetAddress_Type = InetAddress
_HpicfOpenFlowControllerInetAddress_Object = MibTableColumn
hpicfOpenFlowControllerInetAddress = _HpicfOpenFlowControllerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 6, 1, 3),
    _HpicfOpenFlowControllerInetAddress_Type()
)
hpicfOpenFlowControllerInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOpenFlowControllerInetAddress.setStatus("current")
_HpicfOpenFlowControllerPort_Type = InetPortNumber
_HpicfOpenFlowControllerPort_Object = MibTableColumn
hpicfOpenFlowControllerPort = _HpicfOpenFlowControllerPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 6, 1, 4),
    _HpicfOpenFlowControllerPort_Type()
)
hpicfOpenFlowControllerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOpenFlowControllerPort.setStatus("current")
_HpicfOpenFlowControllerInterface_Type = InterfaceIndex
_HpicfOpenFlowControllerInterface_Object = MibTableColumn
hpicfOpenFlowControllerInterface = _HpicfOpenFlowControllerInterface_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 6, 1, 5),
    _HpicfOpenFlowControllerInterface_Type()
)
hpicfOpenFlowControllerInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOpenFlowControllerInterface.setStatus("current")
_HpicfOpenFlowControllerRowStatus_Type = RowStatus
_HpicfOpenFlowControllerRowStatus_Object = MibTableColumn
hpicfOpenFlowControllerRowStatus = _HpicfOpenFlowControllerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 6, 1, 6),
    _HpicfOpenFlowControllerRowStatus_Type()
)
hpicfOpenFlowControllerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOpenFlowControllerRowStatus.setStatus("current")
_HpicfOpenFlowControllerSourceAddressType_Type = InetAddressType
_HpicfOpenFlowControllerSourceAddressType_Object = MibTableColumn
hpicfOpenFlowControllerSourceAddressType = _HpicfOpenFlowControllerSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 6, 1, 7),
    _HpicfOpenFlowControllerSourceAddressType_Type()
)
hpicfOpenFlowControllerSourceAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOpenFlowControllerSourceAddressType.setStatus("current")
_HpicfOpenFlowControllerSourceAddress_Type = InetAddress
_HpicfOpenFlowControllerSourceAddress_Object = MibTableColumn
hpicfOpenFlowControllerSourceAddress = _HpicfOpenFlowControllerSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 6, 1, 8),
    _HpicfOpenFlowControllerSourceAddress_Type()
)
hpicfOpenFlowControllerSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOpenFlowControllerSourceAddress.setStatus("current")
_HpicfOpenFlowInstanceControllerTable_Object = MibTable
hpicfOpenFlowInstanceControllerTable = _HpicfOpenFlowInstanceControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 8)
)
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceControllerTable.setStatus("current")
_HpicfOpenFlowInstanceControllerEntry_Object = MibTableRow
hpicfOpenFlowInstanceControllerEntry = _HpicfOpenFlowInstanceControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 8, 1)
)
hpicfOpenFlowInstanceControllerEntry.setIndexNames(
    (0, "HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceName"),
    (0, "HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowControllerID"),
)
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceControllerEntry.setStatus("current")


class _HpicfOpenFlowInstanceControllerStatus_Type(Integer32):
    """Custom type hpicfOpenFlowInstanceControllerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 2))
    )


_HpicfOpenFlowInstanceControllerStatus_Type.__name__ = "Integer32"
_HpicfOpenFlowInstanceControllerStatus_Object = MibTableColumn
hpicfOpenFlowInstanceControllerStatus = _HpicfOpenFlowInstanceControllerStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 8, 1, 1),
    _HpicfOpenFlowInstanceControllerStatus_Type()
)
hpicfOpenFlowInstanceControllerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceControllerStatus.setStatus("current")


class _HpicfOpenFlowInstanceControllerState_Type(Integer32):
    """Custom type hpicfOpenFlowInstanceControllerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 4),
          ("backoff", 2),
          ("connecting", 3),
          ("idle", 5),
          ("void", 1))
    )


_HpicfOpenFlowInstanceControllerState_Type.__name__ = "Integer32"
_HpicfOpenFlowInstanceControllerState_Object = MibTableColumn
hpicfOpenFlowInstanceControllerState = _HpicfOpenFlowInstanceControllerState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 8, 1, 2),
    _HpicfOpenFlowInstanceControllerState_Type()
)
hpicfOpenFlowInstanceControllerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceControllerState.setStatus("current")


class _HpicfOpenFlowInstanceControllerRole_Type(Integer32):
    """Custom type hpicfOpenFlowInstanceControllerRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("equal", 1),
          ("master", 2),
          ("slave", 3))
    )


_HpicfOpenFlowInstanceControllerRole_Type.__name__ = "Integer32"
_HpicfOpenFlowInstanceControllerRole_Object = MibTableColumn
hpicfOpenFlowInstanceControllerRole = _HpicfOpenFlowInstanceControllerRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 8, 1, 3),
    _HpicfOpenFlowInstanceControllerRole_Type()
)
hpicfOpenFlowInstanceControllerRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceControllerRole.setStatus("current")


class _HpicfOpenFlowInstanceControllerConnSecure_Type(TruthValue):
    """Custom type hpicfOpenFlowInstanceControllerConnSecure based on TruthValue"""


_HpicfOpenFlowInstanceControllerConnSecure_Object = MibTableColumn
hpicfOpenFlowInstanceControllerConnSecure = _HpicfOpenFlowInstanceControllerConnSecure_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 8, 1, 4),
    _HpicfOpenFlowInstanceControllerConnSecure_Type()
)
hpicfOpenFlowInstanceControllerConnSecure.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceControllerConnSecure.setStatus("current")
_HpicfOpenFlowInstanceControllerRowStatus_Type = RowStatus
_HpicfOpenFlowInstanceControllerRowStatus_Object = MibTableColumn
hpicfOpenFlowInstanceControllerRowStatus = _HpicfOpenFlowInstanceControllerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 8, 1, 5),
    _HpicfOpenFlowInstanceControllerRowStatus_Type()
)
hpicfOpenFlowInstanceControllerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceControllerRowStatus.setStatus("current")
_HpicfOpenFlowMaxInstances_Type = Integer32
_HpicfOpenFlowMaxInstances_Object = MibScalar
hpicfOpenFlowMaxInstances = _HpicfOpenFlowMaxInstances_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 10),
    _HpicfOpenFlowMaxInstances_Type()
)
hpicfOpenFlowMaxInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOpenFlowMaxInstances.setStatus("current")
_HpicfOpenFlowMaxFlows_Type = Integer32
_HpicfOpenFlowMaxFlows_Object = MibScalar
hpicfOpenFlowMaxFlows = _HpicfOpenFlowMaxFlows_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 11),
    _HpicfOpenFlowMaxFlows_Type()
)
hpicfOpenFlowMaxFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOpenFlowMaxFlows.setStatus("current")
_HpicfOpenFlowMaxControllers_Type = Integer32
_HpicfOpenFlowMaxControllers_Object = MibScalar
hpicfOpenFlowMaxControllers = _HpicfOpenFlowMaxControllers_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 12),
    _HpicfOpenFlowMaxControllers_Type()
)
hpicfOpenFlowMaxControllers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOpenFlowMaxControllers.setStatus("current")
_HpicfOpenFlowInstanceMeterTable_Object = MibTable
hpicfOpenFlowInstanceMeterTable = _HpicfOpenFlowInstanceMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 19)
)
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceMeterTable.setStatus("current")
_HpicfOpenFlowInstanceMeterEntry_Object = MibTableRow
hpicfOpenFlowInstanceMeterEntry = _HpicfOpenFlowInstanceMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 19, 1)
)
hpicfOpenFlowInstanceMeterEntry.setIndexNames(
    (0, "HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceName"),
    (0, "HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceMeterID"),
)
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceMeterEntry.setStatus("current")


class _HpicfOpenFlowInstanceMeterID_Type(Unsigned32):
    """Custom type hpicfOpenFlowInstanceMeterID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfOpenFlowInstanceMeterID_Type.__name__ = "Unsigned32"
_HpicfOpenFlowInstanceMeterID_Object = MibTableColumn
hpicfOpenFlowInstanceMeterID = _HpicfOpenFlowInstanceMeterID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 19, 1, 1),
    _HpicfOpenFlowInstanceMeterID_Type()
)
hpicfOpenFlowInstanceMeterID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceMeterID.setStatus("current")
_HpicfOpenFlowInstanceMeterFlowCount_Type = Unsigned32
_HpicfOpenFlowInstanceMeterFlowCount_Object = MibTableColumn
hpicfOpenFlowInstanceMeterFlowCount = _HpicfOpenFlowInstanceMeterFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 19, 1, 2),
    _HpicfOpenFlowInstanceMeterFlowCount_Type()
)
hpicfOpenFlowInstanceMeterFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceMeterFlowCount.setStatus("current")
_HpicfOpenFlowInstanceMeterInputPktCount_Type = Counter64
_HpicfOpenFlowInstanceMeterInputPktCount_Object = MibTableColumn
hpicfOpenFlowInstanceMeterInputPktCount = _HpicfOpenFlowInstanceMeterInputPktCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 19, 1, 3),
    _HpicfOpenFlowInstanceMeterInputPktCount_Type()
)
hpicfOpenFlowInstanceMeterInputPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceMeterInputPktCount.setStatus("current")
_HpicfOpenFlowInstanceMeterInputByteCount_Type = Counter64
_HpicfOpenFlowInstanceMeterInputByteCount_Object = MibTableColumn
hpicfOpenFlowInstanceMeterInputByteCount = _HpicfOpenFlowInstanceMeterInputByteCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 19, 1, 4),
    _HpicfOpenFlowInstanceMeterInputByteCount_Type()
)
hpicfOpenFlowInstanceMeterInputByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceMeterInputByteCount.setStatus("current")
_HpicfOpenFlowInstanceMeterDuration_Type = Unsigned32
_HpicfOpenFlowInstanceMeterDuration_Object = MibTableColumn
hpicfOpenFlowInstanceMeterDuration = _HpicfOpenFlowInstanceMeterDuration_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 19, 1, 5),
    _HpicfOpenFlowInstanceMeterDuration_Type()
)
hpicfOpenFlowInstanceMeterDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceMeterDuration.setStatus("current")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceMeterDuration.setUnits("seconds")
_HpicfOpenFlowInstanceMeterBandTable_Object = MibTable
hpicfOpenFlowInstanceMeterBandTable = _HpicfOpenFlowInstanceMeterBandTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 20)
)
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceMeterBandTable.setStatus("current")
_HpicfOpenFlowInstanceMeterBandEntry_Object = MibTableRow
hpicfOpenFlowInstanceMeterBandEntry = _HpicfOpenFlowInstanceMeterBandEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 20, 1)
)
hpicfOpenFlowInstanceMeterBandEntry.setIndexNames(
    (0, "HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceName"),
    (0, "HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceMeterID"),
    (0, "HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceMeterBandID"),
)
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceMeterBandEntry.setStatus("current")
_HpicfOpenFlowInstanceMeterBandID_Type = Unsigned32
_HpicfOpenFlowInstanceMeterBandID_Object = MibTableColumn
hpicfOpenFlowInstanceMeterBandID = _HpicfOpenFlowInstanceMeterBandID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 20, 1, 1),
    _HpicfOpenFlowInstanceMeterBandID_Type()
)
hpicfOpenFlowInstanceMeterBandID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceMeterBandID.setStatus("current")


class _HpicfOpenFlowInstanceMeterBandType_Type(Integer32):
    """Custom type hpicfOpenFlowInstanceMeterBandType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("mark", 2))
    )


_HpicfOpenFlowInstanceMeterBandType_Type.__name__ = "Integer32"
_HpicfOpenFlowInstanceMeterBandType_Object = MibTableColumn
hpicfOpenFlowInstanceMeterBandType = _HpicfOpenFlowInstanceMeterBandType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 20, 1, 2),
    _HpicfOpenFlowInstanceMeterBandType_Type()
)
hpicfOpenFlowInstanceMeterBandType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceMeterBandType.setStatus("current")
_HpicfOpenFlowInstanceMeterBandRate_Type = Unsigned32
_HpicfOpenFlowInstanceMeterBandRate_Object = MibTableColumn
hpicfOpenFlowInstanceMeterBandRate = _HpicfOpenFlowInstanceMeterBandRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 20, 1, 3),
    _HpicfOpenFlowInstanceMeterBandRate_Type()
)
hpicfOpenFlowInstanceMeterBandRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceMeterBandRate.setStatus("current")


class _HpicfOpenFlowInstanceMeterBandRateUnit_Type(Integer32):
    """Custom type hpicfOpenFlowInstanceMeterBandRateUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 1),
          ("pps", 2))
    )


_HpicfOpenFlowInstanceMeterBandRateUnit_Type.__name__ = "Integer32"
_HpicfOpenFlowInstanceMeterBandRateUnit_Object = MibTableColumn
hpicfOpenFlowInstanceMeterBandRateUnit = _HpicfOpenFlowInstanceMeterBandRateUnit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 20, 1, 4),
    _HpicfOpenFlowInstanceMeterBandRateUnit_Type()
)
hpicfOpenFlowInstanceMeterBandRateUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceMeterBandRateUnit.setStatus("current")
_HpicfOpenFlowInstanceMeterInBandPktCount_Type = Counter64
_HpicfOpenFlowInstanceMeterInBandPktCount_Object = MibTableColumn
hpicfOpenFlowInstanceMeterInBandPktCount = _HpicfOpenFlowInstanceMeterInBandPktCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 20, 1, 5),
    _HpicfOpenFlowInstanceMeterInBandPktCount_Type()
)
hpicfOpenFlowInstanceMeterInBandPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceMeterInBandPktCount.setStatus("current")
_HpicfOpenFlowInstanceMeterInBandByteCount_Type = Counter64
_HpicfOpenFlowInstanceMeterInBandByteCount_Object = MibTableColumn
hpicfOpenFlowInstanceMeterInBandByteCount = _HpicfOpenFlowInstanceMeterInBandByteCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 20, 1, 6),
    _HpicfOpenFlowInstanceMeterInBandByteCount_Type()
)
hpicfOpenFlowInstanceMeterInBandByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceMeterInBandByteCount.setStatus("current")
_HpicfOpenFlowInstanceMeterPrecedenceLevel_Type = Unsigned32
_HpicfOpenFlowInstanceMeterPrecedenceLevel_Object = MibTableColumn
hpicfOpenFlowInstanceMeterPrecedenceLevel = _HpicfOpenFlowInstanceMeterPrecedenceLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 20, 1, 7),
    _HpicfOpenFlowInstanceMeterPrecedenceLevel_Type()
)
hpicfOpenFlowInstanceMeterPrecedenceLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceMeterPrecedenceLevel.setStatus("current")
_HpicfOpenFlowScalarObjects_ObjectIdentity = ObjectIdentity
hpicfOpenFlowScalarObjects = _HpicfOpenFlowScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 21)
)


class _HpicfOpenFlowIPControlTableUsage_Type(Unsigned32):
    """Custom type hpicfOpenFlowIPControlTableUsage based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpicfOpenFlowIPControlTableUsage_Type.__name__ = "Unsigned32"
_HpicfOpenFlowIPControlTableUsage_Object = MibScalar
hpicfOpenFlowIPControlTableUsage = _HpicfOpenFlowIPControlTableUsage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 21, 1),
    _HpicfOpenFlowIPControlTableUsage_Type()
)
hpicfOpenFlowIPControlTableUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOpenFlowIPControlTableUsage.setStatus("current")
if mibBuilder.loadTexts:
    hpicfOpenFlowIPControlTableUsage.setUnits("%")
_HpicfOpenFlowIPControlTableStatsRefreshRate_Type = Unsigned32
_HpicfOpenFlowIPControlTableStatsRefreshRate_Object = MibScalar
hpicfOpenFlowIPControlTableStatsRefreshRate = _HpicfOpenFlowIPControlTableStatsRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 21, 2),
    _HpicfOpenFlowIPControlTableStatsRefreshRate_Type()
)
hpicfOpenFlowIPControlTableStatsRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOpenFlowIPControlTableStatsRefreshRate.setStatus("current")
if mibBuilder.loadTexts:
    hpicfOpenFlowIPControlTableStatsRefreshRate.setUnits("seconds")


class _HpicfOpenFlowIpControlTableMode_Type(Integer32):
    """Custom type hpicfOpenFlowIpControlTableMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HpicfOpenFlowIpControlTableMode_Type.__name__ = "Integer32"
_HpicfOpenFlowIpControlTableMode_Object = MibScalar
hpicfOpenFlowIpControlTableMode = _HpicfOpenFlowIpControlTableMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 21, 9),
    _HpicfOpenFlowIpControlTableMode_Type()
)
hpicfOpenFlowIpControlTableMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOpenFlowIpControlTableMode.setStatus("deprecated")


class _HpicfOpenFlowEgressOnlyPorts_Type(Integer32):
    """Custom type hpicfOpenFlowEgressOnlyPorts based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HpicfOpenFlowEgressOnlyPorts_Type.__name__ = "Integer32"
_HpicfOpenFlowEgressOnlyPorts_Object = MibScalar
hpicfOpenFlowEgressOnlyPorts = _HpicfOpenFlowEgressOnlyPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 1, 21, 10),
    _HpicfOpenFlowEgressOnlyPorts_Type()
)
hpicfOpenFlowEgressOnlyPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOpenFlowEgressOnlyPorts.setStatus("current")
_HpicfOpenFlowConformance_ObjectIdentity = ObjectIdentity
hpicfOpenFlowConformance = _HpicfOpenFlowConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 2)
)
_HpicfOpenFlowCompliances_ObjectIdentity = ObjectIdentity
hpicfOpenFlowCompliances = _HpicfOpenFlowCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 2, 1)
)
_HpicfOpenFlowGroups_ObjectIdentity = ObjectIdentity
hpicfOpenFlowGroups = _HpicfOpenFlowGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 2, 2)
)

# Managed Objects groups

hpicfOpenFlowGlobalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 2, 2, 1)
)
hpicfOpenFlowGlobalConfigGroup.setObjects(
      *(("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowStatus"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowMaxInstances"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowMaxFlows"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowMaxControllers"))
)
if mibBuilder.loadTexts:
    hpicfOpenFlowGlobalConfigGroup.setStatus("current")

hpicfOpenFlowInstanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 2, 2, 2)
)
hpicfOpenFlowInstanceGroup.setObjects(
      *(("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceAdminStatus"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceListenPortCfg"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceListenPort"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceListenPortIsOobm"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceMode"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceFlowLocationMode"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowConnectionInterruptionMode"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceHwRateLimit"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceSwRateLimit"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceDatapathID"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceNumOfHwFlows"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceNumOfSwFlows"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceOperStatus"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceMaxBackOffInterval"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceRowStatus"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceProbeInterval"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceProtoVersion"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceProtoVersionOnly"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceNumOfSwFlowTable"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceOperStatusReason"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceEgressOnlyPorts"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceCapabilities"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceHwTableMissCount"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceTableModel"))
)
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceGroup.setStatus("deprecated")

hpicfOpenFlowInstanceMembershipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 2, 2, 3)
)
hpicfOpenFlowInstanceMembershipGroup.setObjects(
    ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceMembershipRowStatus")
)
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceMembershipGroup.setStatus("deprecated")

hpicfOpenFlowControllerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 2, 2, 4)
)
hpicfOpenFlowControllerGroup.setObjects(
      *(("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowControllerInetAddressType"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowControllerInetAddress"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowControllerPort"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowControllerInterface"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowControllerRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfOpenFlowControllerGroup.setStatus("deprecated")

hpicfOpenFlowInstanceControllerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 2, 2, 6)
)
hpicfOpenFlowInstanceControllerGroup.setObjects(
      *(("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceControllerStatus"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceControllerState"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceControllerRole"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceControllerConnSecure"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceControllerRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceControllerGroup.setStatus("current")

hpicfOpenFlowInstanceMeterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 2, 2, 13)
)
hpicfOpenFlowInstanceMeterGroup.setObjects(
      *(("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceMeterFlowCount"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceMeterInputPktCount"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceMeterInputByteCount"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceMeterDuration"))
)
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceMeterGroup.setStatus("current")

hpicfOpenFlowInstanceMeterBandGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 2, 2, 14)
)
hpicfOpenFlowInstanceMeterBandGroup.setObjects(
      *(("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceMeterBandType"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceMeterBandRate"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceMeterBandRateUnit"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceMeterInBandPktCount"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceMeterInBandByteCount"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceMeterPrecedenceLevel"))
)
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceMeterBandGroup.setStatus("current")

hpicfOpenFlowScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 2, 2, 15)
)
hpicfOpenFlowScalarsGroup.setObjects(
      *(("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowIPControlTableUsage"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowIPControlTableStatsRefreshRate"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowIpControlTableMode"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowEgressOnlyPorts"))
)
if mibBuilder.loadTexts:
    hpicfOpenFlowScalarsGroup.setStatus("deprecated")

hpicfOpenFlowInstanceGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 2, 2, 16)
)
hpicfOpenFlowInstanceGroup1.setObjects(
      *(("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceAdminStatus"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceListenPortCfg"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceListenPort"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceListenPortIsOobm"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceMode"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceFlowLocationMode"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowConnectionInterruptionMode"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceHwRateLimit"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceSwRateLimit"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceDatapathID"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceNumOfHwFlows"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceNumOfSwFlows"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceOperStatus"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceMaxBackOffInterval"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceRowStatus"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceProbeInterval"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceProtoVersion"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceProtoVersionOnly"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceNumOfSwFlowTable"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceOperStatusReason"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceEgressOnlyPorts"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceCapabilities"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceHwTableMissCount"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceTableModel"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceMembers"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstancePipelineModel"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceDatapathDesc"))
)
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceGroup1.setStatus("deprecated")

hpicfOpenFlowScalarsGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 2, 2, 17)
)
hpicfOpenFlowScalarsGroup1.setObjects(
      *(("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowIPControlTableUsage"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowIPControlTableStatsRefreshRate"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowEgressOnlyPorts"))
)
if mibBuilder.loadTexts:
    hpicfOpenFlowScalarsGroup1.setStatus("current")

hpicfOpenFlowInstanceGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 2, 2, 20)
)
hpicfOpenFlowInstanceGroup2.setObjects(
      *(("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceAdminStatus"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceListenPortCfg"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceListenPort"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceListenPortIsOobm"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceMode"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceFlowLocationMode"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowConnectionInterruptionMode"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceHwRateLimit"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceSwRateLimit"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceDatapathID"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceNumOfHwFlows"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceNumOfSwFlows"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceOperStatus"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceMaxBackOffInterval"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceRowStatus"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceProbeInterval"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceProtoVersion"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceProtoVersionOnly"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceNumOfSwFlowTable"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceOperStatusReason"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceEgressOnlyPorts"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceCapabilities"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceHwTableMissCount"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceTableModel"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceMembers"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstancePipelineModel"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceDatapathDesc"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceSourceMacGrpTable"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceDestMacGrpTable"))
)
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceGroup2.setStatus("deprecated")

hpicfOpenFlowInstanceGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 2, 2, 21)
)
hpicfOpenFlowInstanceGroup3.setObjects(
      *(("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceAdminStatus"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceListenPortCfg"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceListenPort"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceListenPortIsOobm"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceMode"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceFlowLocationMode"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowConnectionInterruptionMode"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceHwRateLimit"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceSwRateLimit"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceDatapathID"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceNumOfHwFlows"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceNumOfSwFlows"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceOperStatus"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceMaxBackOffInterval"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceRowStatus"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceProbeInterval"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceProtoVersion"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceProtoVersionOnly"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceNumOfSwFlowTable"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceOperStatusReason"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceEgressOnlyPorts"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceCapabilities"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceHwTableMissCount"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceTableModel"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceMembers"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstancePipelineModel"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceDatapathDesc"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceSourceMacGrpTable"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceDestMacGrpTable"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceMissRuleDefaultAction"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstanceOverrideProtocol"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowInstancePktInVlanTagging"))
)
if mibBuilder.loadTexts:
    hpicfOpenFlowInstanceGroup3.setStatus("current")

hpicfOpenFlowControllerGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 2, 2, 22)
)
hpicfOpenFlowControllerGroup1.setObjects(
      *(("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowControllerInetAddressType"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowControllerInetAddress"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowControllerPort"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowControllerInterface"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowControllerRowStatus"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowControllerSourceAddressType"),
        ("HP-ICF-OPENFLOW-MIB", "hpicfOpenFlowControllerSourceAddress"))
)
if mibBuilder.loadTexts:
    hpicfOpenFlowControllerGroup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfOpenFlowCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfOpenFlowCompliance.setStatus(
        "deprecated"
    )

hpicfOpenFlowCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfOpenFlowCompliance1.setStatus(
        "deprecated"
    )

hpicfOpenFlowCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfOpenFlowCompliance2.setStatus(
        "deprecated"
    )

hpicfOpenFlowCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfOpenFlowCompliance3.setStatus(
        "deprecated"
    )

hpicfOpenFlowCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89, 2, 1, 5)
)
if mibBuilder.loadTexts:
    hpicfOpenFlowCompliance4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-OPENFLOW-MIB",
    **{"hpicfOpenFlowMIB": hpicfOpenFlowMIB,
       "hpicfOpenFlowNotifications": hpicfOpenFlowNotifications,
       "hpicfOpenFlowObjects": hpicfOpenFlowObjects,
       "hpicfOpenFlowStatus": hpicfOpenFlowStatus,
       "hpicfOpenFlowInstanceTable": hpicfOpenFlowInstanceTable,
       "hpicfOpenFlowInstanceEntry": hpicfOpenFlowInstanceEntry,
       "hpicfOpenFlowInstanceName": hpicfOpenFlowInstanceName,
       "hpicfOpenFlowInstanceAdminStatus": hpicfOpenFlowInstanceAdminStatus,
       "hpicfOpenFlowInstanceListenPortCfg": hpicfOpenFlowInstanceListenPortCfg,
       "hpicfOpenFlowInstanceListenPort": hpicfOpenFlowInstanceListenPort,
       "hpicfOpenFlowInstanceListenPortIsOobm": hpicfOpenFlowInstanceListenPortIsOobm,
       "hpicfOpenFlowInstanceMode": hpicfOpenFlowInstanceMode,
       "hpicfOpenFlowInstanceFlowLocationMode": hpicfOpenFlowInstanceFlowLocationMode,
       "hpicfOpenFlowConnectionInterruptionMode": hpicfOpenFlowConnectionInterruptionMode,
       "hpicfOpenFlowInstanceHwRateLimit": hpicfOpenFlowInstanceHwRateLimit,
       "hpicfOpenFlowInstanceSwRateLimit": hpicfOpenFlowInstanceSwRateLimit,
       "hpicfOpenFlowInstanceDatapathID": hpicfOpenFlowInstanceDatapathID,
       "hpicfOpenFlowInstanceNumOfHwFlows": hpicfOpenFlowInstanceNumOfHwFlows,
       "hpicfOpenFlowInstanceNumOfSwFlows": hpicfOpenFlowInstanceNumOfSwFlows,
       "hpicfOpenFlowInstanceOperStatus": hpicfOpenFlowInstanceOperStatus,
       "hpicfOpenFlowInstanceMaxBackOffInterval": hpicfOpenFlowInstanceMaxBackOffInterval,
       "hpicfOpenFlowInstanceRowStatus": hpicfOpenFlowInstanceRowStatus,
       "hpicfOpenFlowInstanceProbeInterval": hpicfOpenFlowInstanceProbeInterval,
       "hpicfOpenFlowInstanceProtoVersion": hpicfOpenFlowInstanceProtoVersion,
       "hpicfOpenFlowInstanceProtoVersionOnly": hpicfOpenFlowInstanceProtoVersionOnly,
       "hpicfOpenFlowInstanceNumOfSwFlowTable": hpicfOpenFlowInstanceNumOfSwFlowTable,
       "hpicfOpenFlowInstanceOperStatusReason": hpicfOpenFlowInstanceOperStatusReason,
       "hpicfOpenFlowInstanceEgressOnlyPorts": hpicfOpenFlowInstanceEgressOnlyPorts,
       "hpicfOpenFlowInstanceCapabilities": hpicfOpenFlowInstanceCapabilities,
       "hpicfOpenFlowInstanceHwTableMissCount": hpicfOpenFlowInstanceHwTableMissCount,
       "hpicfOpenFlowInstanceTableModel": hpicfOpenFlowInstanceTableModel,
       "hpicfOpenFlowInstanceMembers": hpicfOpenFlowInstanceMembers,
       "hpicfOpenFlowInstancePipelineModel": hpicfOpenFlowInstancePipelineModel,
       "hpicfOpenFlowInstanceDatapathDesc": hpicfOpenFlowInstanceDatapathDesc,
       "hpicfOpenFlowInstanceSourceMacGrpTable": hpicfOpenFlowInstanceSourceMacGrpTable,
       "hpicfOpenFlowInstanceDestMacGrpTable": hpicfOpenFlowInstanceDestMacGrpTable,
       "hpicfOpenFlowInstanceMissRuleDefaultAction": hpicfOpenFlowInstanceMissRuleDefaultAction,
       "hpicfOpenFlowInstanceOverrideProtocol": hpicfOpenFlowInstanceOverrideProtocol,
       "hpicfOpenFlowInstancePktInVlanTagging": hpicfOpenFlowInstancePktInVlanTagging,
       "hpicfOpenFlowInstanceMembershipTable": hpicfOpenFlowInstanceMembershipTable,
       "hpicfOpenFlowInstanceMembershipEntry": hpicfOpenFlowInstanceMembershipEntry,
       "hpicfOpenFlowInstanceMembershipRowStatus": hpicfOpenFlowInstanceMembershipRowStatus,
       "hpicfOpenFlowControllerTable": hpicfOpenFlowControllerTable,
       "hpicfOpenFlowControllerEntry": hpicfOpenFlowControllerEntry,
       "hpicfOpenFlowControllerID": hpicfOpenFlowControllerID,
       "hpicfOpenFlowControllerInetAddressType": hpicfOpenFlowControllerInetAddressType,
       "hpicfOpenFlowControllerInetAddress": hpicfOpenFlowControllerInetAddress,
       "hpicfOpenFlowControllerPort": hpicfOpenFlowControllerPort,
       "hpicfOpenFlowControllerInterface": hpicfOpenFlowControllerInterface,
       "hpicfOpenFlowControllerRowStatus": hpicfOpenFlowControllerRowStatus,
       "hpicfOpenFlowControllerSourceAddressType": hpicfOpenFlowControllerSourceAddressType,
       "hpicfOpenFlowControllerSourceAddress": hpicfOpenFlowControllerSourceAddress,
       "hpicfOpenFlowInstanceControllerTable": hpicfOpenFlowInstanceControllerTable,
       "hpicfOpenFlowInstanceControllerEntry": hpicfOpenFlowInstanceControllerEntry,
       "hpicfOpenFlowInstanceControllerStatus": hpicfOpenFlowInstanceControllerStatus,
       "hpicfOpenFlowInstanceControllerState": hpicfOpenFlowInstanceControllerState,
       "hpicfOpenFlowInstanceControllerRole": hpicfOpenFlowInstanceControllerRole,
       "hpicfOpenFlowInstanceControllerConnSecure": hpicfOpenFlowInstanceControllerConnSecure,
       "hpicfOpenFlowInstanceControllerRowStatus": hpicfOpenFlowInstanceControllerRowStatus,
       "hpicfOpenFlowMaxInstances": hpicfOpenFlowMaxInstances,
       "hpicfOpenFlowMaxFlows": hpicfOpenFlowMaxFlows,
       "hpicfOpenFlowMaxControllers": hpicfOpenFlowMaxControllers,
       "hpicfOpenFlowInstanceMeterTable": hpicfOpenFlowInstanceMeterTable,
       "hpicfOpenFlowInstanceMeterEntry": hpicfOpenFlowInstanceMeterEntry,
       "hpicfOpenFlowInstanceMeterID": hpicfOpenFlowInstanceMeterID,
       "hpicfOpenFlowInstanceMeterFlowCount": hpicfOpenFlowInstanceMeterFlowCount,
       "hpicfOpenFlowInstanceMeterInputPktCount": hpicfOpenFlowInstanceMeterInputPktCount,
       "hpicfOpenFlowInstanceMeterInputByteCount": hpicfOpenFlowInstanceMeterInputByteCount,
       "hpicfOpenFlowInstanceMeterDuration": hpicfOpenFlowInstanceMeterDuration,
       "hpicfOpenFlowInstanceMeterBandTable": hpicfOpenFlowInstanceMeterBandTable,
       "hpicfOpenFlowInstanceMeterBandEntry": hpicfOpenFlowInstanceMeterBandEntry,
       "hpicfOpenFlowInstanceMeterBandID": hpicfOpenFlowInstanceMeterBandID,
       "hpicfOpenFlowInstanceMeterBandType": hpicfOpenFlowInstanceMeterBandType,
       "hpicfOpenFlowInstanceMeterBandRate": hpicfOpenFlowInstanceMeterBandRate,
       "hpicfOpenFlowInstanceMeterBandRateUnit": hpicfOpenFlowInstanceMeterBandRateUnit,
       "hpicfOpenFlowInstanceMeterInBandPktCount": hpicfOpenFlowInstanceMeterInBandPktCount,
       "hpicfOpenFlowInstanceMeterInBandByteCount": hpicfOpenFlowInstanceMeterInBandByteCount,
       "hpicfOpenFlowInstanceMeterPrecedenceLevel": hpicfOpenFlowInstanceMeterPrecedenceLevel,
       "hpicfOpenFlowScalarObjects": hpicfOpenFlowScalarObjects,
       "hpicfOpenFlowIPControlTableUsage": hpicfOpenFlowIPControlTableUsage,
       "hpicfOpenFlowIPControlTableStatsRefreshRate": hpicfOpenFlowIPControlTableStatsRefreshRate,
       "hpicfOpenFlowIpControlTableMode": hpicfOpenFlowIpControlTableMode,
       "hpicfOpenFlowEgressOnlyPorts": hpicfOpenFlowEgressOnlyPorts,
       "hpicfOpenFlowConformance": hpicfOpenFlowConformance,
       "hpicfOpenFlowCompliances": hpicfOpenFlowCompliances,
       "hpicfOpenFlowCompliance": hpicfOpenFlowCompliance,
       "hpicfOpenFlowCompliance1": hpicfOpenFlowCompliance1,
       "hpicfOpenFlowCompliance2": hpicfOpenFlowCompliance2,
       "hpicfOpenFlowCompliance3": hpicfOpenFlowCompliance3,
       "hpicfOpenFlowCompliance4": hpicfOpenFlowCompliance4,
       "hpicfOpenFlowGroups": hpicfOpenFlowGroups,
       "hpicfOpenFlowGlobalConfigGroup": hpicfOpenFlowGlobalConfigGroup,
       "hpicfOpenFlowInstanceGroup": hpicfOpenFlowInstanceGroup,
       "hpicfOpenFlowInstanceMembershipGroup": hpicfOpenFlowInstanceMembershipGroup,
       "hpicfOpenFlowControllerGroup": hpicfOpenFlowControllerGroup,
       "hpicfOpenFlowInstanceControllerGroup": hpicfOpenFlowInstanceControllerGroup,
       "hpicfOpenFlowInstanceMeterGroup": hpicfOpenFlowInstanceMeterGroup,
       "hpicfOpenFlowInstanceMeterBandGroup": hpicfOpenFlowInstanceMeterBandGroup,
       "hpicfOpenFlowScalarsGroup": hpicfOpenFlowScalarsGroup,
       "hpicfOpenFlowInstanceGroup1": hpicfOpenFlowInstanceGroup1,
       "hpicfOpenFlowScalarsGroup1": hpicfOpenFlowScalarsGroup1,
       "hpicfOpenFlowInstanceGroup2": hpicfOpenFlowInstanceGroup2,
       "hpicfOpenFlowInstanceGroup3": hpicfOpenFlowInstanceGroup3,
       "hpicfOpenFlowControllerGroup1": hpicfOpenFlowControllerGroup1}
)
