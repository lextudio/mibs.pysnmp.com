# SNMP MIB module (CADANT-LOADBALANCING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-LOADBALANCING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:05 2024
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

(cadIfCmtsCmStatusMacAddress,) = mibBuilder.importSymbols(
    "CADANT-CMTS-MAC-MIB",
    "cadIfCmtsCmStatusMacAddress")

(cadSchema,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadSchema")

(CardId,
 OUIAddress) = mibBuilder.importSymbols(
    "CADANT-TC",
    "CardId",
    "OUIAddress")

(IfDirection,) = mibBuilder.importSymbols(
    "DOCS-IF3-MIB",
    "IfDirection")

(docsLoadbal3BasicRuleEntry,
 docsLoadbal3ResGrpCfgId) = mibBuilder.importSymbols(
    "DOCS-LOADBAL3-MIB",
    "docsLoadbal3BasicRuleEntry",
    "docsLoadbal3ResGrpCfgId")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

cadLoadBalMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1)
)
cadLoadBalMib.setRevisions(
        ("2014-05-08 00:00",
         "2014-02-21 00:00",
         "2014-01-16 00:00",
         "2010-04-07 00:00",
         "2009-09-28 00:00",
         "2009-09-21 00:00",
         "2009-07-28 00:00",
         "2009-04-17 00:00",
         "2008-01-22 00:00",
         "2007-11-21 00:00",
         "2007-04-11 00:00",
         "2006-05-15 00:00",
         "2006-03-31 00:00",
         "2006-03-08 00:00",
         "2005-08-20 00:00",
         "2004-06-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CadLoadBalChgOverStatusTable_Object = MibTable
cadLoadBalChgOverStatusTable = _CadLoadBalChgOverStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 1)
)
if mibBuilder.loadTexts:
    cadLoadBalChgOverStatusTable.setStatus("current")
_CadLoadBalChgOverStatusEntry_Object = MibTableRow
cadLoadBalChgOverStatusEntry = _CadLoadBalChgOverStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 1, 1)
)
cadLoadBalChgOverStatusEntry.setIndexNames(
    (0, "CADANT-CMTS-MAC-MIB", "cadIfCmtsCmStatusMacAddress"),
)
if mibBuilder.loadTexts:
    cadLoadBalChgOverStatusEntry.setStatus("current")


class _CadLoadBalChgOverStatusValue_Type(Integer32):
    """Custom type cadLoadBalChgOverStatusValue based on Integer32"""
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
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("cmOperationRejected", 5),
          ("cmtsOperationRejected", 6),
          ("dbcTimeout", 11),
          ("messageSent", 1),
          ("modemDeparting", 3),
          ("noOpNeeded", 2),
          ("rejectinit", 9),
          ("success", 10),
          ("timeOutT13", 7),
          ("timeOutT15", 8),
          ("waitToSendMessage", 4))
    )


_CadLoadBalChgOverStatusValue_Type.__name__ = "Integer32"
_CadLoadBalChgOverStatusValue_Object = MibTableColumn
cadLoadBalChgOverStatusValue = _CadLoadBalChgOverStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 1, 1, 1),
    _CadLoadBalChgOverStatusValue_Type()
)
cadLoadBalChgOverStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLoadBalChgOverStatusValue.setStatus("current")
_CadLoadBalCmtsCmStatusTable_Object = MibTable
cadLoadBalCmtsCmStatusTable = _CadLoadBalCmtsCmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 2)
)
if mibBuilder.loadTexts:
    cadLoadBalCmtsCmStatusTable.setStatus("current")
_CadLoadBalCmtsCmStatusEntry_Object = MibTableRow
cadLoadBalCmtsCmStatusEntry = _CadLoadBalCmtsCmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 2, 1)
)
cadLoadBalCmtsCmStatusEntry.setIndexNames(
    (0, "CADANT-CMTS-MAC-MIB", "cadIfCmtsCmStatusMacAddress"),
)
if mibBuilder.loadTexts:
    cadLoadBalCmtsCmStatusEntry.setStatus("current")
