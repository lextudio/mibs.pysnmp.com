# SNMP MIB module (BWM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BWM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:50:12 2024
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

(ipAddrEntry,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipAddrEntry")

(rndErrorDesc,
 rndErrorSeverity,
 rsBWM) = mibBuilder.importSymbols(
    "RADWARE-MIB",
    "rndErrorDesc",
    "rndErrorSeverity",
    "rsBWM")

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



class TruthValue(Integer32):
    """Custom type TruthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )





class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )





class NetNumber(OctetString):
    """Custom type NetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsBWMRulesTable_Object = MibTable
rsBWMRulesTable = _RsBWMRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1)
)
if mibBuilder.loadTexts:
    rsBWMRulesTable.setStatus("mandatory")
_RsBWMRulesEntry_Object = MibTableRow
rsBWMRulesEntry = _RsBWMRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1)
)
rsBWMRulesEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMRulesName"),
)
if mibBuilder.loadTexts:
    rsBWMRulesEntry.setStatus("mandatory")
_RsBWMRulesIndex_Type = Integer32
_RsBWMRulesIndex_Object = MibTableColumn
rsBWMRulesIndex = _RsBWMRulesIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 1),
    _RsBWMRulesIndex_Type()
)
rsBWMRulesIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesIndex.setStatus("mandatory")


class _RsBWMRulesName_Type(DisplayString):
    """Custom type rsBWMRulesName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsBWMRulesName_Type.__name__ = "DisplayString"
_RsBWMRulesName_Object = MibTableColumn
rsBWMRulesName = _RsBWMRulesName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 2),
    _RsBWMRulesName_Type()
)
rsBWMRulesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMRulesName.setStatus("mandatory")


class _RsBWMRulesDestination_Type(DisplayString):
    """Custom type rsBWMRulesDestination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsBWMRulesDestination_Type.__name__ = "DisplayString"
_RsBWMRulesDestination_Object = MibTableColumn
rsBWMRulesDestination = _RsBWMRulesDestination_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 3),
    _RsBWMRulesDestination_Type()
)
rsBWMRulesDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesDestination.setStatus("mandatory")


class _RsBWMRulesSource_Type(DisplayString):
    """Custom type rsBWMRulesSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsBWMRulesSource_Type.__name__ = "DisplayString"
_RsBWMRulesSource_Object = MibTableColumn
rsBWMRulesSource = _RsBWMRulesSource_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 4),
    _RsBWMRulesSource_Type()
)
rsBWMRulesSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesSource.setStatus("mandatory")
_RsBWMRulesStatus_Type = RowStatus
_RsBWMRulesStatus_Object = MibTableColumn
rsBWMRulesStatus = _RsBWMRulesStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 5),
    _RsBWMRulesStatus_Type()
)
rsBWMRulesStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesStatus.setStatus("mandatory")


class _RsBWMRulesAction_Type(Integer32):
    """Custom type rsBWMRulesAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("blockAndBiDirectionalReset", 4),
          ("blockAndReset", 3),
          ("forward", 1),
          ("monitorHTTP", 5),
          ("monitorHTTPS", 6))
    )


_RsBWMRulesAction_Type.__name__ = "Integer32"
_RsBWMRulesAction_Object = MibTableColumn
rsBWMRulesAction = _RsBWMRulesAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 6),
    _RsBWMRulesAction_Type()
)
rsBWMRulesAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesAction.setStatus("mandatory")


class _RsBWMRulesDirection_Type(Integer32):
    """Custom type rsBWMRulesDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneway", 1),
          ("twoway", 2))
    )


_RsBWMRulesDirection_Type.__name__ = "Integer32"
_RsBWMRulesDirection_Object = MibTableColumn
rsBWMRulesDirection = _RsBWMRulesDirection_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 7),
    _RsBWMRulesDirection_Type()
)
rsBWMRulesDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesDirection.setStatus("mandatory")


class _RsBWMRulesPriority_Type(Integer32):
    """Custom type rsBWMRulesPriority based on Integer32"""
    defaultValue = 3


_RsBWMRulesPriority_Object = MibTableColumn
rsBWMRulesPriority = _RsBWMRulesPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 8),
    _RsBWMRulesPriority_Type()
)
rsBWMRulesPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesPriority.setStatus("mandatory")


class _RsBWMRulesPhysicalPort_Type(Integer32):
    """Custom type rsBWMRulesPhysicalPort based on Integer32"""
    defaultValue = 0


_RsBWMRulesPhysicalPort_Object = MibTableColumn
rsBWMRulesPhysicalPort = _RsBWMRulesPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 9),
    _RsBWMRulesPhysicalPort_Type()
)
rsBWMRulesPhysicalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesPhysicalPort.setStatus("mandatory")


class _RsBWMRulesType_Type(Integer32):
    """Custom type rsBWMRulesType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("counter", 2),
          ("facsBandwidth", 1),
          ("ids", 3))
    )


_RsBWMRulesType_Type.__name__ = "Integer32"
_RsBWMRulesType_Object = MibTableColumn
rsBWMRulesType = _RsBWMRulesType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 10),
    _RsBWMRulesType_Type()
)
rsBWMRulesType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesType.setStatus("mandatory")


class _RsBWMRulesDescription_Type(DisplayString):
    """Custom type rsBWMRulesDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsBWMRulesDescription_Type.__name__ = "DisplayString"
_RsBWMRulesDescription_Object = MibTableColumn
rsBWMRulesDescription = _RsBWMRulesDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 11),
    _RsBWMRulesDescription_Type()
)
rsBWMRulesDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesDescription.setStatus("mandatory")
_RsBWMRulesGuaranteedBW_Type = Counter32
_RsBWMRulesGuaranteedBW_Object = MibTableColumn
rsBWMRulesGuaranteedBW = _RsBWMRulesGuaranteedBW_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 12),
    _RsBWMRulesGuaranteedBW_Type()
)
rsBWMRulesGuaranteedBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesGuaranteedBW.setStatus("mandatory")


class _RsBWMRulesPolicyType_Type(Integer32):
    """Custom type rsBWMRulesPolicyType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("filter", 2),
          ("group", 3),
          ("none", 1),
          ("policy", 4))
    )


_RsBWMRulesPolicyType_Type.__name__ = "Integer32"
_RsBWMRulesPolicyType_Object = MibTableColumn
rsBWMRulesPolicyType = _RsBWMRulesPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 13),
    _RsBWMRulesPolicyType_Type()
)
rsBWMRulesPolicyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesPolicyType.setStatus("mandatory")


class _RsBWMRulesPolicy_Type(DisplayString):
    """Custom type rsBWMRulesPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsBWMRulesPolicy_Type.__name__ = "DisplayString"
_RsBWMRulesPolicy_Object = MibTableColumn
rsBWMRulesPolicy = _RsBWMRulesPolicy_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 14),
    _RsBWMRulesPolicy_Type()
)
rsBWMRulesPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesPolicy.setStatus("mandatory")


class _RsBWMRulesOperationalStatus_Type(Integer32):
    """Custom type rsBWMRulesOperationalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RsBWMRulesOperationalStatus_Type.__name__ = "Integer32"
_RsBWMRulesOperationalStatus_Object = MibTableColumn
rsBWMRulesOperationalStatus = _RsBWMRulesOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 15),
    _RsBWMRulesOperationalStatus_Type()
)
rsBWMRulesOperationalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesOperationalStatus.setStatus("mandatory")


class _RsBWMRulesDSCPMarking_Type(Integer32):
    """Custom type rsBWMRulesDSCPMarking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_RsBWMRulesDSCPMarking_Type.__name__ = "Integer32"
_RsBWMRulesDSCPMarking_Object = MibTableColumn
rsBWMRulesDSCPMarking = _RsBWMRulesDSCPMarking_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 16),
    _RsBWMRulesDSCPMarking_Type()
)
rsBWMRulesDSCPMarking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesDSCPMarking.setStatus("mandatory")


class _RsBWMRulesReportBlockedPackets_Type(Integer32):
    """Custom type rsBWMRulesReportBlockedPackets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RsBWMRulesReportBlockedPackets_Type.__name__ = "Integer32"
_RsBWMRulesReportBlockedPackets_Object = MibTableColumn
rsBWMRulesReportBlockedPackets = _RsBWMRulesReportBlockedPackets_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 17),
    _RsBWMRulesReportBlockedPackets_Type()
)
rsBWMRulesReportBlockedPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesReportBlockedPackets.setStatus("mandatory")
_RsBWMRulesMaxBW_Type = Counter32
_RsBWMRulesMaxBW_Object = MibTableColumn
rsBWMRulesMaxBW = _RsBWMRulesMaxBW_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 18),
    _RsBWMRulesMaxBW_Type()
)
rsBWMRulesMaxBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesMaxBW.setStatus("mandatory")
_RsBWMDummy1_Type = Integer32
_RsBWMDummy1_Object = MibScalar
rsBWMDummy1 = _RsBWMDummy1_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 2),
    _RsBWMDummy1_Type()
)
rsBWMDummy1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMDummy1.setStatus("mandatory")
_RsBWMRulesIPObjectTable_Object = MibTable
rsBWMRulesIPObjectTable = _RsBWMRulesIPObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 2)
)
if mibBuilder.loadTexts:
    rsBWMRulesIPObjectTable.setStatus("mandatory")
_RsBWMRulesIPObjectEntry_Object = MibTableRow
rsBWMRulesIPObjectEntry = _RsBWMRulesIPObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 2, 1)
)
rsBWMRulesIPObjectEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMRulesIPObjectName"),
    (0, "BWM-MIB", "rsBWMRulesIPObjectSubIndex"),
)
if mibBuilder.loadTexts:
    rsBWMRulesIPObjectEntry.setStatus("mandatory")


class _RsBWMRulesIPObjectName_Type(DisplayString):
    """Custom type rsBWMRulesIPObjectName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsBWMRulesIPObjectName_Type.__name__ = "DisplayString"
_RsBWMRulesIPObjectName_Object = MibTableColumn
rsBWMRulesIPObjectName = _RsBWMRulesIPObjectName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 2, 1, 1),
    _RsBWMRulesIPObjectName_Type()
)
rsBWMRulesIPObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMRulesIPObjectName.setStatus("mandatory")


class _RsBWMRulesIPObjectSubIndex_Type(Integer32):
    """Custom type rsBWMRulesIPObjectSubIndex based on Integer32"""
    defaultValue = 0


_RsBWMRulesIPObjectSubIndex_Object = MibTableColumn
rsBWMRulesIPObjectSubIndex = _RsBWMRulesIPObjectSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 2, 1, 2),
    _RsBWMRulesIPObjectSubIndex_Type()
)
rsBWMRulesIPObjectSubIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMRulesIPObjectSubIndex.setStatus("mandatory")


class _RsBWMRulesIPObjectAddress_Type(IpAddress):
    """Custom type rsBWMRulesIPObjectAddress based on IpAddress"""
    defaultValue = 0


_RsBWMRulesIPObjectAddress_Object = MibTableColumn
rsBWMRulesIPObjectAddress = _RsBWMRulesIPObjectAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 2, 1, 3),
    _RsBWMRulesIPObjectAddress_Type()
)
rsBWMRulesIPObjectAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesIPObjectAddress.setStatus("mandatory")


class _RsBWMRulesIPObjectMask_Type(IpAddress):
    """Custom type rsBWMRulesIPObjectMask based on IpAddress"""
    defaultValue = 0


_RsBWMRulesIPObjectMask_Object = MibTableColumn
rsBWMRulesIPObjectMask = _RsBWMRulesIPObjectMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 2, 1, 4),
    _RsBWMRulesIPObjectMask_Type()
)
rsBWMRulesIPObjectMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesIPObjectMask.setStatus("mandatory")


class _RsBWMRulesIPObjectFromIP_Type(IpAddress):
    """Custom type rsBWMRulesIPObjectFromIP based on IpAddress"""
    defaultValue = 0


_RsBWMRulesIPObjectFromIP_Object = MibTableColumn
rsBWMRulesIPObjectFromIP = _RsBWMRulesIPObjectFromIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 2, 1, 5),
    _RsBWMRulesIPObjectFromIP_Type()
)
rsBWMRulesIPObjectFromIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesIPObjectFromIP.setStatus("mandatory")


class _RsBWMRulesIPObjectToIP_Type(IpAddress):
    """Custom type rsBWMRulesIPObjectToIP based on IpAddress"""
    defaultValue = 0


_RsBWMRulesIPObjectToIP_Object = MibTableColumn
rsBWMRulesIPObjectToIP = _RsBWMRulesIPObjectToIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 2, 1, 6),
    _RsBWMRulesIPObjectToIP_Type()
)
rsBWMRulesIPObjectToIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesIPObjectToIP.setStatus("mandatory")


class _RsBWMRulesIPObjectMode_Type(Integer32):
    """Custom type rsBWMRulesIPObjectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipMask", 1),
          ("ipRange", 2))
    )


