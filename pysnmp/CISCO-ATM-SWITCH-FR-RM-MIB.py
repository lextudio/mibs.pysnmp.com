# SNMP MIB module (CISCO-ATM-SWITCH-FR-RM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ATM-SWITCH-FR-RM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:03 2024
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

ciscoAtmSwitchFrRmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 110)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CfaInterworkServiceCategory(Integer32, TextualConvention):
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
        *(("abr", 2),
          ("ubr", 3),
          ("vbrNrt", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoAtmSwitchFrRmMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAtmSwitchFrRmMIBObjects = _CiscoAtmSwitchFrRmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 110, 1)
)
_CfaAdapter_ObjectIdentity = ObjectIdentity
cfaAdapter = _CfaAdapter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 110, 1, 1)
)
_CfaAdapterIfVcQThresholdTable_Object = MibTable
cfaAdapterIfVcQThresholdTable = _CfaAdapterIfVcQThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 110, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cfaAdapterIfVcQThresholdTable.setStatus("current")
_CfaAdapterIfVcQThresholdEntry_Object = MibTableRow
cfaAdapterIfVcQThresholdEntry = _CfaAdapterIfVcQThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 110, 1, 1, 1, 1)
)
cfaAdapterIfVcQThresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-SWITCH-FR-RM-MIB", "cfaAdapterIfVcQService"),
)
if mibBuilder.loadTexts:
    cfaAdapterIfVcQThresholdEntry.setStatus("current")
_CfaAdapterIfVcQService_Type = CfaInterworkServiceCategory
_CfaAdapterIfVcQService_Object = MibTableColumn
cfaAdapterIfVcQService = _CfaAdapterIfVcQService_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 110, 1, 1, 1, 1, 1),
    _CfaAdapterIfVcQService_Type()
)
cfaAdapterIfVcQService.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfaAdapterIfVcQService.setStatus("current")


class _CfaAdapterIfVcQInqDiscThresh_Type(Integer32):
    """Custom type cfaAdapterIfVcQInqDiscThresh based on Integer32"""
    defaultValue = 87

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CfaAdapterIfVcQInqDiscThresh_Type.__name__ = "Integer32"
_CfaAdapterIfVcQInqDiscThresh_Object = MibTableColumn
cfaAdapterIfVcQInqDiscThresh = _CfaAdapterIfVcQInqDiscThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 110, 1, 1, 1, 1, 2),
    _CfaAdapterIfVcQInqDiscThresh_Type()
)
cfaAdapterIfVcQInqDiscThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfaAdapterIfVcQInqDiscThresh.setStatus("current")
if mibBuilder.loadTexts:
    cfaAdapterIfVcQInqDiscThresh.setUnits("percent")


class _CfaAdapterIfVcQOutqDiscThresh_Type(Integer32):
    """Custom type cfaAdapterIfVcQOutqDiscThresh based on Integer32"""
    defaultValue = 87

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CfaAdapterIfVcQOutqDiscThresh_Type.__name__ = "Integer32"
_CfaAdapterIfVcQOutqDiscThresh_Object = MibTableColumn
cfaAdapterIfVcQOutqDiscThresh = _CfaAdapterIfVcQOutqDiscThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 110, 1, 1, 1, 1, 3),
    _CfaAdapterIfVcQOutqDiscThresh_Type()
)
cfaAdapterIfVcQOutqDiscThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfaAdapterIfVcQOutqDiscThresh.setStatus("current")
if mibBuilder.loadTexts:
    cfaAdapterIfVcQOutqDiscThresh.setUnits("percent")


class _CfaAdapterIfVcQInqMarkThresh_Type(Integer32):
    """Custom type cfaAdapterIfVcQInqMarkThresh based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CfaAdapterIfVcQInqMarkThresh_Type.__name__ = "Integer32"
_CfaAdapterIfVcQInqMarkThresh_Object = MibTableColumn
cfaAdapterIfVcQInqMarkThresh = _CfaAdapterIfVcQInqMarkThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 110, 1, 1, 1, 1, 4),
    _CfaAdapterIfVcQInqMarkThresh_Type()
)
cfaAdapterIfVcQInqMarkThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfaAdapterIfVcQInqMarkThresh.setStatus("current")
if mibBuilder.loadTexts:
    cfaAdapterIfVcQInqMarkThresh.setUnits("percent")


class _CfaAdapterIfVcQOutqMarkThresh_Type(Integer32):
    """Custom type cfaAdapterIfVcQOutqMarkThresh based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CfaAdapterIfVcQOutqMarkThresh_Type.__name__ = "Integer32"