_CadLoadbal3CmtsCmParamsProvGrpId_Type = Unsigned32
_CadLoadbal3CmtsCmParamsProvGrpId_Object = MibTableColumn
cadLoadbal3CmtsCmParamsProvGrpId = _CadLoadbal3CmtsCmParamsProvGrpId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 2, 1, 1),
    _CadLoadbal3CmtsCmParamsProvGrpId_Type()
)
cadLoadbal3CmtsCmParamsProvGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLoadbal3CmtsCmParamsProvGrpId.setStatus("current")
_CadLoadbal3CmtsCmParamsCurrentGrpId_Type = Unsigned32
_CadLoadbal3CmtsCmParamsCurrentGrpId_Object = MibTableColumn
cadLoadbal3CmtsCmParamsCurrentGrpId = _CadLoadbal3CmtsCmParamsCurrentGrpId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 2, 1, 2),
    _CadLoadbal3CmtsCmParamsCurrentGrpId_Type()
)
cadLoadbal3CmtsCmParamsCurrentGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLoadbal3CmtsCmParamsCurrentGrpId.setStatus("current")


class _CadLoadbal3CmtsCmParamsProvServiceTypeID_Type(SnmpAdminString):
    """Custom type cadLoadbal3CmtsCmParamsProvServiceTypeID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CadLoadbal3CmtsCmParamsProvServiceTypeID_Type.__name__ = "SnmpAdminString"
_CadLoadbal3CmtsCmParamsProvServiceTypeID_Object = MibTableColumn
cadLoadbal3CmtsCmParamsProvServiceTypeID = _CadLoadbal3CmtsCmParamsProvServiceTypeID_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 2, 1, 3),
    _CadLoadbal3CmtsCmParamsProvServiceTypeID_Type()
)
cadLoadbal3CmtsCmParamsProvServiceTypeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLoadbal3CmtsCmParamsProvServiceTypeID.setStatus("current")


class _CadLoadbal3CmtsCmParamsCurrentServiceTypeID_Type(SnmpAdminString):
    """Custom type cadLoadbal3CmtsCmParamsCurrentServiceTypeID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CadLoadbal3CmtsCmParamsCurrentServiceTypeID_Type.__name__ = "SnmpAdminString"
_CadLoadbal3CmtsCmParamsCurrentServiceTypeID_Object = MibTableColumn
cadLoadbal3CmtsCmParamsCurrentServiceTypeID = _CadLoadbal3CmtsCmParamsCurrentServiceTypeID_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 2, 1, 4),
    _CadLoadbal3CmtsCmParamsCurrentServiceTypeID_Type()
)
cadLoadbal3CmtsCmParamsCurrentServiceTypeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLoadbal3CmtsCmParamsCurrentServiceTypeID.setStatus("current")
_CadLoadbal3CmtsCmParamsPolicyId_Type = Unsigned32
_CadLoadbal3CmtsCmParamsPolicyId_Object = MibTableColumn
cadLoadbal3CmtsCmParamsPolicyId = _CadLoadbal3CmtsCmParamsPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 2, 1, 5),
    _CadLoadbal3CmtsCmParamsPolicyId_Type()
)
cadLoadbal3CmtsCmParamsPolicyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLoadbal3CmtsCmParamsPolicyId.setStatus("current")
_CadLoadbal3CmtsCmParamsPriority_Type = Unsigned32
_CadLoadbal3CmtsCmParamsPriority_Object = MibTableColumn
cadLoadbal3CmtsCmParamsPriority = _CadLoadbal3CmtsCmParamsPriority_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 2, 1, 6),
    _CadLoadbal3CmtsCmParamsPriority_Type()
)
cadLoadbal3CmtsCmParamsPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLoadbal3CmtsCmParamsPriority.setStatus("current")
_CadLoadBalBasicRuleTable_Object = MibTable
cadLoadBalBasicRuleTable = _CadLoadBalBasicRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 4)
)
if mibBuilder.loadTexts:
    cadLoadBalBasicRuleTable.setStatus("current")