_RsBWMRulesIPObjectMode_Type.__name__ = "Integer32"
_RsBWMRulesIPObjectMode_Object = MibTableColumn
rsBWMRulesIPObjectMode = _RsBWMRulesIPObjectMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 2, 1, 7),
    _RsBWMRulesIPObjectMode_Type()
)
rsBWMRulesIPObjectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesIPObjectMode.setStatus("mandatory")
_RsBWMRulesIPObjectStatus_Type = RowStatus
_RsBWMRulesIPObjectStatus_Object = MibTableColumn
rsBWMRulesIPObjectStatus = _RsBWMRulesIPObjectStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 2, 1, 8),
    _RsBWMRulesIPObjectStatus_Type()
)
rsBWMRulesIPObjectStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesIPObjectStatus.setStatus("mandatory")
_RsBWMDummy2_Type = Integer32
_RsBWMDummy2_Object = MibScalar
rsBWMDummy2 = _RsBWMDummy2_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 2, 2),
    _RsBWMDummy2_Type()
)
rsBWMDummy2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMDummy2.setStatus("mandatory")


class _RsBWMCBQMode_Type(Integer32):
    """Custom type rsBWMCBQMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cbq", 2),
          ("cyclic", 1))
    )


_RsBWMCBQMode_Type.__name__ = "Integer32"
_RsBWMCBQMode_Object = MibScalar
rsBWMCBQMode = _RsBWMCBQMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 3),
    _RsBWMCBQMode_Type()
)
rsBWMCBQMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMCBQMode.setStatus("mandatory")


class _RsBWMActualQueueSize_Type(Integer32):
    """Custom type rsBWMActualQueueSize based on Integer32"""
    defaultValue = 0


_RsBWMActualQueueSize_Object = MibScalar
rsBWMActualQueueSize = _RsBWMActualQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 4),
    _RsBWMActualQueueSize_Type()
)
rsBWMActualQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMActualQueueSize.setStatus("mandatory")


class _RsBWMAverageQueueSize_Type(Integer32):
    """Custom type rsBWMAverageQueueSize based on Integer32"""
    defaultValue = 0


_RsBWMAverageQueueSize_Object = MibScalar
rsBWMAverageQueueSize = _RsBWMAverageQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 5),
    _RsBWMAverageQueueSize_Type()
)
rsBWMAverageQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMAverageQueueSize.setStatus("mandatory")


class _RsBWMQueueRedDropped_Type(Integer32):
    """Custom type rsBWMQueueRedDropped based on Integer32"""
    defaultValue = 0


_RsBWMQueueRedDropped_Object = MibScalar
rsBWMQueueRedDropped = _RsBWMQueueRedDropped_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 6),
    _RsBWMQueueRedDropped_Type()
)
rsBWMQueueRedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMQueueRedDropped.setStatus("mandatory")
_RsBWMPriorityTable_Object = MibTable
rsBWMPriorityTable = _RsBWMPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 7)
)
if mibBuilder.loadTexts:
    rsBWMPriorityTable.setStatus("mandatory")
_RsBWMPriorityEntry_Object = MibTableRow
rsBWMPriorityEntry = _RsBWMPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 7, 1)
)
rsBWMPriorityEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMPriority"),
)
if mibBuilder.loadTexts:
    rsBWMPriorityEntry.setStatus("mandatory")
_RsBWMPriority_Type = Integer32
_RsBWMPriority_Object = MibTableColumn
rsBWMPriority = _RsBWMPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 7, 1, 1),
    _RsBWMPriority_Type()
)
rsBWMPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMPriority.setStatus("mandatory")
_RsBWMPacketsSent_Type = Integer32
_RsBWMPacketsSent_Object = MibTableColumn
rsBWMPacketsSent = _RsBWMPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 7, 1, 2),
    _RsBWMPacketsSent_Type()
)
rsBWMPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMPacketsSent.setStatus("mandatory")
_RsBWMDummy3_Type = Integer32
_RsBWMDummy3_Object = MibScalar
rsBWMDummy3 = _RsBWMDummy3_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 7, 2),
    _RsBWMDummy3_Type()
)
rsBWMDummy3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMDummy3.setStatus("mandatory")


class _RsBWMRedMode_Type(Integer32):
    """Custom type rsBWMRedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("global", 2),
          ("none", 1),
          ("weighted", 3))
    )


_RsBWMRedMode_Type.__name__ = "Integer32"
_RsBWMRedMode_Object = MibScalar
rsBWMRedMode = _RsBWMRedMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 8),
    _RsBWMRedMode_Type()
)
rsBWMRedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRedMode.setStatus("mandatory")
_RsBWMCurrentRulesTable_Object = MibTable
rsBWMCurrentRulesTable = _RsBWMCurrentRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9)
)
if mibBuilder.loadTexts:
    rsBWMCurrentRulesTable.setStatus("mandatory")
_RsBWMCurrentRulesEntry_Object = MibTableRow
rsBWMCurrentRulesEntry = _RsBWMCurrentRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1)
)
rsBWMCurrentRulesEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMCurrentRulesName"),
)
if mibBuilder.loadTexts:
    rsBWMCurrentRulesEntry.setStatus("mandatory")
_RsBWMCurrentRulesIndex_Type = Integer32
_RsBWMCurrentRulesIndex_Object = MibTableColumn
rsBWMCurrentRulesIndex = _RsBWMCurrentRulesIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 1),
    _RsBWMCurrentRulesIndex_Type()
)
rsBWMCurrentRulesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesIndex.setStatus("mandatory")


class _RsBWMCurrentRulesName_Type(DisplayString):
    """Custom type rsBWMCurrentRulesName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsBWMCurrentRulesName_Type.__name__ = "DisplayString"
_RsBWMCurrentRulesName_Object = MibTableColumn
rsBWMCurrentRulesName = _RsBWMCurrentRulesName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 2),
    _RsBWMCurrentRulesName_Type()
)
rsBWMCurrentRulesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesName.setStatus("mandatory")


class _RsBWMCurrentRulesDestination_Type(DisplayString):
    """Custom type rsBWMCurrentRulesDestination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsBWMCurrentRulesDestination_Type.__name__ = "DisplayString"
_RsBWMCurrentRulesDestination_Object = MibTableColumn
rsBWMCurrentRulesDestination = _RsBWMCurrentRulesDestination_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 3),
    _RsBWMCurrentRulesDestination_Type()
)
rsBWMCurrentRulesDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesDestination.setStatus("mandatory")


class _RsBWMCurrentRulesSource_Type(DisplayString):
    """Custom type rsBWMCurrentRulesSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsBWMCurrentRulesSource_Type.__name__ = "DisplayString"
_RsBWMCurrentRulesSource_Object = MibTableColumn
rsBWMCurrentRulesSource = _RsBWMCurrentRulesSource_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 4),
    _RsBWMCurrentRulesSource_Type()
)
rsBWMCurrentRulesSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesSource.setStatus("mandatory")


class _RsBWMCurrentRulesAction_Type(Integer32):
    """Custom type rsBWMCurrentRulesAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("blockAndBiDirectionalReset", 4),
          ("blockAndReset", 3),
          ("forward", 1),
          ("monitorHTTP", 5),
          ("monitorHTTPS", 6))
    )


_RsBWMCurrentRulesAction_Type.__name__ = "Integer32"
_RsBWMCurrentRulesAction_Object = MibTableColumn
rsBWMCurrentRulesAction = _RsBWMCurrentRulesAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 5),
    _RsBWMCurrentRulesAction_Type()
)
rsBWMCurrentRulesAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesAction.setStatus("mandatory")


class _RsBWMCurrentRulesDirection_Type(Integer32):
    """Custom type rsBWMCurrentRulesDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneway", 1),
          ("twoway", 2))
    )


_RsBWMCurrentRulesDirection_Type.__name__ = "Integer32"
_RsBWMCurrentRulesDirection_Object = MibTableColumn
rsBWMCurrentRulesDirection = _RsBWMCurrentRulesDirection_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 6),
    _RsBWMCurrentRulesDirection_Type()
)
rsBWMCurrentRulesDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesDirection.setStatus("mandatory")
_RsBWMCurrentRulesPriority_Type = Integer32
_RsBWMCurrentRulesPriority_Object = MibTableColumn
rsBWMCurrentRulesPriority = _RsBWMCurrentRulesPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 7),
    _RsBWMCurrentRulesPriority_Type()
)
rsBWMCurrentRulesPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesPriority.setStatus("mandatory")
_RsBWMCurrentRulesPhysicalPort_Type = Integer32
_RsBWMCurrentRulesPhysicalPort_Object = MibTableColumn
rsBWMCurrentRulesPhysicalPort = _RsBWMCurrentRulesPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 8),
    _RsBWMCurrentRulesPhysicalPort_Type()
)
rsBWMCurrentRulesPhysicalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesPhysicalPort.setStatus("mandatory")


class _RsBWMCurrentRulesType_Type(Integer32):
    """Custom type rsBWMCurrentRulesType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("counter", 2),
          ("facsBandwidth", 1),
          ("ids", 3))
    )


_RsBWMCurrentRulesType_Type.__name__ = "Integer32"
_RsBWMCurrentRulesType_Object = MibTableColumn
rsBWMCurrentRulesType = _RsBWMCurrentRulesType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 9),
    _RsBWMCurrentRulesType_Type()
)
rsBWMCurrentRulesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesType.setStatus("mandatory")


class _RsBWMCurrentRulesDescription_Type(DisplayString):
    """Custom type rsBWMCurrentRulesDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsBWMCurrentRulesDescription_Type.__name__ = "DisplayString"
_RsBWMCurrentRulesDescription_Object = MibTableColumn
rsBWMCurrentRulesDescription = _RsBWMCurrentRulesDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 10),
    _RsBWMCurrentRulesDescription_Type()
)
rsBWMCurrentRulesDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesDescription.setStatus("mandatory")
_RsBWMCurrentRulesGuaranteedBW_Type = Counter32
_RsBWMCurrentRulesGuaranteedBW_Object = MibTableColumn
rsBWMCurrentRulesGuaranteedBW = _RsBWMCurrentRulesGuaranteedBW_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 11),
    _RsBWMCurrentRulesGuaranteedBW_Type()
)
rsBWMCurrentRulesGuaranteedBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesGuaranteedBW.setStatus("mandatory")
_RsBWMCurrentRulesMaxBW_Type = Counter32
_RsBWMCurrentRulesMaxBW_Object = MibTableColumn
rsBWMCurrentRulesMaxBW = _RsBWMCurrentRulesMaxBW_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 12),
    _RsBWMCurrentRulesMaxBW_Type()
)
rsBWMCurrentRulesMaxBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesMaxBW.setStatus("mandatory")


class _RsBWMCurrentRulesPolicyType_Type(Integer32):
    """Custom type rsBWMCurrentRulesPolicyType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("filter", 2),
          ("group", 3),
          ("none", 1),
          ("policy", 4))
    )


_RsBWMCurrentRulesPolicyType_Type.__name__ = "Integer32"
_RsBWMCurrentRulesPolicyType_Object = MibTableColumn
rsBWMCurrentRulesPolicyType = _RsBWMCurrentRulesPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 13),
    _RsBWMCurrentRulesPolicyType_Type()
)
rsBWMCurrentRulesPolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesPolicyType.setStatus("mandatory")


class _RsBWMCurrentRulesPolicy_Type(DisplayString):
    """Custom type rsBWMCurrentRulesPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsBWMCurrentRulesPolicy_Type.__name__ = "DisplayString"
_RsBWMCurrentRulesPolicy_Object = MibTableColumn
rsBWMCurrentRulesPolicy = _RsBWMCurrentRulesPolicy_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 14),
    _RsBWMCurrentRulesPolicy_Type()
)
rsBWMCurrentRulesPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesPolicy.setStatus("mandatory")


class _RsBWMCurrentRulesDSCPMarking_Type(Integer32):
    """Custom type rsBWMCurrentRulesDSCPMarking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_RsBWMCurrentRulesDSCPMarking_Type.__name__ = "Integer32"
_RsBWMCurrentRulesDSCPMarking_Object = MibTableColumn
rsBWMCurrentRulesDSCPMarking = _RsBWMCurrentRulesDSCPMarking_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 15),
    _RsBWMCurrentRulesDSCPMarking_Type()
)
rsBWMCurrentRulesDSCPMarking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesDSCPMarking.setStatus("mandatory")


class _RsBWMCurrentRulesReportBlockedPackets_Type(Integer32):
    """Custom type rsBWMCurrentRulesReportBlockedPackets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RsBWMCurrentRulesReportBlockedPackets_Type.__name__ = "Integer32"
_RsBWMCurrentRulesReportBlockedPackets_Object = MibTableColumn
rsBWMCurrentRulesReportBlockedPackets = _RsBWMCurrentRulesReportBlockedPackets_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 16),
    _RsBWMCurrentRulesReportBlockedPackets_Type()
)
rsBWMCurrentRulesReportBlockedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesReportBlockedPackets.setStatus("mandatory")
_RsBWMDummy4_Type = Integer32
_RsBWMDummy4_Object = MibScalar
rsBWMDummy4 = _RsBWMDummy4_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 2),
    _RsBWMDummy4_Type()
)
rsBWMDummy4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMDummy4.setStatus("mandatory")
_RsBWMCurrentRulesIPObjectTable_Object = MibTable
rsBWMCurrentRulesIPObjectTable = _RsBWMCurrentRulesIPObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 10)
)
if mibBuilder.loadTexts:
    rsBWMCurrentRulesIPObjectTable.setStatus("mandatory")
_RsBWMCurrentRulesIPObjectEntry_Object = MibTableRow
rsBWMCurrentRulesIPObjectEntry = _RsBWMCurrentRulesIPObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 10, 1)
)
rsBWMCurrentRulesIPObjectEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMCurrentRulesIPObjectName"),
    (0, "BWM-MIB", "rsBWMCurrentRulesIPObjectSubIndex"),
)
if mibBuilder.loadTexts:
    rsBWMCurrentRulesIPObjectEntry.setStatus("mandatory")


class _RsBWMCurrentRulesIPObjectName_Type(DisplayString):
    """Custom type rsBWMCurrentRulesIPObjectName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsBWMCurrentRulesIPObjectName_Type.__name__ = "DisplayString"