_CfaAdapterIfVcQOutqMarkThresh_Object = MibTableColumn
cfaAdapterIfVcQOutqMarkThresh = _CfaAdapterIfVcQOutqMarkThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 110, 1, 1, 1, 1, 5),
    _CfaAdapterIfVcQOutqMarkThresh_Type()
)
cfaAdapterIfVcQOutqMarkThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfaAdapterIfVcQOutqMarkThresh.setStatus("current")
if mibBuilder.loadTexts:
    cfaAdapterIfVcQOutqMarkThresh.setUnits("percent")
_CfaAdapterIfVbrServOflowTable_Object = MibTable
cfaAdapterIfVbrServOflowTable = _CfaAdapterIfVbrServOflowTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 110, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cfaAdapterIfVbrServOflowTable.setStatus("current")
_CfaAdapterIfVbrServOflowEntry_Object = MibTableRow
cfaAdapterIfVbrServOflowEntry = _CfaAdapterIfVbrServOflowEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 110, 1, 1, 2, 1)
)
cfaAdapterIfVbrServOflowEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cfaAdapterIfVbrServOflowEntry.setStatus("current")


class _CfaAdapterIfVbrServOflow_Type(TruthValue):
    """Custom type cfaAdapterIfVbrServOflow based on TruthValue"""


_CfaAdapterIfVbrServOflow_Object = MibTableColumn
cfaAdapterIfVbrServOflow = _CfaAdapterIfVbrServOflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 110, 1, 1, 2, 1, 1),
    _CfaAdapterIfVbrServOflow_Type()
)
cfaAdapterIfVbrServOflow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfaAdapterIfVbrServOflow.setStatus("current")
_CfaAdapterIfFrConfigTable_Object = MibTable
cfaAdapterIfFrConfigTable = _CfaAdapterIfFrConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 110, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cfaAdapterIfFrConfigTable.setStatus("current")
_CfaAdapterIfFrConfigEntry_Object = MibTableRow
cfaAdapterIfFrConfigEntry = _CfaAdapterIfFrConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 110, 1, 1, 3, 1)
)
cfaAdapterIfFrConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cfaAdapterIfFrConfigEntry.setStatus("current")