_CadLoadBalBasicRuleEntry_Object = MibTableRow
cadLoadBalBasicRuleEntry = _CadLoadBalBasicRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cadLoadBalBasicRuleEntry.setStatus("current")


class _CadLoadBalRuleMethod_Type(Integer32):
    """Custom type cadLoadBalRuleMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("channel-utilization", 2),
          ("cm-count", 1))
    )


_CadLoadBalRuleMethod_Type.__name__ = "Integer32"
_CadLoadBalRuleMethod_Object = MibTableColumn
cadLoadBalRuleMethod = _CadLoadBalRuleMethod_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 4, 1, 1),
    _CadLoadBalRuleMethod_Type()
)
cadLoadBalRuleMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadLoadBalRuleMethod.setStatus("current")


class _CadLoadBalRuleType_Type(Bits):
    """Custom type cadLoadBalRuleType based on Bits"""
    defaultBinValue = "11"

    namedValues = NamedValues(
        *(("rule-bonded-dcc", 4),
          ("rule-bonded-ds-dbc", 3),
          ("rule-bonded-us-dbc", 2),
          ("rule-non-bonded-dcc", 1),
          ("rule-static", 0))
    )

_CadLoadBalRuleType_Type.__name__ = "Bits"
_CadLoadBalRuleType_Object = MibTableColumn
cadLoadBalRuleType = _CadLoadBalRuleType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 4, 1, 2),
    _CadLoadBalRuleType_Type()
)
cadLoadBalRuleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadLoadBalRuleType.setStatus("current")


class _CadLoadBalRuleThreshold_Type(Unsigned32):
    """Custom type cadLoadBalRuleThreshold based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CadLoadBalRuleThreshold_Type.__name__ = "Unsigned32"
_CadLoadBalRuleThreshold_Object = MibTableColumn
cadLoadBalRuleThreshold = _CadLoadBalRuleThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 4, 1, 3),
    _CadLoadBalRuleThreshold_Type()
)
cadLoadBalRuleThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadLoadBalRuleThreshold.setStatus("current")


class _CadLoadBalRuleRegistrationSteeringD2_Type(TruthValue):
    """Custom type cadLoadBalRuleRegistrationSteeringD2 based on TruthValue"""


_CadLoadBalRuleRegistrationSteeringD2_Object = MibTableColumn
cadLoadBalRuleRegistrationSteeringD2 = _CadLoadBalRuleRegistrationSteeringD2_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 4, 1, 4),
    _CadLoadBalRuleRegistrationSteeringD2_Type()
)
cadLoadBalRuleRegistrationSteeringD2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadLoadBalRuleRegistrationSteeringD2.setStatus("current")


class _CadLoadBalRuleRegistrationSteeringD3_Type(TruthValue):
    """Custom type cadLoadBalRuleRegistrationSteeringD3 based on TruthValue"""


_CadLoadBalRuleRegistrationSteeringD3_Object = MibTableColumn
cadLoadBalRuleRegistrationSteeringD3 = _CadLoadBalRuleRegistrationSteeringD3_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 4, 1, 5),
    _CadLoadBalRuleRegistrationSteeringD3_Type()
)
cadLoadBalRuleRegistrationSteeringD3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadLoadBalRuleRegistrationSteeringD3.setStatus("current")


class _CadLoadBalRulePeriodicSteeringD2_Type(TruthValue):
    """Custom type cadLoadBalRulePeriodicSteeringD2 based on TruthValue"""


_CadLoadBalRulePeriodicSteeringD2_Object = MibTableColumn
cadLoadBalRulePeriodicSteeringD2 = _CadLoadBalRulePeriodicSteeringD2_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 4, 1, 6),
    _CadLoadBalRulePeriodicSteeringD2_Type()
)
cadLoadBalRulePeriodicSteeringD2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadLoadBalRulePeriodicSteeringD2.setStatus("current")


class _CadLoadBalRulePeriodicSteeringD3_Type(TruthValue):
    """Custom type cadLoadBalRulePeriodicSteeringD3 based on TruthValue"""