_RsBWMCurrentRulesIPObjectName_Object = MibTableColumn
rsBWMCurrentRulesIPObjectName = _RsBWMCurrentRulesIPObjectName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 10, 1, 1),
    _RsBWMCurrentRulesIPObjectName_Type()
)
rsBWMCurrentRulesIPObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesIPObjectName.setStatus("mandatory")
_RsBWMCurrentRulesIPObjectSubIndex_Type = Integer32
_RsBWMCurrentRulesIPObjectSubIndex_Object = MibTableColumn
rsBWMCurrentRulesIPObjectSubIndex = _RsBWMCurrentRulesIPObjectSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 10, 1, 2),
    _RsBWMCurrentRulesIPObjectSubIndex_Type()
)
rsBWMCurrentRulesIPObjectSubIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesIPObjectSubIndex.setStatus("mandatory")
_RsBWMCurrentRulesIPObjectAddress_Type = IpAddress
_RsBWMCurrentRulesIPObjectAddress_Object = MibTableColumn
rsBWMCurrentRulesIPObjectAddress = _RsBWMCurrentRulesIPObjectAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 10, 1, 3),
    _RsBWMCurrentRulesIPObjectAddress_Type()
)
rsBWMCurrentRulesIPObjectAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesIPObjectAddress.setStatus("mandatory")
_RsBWMCurrentRulesIPObjectMask_Type = IpAddress
_RsBWMCurrentRulesIPObjectMask_Object = MibTableColumn
rsBWMCurrentRulesIPObjectMask = _RsBWMCurrentRulesIPObjectMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 10, 1, 4),
    _RsBWMCurrentRulesIPObjectMask_Type()
)
rsBWMCurrentRulesIPObjectMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesIPObjectMask.setStatus("mandatory")
_RsBWMCurrentRulesIPObjectFromIP_Type = IpAddress
_RsBWMCurrentRulesIPObjectFromIP_Object = MibTableColumn
rsBWMCurrentRulesIPObjectFromIP = _RsBWMCurrentRulesIPObjectFromIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 10, 1, 5),
    _RsBWMCurrentRulesIPObjectFromIP_Type()
)
rsBWMCurrentRulesIPObjectFromIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesIPObjectFromIP.setStatus("mandatory")
_RsBWMCurrentRulesIPObjectToIP_Type = IpAddress
_RsBWMCurrentRulesIPObjectToIP_Object = MibTableColumn
rsBWMCurrentRulesIPObjectToIP = _RsBWMCurrentRulesIPObjectToIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 10, 1, 6),
    _RsBWMCurrentRulesIPObjectToIP_Type()
)
rsBWMCurrentRulesIPObjectToIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesIPObjectToIP.setStatus("mandatory")


class _RsBWMCurrentRulesIPObjectMode_Type(Integer32):
    """Custom type rsBWMCurrentRulesIPObjectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipMask", 1),
          ("ipRange", 2))
    )


_RsBWMCurrentRulesIPObjectMode_Type.__name__ = "Integer32"
_RsBWMCurrentRulesIPObjectMode_Object = MibTableColumn
rsBWMCurrentRulesIPObjectMode = _RsBWMCurrentRulesIPObjectMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 10, 1, 7),
    _RsBWMCurrentRulesIPObjectMode_Type()
)
rsBWMCurrentRulesIPObjectMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesIPObjectMode.setStatus("mandatory")
_RsBWMDummy5_Type = Integer32
_RsBWMDummy5_Object = MibScalar
rsBWMDummy5 = _RsBWMDummy5_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 10, 2),
    _RsBWMDummy5_Type()
)
rsBWMDummy5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMDummy5.setStatus("mandatory")


class _RsBWMClassificationMode_Type(Integer32):
    """Custom type rsBWMClassificationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("diffserv", 3),
          ("disabled", 2),
          ("policies", 1),
          ("tos", 4))
    )


_RsBWMClassificationMode_Type.__name__ = "Integer32"
_RsBWMClassificationMode_Object = MibScalar
rsBWMClassificationMode = _RsBWMClassificationMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 11),
    _RsBWMClassificationMode_Type()
)
rsBWMClassificationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMClassificationMode.setStatus("mandatory")
_RsBWMMaximumBandwidth_Type = Counter32
_RsBWMMaximumBandwidth_Object = MibScalar
rsBWMMaximumBandwidth = _RsBWMMaximumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 12),
    _RsBWMMaximumBandwidth_Type()
)
rsBWMMaximumBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMMaximumBandwidth.setStatus("mandatory")


class _RsBWMBandwidthBorrowingMode_Type(Integer32):
    """Custom type rsBWMBandwidthBorrowingMode based on Integer32"""
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


_RsBWMBandwidthBorrowingMode_Type.__name__ = "Integer32"
_RsBWMBandwidthBorrowingMode_Object = MibScalar
rsBWMBandwidthBorrowingMode = _RsBWMBandwidthBorrowingMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 13),
    _RsBWMBandwidthBorrowingMode_Type()
)
rsBWMBandwidthBorrowingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMBandwidthBorrowingMode.setStatus("mandatory")


class _RsBWMActions_Type(Integer32):
    """Custom type rsBWMActions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("defaultDSCPs", 2),
          ("updateRules", 1))
    )


_RsBWMActions_Type.__name__ = "Integer32"
_RsBWMActions_Object = MibScalar
rsBWMActions = _RsBWMActions_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 14),
    _RsBWMActions_Type()
)
rsBWMActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMActions.setStatus("mandatory")
_RsBWMFilterEntryTable_Object = MibTable
rsBWMFilterEntryTable = _RsBWMFilterEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15)
)
if mibBuilder.loadTexts:
    rsBWMFilterEntryTable.setStatus("mandatory")
_RsBWMFilterEntry_Object = MibTableRow
rsBWMFilterEntry = _RsBWMFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1)
)
rsBWMFilterEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMFilterName"),
)
if mibBuilder.loadTexts:
    rsBWMFilterEntry.setStatus("mandatory")


class _RsBWMFilterName_Type(DisplayString):
    """Custom type rsBWMFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsBWMFilterName_Type.__name__ = "DisplayString"
_RsBWMFilterName_Object = MibTableColumn
rsBWMFilterName = _RsBWMFilterName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 1),
    _RsBWMFilterName_Type()
)
rsBWMFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMFilterName.setStatus("mandatory")


class _RsBWMFilterDescription_Type(DisplayString):
    """Custom type rsBWMFilterDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsBWMFilterDescription_Type.__name__ = "DisplayString"
_RsBWMFilterDescription_Object = MibTableColumn
rsBWMFilterDescription = _RsBWMFilterDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 2),
    _RsBWMFilterDescription_Type()
)
rsBWMFilterDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterDescription.setStatus("mandatory")


class _RsBWMFilterProtocol_Type(Integer32):
    """Custom type rsBWMFilterProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("tcp", 2),
          ("udp", 3))
    )


_RsBWMFilterProtocol_Type.__name__ = "Integer32"
_RsBWMFilterProtocol_Object = MibTableColumn
rsBWMFilterProtocol = _RsBWMFilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 3),
    _RsBWMFilterProtocol_Type()
)
rsBWMFilterProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterProtocol.setStatus("mandatory")
_RsBWMFilterDestinationPort_Type = Integer32
_RsBWMFilterDestinationPort_Object = MibTableColumn
rsBWMFilterDestinationPort = _RsBWMFilterDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 4),
    _RsBWMFilterDestinationPort_Type()
)
rsBWMFilterDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterDestinationPort.setStatus("mandatory")
_RsBWMFilterSourceFromPort_Type = Integer32
_RsBWMFilterSourceFromPort_Object = MibTableColumn
rsBWMFilterSourceFromPort = _RsBWMFilterSourceFromPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 5),
    _RsBWMFilterSourceFromPort_Type()
)
rsBWMFilterSourceFromPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterSourceFromPort.setStatus("mandatory")
_RsBWMFilterSourceToPort_Type = Integer32
_RsBWMFilterSourceToPort_Object = MibTableColumn
rsBWMFilterSourceToPort = _RsBWMFilterSourceToPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 6),
    _RsBWMFilterSourceToPort_Type()
)
rsBWMFilterSourceToPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterSourceToPort.setStatus("mandatory")
_RsBWMFilterOMPCOffset_Type = Integer32
_RsBWMFilterOMPCOffset_Object = MibTableColumn
rsBWMFilterOMPCOffset = _RsBWMFilterOMPCOffset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 7),
    _RsBWMFilterOMPCOffset_Type()
)
rsBWMFilterOMPCOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterOMPCOffset.setStatus("mandatory")


class _RsBWMFilterOMPCMask_Type(OctetString):
    """Custom type rsBWMFilterOMPCMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RsBWMFilterOMPCMask_Type.__name__ = "OctetString"
_RsBWMFilterOMPCMask_Object = MibTableColumn
rsBWMFilterOMPCMask = _RsBWMFilterOMPCMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 8),
    _RsBWMFilterOMPCMask_Type()
)
rsBWMFilterOMPCMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterOMPCMask.setStatus("mandatory")


class _RsBWMFilterOMPCPattern_Type(OctetString):
    """Custom type rsBWMFilterOMPCPattern based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RsBWMFilterOMPCPattern_Type.__name__ = "OctetString"
_RsBWMFilterOMPCPattern_Object = MibTableColumn
rsBWMFilterOMPCPattern = _RsBWMFilterOMPCPattern_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 9),
    _RsBWMFilterOMPCPattern_Type()
)
rsBWMFilterOMPCPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterOMPCPattern.setStatus("mandatory")


class _RsBWMFilterOMPCCondition_Type(Integer32):
    """Custom type rsBWMFilterOMPCCondition based on Integer32"""
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
        *(("equal", 2),
          ("greaterThan", 4),
          ("lessThan", 5),
          ("notApplicable", 1),
          ("notEqual", 3))
    )


_RsBWMFilterOMPCCondition_Type.__name__ = "Integer32"
_RsBWMFilterOMPCCondition_Object = MibTableColumn
rsBWMFilterOMPCCondition = _RsBWMFilterOMPCCondition_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 10),
    _RsBWMFilterOMPCCondition_Type()
)
rsBWMFilterOMPCCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterOMPCCondition.setStatus("mandatory")


class _RsBWMFilterOMPCLength_Type(Integer32):
    """Custom type rsBWMFilterOMPCLength based on Integer32"""
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
        *(("fourBytes", 4),
          ("notApplicable", 5),
          ("oneByte", 1),
          ("threeBytes", 3),
          ("twoBytes", 2))
    )


_RsBWMFilterOMPCLength_Type.__name__ = "Integer32"
_RsBWMFilterOMPCLength_Object = MibTableColumn
rsBWMFilterOMPCLength = _RsBWMFilterOMPCLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 11),
    _RsBWMFilterOMPCLength_Type()
)
rsBWMFilterOMPCLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterOMPCLength.setStatus("mandatory")
_RsBWMFilterContentOffset_Type = Integer32
_RsBWMFilterContentOffset_Object = MibTableColumn
rsBWMFilterContentOffset = _RsBWMFilterContentOffset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 12),
    _RsBWMFilterContentOffset_Type()
)
rsBWMFilterContentOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterContentOffset.setStatus("mandatory")


class _RsBWMFilterContent_Type(DisplayString):
    """Custom type rsBWMFilterContent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RsBWMFilterContent_Type.__name__ = "DisplayString"
_RsBWMFilterContent_Object = MibTableColumn
rsBWMFilterContent = _RsBWMFilterContent_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 13),
    _RsBWMFilterContent_Type()
)
rsBWMFilterContent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterContent.setStatus("mandatory")


class _RsBWMFilterContentType_Type(Integer32):
    """Custom type rsBWMFilterContentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("text", 3),
          ("url", 2))
    )


_RsBWMFilterContentType_Type.__name__ = "Integer32"
_RsBWMFilterContentType_Object = MibTableColumn
rsBWMFilterContentType = _RsBWMFilterContentType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 14),
    _RsBWMFilterContentType_Type()
)
rsBWMFilterContentType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterContentType.setStatus("mandatory")