class _CfaAdapterIfOverbooking_Type(Integer32):
    """Custom type cfaAdapterIfOverbooking based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_CfaAdapterIfOverbooking_Type.__name__ = "Integer32"
_CfaAdapterIfOverbooking_Object = MibTableColumn
cfaAdapterIfOverbooking = _CfaAdapterIfOverbooking_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 110, 1, 1, 3, 1, 1),
    _CfaAdapterIfOverbooking_Type()
)
cfaAdapterIfOverbooking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfaAdapterIfOverbooking.setStatus("current")
if mibBuilder.loadTexts:
    cfaAdapterIfOverbooking.setUnits("percent")
_CfaInterwork_ObjectIdentity = ObjectIdentity
cfaInterwork = _CfaInterwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 110, 1, 2)
)
_CfaInterworkIfResourceTable_Object = MibTable
cfaInterworkIfResourceTable = _CfaInterworkIfResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 110, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cfaInterworkIfResourceTable.setStatus("current")
_CfaInterworkIfResourceEntry_Object = MibTableRow
cfaInterworkIfResourceEntry = _CfaInterworkIfResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 110, 1, 2, 1, 1)
)
cfaInterworkIfResourceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-SWITCH-FR-RM-MIB", "cfaInterworkIfVcQService"),
)
if mibBuilder.loadTexts:
    cfaInterworkIfResourceEntry.setStatus("current")
_CfaInterworkIfVcQService_Type = CfaInterworkServiceCategory
_CfaInterworkIfVcQService_Object = MibTableColumn
cfaInterworkIfVcQService = _CfaInterworkIfVcQService_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 110, 1, 2, 1, 1, 1),
    _CfaInterworkIfVcQService_Type()
)
cfaInterworkIfVcQService.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfaInterworkIfVcQService.setStatus("current")
_CfaInterworkIfRxAvailRate_Type = Gauge32
_CfaInterworkIfRxAvailRate_Object = MibTableColumn
cfaInterworkIfRxAvailRate = _CfaInterworkIfRxAvailRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 110, 1, 2, 1, 1, 2),
    _CfaInterworkIfRxAvailRate_Type()
)
cfaInterworkIfRxAvailRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfaInterworkIfRxAvailRate.setStatus("current")
if mibBuilder.loadTexts:
    cfaInterworkIfRxAvailRate.setUnits("bits-per-second")
_CfaInterworkIfTxAvailRate_Type = Gauge32
_CfaInterworkIfTxAvailRate_Object = MibTableColumn
cfaInterworkIfTxAvailRate = _CfaInterworkIfTxAvailRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 110, 1, 2, 1, 1, 3),
    _CfaInterworkIfTxAvailRate_Type()
)
cfaInterworkIfTxAvailRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfaInterworkIfTxAvailRate.setStatus("current")
if mibBuilder.loadTexts:
    cfaInterworkIfTxAvailRate.setUnits("bits-per-second")
_CfaInterworkIfRxAllocRate_Type = Gauge32
_CfaInterworkIfRxAllocRate_Object = MibTableColumn
cfaInterworkIfRxAllocRate = _CfaInterworkIfRxAllocRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 110, 1, 2, 1, 1, 4),
    _CfaInterworkIfRxAllocRate_Type()
)
cfaInterworkIfRxAllocRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfaInterworkIfRxAllocRate.setStatus("current")
if mibBuilder.loadTexts:
    cfaInterworkIfRxAllocRate.setUnits("bits-per-second")
_CfaInterworkIfTxAllocRate_Type = Gauge32
_CfaInterworkIfTxAllocRate_Object = MibTableColumn
cfaInterworkIfTxAllocRate = _CfaInterworkIfTxAllocRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 110, 1, 2, 1, 1, 5),
    _CfaInterworkIfTxAllocRate_Type()
)
cfaInterworkIfTxAllocRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfaInterworkIfTxAllocRate.setStatus("current")
if mibBuilder.loadTexts:
    cfaInterworkIfTxAllocRate.setUnits("bits-per-second")
_CiscoAtmSwitchFrRmMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoAtmSwitchFrRmMIBNotifications = _CiscoAtmSwitchFrRmMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 110, 2)
)
_CiscoAtmSwitchFrRmMIBConformance_ObjectIdentity = ObjectIdentity
ciscoAtmSwitchFrRmMIBConformance = _CiscoAtmSwitchFrRmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 110, 3)
)
_CiscoAtmSwitchFrRmMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoAtmSwitchFrRmMIBCompliances = _CiscoAtmSwitchFrRmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 110, 3, 1)
)
_CiscoAtmSwitchFrRmMIBGroups_ObjectIdentity = ObjectIdentity
ciscoAtmSwitchFrRmMIBGroups = _CiscoAtmSwitchFrRmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 110, 3, 2)
)

# Managed Objects groups

cfaAdapterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 110, 3, 2, 1)
)
cfaAdapterGroup.setObjects(
      *(("CISCO-ATM-SWITCH-FR-RM-MIB", "cfaAdapterIfVcQInqDiscThresh"),
        ("CISCO-ATM-SWITCH-FR-RM-MIB", "cfaAdapterIfVcQOutqDiscThresh"),
        ("CISCO-ATM-SWITCH-FR-RM-MIB", "cfaAdapterIfVcQInqMarkThresh"),
        ("CISCO-ATM-SWITCH-FR-RM-MIB", "cfaAdapterIfVcQOutqMarkThresh"),
        ("CISCO-ATM-SWITCH-FR-RM-MIB", "cfaAdapterIfVbrServOflow"),
        ("CISCO-ATM-SWITCH-FR-RM-MIB", "cfaAdapterIfOverbooking"))
)
if mibBuilder.loadTexts:
    cfaAdapterGroup.setStatus("current")

cfaInterworkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 110, 3, 2, 2)
)
cfaInterworkGroup.setObjects(
      *(("CISCO-ATM-SWITCH-FR-RM-MIB", "cfaInterworkIfRxAvailRate"),
        ("CISCO-ATM-SWITCH-FR-RM-MIB", "cfaInterworkIfTxAvailRate"),
        ("CISCO-ATM-SWITCH-FR-RM-MIB", "cfaInterworkIfRxAllocRate"),
        ("CISCO-ATM-SWITCH-FR-RM-MIB", "cfaInterworkIfTxAllocRate"))
)
if mibBuilder.loadTexts:
    cfaInterworkGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoAtmSwitchFrRmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 110, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoAtmSwitchFrRmMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ATM-SWITCH-FR-RM-MIB",
    **{"CfaInterworkServiceCategory": CfaInterworkServiceCategory,
       "ciscoAtmSwitchFrRmMIB": ciscoAtmSwitchFrRmMIB,
       "ciscoAtmSwitchFrRmMIBObjects": ciscoAtmSwitchFrRmMIBObjects,
       "cfaAdapter": cfaAdapter,
       "cfaAdapterIfVcQThresholdTable": cfaAdapterIfVcQThresholdTable,
       "cfaAdapterIfVcQThresholdEntry": cfaAdapterIfVcQThresholdEntry,
       "cfaAdapterIfVcQService": cfaAdapterIfVcQService,
       "cfaAdapterIfVcQInqDiscThresh": cfaAdapterIfVcQInqDiscThresh,
       "cfaAdapterIfVcQOutqDiscThresh": cfaAdapterIfVcQOutqDiscThresh,
       "cfaAdapterIfVcQInqMarkThresh": cfaAdapterIfVcQInqMarkThresh,
       "cfaAdapterIfVcQOutqMarkThresh": cfaAdapterIfVcQOutqMarkThresh,
       "cfaAdapterIfVbrServOflowTable": cfaAdapterIfVbrServOflowTable,
       "cfaAdapterIfVbrServOflowEntry": cfaAdapterIfVbrServOflowEntry,
       "cfaAdapterIfVbrServOflow": cfaAdapterIfVbrServOflow,
       "cfaAdapterIfFrConfigTable": cfaAdapterIfFrConfigTable,
       "cfaAdapterIfFrConfigEntry": cfaAdapterIfFrConfigEntry,
       "cfaAdapterIfOverbooking": cfaAdapterIfOverbooking,
       "cfaInterwork": cfaInterwork,
       "cfaInterworkIfResourceTable": cfaInterworkIfResourceTable,
       "cfaInterworkIfResourceEntry": cfaInterworkIfResourceEntry,
       "cfaInterworkIfVcQService": cfaInterworkIfVcQService,
       "cfaInterworkIfRxAvailRate": cfaInterworkIfRxAvailRate,
       "cfaInterworkIfTxAvailRate": cfaInterworkIfTxAvailRate,
       "cfaInterworkIfRxAllocRate": cfaInterworkIfRxAllocRate,
       "cfaInterworkIfTxAllocRate": cfaInterworkIfTxAllocRate,
       "ciscoAtmSwitchFrRmMIBNotifications": ciscoAtmSwitchFrRmMIBNotifications,
       "ciscoAtmSwitchFrRmMIBConformance": ciscoAtmSwitchFrRmMIBConformance,
       "ciscoAtmSwitchFrRmMIBCompliances": ciscoAtmSwitchFrRmMIBCompliances,
       "ciscoAtmSwitchFrRmMIBCompliance": ciscoAtmSwitchFrRmMIBCompliance,
       "ciscoAtmSwitchFrRmMIBGroups": ciscoAtmSwitchFrRmMIBGroups,
       "cfaAdapterGroup": cfaAdapterGroup,
       "cfaInterworkGroup": cfaInterworkGroup}
)