_CadLoadBalRulePeriodicSteeringD3_Object = MibTableColumn
cadLoadBalRulePeriodicSteeringD3 = _CadLoadBalRulePeriodicSteeringD3_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 4, 1, 7),
    _CadLoadBalRulePeriodicSteeringD3_Type()
)
cadLoadBalRulePeriodicSteeringD3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadLoadBalRulePeriodicSteeringD3.setStatus("current")


class _CadLoadBalRuleChannelWeight_Type(Integer32):
    """Custom type cadLoadBalRuleChannelWeight based on Integer32"""
    defaultValue = 1

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
        *(("dsOnly", 3),
          ("dsPlus", 5),
          ("equal", 1),
          ("usOnly", 2),
          ("usPlus", 4))
    )


_CadLoadBalRuleChannelWeight_Type.__name__ = "Integer32"
_CadLoadBalRuleChannelWeight_Object = MibTableColumn
cadLoadBalRuleChannelWeight = _CadLoadBalRuleChannelWeight_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 4, 1, 8),
    _CadLoadBalRuleChannelWeight_Type()
)
cadLoadBalRuleChannelWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadLoadBalRuleChannelWeight.setStatus("current")
_CadLoadBalExcludedOUITable_Object = MibTable
cadLoadBalExcludedOUITable = _CadLoadBalExcludedOUITable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 5)
)
if mibBuilder.loadTexts:
    cadLoadBalExcludedOUITable.setStatus("current")
_CadLoadBalExcludedOUIEntry_Object = MibTableRow
cadLoadBalExcludedOUIEntry = _CadLoadBalExcludedOUIEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 5, 1)
)
cadLoadBalExcludedOUIEntry.setIndexNames(
    (0, "CADANT-LOADBALANCING-MIB", "cadLoadBalExclOUIAddress"),
)
if mibBuilder.loadTexts:
    cadLoadBalExcludedOUIEntry.setStatus("current")
_CadLoadBalExclOUIAddress_Type = OUIAddress
_CadLoadBalExclOUIAddress_Object = MibTableColumn
cadLoadBalExclOUIAddress = _CadLoadBalExclOUIAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 5, 1, 1),
    _CadLoadBalExclOUIAddress_Type()
)
cadLoadBalExclOUIAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadLoadBalExclOUIAddress.setStatus("current")
_CadLoadBalExclRowStatus_Type = RowStatus
_CadLoadBalExclRowStatus_Object = MibTableColumn
cadLoadBalExclRowStatus = _CadLoadBalExclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 5, 1, 2),
    _CadLoadBalExclRowStatus_Type()
)
cadLoadBalExclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadLoadBalExclRowStatus.setStatus("current")
_CadLoadBalSystemGroup_ObjectIdentity = ObjectIdentity
cadLoadBalSystemGroup = _CadLoadBalSystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 6)
)


class _CadLoadBalMacDomainLoadBalanceInterval_Type(Unsigned32):
    """Custom type cadLoadBalMacDomainLoadBalanceInterval based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CadLoadBalMacDomainLoadBalanceInterval_Type.__name__ = "Unsigned32"
_CadLoadBalMacDomainLoadBalanceInterval_Object = MibScalar
cadLoadBalMacDomainLoadBalanceInterval = _CadLoadBalMacDomainLoadBalanceInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 6, 5),
    _CadLoadBalMacDomainLoadBalanceInterval_Type()
)
cadLoadBalMacDomainLoadBalanceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadLoadBalMacDomainLoadBalanceInterval.setStatus("current")
if mibBuilder.loadTexts:
    cadLoadBalMacDomainLoadBalanceInterval.setUnits("seconds")


class _CadLoadBalAcrossMacDomainLoadBalanceInterval_Type(Unsigned32):
    """Custom type cadLoadBalAcrossMacDomainLoadBalanceInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CadLoadBalAcrossMacDomainLoadBalanceInterval_Type.__name__ = "Unsigned32"
