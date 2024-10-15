# SNMP MIB module (CISCO-IP-URPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IP-URPF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:17 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoIpUrpfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 451)
)
ciscoIpUrpfMIB.setRevisions(
        ("2011-12-29 00:00",
         "2004-11-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UnicastRpfType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("loose", 2),
          ("strict", 1))
    )



class UnicastRpfOptions(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CiscoIpUrpfMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoIpUrpfMIBNotifs = _CiscoIpUrpfMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 0)
)
_CiscoIpUrpfMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIpUrpfMIBObjects = _CiscoIpUrpfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1)
)
_CipUrpfScalar_ObjectIdentity = ObjectIdentity
cipUrpfScalar = _CipUrpfScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 1)
)


class _CipUrpfDropRateWindow_Type(Integer32):
    """Custom type cipUrpfDropRateWindow based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_CipUrpfDropRateWindow_Type.__name__ = "Integer32"
_CipUrpfDropRateWindow_Object = MibScalar
cipUrpfDropRateWindow = _CipUrpfDropRateWindow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 1, 1),
    _CipUrpfDropRateWindow_Type()
)
cipUrpfDropRateWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipUrpfDropRateWindow.setStatus("current")
if mibBuilder.loadTexts:
    cipUrpfDropRateWindow.setUnits("seconds")


class _CipUrpfComputeInterval_Type(Integer32):
    """Custom type cipUrpfComputeInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_CipUrpfComputeInterval_Type.__name__ = "Integer32"
_CipUrpfComputeInterval_Object = MibScalar
cipUrpfComputeInterval = _CipUrpfComputeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 1, 2),
    _CipUrpfComputeInterval_Type()
)
cipUrpfComputeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipUrpfComputeInterval.setStatus("current")
if mibBuilder.loadTexts:
    cipUrpfComputeInterval.setUnits("seconds")


class _CipUrpfDropNotifyHoldDownTime_Type(Integer32):
    """Custom type cipUrpfDropNotifyHoldDownTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CipUrpfDropNotifyHoldDownTime_Type.__name__ = "Integer32"
_CipUrpfDropNotifyHoldDownTime_Object = MibScalar
cipUrpfDropNotifyHoldDownTime = _CipUrpfDropNotifyHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 1, 3),
    _CipUrpfDropNotifyHoldDownTime_Type()
)
cipUrpfDropNotifyHoldDownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipUrpfDropNotifyHoldDownTime.setStatus("current")
if mibBuilder.loadTexts:
    cipUrpfDropNotifyHoldDownTime.setUnits("seconds")
_CipUrpfStatistics_ObjectIdentity = ObjectIdentity
cipUrpfStatistics = _CipUrpfStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 2)
)
_CipUrpfTable_Object = MibTable
cipUrpfTable = _CipUrpfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cipUrpfTable.setStatus("current")
_CipUrpfEntry_Object = MibTableRow
cipUrpfEntry = _CipUrpfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 2, 1, 1)
)
cipUrpfEntry.setIndexNames(
    (0, "CISCO-IP-URPF-MIB", "cipUrpfIpVersion"),
)
if mibBuilder.loadTexts:
    cipUrpfEntry.setStatus("current")


class _CipUrpfIpVersion_Type(Integer32):
    """Custom type cipUrpfIpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_CipUrpfIpVersion_Type.__name__ = "Integer32"
_CipUrpfIpVersion_Object = MibTableColumn
cipUrpfIpVersion = _CipUrpfIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 2, 1, 1, 1),
    _CipUrpfIpVersion_Type()
)
cipUrpfIpVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipUrpfIpVersion.setStatus("current")
_CipUrpfDrops_Type = Counter32
_CipUrpfDrops_Object = MibTableColumn
cipUrpfDrops = _CipUrpfDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 2, 1, 1, 2),
    _CipUrpfDrops_Type()
)
cipUrpfDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipUrpfDrops.setStatus("current")
if mibBuilder.loadTexts:
    cipUrpfDrops.setUnits("packets")
_CipUrpfDropRate_Type = Gauge32
_CipUrpfDropRate_Object = MibTableColumn
cipUrpfDropRate = _CipUrpfDropRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 2, 1, 1, 3),
    _CipUrpfDropRate_Type()
)
cipUrpfDropRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipUrpfDropRate.setStatus("current")
if mibBuilder.loadTexts:
    cipUrpfDropRate.setUnits("packets per second")