class _RsBWMFilterType_Type(Integer32):
    """Custom type rsBWMFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ids", 3),
          ("idsStatic", 4),
          ("regular", 1),
          ("static", 2))
    )


_RsBWMFilterType_Type.__name__ = "Integer32"
_RsBWMFilterType_Object = MibTableColumn
rsBWMFilterType = _RsBWMFilterType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 15),
    _RsBWMFilterType_Type()
)
rsBWMFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterType.setStatus("mandatory")
_RsBWMFilterStatus_Type = RowStatus
_RsBWMFilterStatus_Object = MibTableColumn
rsBWMFilterStatus = _RsBWMFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 16),
    _RsBWMFilterStatus_Type()
)
rsBWMFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterStatus.setStatus("mandatory")
_RsBWMDummy6_Type = Integer32
_RsBWMDummy6_Object = MibScalar
rsBWMDummy6 = _RsBWMDummy6_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 2),
    _RsBWMDummy6_Type()
)
rsBWMDummy6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMDummy6.setStatus("mandatory")
_RsBWMCurrentFilterEntryTable_Object = MibTable
rsBWMCurrentFilterEntryTable = _RsBWMCurrentFilterEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16)
)
if mibBuilder.loadTexts:
    rsBWMCurrentFilterEntryTable.setStatus("mandatory")
_RsBWMCurrentFilterEntry_Object = MibTableRow
rsBWMCurrentFilterEntry = _RsBWMCurrentFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1)
)
rsBWMCurrentFilterEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMCurrentFilterName"),
)
if mibBuilder.loadTexts:
    rsBWMCurrentFilterEntry.setStatus("mandatory")


class _RsBWMCurrentFilterName_Type(DisplayString):
    """Custom type rsBWMCurrentFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsBWMCurrentFilterName_Type.__name__ = "DisplayString"
_RsBWMCurrentFilterName_Object = MibTableColumn
rsBWMCurrentFilterName = _RsBWMCurrentFilterName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 1),
    _RsBWMCurrentFilterName_Type()
)
rsBWMCurrentFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterName.setStatus("mandatory")


class _RsBWMCurrentFilterDescription_Type(DisplayString):
    """Custom type rsBWMCurrentFilterDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsBWMCurrentFilterDescription_Type.__name__ = "DisplayString"
_RsBWMCurrentFilterDescription_Object = MibTableColumn
rsBWMCurrentFilterDescription = _RsBWMCurrentFilterDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 2),
    _RsBWMCurrentFilterDescription_Type()
)
rsBWMCurrentFilterDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterDescription.setStatus("mandatory")


class _RsBWMCurrentFilterProtocol_Type(Integer32):
    """Custom type rsBWMCurrentFilterProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("tcp", 2),
          ("udp", 3))
    )


_RsBWMCurrentFilterProtocol_Type.__name__ = "Integer32"
_RsBWMCurrentFilterProtocol_Object = MibTableColumn
rsBWMCurrentFilterProtocol = _RsBWMCurrentFilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 3),
    _RsBWMCurrentFilterProtocol_Type()
)
rsBWMCurrentFilterProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterProtocol.setStatus("mandatory")
_RsBWMCurrentFilterDestinationPort_Type = Integer32
_RsBWMCurrentFilterDestinationPort_Object = MibTableColumn
rsBWMCurrentFilterDestinationPort = _RsBWMCurrentFilterDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 4),
    _RsBWMCurrentFilterDestinationPort_Type()
)
rsBWMCurrentFilterDestinationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterDestinationPort.setStatus("mandatory")
_RsBWMCurrentFilterSourceFromPort_Type = Integer32
_RsBWMCurrentFilterSourceFromPort_Object = MibTableColumn
rsBWMCurrentFilterSourceFromPort = _RsBWMCurrentFilterSourceFromPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 5),
    _RsBWMCurrentFilterSourceFromPort_Type()
)
rsBWMCurrentFilterSourceFromPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterSourceFromPort.setStatus("mandatory")
_RsBWMCurrentFilterSourceToPort_Type = Integer32
_RsBWMCurrentFilterSourceToPort_Object = MibTableColumn
rsBWMCurrentFilterSourceToPort = _RsBWMCurrentFilterSourceToPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 6),
    _RsBWMCurrentFilterSourceToPort_Type()
)
rsBWMCurrentFilterSourceToPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterSourceToPort.setStatus("mandatory")
_RsBWMCurrentFilterOMPCOffset_Type = Integer32
_RsBWMCurrentFilterOMPCOffset_Object = MibTableColumn
rsBWMCurrentFilterOMPCOffset = _RsBWMCurrentFilterOMPCOffset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 7),
    _RsBWMCurrentFilterOMPCOffset_Type()
)
rsBWMCurrentFilterOMPCOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterOMPCOffset.setStatus("mandatory")


class _RsBWMCurrentFilterOMPCMask_Type(OctetString):
    """Custom type rsBWMCurrentFilterOMPCMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RsBWMCurrentFilterOMPCMask_Type.__name__ = "OctetString"
_RsBWMCurrentFilterOMPCMask_Object = MibTableColumn
rsBWMCurrentFilterOMPCMask = _RsBWMCurrentFilterOMPCMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 8),
    _RsBWMCurrentFilterOMPCMask_Type()
)
rsBWMCurrentFilterOMPCMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterOMPCMask.setStatus("mandatory")


class _RsBWMCurrentFilterOMPCPattern_Type(OctetString):
    """Custom type rsBWMCurrentFilterOMPCPattern based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RsBWMCurrentFilterOMPCPattern_Type.__name__ = "OctetString"
_RsBWMCurrentFilterOMPCPattern_Object = MibTableColumn
rsBWMCurrentFilterOMPCPattern = _RsBWMCurrentFilterOMPCPattern_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 9),
    _RsBWMCurrentFilterOMPCPattern_Type()
)
rsBWMCurrentFilterOMPCPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterOMPCPattern.setStatus("mandatory")


class _RsBWMCurrentFilterOMPCCondition_Type(Integer32):
    """Custom type rsBWMCurrentFilterOMPCCondition based on Integer32"""
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
        *(("equal", 2),
          ("greaterThan", 4),
          ("lessThan", 5),
          ("notApplicable", 1),
          ("notEqual", 3))
    )


_RsBWMCurrentFilterOMPCCondition_Type.__name__ = "Integer32"
_RsBWMCurrentFilterOMPCCondition_Object = MibTableColumn
rsBWMCurrentFilterOMPCCondition = _RsBWMCurrentFilterOMPCCondition_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 10),
    _RsBWMCurrentFilterOMPCCondition_Type()
)
rsBWMCurrentFilterOMPCCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterOMPCCondition.setStatus("mandatory")


class _RsBWMCurrentFilterOMPCLength_Type(Integer32):
    """Custom type rsBWMCurrentFilterOMPCLength based on Integer32"""
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
        *(("fourBytes", 4),
          ("notApplicable", 5),
          ("oneByte", 1),
          ("threeBytes", 3),
          ("twoBytes", 2))
    )


_RsBWMCurrentFilterOMPCLength_Type.__name__ = "Integer32"
_RsBWMCurrentFilterOMPCLength_Object = MibTableColumn
rsBWMCurrentFilterOMPCLength = _RsBWMCurrentFilterOMPCLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 11),
    _RsBWMCurrentFilterOMPCLength_Type()
)
rsBWMCurrentFilterOMPCLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterOMPCLength.setStatus("mandatory")
_RsBWMCurrentFilterContentOffset_Type = Integer32
_RsBWMCurrentFilterContentOffset_Object = MibTableColumn
rsBWMCurrentFilterContentOffset = _RsBWMCurrentFilterContentOffset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 12),
    _RsBWMCurrentFilterContentOffset_Type()
)
rsBWMCurrentFilterContentOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterContentOffset.setStatus("mandatory")


class _RsBWMCurrentFilterContent_Type(DisplayString):
    """Custom type rsBWMCurrentFilterContent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RsBWMCurrentFilterContent_Type.__name__ = "DisplayString"
_RsBWMCurrentFilterContent_Object = MibTableColumn
rsBWMCurrentFilterContent = _RsBWMCurrentFilterContent_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 13),
    _RsBWMCurrentFilterContent_Type()
)
rsBWMCurrentFilterContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterContent.setStatus("mandatory")


class _RsBWMCurrentFilterContentType_Type(Integer32):
    """Custom type rsBWMCurrentFilterContentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("text", 3),
          ("url", 2))
    )


_RsBWMCurrentFilterContentType_Type.__name__ = "Integer32"
_RsBWMCurrentFilterContentType_Object = MibTableColumn
rsBWMCurrentFilterContentType = _RsBWMCurrentFilterContentType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 14),
    _RsBWMCurrentFilterContentType_Type()
)
rsBWMCurrentFilterContentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterContentType.setStatus("mandatory")


class _RsBWMCurrentFilterType_Type(Integer32):
    """Custom type rsBWMCurrentFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ids", 3),
          ("idsStatic", 4),
          ("regular", 1),
          ("static", 2))
    )


_RsBWMCurrentFilterType_Type.__name__ = "Integer32"
_RsBWMCurrentFilterType_Object = MibTableColumn
rsBWMCurrentFilterType = _RsBWMCurrentFilterType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 15),
    _RsBWMCurrentFilterType_Type()
)
rsBWMCurrentFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterType.setStatus("mandatory")
_RsBWMDummy7_Type = Integer32
_RsBWMDummy7_Object = MibScalar
rsBWMDummy7 = _RsBWMDummy7_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 2),
    _RsBWMDummy7_Type()
)
rsBWMDummy7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMDummy7.setStatus("mandatory")
_RsBWMFilterGroupTable_Object = MibTable
rsBWMFilterGroupTable = _RsBWMFilterGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 17)
)
if mibBuilder.loadTexts:
    rsBWMFilterGroupTable.setStatus("mandatory")
_RsBWMFilterGroup_Object = MibTableRow
rsBWMFilterGroup = _RsBWMFilterGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 17, 1)
)
rsBWMFilterGroup.setIndexNames(
    (0, "BWM-MIB", "rsBWMFilterGroupName"),
    (0, "BWM-MIB", "rsBWMFilterEntryName"),
)
if mibBuilder.loadTexts:
    rsBWMFilterGroup.setStatus("mandatory")


class _RsBWMFilterGroupName_Type(DisplayString):
    """Custom type rsBWMFilterGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsBWMFilterGroupName_Type.__name__ = "DisplayString"
_RsBWMFilterGroupName_Object = MibTableColumn
rsBWMFilterGroupName = _RsBWMFilterGroupName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 17, 1, 1),
    _RsBWMFilterGroupName_Type()
)
rsBWMFilterGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMFilterGroupName.setStatus("mandatory")


class _RsBWMFilterEntryName_Type(DisplayString):
    """Custom type rsBWMFilterEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsBWMFilterEntryName_Type.__name__ = "DisplayString"
_RsBWMFilterEntryName_Object = MibTableColumn
rsBWMFilterEntryName = _RsBWMFilterEntryName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 17, 1, 2),
    _RsBWMFilterEntryName_Type()
)
rsBWMFilterEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMFilterEntryName.setStatus("mandatory")


class _RsBWMFilterGroupType_Type(Integer32):
    """Custom type rsBWMFilterGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ids", 3),
          ("idsStatic", 4),
          ("regular", 1),
          ("static", 2))
    )


_RsBWMFilterGroupType_Type.__name__ = "Integer32"
_RsBWMFilterGroupType_Object = MibTableColumn
rsBWMFilterGroupType = _RsBWMFilterGroupType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 17, 1, 3),
    _RsBWMFilterGroupType_Type()
)
rsBWMFilterGroupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterGroupType.setStatus("mandatory")
_RsBWMFilterGroupStatus_Type = RowStatus
_RsBWMFilterGroupStatus_Object = MibTableColumn
rsBWMFilterGroupStatus = _RsBWMFilterGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 17, 1, 4),
    _RsBWMFilterGroupStatus_Type()
)
rsBWMFilterGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterGroupStatus.setStatus("mandatory")
_RsBWMDummy8_Type = Integer32
_RsBWMDummy8_Object = MibScalar
rsBWMDummy8 = _RsBWMDummy8_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 17, 2),
    _RsBWMDummy8_Type()
)
rsBWMDummy8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMDummy8.setStatus("mandatory")
_RsBWMCurrentFilterGroupTable_Object = MibTable
rsBWMCurrentFilterGroupTable = _RsBWMCurrentFilterGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 18)
)
if mibBuilder.loadTexts:
    rsBWMCurrentFilterGroupTable.setStatus("mandatory")
_RsBWMCurrentFilterGroup_Object = MibTableRow
rsBWMCurrentFilterGroup = _RsBWMCurrentFilterGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 18, 1)
)
rsBWMCurrentFilterGroup.setIndexNames(
    (0, "BWM-MIB", "rsBWMCurrentFilterGroupName"),
    (0, "BWM-MIB", "rsBWMCurrentFilterEntryName"),
)
if mibBuilder.loadTexts:
    rsBWMCurrentFilterGroup.setStatus("mandatory")


class _RsBWMCurrentFilterGroupName_Type(DisplayString):
    """Custom type rsBWMCurrentFilterGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsBWMCurrentFilterGroupName_Type.__name__ = "DisplayString"
_RsBWMCurrentFilterGroupName_Object = MibTableColumn
rsBWMCurrentFilterGroupName = _RsBWMCurrentFilterGroupName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 18, 1, 1),
    _RsBWMCurrentFilterGroupName_Type()
)
rsBWMCurrentFilterGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterGroupName.setStatus("mandatory")


class _RsBWMCurrentFilterEntryName_Type(DisplayString):
    """Custom type rsBWMCurrentFilterEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsBWMCurrentFilterEntryName_Type.__name__ = "DisplayString"