_CadLoadBalAcrossMacDomainLoadBalanceInterval_Object = MibScalar
cadLoadBalAcrossMacDomainLoadBalanceInterval = _CadLoadBalAcrossMacDomainLoadBalanceInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 6, 6),
    _CadLoadBalAcrossMacDomainLoadBalanceInterval_Type()
)
cadLoadBalAcrossMacDomainLoadBalanceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadLoadBalAcrossMacDomainLoadBalanceInterval.setStatus("current")
if mibBuilder.loadTexts:
    cadLoadBalAcrossMacDomainLoadBalanceInterval.setUnits("seconds")


class _CadLoadBalStartDsUtilizationThreshold_Type(Unsigned32):
    """Custom type cadLoadBalStartDsUtilizationThreshold based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CadLoadBalStartDsUtilizationThreshold_Type.__name__ = "Unsigned32"
_CadLoadBalStartDsUtilizationThreshold_Object = MibScalar
cadLoadBalStartDsUtilizationThreshold = _CadLoadBalStartDsUtilizationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 6, 7),
    _CadLoadBalStartDsUtilizationThreshold_Type()
)
cadLoadBalStartDsUtilizationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadLoadBalStartDsUtilizationThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cadLoadBalStartDsUtilizationThreshold.setUnits("seconds")


class _CadLoadBalStartUsUtilizationThreshold_Type(Unsigned32):
    """Custom type cadLoadBalStartUsUtilizationThreshold based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CadLoadBalStartUsUtilizationThreshold_Type.__name__ = "Unsigned32"
_CadLoadBalStartUsUtilizationThreshold_Object = MibScalar
cadLoadBalStartUsUtilizationThreshold = _CadLoadBalStartUsUtilizationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 6, 8),
    _CadLoadBalStartUsUtilizationThreshold_Type()
)
cadLoadBalStartUsUtilizationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadLoadBalStartUsUtilizationThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cadLoadBalStartUsUtilizationThreshold.setUnits("seconds")


class _CadLoadBalFailedListAgeOutTime_Type(Unsigned32):
    """Custom type cadLoadBalFailedListAgeOutTime based on Unsigned32"""
    defaultValue = 0


_CadLoadBalFailedListAgeOutTime_Object = MibScalar
cadLoadBalFailedListAgeOutTime = _CadLoadBalFailedListAgeOutTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 6, 9),
    _CadLoadBalFailedListAgeOutTime_Type()
)
cadLoadBalFailedListAgeOutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadLoadBalFailedListAgeOutTime.setStatus("current")
if mibBuilder.loadTexts:
    cadLoadBalFailedListAgeOutTime.setUnits("hours")


class _CadLoadBalFailedListExcludeCount_Type(Unsigned32):
    """Custom type cadLoadBalFailedListExcludeCount based on Unsigned32"""
    defaultValue = 1


_CadLoadBalFailedListExcludeCount_Object = MibScalar
cadLoadBalFailedListExcludeCount = _CadLoadBalFailedListExcludeCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 6, 10),
    _CadLoadBalFailedListExcludeCount_Type()
)
cadLoadBalFailedListExcludeCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadLoadBalFailedListExcludeCount.setStatus("current")


class _CadLoadBalNumberModemsToCheckPerInterval_Type(Unsigned32):
    """Custom type cadLoadBalNumberModemsToCheckPerInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CadLoadBalNumberModemsToCheckPerInterval_Type.__name__ = "Unsigned32"
_CadLoadBalNumberModemsToCheckPerInterval_Object = MibScalar
cadLoadBalNumberModemsToCheckPerInterval = _CadLoadBalNumberModemsToCheckPerInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 6, 11),
    _CadLoadBalNumberModemsToCheckPerInterval_Type()
)
cadLoadBalNumberModemsToCheckPerInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadLoadBalNumberModemsToCheckPerInterval.setStatus("current")
if mibBuilder.loadTexts:
    cadLoadBalNumberModemsToCheckPerInterval.setUnits("hours")
_CadLoadBalChannelTable_Object = MibTable
cadLoadBalChannelTable = _CadLoadBalChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 7)
)
if mibBuilder.loadTexts:
    cadLoadBalChannelTable.setStatus("current")
_CadLoadBalChannelEntry_Object = MibTableRow
cadLoadBalChannelEntry = _CadLoadBalChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 7, 1)
)
cadLoadBalChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cadLoadBalChannelEntry.setStatus("current")


class _CadLoadBalChannelUtilization_Type(Integer32):
    """Custom type cadLoadBalChannelUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadLoadBalChannelUtilization_Type.__name__ = "Integer32"