_CipUrpfIfMonTable_Object = MibTable
cipUrpfIfMonTable = _CipUrpfIfMonTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cipUrpfIfMonTable.setStatus("current")
_CipUrpfIfMonEntry_Object = MibTableRow
cipUrpfIfMonEntry = _CipUrpfIfMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 2, 2, 1)
)
cipUrpfIfMonEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IP-URPF-MIB", "cipUrpfIfIpVersion"),
)
if mibBuilder.loadTexts:
    cipUrpfIfMonEntry.setStatus("current")


class _CipUrpfIfIpVersion_Type(Integer32):
    """Custom type cipUrpfIfIpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_CipUrpfIfIpVersion_Type.__name__ = "Integer32"
_CipUrpfIfIpVersion_Object = MibTableColumn
cipUrpfIfIpVersion = _CipUrpfIfIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 2, 2, 1, 1),
    _CipUrpfIfIpVersion_Type()
)
cipUrpfIfIpVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipUrpfIfIpVersion.setStatus("current")
_CipUrpfIfDrops_Type = Counter32
_CipUrpfIfDrops_Object = MibTableColumn
cipUrpfIfDrops = _CipUrpfIfDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 2, 2, 1, 2),
    _CipUrpfIfDrops_Type()
)
cipUrpfIfDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipUrpfIfDrops.setStatus("current")
if mibBuilder.loadTexts:
    cipUrpfIfDrops.setUnits("packets")
_CipUrpfIfSuppressedDrops_Type = Counter32
_CipUrpfIfSuppressedDrops_Object = MibTableColumn
cipUrpfIfSuppressedDrops = _CipUrpfIfSuppressedDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 2, 2, 1, 3),
    _CipUrpfIfSuppressedDrops_Type()
)
cipUrpfIfSuppressedDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipUrpfIfSuppressedDrops.setStatus("current")
if mibBuilder.loadTexts:
    cipUrpfIfSuppressedDrops.setUnits("packets")
_CipUrpfIfDropRate_Type = Gauge32
_CipUrpfIfDropRate_Object = MibTableColumn
cipUrpfIfDropRate = _CipUrpfIfDropRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 2, 2, 1, 4),
    _CipUrpfIfDropRate_Type()
)
cipUrpfIfDropRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipUrpfIfDropRate.setStatus("current")
if mibBuilder.loadTexts:
    cipUrpfIfDropRate.setUnits("packets/second")
_CipUrpfIfDiscontinuityTime_Type = TimeStamp
_CipUrpfIfDiscontinuityTime_Object = MibTableColumn
cipUrpfIfDiscontinuityTime = _CipUrpfIfDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 2, 2, 1, 5),
    _CipUrpfIfDiscontinuityTime_Type()
)
cipUrpfIfDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipUrpfIfDiscontinuityTime.setStatus("current")
_CipUrpfVrfIfTable_Object = MibTable
cipUrpfVrfIfTable = _CipUrpfVrfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cipUrpfVrfIfTable.setStatus("current")
_CipUrpfVrfIfEntry_Object = MibTableRow
cipUrpfVrfIfEntry = _CipUrpfVrfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 2, 3, 1)
)
cipUrpfVrfIfEntry.setIndexNames(
    (0, "CISCO-IP-URPF-MIB", "cipUrpfVrfName"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cipUrpfVrfIfEntry.setStatus("current")
_CipUrpfVrfIfDrops_Type = Counter32
_CipUrpfVrfIfDrops_Object = MibTableColumn
cipUrpfVrfIfDrops = _CipUrpfVrfIfDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 2, 3, 1, 2),
    _CipUrpfVrfIfDrops_Type()
)
cipUrpfVrfIfDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipUrpfVrfIfDrops.setStatus("current")
if mibBuilder.loadTexts:
    cipUrpfVrfIfDrops.setUnits("packets")
_CipUrpfVrfIfDiscontinuityTime_Type = TimeStamp
_CipUrpfVrfIfDiscontinuityTime_Object = MibTableColumn
cipUrpfVrfIfDiscontinuityTime = _CipUrpfVrfIfDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 2, 3, 1, 3),
    _CipUrpfVrfIfDiscontinuityTime_Type()
)
cipUrpfVrfIfDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipUrpfVrfIfDiscontinuityTime.setStatus("current")
_CipUrpfInterfaceConfig_ObjectIdentity = ObjectIdentity
cipUrpfInterfaceConfig = _CipUrpfInterfaceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 3)
)
_CipUrpfIfConfTable_Object = MibTable
cipUrpfIfConfTable = _CipUrpfIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cipUrpfIfConfTable.setStatus("current")
_CipUrpfIfConfEntry_Object = MibTableRow
cipUrpfIfConfEntry = _CipUrpfIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cipUrpfIfConfEntry.setStatus("current")


class _CipUrpfIfDropRateNotifyEnable_Type(TruthValue):
    """Custom type cipUrpfIfDropRateNotifyEnable based on TruthValue"""


_CipUrpfIfDropRateNotifyEnable_Object = MibTableColumn
cipUrpfIfDropRateNotifyEnable = _CipUrpfIfDropRateNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 3, 1, 1, 1),
    _CipUrpfIfDropRateNotifyEnable_Type()
)
cipUrpfIfDropRateNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipUrpfIfDropRateNotifyEnable.setStatus("current")


class _CipUrpfIfNotifyDropRateThreshold_Type(Unsigned32):
    """Custom type cipUrpfIfNotifyDropRateThreshold based on Unsigned32"""
    defaultValue = 1000


_CipUrpfIfNotifyDropRateThreshold_Object = MibTableColumn
cipUrpfIfNotifyDropRateThreshold = _CipUrpfIfNotifyDropRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 3, 1, 1, 2),
    _CipUrpfIfNotifyDropRateThreshold_Type()
)
cipUrpfIfNotifyDropRateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipUrpfIfNotifyDropRateThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cipUrpfIfNotifyDropRateThreshold.setUnits("packets/second")


class _CipUrpfIfNotifyDrHoldDownReset_Type(TruthValue):
    """Custom type cipUrpfIfNotifyDrHoldDownReset based on TruthValue"""


_CipUrpfIfNotifyDrHoldDownReset_Object = MibTableColumn
cipUrpfIfNotifyDrHoldDownReset = _CipUrpfIfNotifyDrHoldDownReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 3, 1, 1, 3),
    _CipUrpfIfNotifyDrHoldDownReset_Type()
)
cipUrpfIfNotifyDrHoldDownReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipUrpfIfNotifyDrHoldDownReset.setStatus("current")


class _CipUrpfIfCheckStrict_Type(Integer32):
    """Custom type cipUrpfIfCheckStrict based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loose", 2),
          ("strict", 1))
    )