_RsBWMCurrentFilterEntryName_Object = MibTableColumn
rsBWMCurrentFilterEntryName = _RsBWMCurrentFilterEntryName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 18, 1, 2),
    _RsBWMCurrentFilterEntryName_Type()
)
rsBWMCurrentFilterEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterEntryName.setStatus("mandatory")


class _RsBWMCurrentFilterGroupType_Type(Integer32):
    """Custom type rsBWMCurrentFilterGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ids", 3),
          ("idsStatic", 4),
          ("regular", 1),
          ("static", 2))
    )


_RsBWMCurrentFilterGroupType_Type.__name__ = "Integer32"
_RsBWMCurrentFilterGroupType_Object = MibTableColumn
rsBWMCurrentFilterGroupType = _RsBWMCurrentFilterGroupType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 18, 1, 3),
    _RsBWMCurrentFilterGroupType_Type()
)
rsBWMCurrentFilterGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterGroupType.setStatus("mandatory")
_RsBWMDummy9_Type = Integer32
_RsBWMDummy9_Object = MibScalar
rsBWMDummy9 = _RsBWMDummy9_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 18, 2),
    _RsBWMDummy9_Type()
)
rsBWMDummy9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMDummy9.setStatus("mandatory")
_RsBWMFilterPolicyTable_Object = MibTable
rsBWMFilterPolicyTable = _RsBWMFilterPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 19)
)
if mibBuilder.loadTexts:
    rsBWMFilterPolicyTable.setStatus("mandatory")
_RsBWMFilterPolicyEntry_Object = MibTableRow
rsBWMFilterPolicyEntry = _RsBWMFilterPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 19, 1)
)
rsBWMFilterPolicyEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMFilterPolicyName"),
    (0, "BWM-MIB", "rsBWMFilterPolicyEntryName"),
)
if mibBuilder.loadTexts:
    rsBWMFilterPolicyEntry.setStatus("mandatory")


class _RsBWMFilterPolicyName_Type(DisplayString):
    """Custom type rsBWMFilterPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsBWMFilterPolicyName_Type.__name__ = "DisplayString"
_RsBWMFilterPolicyName_Object = MibTableColumn
rsBWMFilterPolicyName = _RsBWMFilterPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 19, 1, 1),
    _RsBWMFilterPolicyName_Type()
)
rsBWMFilterPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMFilterPolicyName.setStatus("mandatory")


class _RsBWMFilterPolicyEntryName_Type(DisplayString):
    """Custom type rsBWMFilterPolicyEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsBWMFilterPolicyEntryName_Type.__name__ = "DisplayString"
_RsBWMFilterPolicyEntryName_Object = MibTableColumn
rsBWMFilterPolicyEntryName = _RsBWMFilterPolicyEntryName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 19, 1, 2),
    _RsBWMFilterPolicyEntryName_Type()
)
rsBWMFilterPolicyEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMFilterPolicyEntryName.setStatus("mandatory")


class _RsBWMFilterPolicyType_Type(Integer32):
    """Custom type rsBWMFilterPolicyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ids", 3),
          ("idsStatic", 4),
          ("regular", 1),
          ("static", 2))
    )


_RsBWMFilterPolicyType_Type.__name__ = "Integer32"
_RsBWMFilterPolicyType_Object = MibTableColumn
rsBWMFilterPolicyType = _RsBWMFilterPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 19, 1, 3),
    _RsBWMFilterPolicyType_Type()
)
rsBWMFilterPolicyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterPolicyType.setStatus("mandatory")
_RsBWMFilterPolicyStatus_Type = RowStatus
_RsBWMFilterPolicyStatus_Object = MibTableColumn
rsBWMFilterPolicyStatus = _RsBWMFilterPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 19, 1, 4),
    _RsBWMFilterPolicyStatus_Type()
)
rsBWMFilterPolicyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterPolicyStatus.setStatus("mandatory")
_RsBWMDummy10_Type = Integer32
_RsBWMDummy10_Object = MibScalar
rsBWMDummy10 = _RsBWMDummy10_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 19, 2),
    _RsBWMDummy10_Type()
)
rsBWMDummy10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMDummy10.setStatus("mandatory")
_RsBWMCurrentFilterPolicyTable_Object = MibTable
rsBWMCurrentFilterPolicyTable = _RsBWMCurrentFilterPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 20)
)
if mibBuilder.loadTexts:
    rsBWMCurrentFilterPolicyTable.setStatus("mandatory")
_RsBWMCurrentFilterPolicyEntry_Object = MibTableRow
rsBWMCurrentFilterPolicyEntry = _RsBWMCurrentFilterPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 20, 1)
)
rsBWMCurrentFilterPolicyEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMCurrentFilterPolicyName"),
    (0, "BWM-MIB", "rsBWMCurrentFilterPolicyEntryName"),
)
if mibBuilder.loadTexts:
    rsBWMCurrentFilterPolicyEntry.setStatus("mandatory")


class _RsBWMCurrentFilterPolicyName_Type(DisplayString):
    """Custom type rsBWMCurrentFilterPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsBWMCurrentFilterPolicyName_Type.__name__ = "DisplayString"
_RsBWMCurrentFilterPolicyName_Object = MibTableColumn
rsBWMCurrentFilterPolicyName = _RsBWMCurrentFilterPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 20, 1, 1),
    _RsBWMCurrentFilterPolicyName_Type()
)
rsBWMCurrentFilterPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterPolicyName.setStatus("mandatory")


class _RsBWMCurrentFilterPolicyEntryName_Type(DisplayString):
    """Custom type rsBWMCurrentFilterPolicyEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsBWMCurrentFilterPolicyEntryName_Type.__name__ = "DisplayString"
_RsBWMCurrentFilterPolicyEntryName_Object = MibTableColumn
rsBWMCurrentFilterPolicyEntryName = _RsBWMCurrentFilterPolicyEntryName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 20, 1, 2),
    _RsBWMCurrentFilterPolicyEntryName_Type()
)
rsBWMCurrentFilterPolicyEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterPolicyEntryName.setStatus("mandatory")


class _RsBWMCurrentFilterPolicyType_Type(Integer32):
    """Custom type rsBWMCurrentFilterPolicyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ids", 3),
          ("idsStatic", 4),
          ("regular", 1),
          ("static", 2))
    )


_RsBWMCurrentFilterPolicyType_Type.__name__ = "Integer32"
_RsBWMCurrentFilterPolicyType_Object = MibTableColumn
rsBWMCurrentFilterPolicyType = _RsBWMCurrentFilterPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 20, 1, 3),
    _RsBWMCurrentFilterPolicyType_Type()
)
rsBWMCurrentFilterPolicyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterPolicyType.setStatus("mandatory")
_RsBWMDummy11_Type = Integer32
_RsBWMDummy11_Object = MibScalar
rsBWMDummy11 = _RsBWMDummy11_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 20, 2),
    _RsBWMDummy11_Type()
)
rsBWMDummy11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMDummy11.setStatus("mandatory")


class _RsBWMApplicationClassification_Type(Integer32):
    """Custom type rsBWMApplicationClassification based on Integer32"""
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


_RsBWMApplicationClassification_Type.__name__ = "Integer32"
_RsBWMApplicationClassification_Object = MibScalar
rsBWMApplicationClassification = _RsBWMApplicationClassification_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 21),
    _RsBWMApplicationClassification_Type()
)
rsBWMApplicationClassification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMApplicationClassification.setStatus("mandatory")
_RsBWMPortBandwidthEntryTable_Object = MibTable
rsBWMPortBandwidthEntryTable = _RsBWMPortBandwidthEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 22)
)
if mibBuilder.loadTexts:
    rsBWMPortBandwidthEntryTable.setStatus("mandatory")
_RsBWMPortBandwidthEntry_Object = MibTableRow
rsBWMPortBandwidthEntry = _RsBWMPortBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 22, 1)
)
rsBWMPortBandwidthEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMPortIndex"),
)
if mibBuilder.loadTexts:
    rsBWMPortBandwidthEntry.setStatus("mandatory")
_RsBWMPortIndex_Type = Integer32
_RsBWMPortIndex_Object = MibTableColumn
rsBWMPortIndex = _RsBWMPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 22, 1, 1),
    _RsBWMPortIndex_Type()
)
rsBWMPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMPortIndex.setStatus("mandatory")
_RsBWMPortBandwidth_Type = Counter32
_RsBWMPortBandwidth_Object = MibTableColumn
rsBWMPortBandwidth = _RsBWMPortBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 22, 1, 2),
    _RsBWMPortBandwidth_Type()
)
rsBWMPortBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMPortBandwidth.setStatus("mandatory")
_RsBwmPortUsedBandwidth_Type = Counter32
_RsBwmPortUsedBandwidth_Object = MibTableColumn
rsBwmPortUsedBandwidth = _RsBwmPortUsedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 22, 1, 3),
    _RsBwmPortUsedBandwidth_Type()
)
rsBwmPortUsedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBwmPortUsedBandwidth.setStatus("mandatory")
_RsBWMDummy12_Type = Integer32
_RsBWMDummy12_Object = MibScalar
rsBWMDummy12 = _RsBWMDummy12_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 22, 2),
    _RsBWMDummy12_Type()
)
rsBWMDummy12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMDummy12.setStatus("mandatory")
_RsBWMTuning_ObjectIdentity = ObjectIdentity
rsBWMTuning = _RsBWMTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23)
)
_RsBWMPolicyTuning_ObjectIdentity = ObjectIdentity
rsBWMPolicyTuning = _RsBWMPolicyTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 1)
)
_RsBWMPolicyEntries_Type = Integer32
_RsBWMPolicyEntries_Object = MibScalar
rsBWMPolicyEntries = _RsBWMPolicyEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 1, 1),
    _RsBWMPolicyEntries_Type()
)
rsBWMPolicyEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMPolicyEntries.setStatus("mandatory")
_RsBWMPolicyEntriesAfterReset_Type = Integer32
_RsBWMPolicyEntriesAfterReset_Object = MibScalar
rsBWMPolicyEntriesAfterReset = _RsBWMPolicyEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 1, 2),
    _RsBWMPolicyEntriesAfterReset_Type()
)
rsBWMPolicyEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMPolicyEntriesAfterReset.setStatus("mandatory")
_RsBWMNetworkTuning_ObjectIdentity = ObjectIdentity
rsBWMNetworkTuning = _RsBWMNetworkTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 2)
)
_RsBWMNetworkEntries_Type = Integer32
_RsBWMNetworkEntries_Object = MibScalar
rsBWMNetworkEntries = _RsBWMNetworkEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 2, 1),
    _RsBWMNetworkEntries_Type()
)
rsBWMNetworkEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMNetworkEntries.setStatus("mandatory")
_RsBWMNetworkEntriesAfterReset_Type = Integer32
_RsBWMNetworkEntriesAfterReset_Object = MibScalar
rsBWMNetworkEntriesAfterReset = _RsBWMNetworkEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 2, 2),
    _RsBWMNetworkEntriesAfterReset_Type()
)
rsBWMNetworkEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMNetworkEntriesAfterReset.setStatus("mandatory")
_RsBWMFilterTuning_ObjectIdentity = ObjectIdentity
rsBWMFilterTuning = _RsBWMFilterTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 3)
)
_RsBWMFilterEntries_Type = Integer32
_RsBWMFilterEntries_Object = MibScalar
rsBWMFilterEntries = _RsBWMFilterEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 3, 1),
    _RsBWMFilterEntries_Type()
)
rsBWMFilterEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMFilterEntries.setStatus("mandatory")
_RsBWMFilterEntriesAfterReset_Type = Integer32
_RsBWMFilterEntriesAfterReset_Object = MibScalar
rsBWMFilterEntriesAfterReset = _RsBWMFilterEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 3, 2),
    _RsBWMFilterEntriesAfterReset_Type()
)
rsBWMFilterEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterEntriesAfterReset.setStatus("mandatory")
_RsBWMAdvancedTuning_ObjectIdentity = ObjectIdentity
rsBWMAdvancedTuning = _RsBWMAdvancedTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 4)
)
_RsBWMAdvancedEntries_Type = Integer32
_RsBWMAdvancedEntries_Object = MibScalar
rsBWMAdvancedEntries = _RsBWMAdvancedEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 4, 1),
    _RsBWMAdvancedEntries_Type()
)
rsBWMAdvancedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMAdvancedEntries.setStatus("mandatory")
_RsBWMAdvancedEntriesAfterReset_Type = Integer32
_RsBWMAdvancedEntriesAfterReset_Object = MibScalar
rsBWMAdvancedEntriesAfterReset = _RsBWMAdvancedEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 4, 2),
    _RsBWMAdvancedEntriesAfterReset_Type()
)
rsBWMAdvancedEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMAdvancedEntriesAfterReset.setStatus("mandatory")
_RsBWMGroupTuning_ObjectIdentity = ObjectIdentity
rsBWMGroupTuning = _RsBWMGroupTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 5)
)
_RsBWMGroupEntries_Type = Integer32
_RsBWMGroupEntries_Object = MibScalar
rsBWMGroupEntries = _RsBWMGroupEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 5, 1),
    _RsBWMGroupEntries_Type()
)
rsBWMGroupEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMGroupEntries.setStatus("mandatory")
_RsBWMGroupEntriesAfterReset_Type = Integer32
_RsBWMGroupEntriesAfterReset_Object = MibScalar
rsBWMGroupEntriesAfterReset = _RsBWMGroupEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 5, 2),
    _RsBWMGroupEntriesAfterReset_Type()
)
rsBWMGroupEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMGroupEntriesAfterReset.setStatus("mandatory")
_RsBWMDestinationTuning_ObjectIdentity = ObjectIdentity
rsBWMDestinationTuning = _RsBWMDestinationTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 6)
)
_RsBWMDestinationEntries_Type = Integer32
_RsBWMDestinationEntries_Object = MibScalar
rsBWMDestinationEntries = _RsBWMDestinationEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 6, 1),
    _RsBWMDestinationEntries_Type()
)
rsBWMDestinationEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMDestinationEntries.setStatus("mandatory")
_RsBWMDestinationEntriesAfterReset_Type = Integer32
_RsBWMDestinationEntriesAfterReset_Object = MibScalar
rsBWMDestinationEntriesAfterReset = _RsBWMDestinationEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 6, 2),
    _RsBWMDestinationEntriesAfterReset_Type()
)
rsBWMDestinationEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMDestinationEntriesAfterReset.setStatus("mandatory")
_RsBWMSessionTuning_ObjectIdentity = ObjectIdentity
rsBWMSessionTuning = _RsBWMSessionTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 7)
)
_RsBWMSessionEntries_Type = Integer32
_RsBWMSessionEntries_Object = MibScalar
rsBWMSessionEntries = _RsBWMSessionEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 7, 1),
    _RsBWMSessionEntries_Type()
)
rsBWMSessionEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMSessionEntries.setStatus("mandatory")
_RsBWMSessionEntriesAfterReset_Type = Integer32
_RsBWMSessionEntriesAfterReset_Object = MibScalar
rsBWMSessionEntriesAfterReset = _RsBWMSessionEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 7, 2),
    _RsBWMSessionEntriesAfterReset_Type()
)
rsBWMSessionEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMSessionEntriesAfterReset.setStatus("mandatory")
_RsBWMDSCPEntryTable_Object = MibTable
rsBWMDSCPEntryTable = _RsBWMDSCPEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 24)
)
if mibBuilder.loadTexts:
    rsBWMDSCPEntryTable.setStatus("mandatory")
_RsBWMDSCPEntry_Object = MibTableRow
rsBWMDSCPEntry = _RsBWMDSCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 24, 1)
)
rsBWMDSCPEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMDSCP"),
)
if mibBuilder.loadTexts:
    rsBWMDSCPEntry.setStatus("mandatory")


class _RsBWMDSCP_Type(Integer32):
    """Custom type rsBWMDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RsBWMDSCP_Type.__name__ = "Integer32"