_CadLoadBalChannelUtilization_Object = MibTableColumn
cadLoadBalChannelUtilization = _CadLoadBalChannelUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 7, 1, 1),
    _CadLoadBalChannelUtilization_Type()
)
cadLoadBalChannelUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLoadBalChannelUtilization.setStatus("current")
_CadLoadBalChannelCmCount_Type = Integer32
_CadLoadBalChannelCmCount_Object = MibTableColumn
cadLoadBalChannelCmCount = _CadLoadBalChannelCmCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 7, 1, 2),
    _CadLoadBalChannelCmCount_Type()
)
cadLoadBalChannelCmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLoadBalChannelCmCount.setStatus("current")
_CadLoadBalChannelDynamicTransfersIn_Type = Counter32
_CadLoadBalChannelDynamicTransfersIn_Object = MibTableColumn
cadLoadBalChannelDynamicTransfersIn = _CadLoadBalChannelDynamicTransfersIn_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 7, 1, 3),
    _CadLoadBalChannelDynamicTransfersIn_Type()
)
cadLoadBalChannelDynamicTransfersIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLoadBalChannelDynamicTransfersIn.setStatus("current")
_CadLoadBalChannelDynamicTransfersOut_Type = Counter32
_CadLoadBalChannelDynamicTransfersOut_Object = MibTableColumn
cadLoadBalChannelDynamicTransfersOut = _CadLoadBalChannelDynamicTransfersOut_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 7, 1, 4),
    _CadLoadBalChannelDynamicTransfersOut_Type()
)
cadLoadBalChannelDynamicTransfersOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLoadBalChannelDynamicTransfersOut.setStatus("current")
_CadLoadBalChannelStaticTransfersIn_Type = Counter32
_CadLoadBalChannelStaticTransfersIn_Object = MibTableColumn
cadLoadBalChannelStaticTransfersIn = _CadLoadBalChannelStaticTransfersIn_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 7, 1, 5),
    _CadLoadBalChannelStaticTransfersIn_Type()
)
cadLoadBalChannelStaticTransfersIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLoadBalChannelStaticTransfersIn.setStatus("current")
_CadLoadBalChannelStaticTransfersOut_Type = Counter32
_CadLoadBalChannelStaticTransfersOut_Object = MibTableColumn
cadLoadBalChannelStaticTransfersOut = _CadLoadBalChannelStaticTransfersOut_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 7, 1, 6),
    _CadLoadBalChannelStaticTransfersOut_Type()
)
cadLoadBalChannelStaticTransfersOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLoadBalChannelStaticTransfersOut.setStatus("current")
_CadLoadBalChannelDbcTransfersIn_Type = Counter32
_CadLoadBalChannelDbcTransfersIn_Object = MibTableColumn
cadLoadBalChannelDbcTransfersIn = _CadLoadBalChannelDbcTransfersIn_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 7, 1, 7),
    _CadLoadBalChannelDbcTransfersIn_Type()
)
cadLoadBalChannelDbcTransfersIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLoadBalChannelDbcTransfersIn.setStatus("current")
_CadLoadBalChannelDbcTransfersOut_Type = Counter32
_CadLoadBalChannelDbcTransfersOut_Object = MibTableColumn
cadLoadBalChannelDbcTransfersOut = _CadLoadBalChannelDbcTransfersOut_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 7, 1, 8),
    _CadLoadBalChannelDbcTransfersOut_Type()
)
cadLoadBalChannelDbcTransfersOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLoadBalChannelDbcTransfersOut.setStatus("current")
_CadLoadBalControlGroup_ObjectIdentity = ObjectIdentity
cadLoadBalControlGroup = _CadLoadBalControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 8)
)


class _CadLoadBalClearCounts_Type(TruthValue):
    """Custom type cadLoadBalClearCounts based on TruthValue"""