_CipUrpfIfCheckStrict_Type.__name__ = "Integer32"
_CipUrpfIfCheckStrict_Object = MibTableColumn
cipUrpfIfCheckStrict = _CipUrpfIfCheckStrict_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 3, 1, 1, 4),
    _CipUrpfIfCheckStrict_Type()
)
cipUrpfIfCheckStrict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipUrpfIfCheckStrict.setStatus("current")


class _CipUrpfIfWhichRouteTableID_Type(Integer32):
    """Custom type cipUrpfIfWhichRouteTableID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("vrf", 2))
    )


_CipUrpfIfWhichRouteTableID_Type.__name__ = "Integer32"
_CipUrpfIfWhichRouteTableID_Object = MibTableColumn
cipUrpfIfWhichRouteTableID = _CipUrpfIfWhichRouteTableID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 3, 1, 1, 5),
    _CipUrpfIfWhichRouteTableID_Type()
)
cipUrpfIfWhichRouteTableID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipUrpfIfWhichRouteTableID.setStatus("current")


class _CipUrpfIfVrfName_Type(SnmpAdminString):
    """Custom type cipUrpfIfVrfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CipUrpfIfVrfName_Type.__name__ = "SnmpAdminString"
_CipUrpfIfVrfName_Object = MibTableColumn
cipUrpfIfVrfName = _CipUrpfIfVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 3, 1, 1, 6),
    _CipUrpfIfVrfName_Type()
)
cipUrpfIfVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipUrpfIfVrfName.setStatus("current")
_CipUrpfVrf_ObjectIdentity = ObjectIdentity
cipUrpfVrf = _CipUrpfVrf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 4)
)
_CipUrpfVrfTable_Object = MibTable
cipUrpfVrfTable = _CipUrpfVrfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cipUrpfVrfTable.setStatus("current")
_CipUrpfVrfEntry_Object = MibTableRow
cipUrpfVrfEntry = _CipUrpfVrfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 4, 1, 1)
)
cipUrpfVrfEntry.setIndexNames(
    (0, "CISCO-IP-URPF-MIB", "cipUrpfVrfName"),
)
if mibBuilder.loadTexts:
    cipUrpfVrfEntry.setStatus("current")