_RsBWMDSCP_Object = MibTableColumn
rsBWMDSCP = _RsBWMDSCP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 24, 1, 1),
    _RsBWMDSCP_Type()
)
rsBWMDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMDSCP.setStatus("mandatory")
_RsBWMDSCPPriority_Type = Integer32
_RsBWMDSCPPriority_Object = MibTableColumn
rsBWMDSCPPriority = _RsBWMDSCPPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 24, 1, 2),
    _RsBWMDSCPPriority_Type()
)
rsBWMDSCPPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMDSCPPriority.setStatus("mandatory")
_RsBWMDSCPGuaranteedBW_Type = Counter32
_RsBWMDSCPGuaranteedBW_Object = MibTableColumn
rsBWMDSCPGuaranteedBW = _RsBWMDSCPGuaranteedBW_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 24, 1, 3),
    _RsBWMDSCPGuaranteedBW_Type()
)
rsBWMDSCPGuaranteedBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMDSCPGuaranteedBW.setStatus("mandatory")
_RsBWMDSCPMaxBW_Type = Counter32
_RsBWMDSCPMaxBW_Object = MibTableColumn
rsBWMDSCPMaxBW = _RsBWMDSCPMaxBW_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 24, 1, 4),
    _RsBWMDSCPMaxBW_Type()
)
rsBWMDSCPMaxBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMDSCPMaxBW.setStatus("mandatory")
_RsBWMDummy13_Type = Integer32
_RsBWMDummy13_Object = MibScalar
rsBWMDummy13 = _RsBWMDummy13_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 24, 2),
    _RsBWMDummy13_Type()
)
rsBWMDummy13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMDummy13.setStatus("mandatory")
_RsBWMCurrentDSCPEntryTable_Object = MibTable
rsBWMCurrentDSCPEntryTable = _RsBWMCurrentDSCPEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 25)
)
if mibBuilder.loadTexts:
    rsBWMCurrentDSCPEntryTable.setStatus("mandatory")
_RsBWMCurrentDSCPEntry_Object = MibTableRow
rsBWMCurrentDSCPEntry = _RsBWMCurrentDSCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 25, 1)
)
rsBWMCurrentDSCPEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMCurrentDSCP"),
)
if mibBuilder.loadTexts:
    rsBWMCurrentDSCPEntry.setStatus("mandatory")


class _RsBWMCurrentDSCP_Type(Integer32):
    """Custom type rsBWMCurrentDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RsBWMCurrentDSCP_Type.__name__ = "Integer32"
_RsBWMCurrentDSCP_Object = MibTableColumn
rsBWMCurrentDSCP = _RsBWMCurrentDSCP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 25, 1, 1),
    _RsBWMCurrentDSCP_Type()
)
rsBWMCurrentDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentDSCP.setStatus("mandatory")
_RsBWMCurrentDSCPPriority_Type = Integer32
_RsBWMCurrentDSCPPriority_Object = MibTableColumn
rsBWMCurrentDSCPPriority = _RsBWMCurrentDSCPPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 25, 1, 2),
    _RsBWMCurrentDSCPPriority_Type()
)
rsBWMCurrentDSCPPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMCurrentDSCPPriority.setStatus("mandatory")
_RsBWMCurrentDSCPGuaranteedBW_Type = Counter32
_RsBWMCurrentDSCPGuaranteedBW_Object = MibTableColumn
rsBWMCurrentDSCPGuaranteedBW = _RsBWMCurrentDSCPGuaranteedBW_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 25, 1, 3),
    _RsBWMCurrentDSCPGuaranteedBW_Type()
)
rsBWMCurrentDSCPGuaranteedBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMCurrentDSCPGuaranteedBW.setStatus("mandatory")
_RsBWMCurrentDSCPMaxBW_Type = Counter32
_RsBWMCurrentDSCPMaxBW_Object = MibTableColumn
rsBWMCurrentDSCPMaxBW = _RsBWMCurrentDSCPMaxBW_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 25, 1, 4),
    _RsBWMCurrentDSCPMaxBW_Type()
)
rsBWMCurrentDSCPMaxBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMCurrentDSCPMaxBW.setStatus("mandatory")
_RsBWMDummy14_Type = Integer32
_RsBWMDummy14_Object = MibScalar
rsBWMDummy14 = _RsBWMDummy14_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 25, 2),
    _RsBWMDummy14_Type()
)
rsBWMDummy14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMDummy14.setStatus("mandatory")
_RsBWMVersion_Type = DisplayString
_RsBWMVersion_Object = MibScalar
rsBWMVersion = _RsBWMVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 26),
    _RsBWMVersion_Type()
)
rsBWMVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMVersion.setStatus("mandatory")
_RsBWMBwmPortOperationTable_Object = MibTable
rsBWMBwmPortOperationTable = _RsBWMBwmPortOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 27)
)
if mibBuilder.loadTexts:
    rsBWMBwmPortOperationTable.setStatus("mandatory")
_RsBWMBwmPortOperationEntry_Object = MibTableRow
rsBWMBwmPortOperationEntry = _RsBWMBwmPortOperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 27, 1)
)
rsBWMBwmPortOperationEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMBwmInboundPort"),
    (0, "BWM-MIB", "rsBWMBwmOutboundPort"),
)
if mibBuilder.loadTexts:
    rsBWMBwmPortOperationEntry.setStatus("mandatory")
_RsBWMBwmInboundPort_Type = Integer32
_RsBWMBwmInboundPort_Object = MibTableColumn
rsBWMBwmInboundPort = _RsBWMBwmInboundPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 27, 1, 1),
    _RsBWMBwmInboundPort_Type()
)
rsBWMBwmInboundPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMBwmInboundPort.setStatus("mandatory")
_RsBWMBwmOutboundPort_Type = Integer32
_RsBWMBwmOutboundPort_Object = MibTableColumn
rsBWMBwmOutboundPort = _RsBWMBwmOutboundPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 27, 1, 2),
    _RsBWMBwmOutboundPort_Type()
)
rsBWMBwmOutboundPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMBwmOutboundPort.setStatus("mandatory")


class _RsBWMBwmDirection_Type(Integer32):
    """Custom type rsBWMBwmDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneway", 1),
          ("twoway", 2))
    )


_RsBWMBwmDirection_Type.__name__ = "Integer32"
_RsBWMBwmDirection_Object = MibTableColumn
rsBWMBwmDirection = _RsBWMBwmDirection_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 27, 1, 3),
    _RsBWMBwmDirection_Type()
)
rsBWMBwmDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMBwmDirection.setStatus("mandatory")
_RsBWMBwmOperationStatus_Type = RowStatus
_RsBWMBwmOperationStatus_Object = MibTableColumn
rsBWMBwmOperationStatus = _RsBWMBwmOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 27, 1, 4),
    _RsBWMBwmOperationStatus_Type()
)
rsBWMBwmOperationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMBwmOperationStatus.setStatus("mandatory")
_RsBWMDummy15_Type = Integer32
_RsBWMDummy15_Object = MibScalar
rsBWMDummy15 = _RsBWMDummy15_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 27, 2),
    _RsBWMDummy15_Type()
)
rsBWMDummy15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMDummy15.setStatus("mandatory")
_RsBWMBwmVLANOperationTable_Object = MibTable
rsBWMBwmVLANOperationTable = _RsBWMBwmVLANOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 28)
)
if mibBuilder.loadTexts:
    rsBWMBwmVLANOperationTable.setStatus("mandatory")
_RsBWMBwmVLANOperationEntry_Object = MibTableRow
rsBWMBwmVLANOperationEntry = _RsBWMBwmVLANOperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 28, 1)
)
rsBWMBwmVLANOperationEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMBwmVLAN"),
)
if mibBuilder.loadTexts:
    rsBWMBwmVLANOperationEntry.setStatus("mandatory")
_RsBWMBwmVLAN_Type = Integer32
_RsBWMBwmVLAN_Object = MibTableColumn
rsBWMBwmVLAN = _RsBWMBwmVLAN_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 28, 1, 1),
    _RsBWMBwmVLAN_Type()
)
rsBWMBwmVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMBwmVLAN.setStatus("mandatory")
_RsBWMBwmVLANOperationStatus_Type = RowStatus
_RsBWMBwmVLANOperationStatus_Object = MibTableColumn
rsBWMBwmVLANOperationStatus = _RsBWMBwmVLANOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 28, 1, 2),
    _RsBWMBwmVLANOperationStatus_Type()
)
rsBWMBwmVLANOperationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMBwmVLANOperationStatus.setStatus("mandatory")
_RsBWMDummy16_Type = Integer32
_RsBWMDummy16_Object = MibScalar
rsBWMDummy16 = _RsBWMDummy16_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 28, 2),
    _RsBWMDummy16_Type()
)
rsBWMDummy16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMDummy16.setStatus("mandatory")
_RsBWMSessionAgingTime_Type = Integer32
_RsBWMSessionAgingTime_Object = MibScalar
rsBWMSessionAgingTime = _RsBWMSessionAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 29),
    _RsBWMSessionAgingTime_Type()
)
rsBWMSessionAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMSessionAgingTime.setStatus("mandatory")
_RsBWMStatisticsTable_Object = MibTable
rsBWMStatisticsTable = _RsBWMStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30)
)
if mibBuilder.loadTexts:
    rsBWMStatisticsTable.setStatus("mandatory")
_RsBWMStatisticsEntry_Object = MibTableRow
rsBWMStatisticsEntry = _RsBWMStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1)
)
rsBWMStatisticsEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMStatisticsPolicyName"),
)
if mibBuilder.loadTexts:
    rsBWMStatisticsEntry.setStatus("mandatory")


