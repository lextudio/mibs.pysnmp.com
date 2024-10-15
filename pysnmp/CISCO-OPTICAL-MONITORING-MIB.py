# SNMP MIB module (CISCO-OPTICAL-MONITORING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-OPTICAL-MONITORING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:25 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoOpticalMonitoringMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 83)
)
ciscoOpticalMonitoringMIB.setRevisions(
        ("2001-12-04 11:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoOpticalMonMIBObjects_ObjectIdentity = ObjectIdentity
ciscoOpticalMonMIBObjects = _CiscoOpticalMonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 83, 1)
)
_ComParameters_ObjectIdentity = ObjectIdentity
comParameters = _ComParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 83, 1, 1)
)
_ComParametersTable_Object = MibTable
comParametersTable = _ComParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 83, 1, 1, 1)
)
if mibBuilder.loadTexts:
    comParametersTable.setStatus("current")
_ComParametersEntry_Object = MibTableRow
comParametersEntry = _ComParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 83, 1, 1, 1, 1)
)
comParametersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    comParametersEntry.setStatus("current")


class _ComTxBiasCurrent_Type(Integer32):
    """Custom type comTxBiasCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_ComTxBiasCurrent_Type.__name__ = "Integer32"
_ComTxBiasCurrent_Object = MibTableColumn
comTxBiasCurrent = _ComTxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 83, 1, 1, 1, 1, 1),
    _ComTxBiasCurrent_Type()
)
comTxBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comTxBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    comTxBiasCurrent.setUnits("milliamps")
_ComTxPowerSupported_Type = TruthValue
_ComTxPowerSupported_Object = MibTableColumn
comTxPowerSupported = _ComTxPowerSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 83, 1, 1, 1, 1, 2),
    _ComTxPowerSupported_Type()
)
comTxPowerSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comTxPowerSupported.setStatus("current")


class _ComTxPower_Type(Integer32):
    """Custom type comTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ComTxPower_Type.__name__ = "Integer32"
_ComTxPower_Object = MibTableColumn
comTxPower = _ComTxPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 83, 1, 1, 1, 1, 3),
    _ComTxPower_Type()
)
comTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comTxPower.setStatus("current")
if mibBuilder.loadTexts:
    comTxPower.setUnits("microWatts")
_ComTxLaserTempSupported_Type = TruthValue
_ComTxLaserTempSupported_Object = MibTableColumn
comTxLaserTempSupported = _ComTxLaserTempSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 83, 1, 1, 1, 1, 4),
    _ComTxLaserTempSupported_Type()
)
comTxLaserTempSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comTxLaserTempSupported.setStatus("current")


class _ComTxLaserTemp_Type(Integer32):
    """Custom type comTxLaserTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-253, 200),
    )


_ComTxLaserTemp_Type.__name__ = "Integer32"
_ComTxLaserTemp_Object = MibTableColumn
comTxLaserTemp = _ComTxLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 83, 1, 1, 1, 1, 5),
    _ComTxLaserTemp_Type()
)
comTxLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comTxLaserTemp.setStatus("current")
if mibBuilder.loadTexts:
    comTxLaserTemp.setUnits(" Degree Centigrade")


class _ComRxPowerACDC_Type(Integer32):
    """Custom type comRxPowerACDC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ComRxPowerACDC_Type.__name__ = "Integer32"
_ComRxPowerACDC_Object = MibTableColumn
comRxPowerACDC = _ComRxPowerACDC_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 83, 1, 1, 1, 1, 6),
    _ComRxPowerACDC_Type()
)
comRxPowerACDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comRxPowerACDC.setStatus("current")
if mibBuilder.loadTexts:
    comRxPowerACDC.setUnits("microWatts")
_ComRxPowerACSupported_Type = TruthValue
_ComRxPowerACSupported_Object = MibTableColumn
comRxPowerACSupported = _ComRxPowerACSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 83, 1, 1, 1, 1, 7),
    _ComRxPowerACSupported_Type()
)
comRxPowerACSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comRxPowerACSupported.setStatus("current")