class _CipUrpfVrfName_Type(SnmpAdminString):
    """Custom type cipUrpfVrfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CipUrpfVrfName_Type.__name__ = "SnmpAdminString"
_CipUrpfVrfName_Object = MibTableColumn
cipUrpfVrfName = _CipUrpfVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 1, 4, 1, 1, 1),
    _CipUrpfVrfName_Type()
)
cipUrpfVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipUrpfVrfName.setStatus("current")
_CiscoIpUrpfMIBConformance_ObjectIdentity = ObjectIdentity
ciscoIpUrpfMIBConformance = _CiscoIpUrpfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 2)
)
_CiscoIpUrpfMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIpUrpfMIBCompliances = _CiscoIpUrpfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 2, 1)
)
_CiscoIpUrpfMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIpUrpfMIBGroups = _CiscoIpUrpfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 2, 2)
)
cipUrpfIfMonEntry.registerAugmentions(
    ("CISCO-IP-URPF-MIB",
     "cipUrpfIfConfEntry")
)
cipUrpfIfConfEntry.setIndexNames(*cipUrpfIfMonEntry.getIndexNames())

# Managed Objects groups

ciscoIpUrpfMIBMainObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 2, 2, 1)
)
ciscoIpUrpfMIBMainObjectGroup.setObjects(
      *(("CISCO-IP-URPF-MIB", "cipUrpfDropRateWindow"),
        ("CISCO-IP-URPF-MIB", "cipUrpfComputeInterval"),
        ("CISCO-IP-URPF-MIB", "cipUrpfDropNotifyHoldDownTime"),
        ("CISCO-IP-URPF-MIB", "cipUrpfDrops"),
        ("CISCO-IP-URPF-MIB", "cipUrpfDropRate"),
        ("CISCO-IP-URPF-MIB", "cipUrpfIfDrops"),
        ("CISCO-IP-URPF-MIB", "cipUrpfIfSuppressedDrops"),
        ("CISCO-IP-URPF-MIB", "cipUrpfIfDropRate"),
        ("CISCO-IP-URPF-MIB", "cipUrpfIfDropRateNotifyEnable"),
        ("CISCO-IP-URPF-MIB", "cipUrpfIfNotifyDropRateThreshold"),
        ("CISCO-IP-URPF-MIB", "cipUrpfIfNotifyDrHoldDownReset"),
        ("CISCO-IP-URPF-MIB", "cipUrpfIfCheckStrict"),
        ("CISCO-IP-URPF-MIB", "cipUrpfIfDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    ciscoIpUrpfMIBMainObjectGroup.setStatus("current")

ciscoIpUrpfMIBVrfObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 2, 2, 2)
)
ciscoIpUrpfMIBVrfObjectGroup.setObjects(
      *(("CISCO-IP-URPF-MIB", "cipUrpfVrfName"),
        ("CISCO-IP-URPF-MIB", "cipUrpfIfWhichRouteTableID"),
        ("CISCO-IP-URPF-MIB", "cipUrpfIfVrfName"),
        ("CISCO-IP-URPF-MIB", "cipUrpfVrfIfDrops"),
        ("CISCO-IP-URPF-MIB", "cipUrpfVrfIfDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    ciscoIpUrpfMIBVrfObjectGroup.setStatus("current")


# Notification objects

cipUrpfIfDropRateNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 0, 1)
)
cipUrpfIfDropRateNotify.setObjects(
    ("CISCO-IP-URPF-MIB", "cipUrpfIfDropRate")
)
if mibBuilder.loadTexts:
    cipUrpfIfDropRateNotify.setStatus(
        "current"
    )


# Notifications groups

ciscoIpUrpfMIBNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 2, 2, 6)
)
ciscoIpUrpfMIBNotifyGroup.setObjects(
    ("CISCO-IP-URPF-MIB", "cipUrpfIfDropRateNotify")
)
if mibBuilder.loadTexts:
    ciscoIpUrpfMIBNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoIpUrpfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 451, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIpUrpfMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IP-URPF-MIB",
    **{"UnicastRpfType": UnicastRpfType,
       "UnicastRpfOptions": UnicastRpfOptions,
       "ciscoIpUrpfMIB": ciscoIpUrpfMIB,
       "ciscoIpUrpfMIBNotifs": ciscoIpUrpfMIBNotifs,
       "cipUrpfIfDropRateNotify": cipUrpfIfDropRateNotify,
       "ciscoIpUrpfMIBObjects": ciscoIpUrpfMIBObjects,
       "cipUrpfScalar": cipUrpfScalar,
       "cipUrpfDropRateWindow": cipUrpfDropRateWindow,
       "cipUrpfComputeInterval": cipUrpfComputeInterval,
       "cipUrpfDropNotifyHoldDownTime": cipUrpfDropNotifyHoldDownTime,
       "cipUrpfStatistics": cipUrpfStatistics,
       "cipUrpfTable": cipUrpfTable,
       "cipUrpfEntry": cipUrpfEntry,
       "cipUrpfIpVersion": cipUrpfIpVersion,
       "cipUrpfDrops": cipUrpfDrops,
       "cipUrpfDropRate": cipUrpfDropRate,
       "cipUrpfIfMonTable": cipUrpfIfMonTable,
       "cipUrpfIfMonEntry": cipUrpfIfMonEntry,
       "cipUrpfIfIpVersion": cipUrpfIfIpVersion,
       "cipUrpfIfDrops": cipUrpfIfDrops,
       "cipUrpfIfSuppressedDrops": cipUrpfIfSuppressedDrops,
       "cipUrpfIfDropRate": cipUrpfIfDropRate,
       "cipUrpfIfDiscontinuityTime": cipUrpfIfDiscontinuityTime,
       "cipUrpfVrfIfTable": cipUrpfVrfIfTable,
       "cipUrpfVrfIfEntry": cipUrpfVrfIfEntry,
       "cipUrpfVrfIfDrops": cipUrpfVrfIfDrops,
       "cipUrpfVrfIfDiscontinuityTime": cipUrpfVrfIfDiscontinuityTime,
       "cipUrpfInterfaceConfig": cipUrpfInterfaceConfig,
       "cipUrpfIfConfTable": cipUrpfIfConfTable,
       "cipUrpfIfConfEntry": cipUrpfIfConfEntry,
       "cipUrpfIfDropRateNotifyEnable": cipUrpfIfDropRateNotifyEnable,
       "cipUrpfIfNotifyDropRateThreshold": cipUrpfIfNotifyDropRateThreshold,
       "cipUrpfIfNotifyDrHoldDownReset": cipUrpfIfNotifyDrHoldDownReset,
       "cipUrpfIfCheckStrict": cipUrpfIfCheckStrict,
       "cipUrpfIfWhichRouteTableID": cipUrpfIfWhichRouteTableID,
       "cipUrpfIfVrfName": cipUrpfIfVrfName,
       "cipUrpfVrf": cipUrpfVrf,
       "cipUrpfVrfTable": cipUrpfVrfTable,
       "cipUrpfVrfEntry": cipUrpfVrfEntry,
       "cipUrpfVrfName": cipUrpfVrfName,
       "ciscoIpUrpfMIBConformance": ciscoIpUrpfMIBConformance,
       "ciscoIpUrpfMIBCompliances": ciscoIpUrpfMIBCompliances,
       "ciscoIpUrpfMIBCompliance": ciscoIpUrpfMIBCompliance,
       "ciscoIpUrpfMIBGroups": ciscoIpUrpfMIBGroups,
       "ciscoIpUrpfMIBMainObjectGroup": ciscoIpUrpfMIBMainObjectGroup,
       "ciscoIpUrpfMIBVrfObjectGroup": ciscoIpUrpfMIBVrfObjectGroup,
       "ciscoIpUrpfMIBNotifyGroup": ciscoIpUrpfMIBNotifyGroup}
)