class _RsBWMStatisticsPolicyName_Type(DisplayString):
    """Custom type rsBWMStatisticsPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsBWMStatisticsPolicyName_Type.__name__ = "DisplayString"
_RsBWMStatisticsPolicyName_Object = MibTableColumn
rsBWMStatisticsPolicyName = _RsBWMStatisticsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 1),
    _RsBWMStatisticsPolicyName_Type()
)
rsBWMStatisticsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsPolicyName.setStatus("mandatory")
_RsBWMStatisticsBandwidthUsedLastSec_Type = Counter32
_RsBWMStatisticsBandwidthUsedLastSec_Object = MibTableColumn
rsBWMStatisticsBandwidthUsedLastSec = _RsBWMStatisticsBandwidthUsedLastSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 2),
    _RsBWMStatisticsBandwidthUsedLastSec_Type()
)
rsBWMStatisticsBandwidthUsedLastSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsBandwidthUsedLastSec.setStatus("mandatory")
_RsBWMStatisticsPacketNumberLastSec_Type = Counter32
_RsBWMStatisticsPacketNumberLastSec_Object = MibTableColumn
rsBWMStatisticsPacketNumberLastSec = _RsBWMStatisticsPacketNumberLastSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 3),
    _RsBWMStatisticsPacketNumberLastSec_Type()
)
rsBWMStatisticsPacketNumberLastSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsPacketNumberLastSec.setStatus("mandatory")
_RsBWMStatisticsFullQueueFailuresBWLastSec_Type = Counter32
_RsBWMStatisticsFullQueueFailuresBWLastSec_Object = MibTableColumn
rsBWMStatisticsFullQueueFailuresBWLastSec = _RsBWMStatisticsFullQueueFailuresBWLastSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 4),
    _RsBWMStatisticsFullQueueFailuresBWLastSec_Type()
)
rsBWMStatisticsFullQueueFailuresBWLastSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsFullQueueFailuresBWLastSec.setStatus("mandatory")
_RsBWMStatisticsAgedPacketsFailuresBWLastSec_Type = Counter32
_RsBWMStatisticsAgedPacketsFailuresBWLastSec_Object = MibTableColumn
rsBWMStatisticsAgedPacketsFailuresBWLastSec = _RsBWMStatisticsAgedPacketsFailuresBWLastSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 5),
    _RsBWMStatisticsAgedPacketsFailuresBWLastSec_Type()
)
rsBWMStatisticsAgedPacketsFailuresBWLastSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsAgedPacketsFailuresBWLastSec.setStatus("mandatory")
_RsBWMStatisticsGuaranteedReachedLastSec_Type = TruthValue
_RsBWMStatisticsGuaranteedReachedLastSec_Object = MibTableColumn
rsBWMStatisticsGuaranteedReachedLastSec = _RsBWMStatisticsGuaranteedReachedLastSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 6),
    _RsBWMStatisticsGuaranteedReachedLastSec_Type()
)
rsBWMStatisticsGuaranteedReachedLastSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsGuaranteedReachedLastSec.setStatus("mandatory")
_RsBWMStatisticsMaximumReachedLastSec_Type = TruthValue
_RsBWMStatisticsMaximumReachedLastSec_Object = MibTableColumn
rsBWMStatisticsMaximumReachedLastSec = _RsBWMStatisticsMaximumReachedLastSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 7),
    _RsBWMStatisticsMaximumReachedLastSec_Type()
)
rsBWMStatisticsMaximumReachedLastSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsMaximumReachedLastSec.setStatus("mandatory")
_RsBWMStatisticsBandwidthUsedLastPeriod_Type = Counter32
_RsBWMStatisticsBandwidthUsedLastPeriod_Object = MibTableColumn
rsBWMStatisticsBandwidthUsedLastPeriod = _RsBWMStatisticsBandwidthUsedLastPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 8),
    _RsBWMStatisticsBandwidthUsedLastPeriod_Type()
)
rsBWMStatisticsBandwidthUsedLastPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsBandwidthUsedLastPeriod.setStatus("mandatory")
_RsBWMStatisticsPeakBandwidthLastPeriod_Type = Counter32
_RsBWMStatisticsPeakBandwidthLastPeriod_Object = MibTableColumn
rsBWMStatisticsPeakBandwidthLastPeriod = _RsBWMStatisticsPeakBandwidthLastPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 9),
    _RsBWMStatisticsPeakBandwidthLastPeriod_Type()
)
rsBWMStatisticsPeakBandwidthLastPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsPeakBandwidthLastPeriod.setStatus("mandatory")
_RsBWMStatisticsPacketNumberLastPeriod_Type = Counter32
_RsBWMStatisticsPacketNumberLastPeriod_Object = MibTableColumn
rsBWMStatisticsPacketNumberLastPeriod = _RsBWMStatisticsPacketNumberLastPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 10),
    _RsBWMStatisticsPacketNumberLastPeriod_Type()
)
rsBWMStatisticsPacketNumberLastPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsPacketNumberLastPeriod.setStatus("mandatory")
_RsBWMStatisticsFullQueueFailuresBWLastPeriod_Type = Counter32
_RsBWMStatisticsFullQueueFailuresBWLastPeriod_Object = MibTableColumn
rsBWMStatisticsFullQueueFailuresBWLastPeriod = _RsBWMStatisticsFullQueueFailuresBWLastPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 11),
    _RsBWMStatisticsFullQueueFailuresBWLastPeriod_Type()
)
rsBWMStatisticsFullQueueFailuresBWLastPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsFullQueueFailuresBWLastPeriod.setStatus("mandatory")
_RsBWMStatisticsAgedPacketsFailuresBWLastPeriod_Type = Counter32
_RsBWMStatisticsAgedPacketsFailuresBWLastPeriod_Object = MibTableColumn
rsBWMStatisticsAgedPacketsFailuresBWLastPeriod = _RsBWMStatisticsAgedPacketsFailuresBWLastPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 12),
    _RsBWMStatisticsAgedPacketsFailuresBWLastPeriod_Type()
)
rsBWMStatisticsAgedPacketsFailuresBWLastPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsAgedPacketsFailuresBWLastPeriod.setStatus("mandatory")
_RsBWMStatisticsGuaranteedReachedCounterLastPeriod_Type = Integer32
_RsBWMStatisticsGuaranteedReachedCounterLastPeriod_Object = MibTableColumn
rsBWMStatisticsGuaranteedReachedCounterLastPeriod = _RsBWMStatisticsGuaranteedReachedCounterLastPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 13),
    _RsBWMStatisticsGuaranteedReachedCounterLastPeriod_Type()
)
rsBWMStatisticsGuaranteedReachedCounterLastPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsGuaranteedReachedCounterLastPeriod.setStatus("mandatory")
_RsBWMStatisticsMaximumReachedCounterLastPeriod_Type = Integer32
_RsBWMStatisticsMaximumReachedCounterLastPeriod_Object = MibTableColumn
rsBWMStatisticsMaximumReachedCounterLastPeriod = _RsBWMStatisticsMaximumReachedCounterLastPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 14),
    _RsBWMStatisticsMaximumReachedCounterLastPeriod_Type()
)
rsBWMStatisticsMaximumReachedCounterLastPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsMaximumReachedCounterLastPeriod.setStatus("mandatory")


class _RsBWMStatisticsMonitorPolicy_Type(Integer32):
    """Custom type rsBWMStatisticsMonitorPolicy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_RsBWMStatisticsMonitorPolicy_Type.__name__ = "Integer32"
_RsBWMStatisticsMonitorPolicy_Object = MibScalar
rsBWMStatisticsMonitorPolicy = _RsBWMStatisticsMonitorPolicy_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 2),
    _RsBWMStatisticsMonitorPolicy_Type()
)
rsBWMStatisticsMonitorPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMStatisticsMonitorPolicy.setStatus("mandatory")


class _RsBWMStatisticsTableUseSRP_Type(TruthValue):
    """Custom type rsBWMStatisticsTableUseSRP based on TruthValue"""


_RsBWMStatisticsTableUseSRP_Object = MibScalar
rsBWMStatisticsTableUseSRP = _RsBWMStatisticsTableUseSRP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 3),
    _RsBWMStatisticsTableUseSRP_Type()
)
rsBWMStatisticsTableUseSRP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMStatisticsTableUseSRP.setStatus("mandatory")


class _RsBWMStatisticsReportingPeriod_Type(Integer32):
    """Custom type rsBWMStatisticsReportingPeriod based on Integer32"""
    defaultValue = 60


_RsBWMStatisticsReportingPeriod_Object = MibScalar
rsBWMStatisticsReportingPeriod = _RsBWMStatisticsReportingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 4),
    _RsBWMStatisticsReportingPeriod_Type()
)
rsBWMStatisticsReportingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMStatisticsReportingPeriod.setStatus("mandatory")

# Managed Objects groups


# Notification objects

rsBWMPacketBlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 0, 1)
)
rsBWMPacketBlocked.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsBWMPacketBlocked.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BWM-MIB",
    **{"TruthValue": TruthValue,
       "RowStatus": RowStatus,
       "NetNumber": NetNumber,
       "rsBWMPacketBlocked": rsBWMPacketBlocked,
       "rsBWMRulesTable": rsBWMRulesTable,
       "rsBWMRulesEntry": rsBWMRulesEntry,
       "rsBWMRulesIndex": rsBWMRulesIndex,
       "rsBWMRulesName": rsBWMRulesName,
       "rsBWMRulesDestination": rsBWMRulesDestination,
       "rsBWMRulesSource": rsBWMRulesSource,
       "rsBWMRulesStatus": rsBWMRulesStatus,
       "rsBWMRulesAction": rsBWMRulesAction,
       "rsBWMRulesDirection": rsBWMRulesDirection,
       "rsBWMRulesPriority": rsBWMRulesPriority,
       "rsBWMRulesPhysicalPort": rsBWMRulesPhysicalPort,
       "rsBWMRulesType": rsBWMRulesType,
       "rsBWMRulesDescription": rsBWMRulesDescription,
       "rsBWMRulesGuaranteedBW": rsBWMRulesGuaranteedBW,
       "rsBWMRulesPolicyType": rsBWMRulesPolicyType,
       "rsBWMRulesPolicy": rsBWMRulesPolicy,
       "rsBWMRulesOperationalStatus": rsBWMRulesOperationalStatus,
       "rsBWMRulesDSCPMarking": rsBWMRulesDSCPMarking,
       "rsBWMRulesReportBlockedPackets": rsBWMRulesReportBlockedPackets,
       "rsBWMRulesMaxBW": rsBWMRulesMaxBW,
       "rsBWMDummy1": rsBWMDummy1,
       "rsBWMRulesIPObjectTable": rsBWMRulesIPObjectTable,
       "rsBWMRulesIPObjectEntry": rsBWMRulesIPObjectEntry,
       "rsBWMRulesIPObjectName": rsBWMRulesIPObjectName,
       "rsBWMRulesIPObjectSubIndex": rsBWMRulesIPObjectSubIndex,
       "rsBWMRulesIPObjectAddress": rsBWMRulesIPObjectAddress,
       "rsBWMRulesIPObjectMask": rsBWMRulesIPObjectMask,
       "rsBWMRulesIPObjectFromIP": rsBWMRulesIPObjectFromIP,
       "rsBWMRulesIPObjectToIP": rsBWMRulesIPObjectToIP,
       "rsBWMRulesIPObjectMode": rsBWMRulesIPObjectMode,
       "rsBWMRulesIPObjectStatus": rsBWMRulesIPObjectStatus,
       "rsBWMDummy2": rsBWMDummy2,
       "rsBWMCBQMode": rsBWMCBQMode,
       "rsBWMActualQueueSize": rsBWMActualQueueSize,
       "rsBWMAverageQueueSize": rsBWMAverageQueueSize,
       "rsBWMQueueRedDropped": rsBWMQueueRedDropped,
       "rsBWMPriorityTable": rsBWMPriorityTable,
       "rsBWMPriorityEntry": rsBWMPriorityEntry,
       "rsBWMPriority": rsBWMPriority,
       "rsBWMPacketsSent": rsBWMPacketsSent,
       "rsBWMDummy3": rsBWMDummy3,
       "rsBWMRedMode": rsBWMRedMode,
       "rsBWMCurrentRulesTable": rsBWMCurrentRulesTable,
       "rsBWMCurrentRulesEntry": rsBWMCurrentRulesEntry,
       "rsBWMCurrentRulesIndex": rsBWMCurrentRulesIndex,
       "rsBWMCurrentRulesName": rsBWMCurrentRulesName,
       "rsBWMCurrentRulesDestination": rsBWMCurrentRulesDestination,
       "rsBWMCurrentRulesSource": rsBWMCurrentRulesSource,
       "rsBWMCurrentRulesAction": rsBWMCurrentRulesAction,
       "rsBWMCurrentRulesDirection": rsBWMCurrentRulesDirection,
       "rsBWMCurrentRulesPriority": rsBWMCurrentRulesPriority,
       "rsBWMCurrentRulesPhysicalPort": rsBWMCurrentRulesPhysicalPort,
       "rsBWMCurrentRulesType": rsBWMCurrentRulesType,
       "rsBWMCurrentRulesDescription": rsBWMCurrentRulesDescription,
       "rsBWMCurrentRulesGuaranteedBW": rsBWMCurrentRulesGuaranteedBW,
       "rsBWMCurrentRulesMaxBW": rsBWMCurrentRulesMaxBW,
       "rsBWMCurrentRulesPolicyType": rsBWMCurrentRulesPolicyType,
       "rsBWMCurrentRulesPolicy": rsBWMCurrentRulesPolicy,
       "rsBWMCurrentRulesDSCPMarking": rsBWMCurrentRulesDSCPMarking,
       "rsBWMCurrentRulesReportBlockedPackets": rsBWMCurrentRulesReportBlockedPackets,
       "rsBWMDummy4": rsBWMDummy4,
       "rsBWMCurrentRulesIPObjectTable": rsBWMCurrentRulesIPObjectTable,
       "rsBWMCurrentRulesIPObjectEntry": rsBWMCurrentRulesIPObjectEntry,
       "rsBWMCurrentRulesIPObjectName": rsBWMCurrentRulesIPObjectName,
       "rsBWMCurrentRulesIPObjectSubIndex": rsBWMCurrentRulesIPObjectSubIndex,
       "rsBWMCurrentRulesIPObjectAddress": rsBWMCurrentRulesIPObjectAddress,
       "rsBWMCurrentRulesIPObjectMask": rsBWMCurrentRulesIPObjectMask,
       "rsBWMCurrentRulesIPObjectFromIP": rsBWMCurrentRulesIPObjectFromIP,
       "rsBWMCurrentRulesIPObjectToIP": rsBWMCurrentRulesIPObjectToIP,
       "rsBWMCurrentRulesIPObjectMode": rsBWMCurrentRulesIPObjectMode,
       "rsBWMDummy5": rsBWMDummy5,
       "rsBWMClassificationMode": rsBWMClassificationMode,
       "rsBWMMaximumBandwidth": rsBWMMaximumBandwidth,
       "rsBWMBandwidthBorrowingMode": rsBWMBandwidthBorrowingMode,
       "rsBWMActions": rsBWMActions,
       "rsBWMFilterEntryTable": rsBWMFilterEntryTable,
       "rsBWMFilterEntry": rsBWMFilterEntry,
       "rsBWMFilterName": rsBWMFilterName,
       "rsBWMFilterDescription": rsBWMFilterDescription,
       "rsBWMFilterProtocol": rsBWMFilterProtocol,
       "rsBWMFilterDestinationPort": rsBWMFilterDestinationPort,
       "rsBWMFilterSourceFromPort": rsBWMFilterSourceFromPort,
       "rsBWMFilterSourceToPort": rsBWMFilterSourceToPort,
       "rsBWMFilterOMPCOffset": rsBWMFilterOMPCOffset,
       "rsBWMFilterOMPCMask": rsBWMFilterOMPCMask,
       "rsBWMFilterOMPCPattern": rsBWMFilterOMPCPattern,
       "rsBWMFilterOMPCCondition": rsBWMFilterOMPCCondition,
       "rsBWMFilterOMPCLength": rsBWMFilterOMPCLength,
       "rsBWMFilterContentOffset": rsBWMFilterContentOffset,
       "rsBWMFilterContent": rsBWMFilterContent,
       "rsBWMFilterContentType": rsBWMFilterContentType,
       "rsBWMFilterType": rsBWMFilterType,
       "rsBWMFilterStatus": rsBWMFilterStatus,
       "rsBWMDummy6": rsBWMDummy6,
       "rsBWMCurrentFilterEntryTable": rsBWMCurrentFilterEntryTable,
       "rsBWMCurrentFilterEntry": rsBWMCurrentFilterEntry,
       "rsBWMCurrentFilterName": rsBWMCurrentFilterName,
       "rsBWMCurrentFilterDescription": rsBWMCurrentFilterDescription,
       "rsBWMCurrentFilterProtocol": rsBWMCurrentFilterProtocol,
       "rsBWMCurrentFilterDestinationPort": rsBWMCurrentFilterDestinationPort,
       "rsBWMCurrentFilterSourceFromPort": rsBWMCurrentFilterSourceFromPort,
       "rsBWMCurrentFilterSourceToPort": rsBWMCurrentFilterSourceToPort,
       "rsBWMCurrentFilterOMPCOffset": rsBWMCurrentFilterOMPCOffset,
       "rsBWMCurrentFilterOMPCMask": rsBWMCurrentFilterOMPCMask,
       "rsBWMCurrentFilterOMPCPattern": rsBWMCurrentFilterOMPCPattern,
       "rsBWMCurrentFilterOMPCCondition": rsBWMCurrentFilterOMPCCondition,
       "rsBWMCurrentFilterOMPCLength": rsBWMCurrentFilterOMPCLength,
       "rsBWMCurrentFilterContentOffset": rsBWMCurrentFilterContentOffset,
       "rsBWMCurrentFilterContent": rsBWMCurrentFilterContent,
       "rsBWMCurrentFilterContentType": rsBWMCurrentFilterContentType,
       "rsBWMCurrentFilterType": rsBWMCurrentFilterType,
       "rsBWMDummy7": rsBWMDummy7,
       "rsBWMFilterGroupTable": rsBWMFilterGroupTable,
       "rsBWMFilterGroup": rsBWMFilterGroup,
       "rsBWMFilterGroupName": rsBWMFilterGroupName,
       "rsBWMFilterEntryName": rsBWMFilterEntryName,
       "rsBWMFilterGroupType": rsBWMFilterGroupType,
       "rsBWMFilterGroupStatus": rsBWMFilterGroupStatus,
       "rsBWMDummy8": rsBWMDummy8,
       "rsBWMCurrentFilterGroupTable": rsBWMCurrentFilterGroupTable,
       "rsBWMCurrentFilterGroup": rsBWMCurrentFilterGroup,
       "rsBWMCurrentFilterGroupName": rsBWMCurrentFilterGroupName,
       "rsBWMCurrentFilterEntryName": rsBWMCurrentFilterEntryName,
       "rsBWMCurrentFilterGroupType": rsBWMCurrentFilterGroupType,
       "rsBWMDummy9": rsBWMDummy9,
       "rsBWMFilterPolicyTable": rsBWMFilterPolicyTable,
       "rsBWMFilterPolicyEntry": rsBWMFilterPolicyEntry,
       "rsBWMFilterPolicyName": rsBWMFilterPolicyName,
       "rsBWMFilterPolicyEntryName": rsBWMFilterPolicyEntryName,
       "rsBWMFilterPolicyType": rsBWMFilterPolicyType,
       "rsBWMFilterPolicyStatus": rsBWMFilterPolicyStatus,
       "rsBWMDummy10": rsBWMDummy10,
       "rsBWMCurrentFilterPolicyTable": rsBWMCurrentFilterPolicyTable,
       "rsBWMCurrentFilterPolicyEntry": rsBWMCurrentFilterPolicyEntry,
       "rsBWMCurrentFilterPolicyName": rsBWMCurrentFilterPolicyName,
       "rsBWMCurrentFilterPolicyEntryName": rsBWMCurrentFilterPolicyEntryName,
       "rsBWMCurrentFilterPolicyType": rsBWMCurrentFilterPolicyType,
       "rsBWMDummy11": rsBWMDummy11,
       "rsBWMApplicationClassification": rsBWMApplicationClassification,
       "rsBWMPortBandwidthEntryTable": rsBWMPortBandwidthEntryTable,
       "rsBWMPortBandwidthEntry": rsBWMPortBandwidthEntry,
       "rsBWMPortIndex": rsBWMPortIndex,
       "rsBWMPortBandwidth": rsBWMPortBandwidth,
       "rsBwmPortUsedBandwidth": rsBwmPortUsedBandwidth,
       "rsBWMDummy12": rsBWMDummy12,
       "rsBWMTuning": rsBWMTuning,
       "rsBWMPolicyTuning": rsBWMPolicyTuning,
       "rsBWMPolicyEntries": rsBWMPolicyEntries,
       "rsBWMPolicyEntriesAfterReset": rsBWMPolicyEntriesAfterReset,
       "rsBWMNetworkTuning": rsBWMNetworkTuning,
       "rsBWMNetworkEntries": rsBWMNetworkEntries,
       "rsBWMNetworkEntriesAfterReset": rsBWMNetworkEntriesAfterReset,
       "rsBWMFilterTuning": rsBWMFilterTuning,
       "rsBWMFilterEntries": rsBWMFilterEntries,
       "rsBWMFilterEntriesAfterReset": rsBWMFilterEntriesAfterReset,
       "rsBWMAdvancedTuning": rsBWMAdvancedTuning,
       "rsBWMAdvancedEntries": rsBWMAdvancedEntries,
       "rsBWMAdvancedEntriesAfterReset": rsBWMAdvancedEntriesAfterReset,
       "rsBWMGroupTuning": rsBWMGroupTuning,
       "rsBWMGroupEntries": rsBWMGroupEntries,
       "rsBWMGroupEntriesAfterReset": rsBWMGroupEntriesAfterReset,
       "rsBWMDestinationTuning": rsBWMDestinationTuning,
       "rsBWMDestinationEntries": rsBWMDestinationEntries,
       "rsBWMDestinationEntriesAfterReset": rsBWMDestinationEntriesAfterReset,
       "rsBWMSessionTuning": rsBWMSessionTuning,
       "rsBWMSessionEntries": rsBWMSessionEntries,
       "rsBWMSessionEntriesAfterReset": rsBWMSessionEntriesAfterReset,
       "rsBWMDSCPEntryTable": rsBWMDSCPEntryTable,
       "rsBWMDSCPEntry": rsBWMDSCPEntry,
       "rsBWMDSCP": rsBWMDSCP,
       "rsBWMDSCPPriority": rsBWMDSCPPriority,
       "rsBWMDSCPGuaranteedBW": rsBWMDSCPGuaranteedBW,
       "rsBWMDSCPMaxBW": rsBWMDSCPMaxBW,
       "rsBWMDummy13": rsBWMDummy13,
       "rsBWMCurrentDSCPEntryTable": rsBWMCurrentDSCPEntryTable,
       "rsBWMCurrentDSCPEntry": rsBWMCurrentDSCPEntry,
       "rsBWMCurrentDSCP": rsBWMCurrentDSCP,
       "rsBWMCurrentDSCPPriority": rsBWMCurrentDSCPPriority,
       "rsBWMCurrentDSCPGuaranteedBW": rsBWMCurrentDSCPGuaranteedBW,
       "rsBWMCurrentDSCPMaxBW": rsBWMCurrentDSCPMaxBW,
       "rsBWMDummy14": rsBWMDummy14,
       "rsBWMVersion": rsBWMVersion,
       "rsBWMBwmPortOperationTable": rsBWMBwmPortOperationTable,
       "rsBWMBwmPortOperationEntry": rsBWMBwmPortOperationEntry,
       "rsBWMBwmInboundPort": rsBWMBwmInboundPort,
       "rsBWMBwmOutboundPort": rsBWMBwmOutboundPort,
       "rsBWMBwmDirection": rsBWMBwmDirection,
       "rsBWMBwmOperationStatus": rsBWMBwmOperationStatus,
       "rsBWMDummy15": rsBWMDummy15,
       "rsBWMBwmVLANOperationTable": rsBWMBwmVLANOperationTable,
       "rsBWMBwmVLANOperationEntry": rsBWMBwmVLANOperationEntry,
       "rsBWMBwmVLAN": rsBWMBwmVLAN,
       "rsBWMBwmVLANOperationStatus": rsBWMBwmVLANOperationStatus,
       "rsBWMDummy16": rsBWMDummy16,
       "rsBWMSessionAgingTime": rsBWMSessionAgingTime,
       "rsBWMStatisticsTable": rsBWMStatisticsTable,
       "rsBWMStatisticsEntry": rsBWMStatisticsEntry,
       "rsBWMStatisticsPolicyName": rsBWMStatisticsPolicyName,
       "rsBWMStatisticsBandwidthUsedLastSec": rsBWMStatisticsBandwidthUsedLastSec,
       "rsBWMStatisticsPacketNumberLastSec": rsBWMStatisticsPacketNumberLastSec,
       "rsBWMStatisticsFullQueueFailuresBWLastSec": rsBWMStatisticsFullQueueFailuresBWLastSec,
       "rsBWMStatisticsAgedPacketsFailuresBWLastSec": rsBWMStatisticsAgedPacketsFailuresBWLastSec,
       "rsBWMStatisticsGuaranteedReachedLastSec": rsBWMStatisticsGuaranteedReachedLastSec,
       "rsBWMStatisticsMaximumReachedLastSec": rsBWMStatisticsMaximumReachedLastSec,
       "rsBWMStatisticsBandwidthUsedLastPeriod": rsBWMStatisticsBandwidthUsedLastPeriod,
       "rsBWMStatisticsPeakBandwidthLastPeriod": rsBWMStatisticsPeakBandwidthLastPeriod,
       "rsBWMStatisticsPacketNumberLastPeriod": rsBWMStatisticsPacketNumberLastPeriod,
       "rsBWMStatisticsFullQueueFailuresBWLastPeriod": rsBWMStatisticsFullQueueFailuresBWLastPeriod,
       "rsBWMStatisticsAgedPacketsFailuresBWLastPeriod": rsBWMStatisticsAgedPacketsFailuresBWLastPeriod,
       "rsBWMStatisticsGuaranteedReachedCounterLastPeriod": rsBWMStatisticsGuaranteedReachedCounterLastPeriod,
       "rsBWMStatisticsMaximumReachedCounterLastPeriod": rsBWMStatisticsMaximumReachedCounterLastPeriod,
       "rsBWMStatisticsMonitorPolicy": rsBWMStatisticsMonitorPolicy,
       "rsBWMStatisticsTableUseSRP": rsBWMStatisticsTableUseSRP,
       "rsBWMStatisticsReportingPeriod": rsBWMStatisticsReportingPeriod}
)