_CadLoadBalClearCounts_Object = MibScalar
cadLoadBalClearCounts = _CadLoadBalClearCounts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 8, 1),
    _CadLoadBalClearCounts_Type()
)
cadLoadBalClearCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadLoadBalClearCounts.setStatus("current")


class _CadLoadBalRCSControl_Type(Integer32):
    """Custom type cadLoadBalRCSControl based on Integer32"""
    defaultValue = 1

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


_CadLoadBalRCSControl_Type.__name__ = "Integer32"
_CadLoadBalRCSControl_Object = MibScalar
cadLoadBalRCSControl = _CadLoadBalRCSControl_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 8, 2),
    _CadLoadBalRCSControl_Type()
)
cadLoadBalRCSControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadLoadBalRCSControl.setStatus("current")


class _CadLoadBalTCSControl_Type(Integer32):
    """Custom type cadLoadBalTCSControl based on Integer32"""
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


_CadLoadBalTCSControl_Type.__name__ = "Integer32"
_CadLoadBalTCSControl_Object = MibScalar
cadLoadBalTCSControl = _CadLoadBalTCSControl_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 8, 3),
    _CadLoadBalTCSControl_Type()
)
cadLoadBalTCSControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadLoadBalTCSControl.setStatus("current")


class _CadLoadBalTCSMoveUsPrimaryControl_Type(Integer32):
    """Custom type cadLoadBalTCSMoveUsPrimaryControl based on Integer32"""
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


_CadLoadBalTCSMoveUsPrimaryControl_Type.__name__ = "Integer32"
_CadLoadBalTCSMoveUsPrimaryControl_Object = MibScalar
cadLoadBalTCSMoveUsPrimaryControl = _CadLoadBalTCSMoveUsPrimaryControl_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 8, 4),
    _CadLoadBalTCSMoveUsPrimaryControl_Type()
)
cadLoadBalTCSMoveUsPrimaryControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadLoadBalTCSMoveUsPrimaryControl.setStatus("current")


class _CadLoadBalDbcMoveUsPrimaryControl_Type(Integer32):
    """Custom type cadLoadBalDbcMoveUsPrimaryControl based on Integer32"""
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