class _ComRxPowerAC_Type(Integer32):
    """Custom type comRxPowerAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ComRxPowerAC_Type.__name__ = "Integer32"
_ComRxPowerAC_Object = MibTableColumn
comRxPowerAC = _ComRxPowerAC_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 83, 1, 1, 1, 1, 8),
    _ComRxPowerAC_Type()
)
comRxPowerAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comRxPowerAC.setStatus("current")
if mibBuilder.loadTexts:
    comRxPowerAC.setUnits("microWatts")
_CiscoOpticalMonMIBNotifPrefix_ObjectIdentity = ObjectIdentity
ciscoOpticalMonMIBNotifPrefix = _CiscoOpticalMonMIBNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 83, 2)
)
_CiscoOpticalMonMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoOpticalMonMIBNotifications = _CiscoOpticalMonMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 83, 2, 0)
)
_CiscoOpticalMonMIBConformance_ObjectIdentity = ObjectIdentity
ciscoOpticalMonMIBConformance = _CiscoOpticalMonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 83, 3)
)
_CiscoOpticalMonMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoOpticalMonMIBCompliances = _CiscoOpticalMonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 83, 3, 1)
)
_CiscoOpticalMonMIBGroups_ObjectIdentity = ObjectIdentity
ciscoOpticalMonMIBGroups = _CiscoOpticalMonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 83, 3, 2)
)

# Managed Objects groups

ciscoOpticalMonMIBParamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 83, 3, 2, 1)
)
ciscoOpticalMonMIBParamGroup.setObjects(
      *(("CISCO-OPTICAL-MONITORING-MIB", "comTxBiasCurrent"),
        ("CISCO-OPTICAL-MONITORING-MIB", "comTxPowerSupported"),
        ("CISCO-OPTICAL-MONITORING-MIB", "comTxPower"),
        ("CISCO-OPTICAL-MONITORING-MIB", "comTxLaserTempSupported"),
        ("CISCO-OPTICAL-MONITORING-MIB", "comTxLaserTemp"),
        ("CISCO-OPTICAL-MONITORING-MIB", "comRxPowerACDC"),
        ("CISCO-OPTICAL-MONITORING-MIB", "comRxPowerACSupported"),
        ("CISCO-OPTICAL-MONITORING-MIB", "comRxPowerAC"))
)
if mibBuilder.loadTexts:
    ciscoOpticalMonMIBParamGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoOpticalMonMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 83, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoOpticalMonMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-OPTICAL-MONITORING-MIB",
    **{"ciscoOpticalMonitoringMIB": ciscoOpticalMonitoringMIB,
       "ciscoOpticalMonMIBObjects": ciscoOpticalMonMIBObjects,
       "comParameters": comParameters,
       "comParametersTable": comParametersTable,
       "comParametersEntry": comParametersEntry,
       "comTxBiasCurrent": comTxBiasCurrent,
       "comTxPowerSupported": comTxPowerSupported,
       "comTxPower": comTxPower,
       "comTxLaserTempSupported": comTxLaserTempSupported,
       "comTxLaserTemp": comTxLaserTemp,
       "comRxPowerACDC": comRxPowerACDC,
       "comRxPowerACSupported": comRxPowerACSupported,
       "comRxPowerAC": comRxPowerAC,
       "ciscoOpticalMonMIBNotifPrefix": ciscoOpticalMonMIBNotifPrefix,
       "ciscoOpticalMonMIBNotifications": ciscoOpticalMonMIBNotifications,
       "ciscoOpticalMonMIBConformance": ciscoOpticalMonMIBConformance,
       "ciscoOpticalMonMIBCompliances": ciscoOpticalMonMIBCompliances,
       "ciscoOpticalMonMIBCompliance": ciscoOpticalMonMIBCompliance,
       "ciscoOpticalMonMIBGroups": ciscoOpticalMonMIBGroups,
       "ciscoOpticalMonMIBParamGroup": ciscoOpticalMonMIBParamGroup}
)