_CadLoadBalDbcMoveUsPrimaryControl_Type.__name__ = "Integer32"
_CadLoadBalDbcMoveUsPrimaryControl_Object = MibScalar
cadLoadBalDbcMoveUsPrimaryControl = _CadLoadBalDbcMoveUsPrimaryControl_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50, 1, 8, 5),
    _CadLoadBalDbcMoveUsPrimaryControl_Type()
)
cadLoadBalDbcMoveUsPrimaryControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadLoadBalDbcMoveUsPrimaryControl.setStatus("current")
docsLoadbal3BasicRuleEntry.registerAugmentions(
    ("CADANT-LOADBALANCING-MIB",
     "cadLoadBalBasicRuleEntry")
)
cadLoadBalBasicRuleEntry.setIndexNames(*docsLoadbal3BasicRuleEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-LOADBALANCING-MIB",
    **{"cadLoadBalMib": cadLoadBalMib,
       "cadLoadBalChgOverStatusTable": cadLoadBalChgOverStatusTable,
       "cadLoadBalChgOverStatusEntry": cadLoadBalChgOverStatusEntry,
       "cadLoadBalChgOverStatusValue": cadLoadBalChgOverStatusValue,
       "cadLoadBalCmtsCmStatusTable": cadLoadBalCmtsCmStatusTable,
       "cadLoadBalCmtsCmStatusEntry": cadLoadBalCmtsCmStatusEntry,
       "cadLoadbal3CmtsCmParamsProvGrpId": cadLoadbal3CmtsCmParamsProvGrpId,
       "cadLoadbal3CmtsCmParamsCurrentGrpId": cadLoadbal3CmtsCmParamsCurrentGrpId,
       "cadLoadbal3CmtsCmParamsProvServiceTypeID": cadLoadbal3CmtsCmParamsProvServiceTypeID,
       "cadLoadbal3CmtsCmParamsCurrentServiceTypeID": cadLoadbal3CmtsCmParamsCurrentServiceTypeID,
       "cadLoadbal3CmtsCmParamsPolicyId": cadLoadbal3CmtsCmParamsPolicyId,
       "cadLoadbal3CmtsCmParamsPriority": cadLoadbal3CmtsCmParamsPriority,
       "cadLoadBalBasicRuleTable": cadLoadBalBasicRuleTable,
       "cadLoadBalBasicRuleEntry": cadLoadBalBasicRuleEntry,
       "cadLoadBalRuleMethod": cadLoadBalRuleMethod,
       "cadLoadBalRuleType": cadLoadBalRuleType,
       "cadLoadBalRuleThreshold": cadLoadBalRuleThreshold,
       "cadLoadBalRuleRegistrationSteeringD2": cadLoadBalRuleRegistrationSteeringD2,
       "cadLoadBalRuleRegistrationSteeringD3": cadLoadBalRuleRegistrationSteeringD3,
       "cadLoadBalRulePeriodicSteeringD2": cadLoadBalRulePeriodicSteeringD2,
       "cadLoadBalRulePeriodicSteeringD3": cadLoadBalRulePeriodicSteeringD3,
       "cadLoadBalRuleChannelWeight": cadLoadBalRuleChannelWeight,
       "cadLoadBalExcludedOUITable": cadLoadBalExcludedOUITable,
       "cadLoadBalExcludedOUIEntry": cadLoadBalExcludedOUIEntry,
       "cadLoadBalExclOUIAddress": cadLoadBalExclOUIAddress,
       "cadLoadBalExclRowStatus": cadLoadBalExclRowStatus,
       "cadLoadBalSystemGroup": cadLoadBalSystemGroup,
       "cadLoadBalMacDomainLoadBalanceInterval": cadLoadBalMacDomainLoadBalanceInterval,
       "cadLoadBalAcrossMacDomainLoadBalanceInterval": cadLoadBalAcrossMacDomainLoadBalanceInterval,
       "cadLoadBalStartDsUtilizationThreshold": cadLoadBalStartDsUtilizationThreshold,
       "cadLoadBalStartUsUtilizationThreshold": cadLoadBalStartUsUtilizationThreshold,
       "cadLoadBalFailedListAgeOutTime": cadLoadBalFailedListAgeOutTime,
       "cadLoadBalFailedListExcludeCount": cadLoadBalFailedListExcludeCount,
       "cadLoadBalNumberModemsToCheckPerInterval": cadLoadBalNumberModemsToCheckPerInterval,
       "cadLoadBalChannelTable": cadLoadBalChannelTable,
       "cadLoadBalChannelEntry": cadLoadBalChannelEntry,
       "cadLoadBalChannelUtilization": cadLoadBalChannelUtilization,
       "cadLoadBalChannelCmCount": cadLoadBalChannelCmCount,
       "cadLoadBalChannelDynamicTransfersIn": cadLoadBalChannelDynamicTransfersIn,
       "cadLoadBalChannelDynamicTransfersOut": cadLoadBalChannelDynamicTransfersOut,
       "cadLoadBalChannelStaticTransfersIn": cadLoadBalChannelStaticTransfersIn,
       "cadLoadBalChannelStaticTransfersOut": cadLoadBalChannelStaticTransfersOut,
       "cadLoadBalChannelDbcTransfersIn": cadLoadBalChannelDbcTransfersIn,
       "cadLoadBalChannelDbcTransfersOut": cadLoadBalChannelDbcTransfersOut,
       "cadLoadBalControlGroup": cadLoadBalControlGroup,
       "cadLoadBalClearCounts": cadLoadBalClearCounts,
       "cadLoadBalRCSControl": cadLoadBalRCSControl,
       "cadLoadBalTCSControl": cadLoadBalTCSControl,
       "cadLoadBalTCSMoveUsPrimaryControl": cadLoadBalTCSMoveUsPrimaryControl,
       "cadLoadBalDbcMoveUsPrimaryControl": cadLoadBalDbcMoveUsPrimaryControl}
)
