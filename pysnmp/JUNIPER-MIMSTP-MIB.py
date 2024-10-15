# SNMP MIB module (JUNIPER-MIMSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-MIMSTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:44 2024
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

(jnxXstpMibs,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxXstpMibs")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

jnxMIMstMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1)
)
jnxMIMstMIB.setRevisions(
        ("2007-05-03 00:00",
         "2007-05-24 00:00",
         "2007-12-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



class BridgeId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class Timeout(Integer32, TextualConvention):
    status = "current"
    displayHint = "d4"


class EnabledStatus(Integer32, TextualConvention):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_JnxMIDot1sJuniperMst_ObjectIdentity = ObjectIdentity
jnxMIDot1sJuniperMst = _JnxMIDot1sJuniperMst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1)
)
_JnxMIMstGlobalTrace_Type = TruthValue
_JnxMIMstGlobalTrace_Object = MibScalar
jnxMIMstGlobalTrace = _JnxMIMstGlobalTrace_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 1),
    _JnxMIMstGlobalTrace_Type()
)
jnxMIMstGlobalTrace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstGlobalTrace.setStatus("current")
_JnxMIMstGlobalDebug_Type = TruthValue
_JnxMIMstGlobalDebug_Object = MibScalar
jnxMIMstGlobalDebug = _JnxMIMstGlobalDebug_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 2),
    _JnxMIMstGlobalDebug_Type()
)
jnxMIMstGlobalDebug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstGlobalDebug.setStatus("current")
_JnxMIDot1sJuniperMstTable_Object = MibTable
jnxMIDot1sJuniperMstTable = _JnxMIDot1sJuniperMstTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3)
)
if mibBuilder.loadTexts:
    jnxMIDot1sJuniperMstTable.setStatus("current")
_JnxMIDot1sJuniperMstEntry_Object = MibTableRow
jnxMIDot1sJuniperMstEntry = _JnxMIDot1sJuniperMstEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1)
)
jnxMIDot1sJuniperMstEntry.setIndexNames(
    (0, "JUNIPER-MIMSTP-MIB", "jnxMIDot1sJuniperMstContextId"),
)
if mibBuilder.loadTexts:
    jnxMIDot1sJuniperMstEntry.setStatus("current")


class _JnxMIDot1sJuniperMstContextId_Type(Integer32):
    """Custom type jnxMIDot1sJuniperMstContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxMIDot1sJuniperMstContextId_Type.__name__ = "Integer32"
_JnxMIDot1sJuniperMstContextId_Object = MibTableColumn
jnxMIDot1sJuniperMstContextId = _JnxMIDot1sJuniperMstContextId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 1),
    _JnxMIDot1sJuniperMstContextId_Type()
)
jnxMIDot1sJuniperMstContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMIDot1sJuniperMstContextId.setStatus("current")


class _JnxMIMstSystemControl_Type(Integer32):
    """Custom type jnxMIMstSystemControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shutdown", 2),
          ("start", 1))
    )


_JnxMIMstSystemControl_Type.__name__ = "Integer32"
_JnxMIMstSystemControl_Object = MibTableColumn
jnxMIMstSystemControl = _JnxMIMstSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 2),
    _JnxMIMstSystemControl_Type()
)
jnxMIMstSystemControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstSystemControl.setStatus("current")
_JnxMIMstModuleStatus_Type = EnabledStatus
_JnxMIMstModuleStatus_Object = MibTableColumn
jnxMIMstModuleStatus = _JnxMIMstModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 3),
    _JnxMIMstModuleStatus_Type()
)
jnxMIMstModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstModuleStatus.setStatus("current")


class _JnxMIMstMaxMstInstanceNumber_Type(Integer32):
    """Custom type jnxMIMstMaxMstInstanceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_JnxMIMstMaxMstInstanceNumber_Type.__name__ = "Integer32"
_JnxMIMstMaxMstInstanceNumber_Object = MibTableColumn
jnxMIMstMaxMstInstanceNumber = _JnxMIMstMaxMstInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 4),
    _JnxMIMstMaxMstInstanceNumber_Type()
)
jnxMIMstMaxMstInstanceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMaxMstInstanceNumber.setStatus("current")
_JnxMIMstNoOfMstiSupported_Type = Integer32
_JnxMIMstNoOfMstiSupported_Object = MibTableColumn
jnxMIMstNoOfMstiSupported = _JnxMIMstNoOfMstiSupported_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 5),
    _JnxMIMstNoOfMstiSupported_Type()
)
jnxMIMstNoOfMstiSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstNoOfMstiSupported.setStatus("current")


class _JnxMIMstMaxHopCount_Type(Integer32):
    """Custom type jnxMIMstMaxHopCount based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_JnxMIMstMaxHopCount_Type.__name__ = "Integer32"
_JnxMIMstMaxHopCount_Object = MibTableColumn
jnxMIMstMaxHopCount = _JnxMIMstMaxHopCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 6),
    _JnxMIMstMaxHopCount_Type()
)
jnxMIMstMaxHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMaxHopCount.setStatus("current")
_JnxMIMstBrgAddress_Type = MacAddress
_JnxMIMstBrgAddress_Object = MibTableColumn
jnxMIMstBrgAddress = _JnxMIMstBrgAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 7),
    _JnxMIMstBrgAddress_Type()
)
jnxMIMstBrgAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstBrgAddress.setStatus("current")
_JnxMIMstCistRoot_Type = BridgeId
_JnxMIMstCistRoot_Object = MibTableColumn
jnxMIMstCistRoot = _JnxMIMstCistRoot_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 8),
    _JnxMIMstCistRoot_Type()
)
jnxMIMstCistRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistRoot.setStatus("current")
_JnxMIMstCistRegionalRoot_Type = BridgeId
_JnxMIMstCistRegionalRoot_Object = MibTableColumn
jnxMIMstCistRegionalRoot = _JnxMIMstCistRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 9),
    _JnxMIMstCistRegionalRoot_Type()
)
jnxMIMstCistRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistRegionalRoot.setStatus("current")
_JnxMIMstCistRootCost_Type = Integer32
_JnxMIMstCistRootCost_Object = MibTableColumn
jnxMIMstCistRootCost = _JnxMIMstCistRootCost_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 10),
    _JnxMIMstCistRootCost_Type()
)
jnxMIMstCistRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistRootCost.setStatus("current")
_JnxMIMstCistRegionalRootCost_Type = Integer32
_JnxMIMstCistRegionalRootCost_Object = MibTableColumn
jnxMIMstCistRegionalRootCost = _JnxMIMstCistRegionalRootCost_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 11),
    _JnxMIMstCistRegionalRootCost_Type()
)
jnxMIMstCistRegionalRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistRegionalRootCost.setStatus("current")
_JnxMIMstCistRootPort_Type = Integer32
_JnxMIMstCistRootPort_Object = MibTableColumn
jnxMIMstCistRootPort = _JnxMIMstCistRootPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 12),
    _JnxMIMstCistRootPort_Type()
)
jnxMIMstCistRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistRootPort.setStatus("current")


class _JnxMIMstCistBridgePriority_Type(Integer32):
    """Custom type jnxMIMstCistBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_JnxMIMstCistBridgePriority_Type.__name__ = "Integer32"
_JnxMIMstCistBridgePriority_Object = MibTableColumn
jnxMIMstCistBridgePriority = _JnxMIMstCistBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 13),
    _JnxMIMstCistBridgePriority_Type()
)
jnxMIMstCistBridgePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistBridgePriority.setStatus("current")


class _JnxMIMstCistBridgeMaxAge_Type(Timeout):
    """Custom type jnxMIMstCistBridgeMaxAge based on Timeout"""
    defaultValue = 2000

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_JnxMIMstCistBridgeMaxAge_Type.__name__ = "Timeout"
_JnxMIMstCistBridgeMaxAge_Object = MibTableColumn
jnxMIMstCistBridgeMaxAge = _JnxMIMstCistBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 14),
    _JnxMIMstCistBridgeMaxAge_Type()
)
jnxMIMstCistBridgeMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistBridgeMaxAge.setStatus("current")


class _JnxMIMstCistBridgeForwardDelay_Type(Timeout):
    """Custom type jnxMIMstCistBridgeForwardDelay based on Timeout"""
    defaultValue = 1500

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_JnxMIMstCistBridgeForwardDelay_Type.__name__ = "Timeout"
_JnxMIMstCistBridgeForwardDelay_Object = MibTableColumn
jnxMIMstCistBridgeForwardDelay = _JnxMIMstCistBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 15),
    _JnxMIMstCistBridgeForwardDelay_Type()
)
jnxMIMstCistBridgeForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistBridgeForwardDelay.setStatus("current")
_JnxMIMstCistHoldTime_Type = Integer32
_JnxMIMstCistHoldTime_Object = MibTableColumn
jnxMIMstCistHoldTime = _JnxMIMstCistHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 16),
    _JnxMIMstCistHoldTime_Type()
)
jnxMIMstCistHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistHoldTime.setStatus("current")
_JnxMIMstCistMaxAge_Type = Timeout
_JnxMIMstCistMaxAge_Object = MibTableColumn
jnxMIMstCistMaxAge = _JnxMIMstCistMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 17),
    _JnxMIMstCistMaxAge_Type()
)
jnxMIMstCistMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistMaxAge.setStatus("current")
_JnxMIMstCistForwardDelay_Type = Timeout
_JnxMIMstCistForwardDelay_Object = MibTableColumn
jnxMIMstCistForwardDelay = _JnxMIMstCistForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 18),
    _JnxMIMstCistForwardDelay_Type()
)
jnxMIMstCistForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistForwardDelay.setStatus("current")
_JnxMIMstMstpUpCount_Type = Counter32
_JnxMIMstMstpUpCount_Object = MibTableColumn
jnxMIMstMstpUpCount = _JnxMIMstMstpUpCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 19),
    _JnxMIMstMstpUpCount_Type()
)
jnxMIMstMstpUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstpUpCount.setStatus("current")
_JnxMIMstMstpDownCount_Type = Counter32
_JnxMIMstMstpDownCount_Object = MibTableColumn
jnxMIMstMstpDownCount = _JnxMIMstMstpDownCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 20),
    _JnxMIMstMstpDownCount_Type()
)
jnxMIMstMstpDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstpDownCount.setStatus("current")


class _JnxMIMstPathCostDefaultType_Type(Integer32):
    """Custom type jnxMIMstPathCostDefaultType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stp8021d1998", 1),
          ("stp8021t2001", 2))
    )


_JnxMIMstPathCostDefaultType_Type.__name__ = "Integer32"
_JnxMIMstPathCostDefaultType_Object = MibTableColumn
jnxMIMstPathCostDefaultType = _JnxMIMstPathCostDefaultType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 21),
    _JnxMIMstPathCostDefaultType_Type()
)
jnxMIMstPathCostDefaultType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstPathCostDefaultType.setStatus("current")


class _JnxMIMstTrace_Type(Integer32):
    """Custom type jnxMIMstTrace based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxMIMstTrace_Type.__name__ = "Integer32"
_JnxMIMstTrace_Object = MibTableColumn
jnxMIMstTrace = _JnxMIMstTrace_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 22),
    _JnxMIMstTrace_Type()
)
jnxMIMstTrace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstTrace.setStatus("current")


class _JnxMIMstDebug_Type(Integer32):
    """Custom type jnxMIMstDebug based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131071),
    )


_JnxMIMstDebug_Type.__name__ = "Integer32"
_JnxMIMstDebug_Object = MibTableColumn
jnxMIMstDebug = _JnxMIMstDebug_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 23),
    _JnxMIMstDebug_Type()
)
jnxMIMstDebug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstDebug.setStatus("current")


class _JnxMIMstForceProtocolVersion_Type(Integer32):
    """Custom type jnxMIMstForceProtocolVersion based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mstp", 3),
          ("rstp", 2),
          ("stpCompatible", 0))
    )


_JnxMIMstForceProtocolVersion_Type.__name__ = "Integer32"
_JnxMIMstForceProtocolVersion_Object = MibTableColumn
jnxMIMstForceProtocolVersion = _JnxMIMstForceProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 24),
    _JnxMIMstForceProtocolVersion_Type()
)
jnxMIMstForceProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstForceProtocolVersion.setStatus("current")


class _JnxMIMstTxHoldCount_Type(Integer32):
    """Custom type jnxMIMstTxHoldCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_JnxMIMstTxHoldCount_Type.__name__ = "Integer32"
_JnxMIMstTxHoldCount_Object = MibTableColumn
jnxMIMstTxHoldCount = _JnxMIMstTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 25),
    _JnxMIMstTxHoldCount_Type()
)
jnxMIMstTxHoldCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstTxHoldCount.setStatus("current")


class _JnxMIMstMstiConfigIdSel_Type(Integer32):
    """Custom type jnxMIMstMstiConfigIdSel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxMIMstMstiConfigIdSel_Type.__name__ = "Integer32"
_JnxMIMstMstiConfigIdSel_Object = MibTableColumn
jnxMIMstMstiConfigIdSel = _JnxMIMstMstiConfigIdSel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 26),
    _JnxMIMstMstiConfigIdSel_Type()
)
jnxMIMstMstiConfigIdSel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiConfigIdSel.setStatus("current")


class _JnxMIMstMstiRegionName_Type(OctetString):
    """Custom type jnxMIMstMstiRegionName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JnxMIMstMstiRegionName_Type.__name__ = "OctetString"
_JnxMIMstMstiRegionName_Object = MibTableColumn
jnxMIMstMstiRegionName = _JnxMIMstMstiRegionName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 27),
    _JnxMIMstMstiRegionName_Type()
)
jnxMIMstMstiRegionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiRegionName.setStatus("current")


class _JnxMIMstMstiRegionVersion_Type(Integer32):
    """Custom type jnxMIMstMstiRegionVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxMIMstMstiRegionVersion_Type.__name__ = "Integer32"
_JnxMIMstMstiRegionVersion_Object = MibTableColumn
jnxMIMstMstiRegionVersion = _JnxMIMstMstiRegionVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 28),
    _JnxMIMstMstiRegionVersion_Type()
)
jnxMIMstMstiRegionVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiRegionVersion.setStatus("current")


class _JnxMIMstMstiConfigDigest_Type(OctetString):
    """Custom type jnxMIMstMstiConfigDigest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JnxMIMstMstiConfigDigest_Type.__name__ = "OctetString"
_JnxMIMstMstiConfigDigest_Object = MibTableColumn
jnxMIMstMstiConfigDigest = _JnxMIMstMstiConfigDigest_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 29),
    _JnxMIMstMstiConfigDigest_Type()
)
jnxMIMstMstiConfigDigest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiConfigDigest.setStatus("current")
_JnxMIMstBufferOverFlowCount_Type = Counter32
_JnxMIMstBufferOverFlowCount_Object = MibTableColumn
jnxMIMstBufferOverFlowCount = _JnxMIMstBufferOverFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 30),
    _JnxMIMstBufferOverFlowCount_Type()
)
jnxMIMstBufferOverFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstBufferOverFlowCount.setStatus("current")
_JnxMIMstMemAllocFailureCount_Type = Counter32
_JnxMIMstMemAllocFailureCount_Object = MibTableColumn
jnxMIMstMemAllocFailureCount = _JnxMIMstMemAllocFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 31),
    _JnxMIMstMemAllocFailureCount_Type()
)
jnxMIMstMemAllocFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMemAllocFailureCount.setStatus("current")
_JnxMIMstRegionConfigChangeCount_Type = Counter32
_JnxMIMstRegionConfigChangeCount_Object = MibTableColumn
jnxMIMstRegionConfigChangeCount = _JnxMIMstRegionConfigChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 32),
    _JnxMIMstRegionConfigChangeCount_Type()
)
jnxMIMstRegionConfigChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstRegionConfigChangeCount.setStatus("current")


class _JnxMIMstCistBridgeRoleSelectionSemState_Type(Integer32):
    """Custom type jnxMIMstCistBridgeRoleSelectionSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("initbridge", 0),
          ("roleselection", 1))
    )


_JnxMIMstCistBridgeRoleSelectionSemState_Type.__name__ = "Integer32"
_JnxMIMstCistBridgeRoleSelectionSemState_Object = MibTableColumn
jnxMIMstCistBridgeRoleSelectionSemState = _JnxMIMstCistBridgeRoleSelectionSemState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 33),
    _JnxMIMstCistBridgeRoleSelectionSemState_Type()
)
jnxMIMstCistBridgeRoleSelectionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistBridgeRoleSelectionSemState.setStatus("current")
_JnxMIMstCistTimeSinceTopologyChange_Type = TimeTicks
_JnxMIMstCistTimeSinceTopologyChange_Object = MibTableColumn
jnxMIMstCistTimeSinceTopologyChange = _JnxMIMstCistTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 34),
    _JnxMIMstCistTimeSinceTopologyChange_Type()
)
jnxMIMstCistTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistTimeSinceTopologyChange.setStatus("current")
_JnxMIMstCistTopChanges_Type = Counter32
_JnxMIMstCistTopChanges_Object = MibTableColumn
jnxMIMstCistTopChanges = _JnxMIMstCistTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 35),
    _JnxMIMstCistTopChanges_Type()
)
jnxMIMstCistTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistTopChanges.setStatus("current")
_JnxMIMstCistNewRootBridgeCount_Type = Counter32
_JnxMIMstCistNewRootBridgeCount_Object = MibTableColumn
jnxMIMstCistNewRootBridgeCount = _JnxMIMstCistNewRootBridgeCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 36),
    _JnxMIMstCistNewRootBridgeCount_Type()
)
jnxMIMstCistNewRootBridgeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistNewRootBridgeCount.setStatus("current")
_JnxMIMstCistHelloTime_Type = Timeout
_JnxMIMstCistHelloTime_Object = MibTableColumn
jnxMIMstCistHelloTime = _JnxMIMstCistHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 37),
    _JnxMIMstCistHelloTime_Type()
)
jnxMIMstCistHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistHelloTime.setStatus("current")


class _JnxMIMstCistBridgeHelloTime_Type(Timeout):
    """Custom type jnxMIMstCistBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_JnxMIMstCistBridgeHelloTime_Type.__name__ = "Timeout"
_JnxMIMstCistBridgeHelloTime_Object = MibTableColumn
jnxMIMstCistBridgeHelloTime = _JnxMIMstCistBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 38),
    _JnxMIMstCistBridgeHelloTime_Type()
)
jnxMIMstCistBridgeHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistBridgeHelloTime.setStatus("current")


class _JnxMIMstCistDynamicPathcostCalculation_Type(TruthValue):
    """Custom type jnxMIMstCistDynamicPathcostCalculation based on TruthValue"""


_JnxMIMstCistDynamicPathcostCalculation_Object = MibTableColumn
jnxMIMstCistDynamicPathcostCalculation = _JnxMIMstCistDynamicPathcostCalculation_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 3, 1, 39),
    _JnxMIMstCistDynamicPathcostCalculation_Type()
)
jnxMIMstCistDynamicPathcostCalculation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistDynamicPathcostCalculation.setStatus("current")
_JnxMIMstMstiBridgeTable_Object = MibTable
jnxMIMstMstiBridgeTable = _JnxMIMstMstiBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 4)
)
if mibBuilder.loadTexts:
    jnxMIMstMstiBridgeTable.setStatus("current")
_JnxMIMstMstiBridgeEntry_Object = MibTableRow
jnxMIMstMstiBridgeEntry = _JnxMIMstMstiBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 4, 1)
)
jnxMIMstMstiBridgeEntry.setIndexNames(
    (0, "JUNIPER-MIMSTP-MIB", "jnxMIDot1sJuniperMstContextId"),
    (0, "JUNIPER-MIMSTP-MIB", "jnxMIMstMstiInstanceIndex"),
)
if mibBuilder.loadTexts:
    jnxMIMstMstiBridgeEntry.setStatus("current")


class _JnxMIMstMstiInstanceIndex_Type(Integer32):
    """Custom type jnxMIMstMstiInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_JnxMIMstMstiInstanceIndex_Type.__name__ = "Integer32"
_JnxMIMstMstiInstanceIndex_Object = MibTableColumn
jnxMIMstMstiInstanceIndex = _JnxMIMstMstiInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 4, 1, 1),
    _JnxMIMstMstiInstanceIndex_Type()
)
jnxMIMstMstiInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiInstanceIndex.setStatus("current")
_JnxMIMstMstiBridgeRegionalRoot_Type = BridgeId
_JnxMIMstMstiBridgeRegionalRoot_Object = MibTableColumn
jnxMIMstMstiBridgeRegionalRoot = _JnxMIMstMstiBridgeRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 4, 1, 2),
    _JnxMIMstMstiBridgeRegionalRoot_Type()
)
jnxMIMstMstiBridgeRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiBridgeRegionalRoot.setStatus("current")


class _JnxMIMstMstiBridgePriority_Type(Integer32):
    """Custom type jnxMIMstMstiBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_JnxMIMstMstiBridgePriority_Type.__name__ = "Integer32"
_JnxMIMstMstiBridgePriority_Object = MibTableColumn
jnxMIMstMstiBridgePriority = _JnxMIMstMstiBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 4, 1, 3),
    _JnxMIMstMstiBridgePriority_Type()
)
jnxMIMstMstiBridgePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiBridgePriority.setStatus("current")
_JnxMIMstMstiRootCost_Type = Integer32
_JnxMIMstMstiRootCost_Object = MibTableColumn
jnxMIMstMstiRootCost = _JnxMIMstMstiRootCost_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 4, 1, 4),
    _JnxMIMstMstiRootCost_Type()
)
jnxMIMstMstiRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiRootCost.setStatus("current")
_JnxMIMstMstiRootPort_Type = Integer32
_JnxMIMstMstiRootPort_Object = MibTableColumn
jnxMIMstMstiRootPort = _JnxMIMstMstiRootPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 4, 1, 5),
    _JnxMIMstMstiRootPort_Type()
)
jnxMIMstMstiRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiRootPort.setStatus("current")
_JnxMIMstMstiTimeSinceTopologyChange_Type = TimeTicks
_JnxMIMstMstiTimeSinceTopologyChange_Object = MibTableColumn
jnxMIMstMstiTimeSinceTopologyChange = _JnxMIMstMstiTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 4, 1, 6),
    _JnxMIMstMstiTimeSinceTopologyChange_Type()
)
jnxMIMstMstiTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiTimeSinceTopologyChange.setStatus("current")
_JnxMIMstMstiTopChanges_Type = Counter32
_JnxMIMstMstiTopChanges_Object = MibTableColumn
jnxMIMstMstiTopChanges = _JnxMIMstMstiTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 4, 1, 7),
    _JnxMIMstMstiTopChanges_Type()
)
jnxMIMstMstiTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiTopChanges.setStatus("current")
_JnxMIMstMstiNewRootBridgeCount_Type = Counter32
_JnxMIMstMstiNewRootBridgeCount_Object = MibTableColumn
jnxMIMstMstiNewRootBridgeCount = _JnxMIMstMstiNewRootBridgeCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 4, 1, 8),
    _JnxMIMstMstiNewRootBridgeCount_Type()
)
jnxMIMstMstiNewRootBridgeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiNewRootBridgeCount.setStatus("current")


class _JnxMIMstMstiBridgeRoleSelectionSemState_Type(Integer32):
    """Custom type jnxMIMstMstiBridgeRoleSelectionSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("initbridge", 0),
          ("roleselection", 1))
    )


_JnxMIMstMstiBridgeRoleSelectionSemState_Type.__name__ = "Integer32"
_JnxMIMstMstiBridgeRoleSelectionSemState_Object = MibTableColumn
jnxMIMstMstiBridgeRoleSelectionSemState = _JnxMIMstMstiBridgeRoleSelectionSemState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 4, 1, 9),
    _JnxMIMstMstiBridgeRoleSelectionSemState_Type()
)
jnxMIMstMstiBridgeRoleSelectionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiBridgeRoleSelectionSemState.setStatus("current")
_JnxMIMstInstanceUpCount_Type = Counter32
_JnxMIMstInstanceUpCount_Object = MibTableColumn
jnxMIMstInstanceUpCount = _JnxMIMstInstanceUpCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 4, 1, 10),
    _JnxMIMstInstanceUpCount_Type()
)
jnxMIMstInstanceUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstInstanceUpCount.setStatus("current")
_JnxMIMstInstanceDownCount_Type = Counter32
_JnxMIMstInstanceDownCount_Object = MibTableColumn
jnxMIMstInstanceDownCount = _JnxMIMstInstanceDownCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 4, 1, 11),
    _JnxMIMstInstanceDownCount_Type()
)
jnxMIMstInstanceDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstInstanceDownCount.setStatus("current")
_JnxMIMstOldDesignatedRoot_Type = BridgeId
_JnxMIMstOldDesignatedRoot_Object = MibTableColumn
jnxMIMstOldDesignatedRoot = _JnxMIMstOldDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 4, 1, 12),
    _JnxMIMstOldDesignatedRoot_Type()
)
jnxMIMstOldDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstOldDesignatedRoot.setStatus("current")
_JnxMIMstVlanInstanceMappingTable_Object = MibTable
jnxMIMstVlanInstanceMappingTable = _JnxMIMstVlanInstanceMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 5)
)
if mibBuilder.loadTexts:
    jnxMIMstVlanInstanceMappingTable.setStatus("current")
_JnxMIMstVlanInstanceMappingEntry_Object = MibTableRow
jnxMIMstVlanInstanceMappingEntry = _JnxMIMstVlanInstanceMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 5, 1)
)
jnxMIMstVlanInstanceMappingEntry.setIndexNames(
    (0, "JUNIPER-MIMSTP-MIB", "jnxMIDot1sJuniperMstContextId"),
    (0, "JUNIPER-MIMSTP-MIB", "jnxMIMstInstanceIndex"),
)
if mibBuilder.loadTexts:
    jnxMIMstVlanInstanceMappingEntry.setStatus("current")


class _JnxMIMstInstanceIndex_Type(Integer32):
    """Custom type jnxMIMstInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_JnxMIMstInstanceIndex_Type.__name__ = "Integer32"
_JnxMIMstInstanceIndex_Object = MibTableColumn
jnxMIMstInstanceIndex = _JnxMIMstInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 5, 1, 1),
    _JnxMIMstInstanceIndex_Type()
)
jnxMIMstInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMIMstInstanceIndex.setStatus("current")
_JnxMIMstMapVlanIndex_Type = VlanId
_JnxMIMstMapVlanIndex_Object = MibTableColumn
jnxMIMstMapVlanIndex = _JnxMIMstMapVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 5, 1, 2),
    _JnxMIMstMapVlanIndex_Type()
)
jnxMIMstMapVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMapVlanIndex.setStatus("current")
_JnxMIMstUnMapVlanIndex_Type = VlanId
_JnxMIMstUnMapVlanIndex_Object = MibTableColumn
jnxMIMstUnMapVlanIndex = _JnxMIMstUnMapVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 5, 1, 3),
    _JnxMIMstUnMapVlanIndex_Type()
)
jnxMIMstUnMapVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstUnMapVlanIndex.setStatus("current")


class _JnxMIMstSetVlanList_Type(OctetString):
    """Custom type jnxMIMstSetVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_JnxMIMstSetVlanList_Type.__name__ = "OctetString"
_JnxMIMstSetVlanList_Object = MibTableColumn
jnxMIMstSetVlanList = _JnxMIMstSetVlanList_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 5, 1, 4),
    _JnxMIMstSetVlanList_Type()
)
jnxMIMstSetVlanList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstSetVlanList.setStatus("current")


class _JnxMIMstResetVlanList_Type(OctetString):
    """Custom type jnxMIMstResetVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_JnxMIMstResetVlanList_Type.__name__ = "OctetString"
_JnxMIMstResetVlanList_Object = MibTableColumn
jnxMIMstResetVlanList = _JnxMIMstResetVlanList_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 5, 1, 5),
    _JnxMIMstResetVlanList_Type()
)
jnxMIMstResetVlanList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstResetVlanList.setStatus("current")


class _JnxMIMstInstanceVlanMapped_Type(OctetString):
    """Custom type jnxMIMstInstanceVlanMapped based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JnxMIMstInstanceVlanMapped_Type.__name__ = "OctetString"
_JnxMIMstInstanceVlanMapped_Object = MibTableColumn
jnxMIMstInstanceVlanMapped = _JnxMIMstInstanceVlanMapped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 5, 1, 6),
    _JnxMIMstInstanceVlanMapped_Type()
)
jnxMIMstInstanceVlanMapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstInstanceVlanMapped.setStatus("current")


class _JnxMIMstInstanceVlanMapped2k_Type(OctetString):
    """Custom type jnxMIMstInstanceVlanMapped2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JnxMIMstInstanceVlanMapped2k_Type.__name__ = "OctetString"
_JnxMIMstInstanceVlanMapped2k_Object = MibTableColumn
jnxMIMstInstanceVlanMapped2k = _JnxMIMstInstanceVlanMapped2k_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 5, 1, 7),
    _JnxMIMstInstanceVlanMapped2k_Type()
)
jnxMIMstInstanceVlanMapped2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstInstanceVlanMapped2k.setStatus("current")


class _JnxMIMstInstanceVlanMapped3k_Type(OctetString):
    """Custom type jnxMIMstInstanceVlanMapped3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JnxMIMstInstanceVlanMapped3k_Type.__name__ = "OctetString"
_JnxMIMstInstanceVlanMapped3k_Object = MibTableColumn
jnxMIMstInstanceVlanMapped3k = _JnxMIMstInstanceVlanMapped3k_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 5, 1, 8),
    _JnxMIMstInstanceVlanMapped3k_Type()
)
jnxMIMstInstanceVlanMapped3k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstInstanceVlanMapped3k.setStatus("current")


class _JnxMIMstInstanceVlanMapped4k_Type(OctetString):
    """Custom type jnxMIMstInstanceVlanMapped4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JnxMIMstInstanceVlanMapped4k_Type.__name__ = "OctetString"
_JnxMIMstInstanceVlanMapped4k_Object = MibTableColumn
jnxMIMstInstanceVlanMapped4k = _JnxMIMstInstanceVlanMapped4k_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 5, 1, 9),
    _JnxMIMstInstanceVlanMapped4k_Type()
)
jnxMIMstInstanceVlanMapped4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstInstanceVlanMapped4k.setStatus("current")
_JnxMIMstCistPortTable_Object = MibTable
jnxMIMstCistPortTable = _JnxMIMstCistPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6)
)
if mibBuilder.loadTexts:
    jnxMIMstCistPortTable.setStatus("current")
_JnxMIMstCistPortEntry_Object = MibTableRow
jnxMIMstCistPortEntry = _JnxMIMstCistPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1)
)
jnxMIMstCistPortEntry.setIndexNames(
    (0, "JUNIPER-MIMSTP-MIB", "jnxMIMstCistPort"),
)
if mibBuilder.loadTexts:
    jnxMIMstCistPortEntry.setStatus("current")


class _JnxMIMstCistPort_Type(Integer32):
    """Custom type jnxMIMstCistPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JnxMIMstCistPort_Type.__name__ = "Integer32"
_JnxMIMstCistPort_Object = MibTableColumn
jnxMIMstCistPort = _JnxMIMstCistPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 1),
    _JnxMIMstCistPort_Type()
)
jnxMIMstCistPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMIMstCistPort.setStatus("current")


class _JnxMIMstCistPortPathCost_Type(Integer32):
    """Custom type jnxMIMstCistPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_JnxMIMstCistPortPathCost_Type.__name__ = "Integer32"
_JnxMIMstCistPortPathCost_Object = MibTableColumn
jnxMIMstCistPortPathCost = _JnxMIMstCistPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 2),
    _JnxMIMstCistPortPathCost_Type()
)
jnxMIMstCistPortPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortPathCost.setStatus("current")


class _JnxMIMstCistPortPriority_Type(Integer32):
    """Custom type jnxMIMstCistPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_JnxMIMstCistPortPriority_Type.__name__ = "Integer32"
_JnxMIMstCistPortPriority_Object = MibTableColumn
jnxMIMstCistPortPriority = _JnxMIMstCistPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 3),
    _JnxMIMstCistPortPriority_Type()
)
jnxMIMstCistPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortPriority.setStatus("current")
_JnxMIMstCistPortDesignatedRoot_Type = BridgeId
_JnxMIMstCistPortDesignatedRoot_Object = MibTableColumn
jnxMIMstCistPortDesignatedRoot = _JnxMIMstCistPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 4),
    _JnxMIMstCistPortDesignatedRoot_Type()
)
jnxMIMstCistPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortDesignatedRoot.setStatus("current")
_JnxMIMstCistPortDesignatedBridge_Type = BridgeId
_JnxMIMstCistPortDesignatedBridge_Object = MibTableColumn
jnxMIMstCistPortDesignatedBridge = _JnxMIMstCistPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 5),
    _JnxMIMstCistPortDesignatedBridge_Type()
)
jnxMIMstCistPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortDesignatedBridge.setStatus("current")


class _JnxMIMstCistPortDesignatedPort_Type(OctetString):
    """Custom type jnxMIMstCistPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_JnxMIMstCistPortDesignatedPort_Type.__name__ = "OctetString"
_JnxMIMstCistPortDesignatedPort_Object = MibTableColumn
jnxMIMstCistPortDesignatedPort = _JnxMIMstCistPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 6),
    _JnxMIMstCistPortDesignatedPort_Type()
)
jnxMIMstCistPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortDesignatedPort.setStatus("current")


class _JnxMIMstCistPortAdminP2P_Type(Integer32):
    """Custom type jnxMIMstCistPortAdminP2P based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("forceFalse", 1),
          ("forceTrue", 0))
    )


_JnxMIMstCistPortAdminP2P_Type.__name__ = "Integer32"
_JnxMIMstCistPortAdminP2P_Object = MibTableColumn
jnxMIMstCistPortAdminP2P = _JnxMIMstCistPortAdminP2P_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 7),
    _JnxMIMstCistPortAdminP2P_Type()
)
jnxMIMstCistPortAdminP2P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortAdminP2P.setStatus("current")
_JnxMIMstCistPortOperP2P_Type = TruthValue
_JnxMIMstCistPortOperP2P_Object = MibTableColumn
jnxMIMstCistPortOperP2P = _JnxMIMstCistPortOperP2P_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 8),
    _JnxMIMstCistPortOperP2P_Type()
)
jnxMIMstCistPortOperP2P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortOperP2P.setStatus("current")
_JnxMIMstCistPortAdminEdgeStatus_Type = TruthValue
_JnxMIMstCistPortAdminEdgeStatus_Object = MibTableColumn
jnxMIMstCistPortAdminEdgeStatus = _JnxMIMstCistPortAdminEdgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 9),
    _JnxMIMstCistPortAdminEdgeStatus_Type()
)
jnxMIMstCistPortAdminEdgeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortAdminEdgeStatus.setStatus("current")
_JnxMIMstCistPortOperEdgeStatus_Type = TruthValue
_JnxMIMstCistPortOperEdgeStatus_Object = MibTableColumn
jnxMIMstCistPortOperEdgeStatus = _JnxMIMstCistPortOperEdgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 10),
    _JnxMIMstCistPortOperEdgeStatus_Type()
)
jnxMIMstCistPortOperEdgeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortOperEdgeStatus.setStatus("current")
_JnxMIMstCistPortProtocolMigration_Type = TruthValue
_JnxMIMstCistPortProtocolMigration_Object = MibTableColumn
jnxMIMstCistPortProtocolMigration = _JnxMIMstCistPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 11),
    _JnxMIMstCistPortProtocolMigration_Type()
)
jnxMIMstCistPortProtocolMigration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortProtocolMigration.setStatus("current")


class _JnxMIMstCistPortState_Type(Integer32):
    """Custom type jnxMIMstCistPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("discarding", 2),
          ("forwarding", 5),
          ("learning", 4))
    )


_JnxMIMstCistPortState_Type.__name__ = "Integer32"
_JnxMIMstCistPortState_Object = MibTableColumn
jnxMIMstCistPortState = _JnxMIMstCistPortState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 12),
    _JnxMIMstCistPortState_Type()
)
jnxMIMstCistPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortState.setStatus("current")


class _JnxMIMstCistForcePortState_Type(Integer32):
    """Custom type jnxMIMstCistForcePortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_JnxMIMstCistForcePortState_Type.__name__ = "Integer32"
_JnxMIMstCistForcePortState_Object = MibTableColumn
jnxMIMstCistForcePortState = _JnxMIMstCistForcePortState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 13),
    _JnxMIMstCistForcePortState_Type()
)
jnxMIMstCistForcePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistForcePortState.setStatus("current")
_JnxMIMstCistPortForwardTransitions_Type = Counter32
_JnxMIMstCistPortForwardTransitions_Object = MibTableColumn
jnxMIMstCistPortForwardTransitions = _JnxMIMstCistPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 14),
    _JnxMIMstCistPortForwardTransitions_Type()
)
jnxMIMstCistPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortForwardTransitions.setStatus("current")
_JnxMIMstCistPortRxMstBpduCount_Type = Counter32
_JnxMIMstCistPortRxMstBpduCount_Object = MibTableColumn
jnxMIMstCistPortRxMstBpduCount = _JnxMIMstCistPortRxMstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 15),
    _JnxMIMstCistPortRxMstBpduCount_Type()
)
jnxMIMstCistPortRxMstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortRxMstBpduCount.setStatus("current")
_JnxMIMstCistPortRxRstBpduCount_Type = Counter32
_JnxMIMstCistPortRxRstBpduCount_Object = MibTableColumn
jnxMIMstCistPortRxRstBpduCount = _JnxMIMstCistPortRxRstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 16),
    _JnxMIMstCistPortRxRstBpduCount_Type()
)
jnxMIMstCistPortRxRstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortRxRstBpduCount.setStatus("current")
_JnxMIMstCistPortRxConfigBpduCount_Type = Counter32
_JnxMIMstCistPortRxConfigBpduCount_Object = MibTableColumn
jnxMIMstCistPortRxConfigBpduCount = _JnxMIMstCistPortRxConfigBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 17),
    _JnxMIMstCistPortRxConfigBpduCount_Type()
)
jnxMIMstCistPortRxConfigBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortRxConfigBpduCount.setStatus("current")
_JnxMIMstCistPortRxTcnBpduCount_Type = Counter32
_JnxMIMstCistPortRxTcnBpduCount_Object = MibTableColumn
jnxMIMstCistPortRxTcnBpduCount = _JnxMIMstCistPortRxTcnBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 18),
    _JnxMIMstCistPortRxTcnBpduCount_Type()
)
jnxMIMstCistPortRxTcnBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortRxTcnBpduCount.setStatus("current")
_JnxMIMstCistPortTxMstBpduCount_Type = Counter32
_JnxMIMstCistPortTxMstBpduCount_Object = MibTableColumn
jnxMIMstCistPortTxMstBpduCount = _JnxMIMstCistPortTxMstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 19),
    _JnxMIMstCistPortTxMstBpduCount_Type()
)
jnxMIMstCistPortTxMstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortTxMstBpduCount.setStatus("current")
_JnxMIMstCistPortTxRstBpduCount_Type = Counter32
_JnxMIMstCistPortTxRstBpduCount_Object = MibTableColumn
jnxMIMstCistPortTxRstBpduCount = _JnxMIMstCistPortTxRstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 20),
    _JnxMIMstCistPortTxRstBpduCount_Type()
)
jnxMIMstCistPortTxRstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortTxRstBpduCount.setStatus("current")
_JnxMIMstCistPortTxConfigBpduCount_Type = Counter32
_JnxMIMstCistPortTxConfigBpduCount_Object = MibTableColumn
jnxMIMstCistPortTxConfigBpduCount = _JnxMIMstCistPortTxConfigBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 21),
    _JnxMIMstCistPortTxConfigBpduCount_Type()
)
jnxMIMstCistPortTxConfigBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortTxConfigBpduCount.setStatus("current")
_JnxMIMstCistPortTxTcnBpduCount_Type = Counter32
_JnxMIMstCistPortTxTcnBpduCount_Object = MibTableColumn
jnxMIMstCistPortTxTcnBpduCount = _JnxMIMstCistPortTxTcnBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 22),
    _JnxMIMstCistPortTxTcnBpduCount_Type()
)
jnxMIMstCistPortTxTcnBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortTxTcnBpduCount.setStatus("current")
_JnxMIMstCistPortInvalidMstBpduRxCount_Type = Counter32
_JnxMIMstCistPortInvalidMstBpduRxCount_Object = MibTableColumn
jnxMIMstCistPortInvalidMstBpduRxCount = _JnxMIMstCistPortInvalidMstBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 23),
    _JnxMIMstCistPortInvalidMstBpduRxCount_Type()
)
jnxMIMstCistPortInvalidMstBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortInvalidMstBpduRxCount.setStatus("current")
_JnxMIMstCistPortInvalidRstBpduRxCount_Type = Counter32
_JnxMIMstCistPortInvalidRstBpduRxCount_Object = MibTableColumn
jnxMIMstCistPortInvalidRstBpduRxCount = _JnxMIMstCistPortInvalidRstBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 24),
    _JnxMIMstCistPortInvalidRstBpduRxCount_Type()
)
jnxMIMstCistPortInvalidRstBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortInvalidRstBpduRxCount.setStatus("current")
_JnxMIMstCistPortInvalidConfigBpduRxCount_Type = Counter32
_JnxMIMstCistPortInvalidConfigBpduRxCount_Object = MibTableColumn
jnxMIMstCistPortInvalidConfigBpduRxCount = _JnxMIMstCistPortInvalidConfigBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 25),
    _JnxMIMstCistPortInvalidConfigBpduRxCount_Type()
)
jnxMIMstCistPortInvalidConfigBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortInvalidConfigBpduRxCount.setStatus("current")
_JnxMIMstCistPortInvalidTcnBpduRxCount_Type = Counter32
_JnxMIMstCistPortInvalidTcnBpduRxCount_Object = MibTableColumn
jnxMIMstCistPortInvalidTcnBpduRxCount = _JnxMIMstCistPortInvalidTcnBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 26),
    _JnxMIMstCistPortInvalidTcnBpduRxCount_Type()
)
jnxMIMstCistPortInvalidTcnBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortInvalidTcnBpduRxCount.setStatus("current")


class _JnxMIMstCistPortTransmitSemState_Type(Integer32):
    """Custom type jnxMIMstCistPortTransmitSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("idle", 5),
          ("transmitconfig", 2),
          ("transmitinit", 0),
          ("transmitperiodic", 1),
          ("transmitrstp", 4),
          ("transmittcn", 3))
    )


_JnxMIMstCistPortTransmitSemState_Type.__name__ = "Integer32"
_JnxMIMstCistPortTransmitSemState_Object = MibTableColumn
jnxMIMstCistPortTransmitSemState = _JnxMIMstCistPortTransmitSemState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 27),
    _JnxMIMstCistPortTransmitSemState_Type()
)
jnxMIMstCistPortTransmitSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortTransmitSemState.setStatus("current")


class _JnxMIMstCistPortReceiveSemState_Type(Integer32):
    """Custom type jnxMIMstCistPortReceiveSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("discard", 0),
          ("receive", 1))
    )


_JnxMIMstCistPortReceiveSemState_Type.__name__ = "Integer32"
_JnxMIMstCistPortReceiveSemState_Object = MibTableColumn
jnxMIMstCistPortReceiveSemState = _JnxMIMstCistPortReceiveSemState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 28),
    _JnxMIMstCistPortReceiveSemState_Type()
)
jnxMIMstCistPortReceiveSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortReceiveSemState.setStatus("current")


class _JnxMIMstCistPortProtMigrationSemState_Type(Integer32):
    """Custom type jnxMIMstCistPortProtMigrationSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("init", 0),
          ("sendingrstp", 2),
          ("sendingstp", 4),
          ("sendrstp", 1),
          ("sendstp", 3))
    )


_JnxMIMstCistPortProtMigrationSemState_Type.__name__ = "Integer32"
_JnxMIMstCistPortProtMigrationSemState_Object = MibTableColumn
jnxMIMstCistPortProtMigrationSemState = _JnxMIMstCistPortProtMigrationSemState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 29),
    _JnxMIMstCistPortProtMigrationSemState_Type()
)
jnxMIMstCistPortProtMigrationSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortProtMigrationSemState.setStatus("current")
_JnxMIMstCistProtocolMigrationCount_Type = Counter32
_JnxMIMstCistProtocolMigrationCount_Object = MibTableColumn
jnxMIMstCistProtocolMigrationCount = _JnxMIMstCistProtocolMigrationCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 30),
    _JnxMIMstCistProtocolMigrationCount_Type()
)
jnxMIMstCistProtocolMigrationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistProtocolMigrationCount.setStatus("current")
_JnxMIMstCistPortDesignatedCost_Type = Integer32
_JnxMIMstCistPortDesignatedCost_Object = MibTableColumn
jnxMIMstCistPortDesignatedCost = _JnxMIMstCistPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 31),
    _JnxMIMstCistPortDesignatedCost_Type()
)
jnxMIMstCistPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortDesignatedCost.setStatus("current")
_JnxMIMstCistPortRegionalRoot_Type = BridgeId
_JnxMIMstCistPortRegionalRoot_Object = MibTableColumn
jnxMIMstCistPortRegionalRoot = _JnxMIMstCistPortRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 32),
    _JnxMIMstCistPortRegionalRoot_Type()
)
jnxMIMstCistPortRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortRegionalRoot.setStatus("current")
_JnxMIMstCistPortRegionalPathCost_Type = Integer32
_JnxMIMstCistPortRegionalPathCost_Object = MibTableColumn
jnxMIMstCistPortRegionalPathCost = _JnxMIMstCistPortRegionalPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 33),
    _JnxMIMstCistPortRegionalPathCost_Type()
)
jnxMIMstCistPortRegionalPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortRegionalPathCost.setStatus("current")


class _JnxMIMstCistSelectedPortRole_Type(Integer32):
    """Custom type jnxMIMstCistSelectedPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 1),
          ("backup", 2),
          ("designated", 4),
          ("disabled", 0),
          ("root", 3))
    )


_JnxMIMstCistSelectedPortRole_Type.__name__ = "Integer32"
_JnxMIMstCistSelectedPortRole_Object = MibTableColumn
jnxMIMstCistSelectedPortRole = _JnxMIMstCistSelectedPortRole_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 34),
    _JnxMIMstCistSelectedPortRole_Type()
)
jnxMIMstCistSelectedPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistSelectedPortRole.setStatus("current")


class _JnxMIMstCistCurrentPortRole_Type(Integer32):
    """Custom type jnxMIMstCistCurrentPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 1),
          ("backup", 2),
          ("designated", 4),
          ("disabled", 0),
          ("root", 3))
    )


_JnxMIMstCistCurrentPortRole_Type.__name__ = "Integer32"
_JnxMIMstCistCurrentPortRole_Object = MibTableColumn
jnxMIMstCistCurrentPortRole = _JnxMIMstCistCurrentPortRole_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 35),
    _JnxMIMstCistCurrentPortRole_Type()
)
jnxMIMstCistCurrentPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistCurrentPortRole.setStatus("current")


class _JnxMIMstCistPortInfoSemState_Type(Integer32):
    """Custom type jnxMIMstCistPortInfoSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("aged", 2),
          ("disabled", 0),
          ("enabled", 1),
          ("other", 7),
          ("present", 8),
          ("receive", 9),
          ("repeatdesg", 5),
          ("root", 6),
          ("superiordesg", 4),
          ("update", 3))
    )


_JnxMIMstCistPortInfoSemState_Type.__name__ = "Integer32"
_JnxMIMstCistPortInfoSemState_Object = MibTableColumn
jnxMIMstCistPortInfoSemState = _JnxMIMstCistPortInfoSemState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 36),
    _JnxMIMstCistPortInfoSemState_Type()
)
jnxMIMstCistPortInfoSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortInfoSemState.setStatus("current")


class _JnxMIMstCistPortRoleTransitionSemState_Type(Integer32):
    """Custom type jnxMIMstCistPortRoleTransitionSemState based on Integer32"""
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
        *(("activeport", 3),
          ("blockedport", 2),
          ("blockport", 1),
          ("init", 0))
    )


_JnxMIMstCistPortRoleTransitionSemState_Type.__name__ = "Integer32"
_JnxMIMstCistPortRoleTransitionSemState_Object = MibTableColumn
jnxMIMstCistPortRoleTransitionSemState = _JnxMIMstCistPortRoleTransitionSemState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 37),
    _JnxMIMstCistPortRoleTransitionSemState_Type()
)
jnxMIMstCistPortRoleTransitionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortRoleTransitionSemState.setStatus("current")


class _JnxMIMstCistPortStateTransitionSemState_Type(Integer32):
    """Custom type jnxMIMstCistPortStateTransitionSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discarding", 0),
          ("forwarding", 2),
          ("learning", 1))
    )


_JnxMIMstCistPortStateTransitionSemState_Type.__name__ = "Integer32"
_JnxMIMstCistPortStateTransitionSemState_Object = MibTableColumn
jnxMIMstCistPortStateTransitionSemState = _JnxMIMstCistPortStateTransitionSemState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 38),
    _JnxMIMstCistPortStateTransitionSemState_Type()
)
jnxMIMstCistPortStateTransitionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortStateTransitionSemState.setStatus("current")


class _JnxMIMstCistPortTopologyChangeSemState_Type(Integer32):
    """Custom type jnxMIMstCistPortTopologyChangeSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("acknowledged", 7),
          ("active", 2),
          ("detected", 3),
          ("inactive", 1),
          ("init", 0),
          ("notifiedtc", 5),
          ("notifiedtcn", 4),
          ("propagating", 6))
    )


_JnxMIMstCistPortTopologyChangeSemState_Type.__name__ = "Integer32"
_JnxMIMstCistPortTopologyChangeSemState_Object = MibTableColumn
jnxMIMstCistPortTopologyChangeSemState = _JnxMIMstCistPortTopologyChangeSemState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 39),
    _JnxMIMstCistPortTopologyChangeSemState_Type()
)
jnxMIMstCistPortTopologyChangeSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortTopologyChangeSemState.setStatus("current")


class _JnxMIMstCistPortHelloTime_Type(Timeout):
    """Custom type jnxMIMstCistPortHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_JnxMIMstCistPortHelloTime_Type.__name__ = "Timeout"
_JnxMIMstCistPortHelloTime_Object = MibTableColumn
jnxMIMstCistPortHelloTime = _JnxMIMstCistPortHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 40),
    _JnxMIMstCistPortHelloTime_Type()
)
jnxMIMstCistPortHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortHelloTime.setStatus("current")


class _JnxMIMstCistPortOperVersion_Type(Integer32):
    """Custom type jnxMIMstCistPortOperVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mstp", 3),
          ("rstp", 2),
          ("stpCompatible", 0))
    )


_JnxMIMstCistPortOperVersion_Type.__name__ = "Integer32"
_JnxMIMstCistPortOperVersion_Object = MibTableColumn
jnxMIMstCistPortOperVersion = _JnxMIMstCistPortOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 41),
    _JnxMIMstCistPortOperVersion_Type()
)
jnxMIMstCistPortOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortOperVersion.setStatus("current")
_JnxMIMstCistPortEffectivePortState_Type = TruthValue
_JnxMIMstCistPortEffectivePortState_Object = MibTableColumn
jnxMIMstCistPortEffectivePortState = _JnxMIMstCistPortEffectivePortState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 42),
    _JnxMIMstCistPortEffectivePortState_Type()
)
jnxMIMstCistPortEffectivePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortEffectivePortState.setStatus("current")
_JnxMIMstCistPortAutoEdgeStatus_Type = TruthValue
_JnxMIMstCistPortAutoEdgeStatus_Object = MibTableColumn
jnxMIMstCistPortAutoEdgeStatus = _JnxMIMstCistPortAutoEdgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 6, 1, 43),
    _JnxMIMstCistPortAutoEdgeStatus_Type()
)
jnxMIMstCistPortAutoEdgeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortAutoEdgeStatus.setStatus("current")
_JnxMIMstMstiPortTable_Object = MibTable
jnxMIMstMstiPortTable = _JnxMIMstMstiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 7)
)
if mibBuilder.loadTexts:
    jnxMIMstMstiPortTable.setStatus("current")
_JnxMIMstMstiPortEntry_Object = MibTableRow
jnxMIMstMstiPortEntry = _JnxMIMstMstiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 7, 1)
)
jnxMIMstMstiPortEntry.setIndexNames(
    (0, "JUNIPER-MIMSTP-MIB", "jnxMIMstMstiPort"),
    (0, "JUNIPER-MIMSTP-MIB", "jnxMIMstInstanceIndex"),
)
if mibBuilder.loadTexts:
    jnxMIMstMstiPortEntry.setStatus("current")


class _JnxMIMstMstiPort_Type(Integer32):
    """Custom type jnxMIMstMstiPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JnxMIMstMstiPort_Type.__name__ = "Integer32"
_JnxMIMstMstiPort_Object = MibTableColumn
jnxMIMstMstiPort = _JnxMIMstMstiPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 7, 1, 1),
    _JnxMIMstMstiPort_Type()
)
jnxMIMstMstiPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMIMstMstiPort.setStatus("current")


class _JnxMIMstMstiPortPathCost_Type(Integer32):
    """Custom type jnxMIMstMstiPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_JnxMIMstMstiPortPathCost_Type.__name__ = "Integer32"
_JnxMIMstMstiPortPathCost_Object = MibTableColumn
jnxMIMstMstiPortPathCost = _JnxMIMstMstiPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 7, 1, 2),
    _JnxMIMstMstiPortPathCost_Type()
)
jnxMIMstMstiPortPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiPortPathCost.setStatus("current")


class _JnxMIMstMstiPortPriority_Type(Integer32):
    """Custom type jnxMIMstMstiPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_JnxMIMstMstiPortPriority_Type.__name__ = "Integer32"
_JnxMIMstMstiPortPriority_Object = MibTableColumn
jnxMIMstMstiPortPriority = _JnxMIMstMstiPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 7, 1, 3),
    _JnxMIMstMstiPortPriority_Type()
)
jnxMIMstMstiPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiPortPriority.setStatus("current")
_JnxMIMstMstiPortDesignatedRoot_Type = BridgeId
_JnxMIMstMstiPortDesignatedRoot_Object = MibTableColumn
jnxMIMstMstiPortDesignatedRoot = _JnxMIMstMstiPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 7, 1, 4),
    _JnxMIMstMstiPortDesignatedRoot_Type()
)
jnxMIMstMstiPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiPortDesignatedRoot.setStatus("current")
_JnxMIMstMstiPortDesignatedBridge_Type = BridgeId
_JnxMIMstMstiPortDesignatedBridge_Object = MibTableColumn
jnxMIMstMstiPortDesignatedBridge = _JnxMIMstMstiPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 7, 1, 5),
    _JnxMIMstMstiPortDesignatedBridge_Type()
)
jnxMIMstMstiPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiPortDesignatedBridge.setStatus("current")


class _JnxMIMstMstiPortDesignatedPort_Type(OctetString):
    """Custom type jnxMIMstMstiPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_JnxMIMstMstiPortDesignatedPort_Type.__name__ = "OctetString"
_JnxMIMstMstiPortDesignatedPort_Object = MibTableColumn
jnxMIMstMstiPortDesignatedPort = _JnxMIMstMstiPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 7, 1, 6),
    _JnxMIMstMstiPortDesignatedPort_Type()
)
jnxMIMstMstiPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiPortDesignatedPort.setStatus("current")


class _JnxMIMstMstiPortState_Type(Integer32):
    """Custom type jnxMIMstMstiPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("discarding", 2),
          ("forwarding", 5),
          ("learning", 4))
    )


_JnxMIMstMstiPortState_Type.__name__ = "Integer32"
_JnxMIMstMstiPortState_Object = MibTableColumn
jnxMIMstMstiPortState = _JnxMIMstMstiPortState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 7, 1, 7),
    _JnxMIMstMstiPortState_Type()
)
jnxMIMstMstiPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiPortState.setStatus("current")


class _JnxMIMstMstiForcePortState_Type(Integer32):
    """Custom type jnxMIMstMstiForcePortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_JnxMIMstMstiForcePortState_Type.__name__ = "Integer32"
_JnxMIMstMstiForcePortState_Object = MibTableColumn
jnxMIMstMstiForcePortState = _JnxMIMstMstiForcePortState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 7, 1, 8),
    _JnxMIMstMstiForcePortState_Type()
)
jnxMIMstMstiForcePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiForcePortState.setStatus("current")
_JnxMIMstMstiPortForwardTransitions_Type = Counter32
_JnxMIMstMstiPortForwardTransitions_Object = MibTableColumn
jnxMIMstMstiPortForwardTransitions = _JnxMIMstMstiPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 7, 1, 9),
    _JnxMIMstMstiPortForwardTransitions_Type()
)
jnxMIMstMstiPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiPortForwardTransitions.setStatus("current")
_JnxMIMstMstiPortReceivedBPDUs_Type = Counter32
_JnxMIMstMstiPortReceivedBPDUs_Object = MibTableColumn
jnxMIMstMstiPortReceivedBPDUs = _JnxMIMstMstiPortReceivedBPDUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 7, 1, 10),
    _JnxMIMstMstiPortReceivedBPDUs_Type()
)
jnxMIMstMstiPortReceivedBPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiPortReceivedBPDUs.setStatus("current")
_JnxMIMstMstiPortTransmittedBPDUs_Type = Counter32
_JnxMIMstMstiPortTransmittedBPDUs_Object = MibTableColumn
jnxMIMstMstiPortTransmittedBPDUs = _JnxMIMstMstiPortTransmittedBPDUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 7, 1, 11),
    _JnxMIMstMstiPortTransmittedBPDUs_Type()
)
jnxMIMstMstiPortTransmittedBPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiPortTransmittedBPDUs.setStatus("current")
_JnxMIMstMstiPortInvalidBPDUsRcvd_Type = Counter32
_JnxMIMstMstiPortInvalidBPDUsRcvd_Object = MibTableColumn
jnxMIMstMstiPortInvalidBPDUsRcvd = _JnxMIMstMstiPortInvalidBPDUsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 7, 1, 12),
    _JnxMIMstMstiPortInvalidBPDUsRcvd_Type()
)
jnxMIMstMstiPortInvalidBPDUsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiPortInvalidBPDUsRcvd.setStatus("current")
_JnxMIMstMstiPortDesignatedCost_Type = Integer32
_JnxMIMstMstiPortDesignatedCost_Object = MibTableColumn
jnxMIMstMstiPortDesignatedCost = _JnxMIMstMstiPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 7, 1, 13),
    _JnxMIMstMstiPortDesignatedCost_Type()
)
jnxMIMstMstiPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiPortDesignatedCost.setStatus("current")


class _JnxMIMstMstiSelectedPortRole_Type(Integer32):
    """Custom type jnxMIMstMstiSelectedPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 1),
          ("backup", 2),
          ("designated", 4),
          ("disabled", 0),
          ("master", 5),
          ("root", 3))
    )


_JnxMIMstMstiSelectedPortRole_Type.__name__ = "Integer32"
_JnxMIMstMstiSelectedPortRole_Object = MibTableColumn
jnxMIMstMstiSelectedPortRole = _JnxMIMstMstiSelectedPortRole_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 7, 1, 14),
    _JnxMIMstMstiSelectedPortRole_Type()
)
jnxMIMstMstiSelectedPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiSelectedPortRole.setStatus("current")


class _JnxMIMstMstiCurrentPortRole_Type(Integer32):
    """Custom type jnxMIMstMstiCurrentPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 1),
          ("backup", 2),
          ("designated", 4),
          ("disabled", 0),
          ("master", 5),
          ("root", 3))
    )


_JnxMIMstMstiCurrentPortRole_Type.__name__ = "Integer32"
_JnxMIMstMstiCurrentPortRole_Object = MibTableColumn
jnxMIMstMstiCurrentPortRole = _JnxMIMstMstiCurrentPortRole_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 7, 1, 15),
    _JnxMIMstMstiCurrentPortRole_Type()
)
jnxMIMstMstiCurrentPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiCurrentPortRole.setStatus("current")


class _JnxMIMstMstiPortInfoSemState_Type(Integer32):
    """Custom type jnxMIMstMstiPortInfoSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("aged", 2),
          ("disabled", 0),
          ("enabled", 1),
          ("other", 7),
          ("present", 8),
          ("receive", 9),
          ("repeatdesg", 5),
          ("root", 6),
          ("superiordesg", 4),
          ("update", 3))
    )


_JnxMIMstMstiPortInfoSemState_Type.__name__ = "Integer32"
_JnxMIMstMstiPortInfoSemState_Object = MibTableColumn
jnxMIMstMstiPortInfoSemState = _JnxMIMstMstiPortInfoSemState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 7, 1, 16),
    _JnxMIMstMstiPortInfoSemState_Type()
)
jnxMIMstMstiPortInfoSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiPortInfoSemState.setStatus("current")


class _JnxMIMstMstiPortRoleTransitionSemState_Type(Integer32):
    """Custom type jnxMIMstMstiPortRoleTransitionSemState based on Integer32"""
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
        *(("activeport", 3),
          ("blockedport", 2),
          ("blockport", 1),
          ("init", 0))
    )


_JnxMIMstMstiPortRoleTransitionSemState_Type.__name__ = "Integer32"
_JnxMIMstMstiPortRoleTransitionSemState_Object = MibTableColumn
jnxMIMstMstiPortRoleTransitionSemState = _JnxMIMstMstiPortRoleTransitionSemState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 7, 1, 17),
    _JnxMIMstMstiPortRoleTransitionSemState_Type()
)
jnxMIMstMstiPortRoleTransitionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiPortRoleTransitionSemState.setStatus("current")


class _JnxMIMstMstiPortStateTransitionSemState_Type(Integer32):
    """Custom type jnxMIMstMstiPortStateTransitionSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discarding", 0),
          ("forwarding", 2),
          ("learning", 1))
    )


_JnxMIMstMstiPortStateTransitionSemState_Type.__name__ = "Integer32"
_JnxMIMstMstiPortStateTransitionSemState_Object = MibTableColumn
jnxMIMstMstiPortStateTransitionSemState = _JnxMIMstMstiPortStateTransitionSemState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 7, 1, 18),
    _JnxMIMstMstiPortStateTransitionSemState_Type()
)
jnxMIMstMstiPortStateTransitionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiPortStateTransitionSemState.setStatus("current")


class _JnxMIMstMstiPortTopologyChangeSemState_Type(Integer32):
    """Custom type jnxMIMstMstiPortTopologyChangeSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("acknowledged", 7),
          ("active", 2),
          ("detected", 3),
          ("inactive", 1),
          ("init", 0),
          ("notifiedtc", 5),
          ("notifiedtcn", 4),
          ("propagating", 6))
    )


_JnxMIMstMstiPortTopologyChangeSemState_Type.__name__ = "Integer32"
_JnxMIMstMstiPortTopologyChangeSemState_Object = MibTableColumn
jnxMIMstMstiPortTopologyChangeSemState = _JnxMIMstMstiPortTopologyChangeSemState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 7, 1, 19),
    _JnxMIMstMstiPortTopologyChangeSemState_Type()
)
jnxMIMstMstiPortTopologyChangeSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiPortTopologyChangeSemState.setStatus("current")
_JnxMIMstMstiPortEffectivePortState_Type = TruthValue
_JnxMIMstMstiPortEffectivePortState_Object = MibTableColumn
jnxMIMstMstiPortEffectivePortState = _JnxMIMstMstiPortEffectivePortState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 7, 1, 20),
    _JnxMIMstMstiPortEffectivePortState_Type()
)
jnxMIMstMstiPortEffectivePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiPortEffectivePortState.setStatus("current")
_JnxMIMstCistPortProtectTable_Object = MibTable
jnxMIMstCistPortProtectTable = _JnxMIMstCistPortProtectTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 8)
)
if mibBuilder.loadTexts:
    jnxMIMstCistPortProtectTable.setStatus("current")
_JnxMIMstCistPortProtectEntry_Object = MibTableRow
jnxMIMstCistPortProtectEntry = _JnxMIMstCistPortProtectEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    jnxMIMstCistPortProtectEntry.setStatus("current")
_JnxMIMstCistPortRootProtectEnabled_Type = TruthValue
_JnxMIMstCistPortRootProtectEnabled_Object = MibTableColumn
jnxMIMstCistPortRootProtectEnabled = _JnxMIMstCistPortRootProtectEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 8, 1, 1),
    _JnxMIMstCistPortRootProtectEnabled_Type()
)
jnxMIMstCistPortRootProtectEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortRootProtectEnabled.setStatus("current")


class _JnxMIMstCistPortRootProtectState_Type(Integer32):
    """Custom type jnxMIMstCistPortRootProtectState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no-error", 0),
          ("root-prevented", 1))
    )


_JnxMIMstCistPortRootProtectState_Type.__name__ = "Integer32"
_JnxMIMstCistPortRootProtectState_Object = MibTableColumn
jnxMIMstCistPortRootProtectState = _JnxMIMstCistPortRootProtectState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 8, 1, 2),
    _JnxMIMstCistPortRootProtectState_Type()
)
jnxMIMstCistPortRootProtectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortRootProtectState.setStatus("current")
_JnxMIMstCistPortLoopProtectEnabled_Type = TruthValue
_JnxMIMstCistPortLoopProtectEnabled_Object = MibTableColumn
jnxMIMstCistPortLoopProtectEnabled = _JnxMIMstCistPortLoopProtectEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 8, 1, 3),
    _JnxMIMstCistPortLoopProtectEnabled_Type()
)
jnxMIMstCistPortLoopProtectEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortLoopProtectEnabled.setStatus("current")


class _JnxMIMstCistPortLoopProtectState_Type(Integer32):
    """Custom type jnxMIMstCistPortLoopProtectState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("loop-prevented", 1),
          ("no-error", 0))
    )


_JnxMIMstCistPortLoopProtectState_Type.__name__ = "Integer32"
_JnxMIMstCistPortLoopProtectState_Object = MibTableColumn
jnxMIMstCistPortLoopProtectState = _JnxMIMstCistPortLoopProtectState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 8, 1, 4),
    _JnxMIMstCistPortLoopProtectState_Type()
)
jnxMIMstCistPortLoopProtectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstCistPortLoopProtectState.setStatus("current")
_JnxMIMstMstiPortProtectTable_Object = MibTable
jnxMIMstMstiPortProtectTable = _JnxMIMstMstiPortProtectTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 9)
)
if mibBuilder.loadTexts:
    jnxMIMstMstiPortProtectTable.setStatus("current")
_JnxMIMstMstiPortProtectEntry_Object = MibTableRow
jnxMIMstMstiPortProtectEntry = _JnxMIMstMstiPortProtectEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    jnxMIMstMstiPortProtectEntry.setStatus("current")


class _JnxMIMstMstiPortRootProtectState_Type(Integer32):
    """Custom type jnxMIMstMstiPortRootProtectState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no-error", 0),
          ("root-prevented", 1))
    )


_JnxMIMstMstiPortRootProtectState_Type.__name__ = "Integer32"
_JnxMIMstMstiPortRootProtectState_Object = MibTableColumn
jnxMIMstMstiPortRootProtectState = _JnxMIMstMstiPortRootProtectState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 9, 1, 1),
    _JnxMIMstMstiPortRootProtectState_Type()
)
jnxMIMstMstiPortRootProtectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiPortRootProtectState.setStatus("current")


class _JnxMIMstMstiPortLoopProtectState_Type(Integer32):
    """Custom type jnxMIMstMstiPortLoopProtectState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("loop-prevented", 1),
          ("no-error", 0))
    )


_JnxMIMstMstiPortLoopProtectState_Type.__name__ = "Integer32"
_JnxMIMstMstiPortLoopProtectState_Object = MibTableColumn
jnxMIMstMstiPortLoopProtectState = _JnxMIMstMstiPortLoopProtectState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 1, 9, 1, 2),
    _JnxMIMstMstiPortLoopProtectState_Type()
)
jnxMIMstMstiPortLoopProtectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstMstiPortLoopProtectState.setStatus("current")
_JnxMIDot1sJnxMstTrapsControl_ObjectIdentity = ObjectIdentity
jnxMIDot1sJnxMstTrapsControl = _JnxMIDot1sJnxMstTrapsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 2)
)


class _JnxMIDot1sJnxMstSetGlobalTrapOption_Type(Integer32):
    """Custom type jnxMIDot1sJnxMstSetGlobalTrapOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_JnxMIDot1sJnxMstSetGlobalTrapOption_Type.__name__ = "Integer32"
_JnxMIDot1sJnxMstSetGlobalTrapOption_Object = MibScalar
jnxMIDot1sJnxMstSetGlobalTrapOption = _JnxMIDot1sJnxMstSetGlobalTrapOption_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 2, 1),
    _JnxMIDot1sJnxMstSetGlobalTrapOption_Type()
)
jnxMIDot1sJnxMstSetGlobalTrapOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIDot1sJnxMstSetGlobalTrapOption.setStatus("current")


class _JnxMIMstGlobalErrTrapType_Type(Integer32):
    """Custom type jnxMIMstGlobalErrTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bufffail", 2),
          ("memfail", 1),
          ("none", 0))
    )


_JnxMIMstGlobalErrTrapType_Type.__name__ = "Integer32"
_JnxMIMstGlobalErrTrapType_Object = MibScalar
jnxMIMstGlobalErrTrapType = _JnxMIMstGlobalErrTrapType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 2, 2),
    _JnxMIMstGlobalErrTrapType_Type()
)
jnxMIMstGlobalErrTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstGlobalErrTrapType.setStatus("current")
_JnxMIDot1sJnxMstTrapsControlTable_Object = MibTable
jnxMIDot1sJnxMstTrapsControlTable = _JnxMIDot1sJnxMstTrapsControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 2, 3)
)
if mibBuilder.loadTexts:
    jnxMIDot1sJnxMstTrapsControlTable.setStatus("current")
_JnxMIDot1sJnxMstTrapsControlEntry_Object = MibTableRow
jnxMIDot1sJnxMstTrapsControlEntry = _JnxMIDot1sJnxMstTrapsControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 2, 3, 1)
)
jnxMIDot1sJnxMstTrapsControlEntry.setIndexNames(
    (0, "JUNIPER-MIMSTP-MIB", "jnxMIDot1sJuniperMstContextId"),
)
if mibBuilder.loadTexts:
    jnxMIDot1sJnxMstTrapsControlEntry.setStatus("current")


class _JnxMIMstSetTraps_Type(Integer32):
    """Custom type jnxMIMstSetTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_JnxMIMstSetTraps_Type.__name__ = "Integer32"
_JnxMIMstSetTraps_Object = MibTableColumn
jnxMIMstSetTraps = _JnxMIMstSetTraps_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 2, 3, 1, 1),
    _JnxMIMstSetTraps_Type()
)
jnxMIMstSetTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstSetTraps.setStatus("current")


class _JnxMIMstGenTrapType_Type(Integer32):
    """Custom type jnxMIMstGenTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("none", 0),
          ("up", 1))
    )


_JnxMIMstGenTrapType_Type.__name__ = "Integer32"
_JnxMIMstGenTrapType_Object = MibTableColumn
jnxMIMstGenTrapType = _JnxMIMstGenTrapType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 2, 3, 1, 2),
    _JnxMIMstGenTrapType_Type()
)
jnxMIMstGenTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstGenTrapType.setStatus("current")
_JnxMIMstPortTrapNotificationTable_Object = MibTable
jnxMIMstPortTrapNotificationTable = _JnxMIMstPortTrapNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 2, 4)
)
if mibBuilder.loadTexts:
    jnxMIMstPortTrapNotificationTable.setStatus("current")
_JnxMIMstPortTrapNotificationEntry_Object = MibTableRow
jnxMIMstPortTrapNotificationEntry = _JnxMIMstPortTrapNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 2, 4, 1)
)
jnxMIMstPortTrapNotificationEntry.setIndexNames(
    (0, "JUNIPER-MIMSTP-MIB", "jnxMIMstPortTrapIndex"),
)
if mibBuilder.loadTexts:
    jnxMIMstPortTrapNotificationEntry.setStatus("current")


class _JnxMIMstPortTrapIndex_Type(Integer32):
    """Custom type jnxMIMstPortTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_JnxMIMstPortTrapIndex_Type.__name__ = "Integer32"
_JnxMIMstPortTrapIndex_Object = MibTableColumn
jnxMIMstPortTrapIndex = _JnxMIMstPortTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 2, 4, 1, 1),
    _JnxMIMstPortTrapIndex_Type()
)
jnxMIMstPortTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstPortTrapIndex.setStatus("current")


class _JnxMIMstPortMigrationType_Type(Integer32):
    """Custom type jnxMIMstPortMigrationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sendrstp", 1),
          ("sendstp", 0))
    )


_JnxMIMstPortMigrationType_Type.__name__ = "Integer32"
_JnxMIMstPortMigrationType_Object = MibTableColumn
jnxMIMstPortMigrationType = _JnxMIMstPortMigrationType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 2, 4, 1, 2),
    _JnxMIMstPortMigrationType_Type()
)
jnxMIMstPortMigrationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstPortMigrationType.setStatus("current")


class _JnxMIMstPktErrType_Type(Integer32):
    """Custom type jnxMIMstPktErrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("configLengthErr", 2),
          ("fwdDelayErr", 6),
          ("helloTimeErr", 7),
          ("invalidBpdu", 1),
          ("maxAgeErr", 5),
          ("mstpLengthErr", 8),
          ("protocolIdErr", 0),
          ("rstpLengthErr", 4),
          ("tcnLengthErr", 3))
    )


_JnxMIMstPktErrType_Type.__name__ = "Integer32"
_JnxMIMstPktErrType_Object = MibTableColumn
jnxMIMstPktErrType = _JnxMIMstPktErrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 2, 4, 1, 3),
    _JnxMIMstPktErrType_Type()
)
jnxMIMstPktErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstPktErrType.setStatus("current")
_JnxMIMstPktErrVal_Type = Integer32
_JnxMIMstPktErrVal_Object = MibTableColumn
jnxMIMstPktErrVal = _JnxMIMstPktErrVal_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 2, 4, 1, 4),
    _JnxMIMstPktErrVal_Type()
)
jnxMIMstPktErrVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMIMstPktErrVal.setStatus("current")
_JnxMIDot1sJuniperMstTraps_ObjectIdentity = ObjectIdentity
jnxMIDot1sJuniperMstTraps = _JnxMIDot1sJuniperMstTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 3)
)
_JnxMIMstTraps_ObjectIdentity = ObjectIdentity
jnxMIMstTraps = _JnxMIMstTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 3, 0)
)
jnxMIMstCistPortEntry.registerAugmentions(
    ("JUNIPER-MIMSTP-MIB",
     "jnxMIMstCistPortProtectEntry")
)
jnxMIMstCistPortProtectEntry.setIndexNames(*jnxMIMstCistPortEntry.getIndexNames())
jnxMIMstMstiPortEntry.registerAugmentions(
    ("JUNIPER-MIMSTP-MIB",
     "jnxMIMstMstiPortProtectEntry")
)
jnxMIMstMstiPortProtectEntry.setIndexNames(*jnxMIMstMstiPortEntry.getIndexNames())

# Managed Objects groups


# Notification objects

jnxMIMstGenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 3, 0, 1)
)
jnxMIMstGenTrap.setObjects(
      *(("JUNIPER-MIMSTP-MIB", "jnxMIMstBrgAddress"),
        ("JUNIPER-MIMSTP-MIB", "jnxMIMstGenTrapType"))
)
if mibBuilder.loadTexts:
    jnxMIMstGenTrap.setStatus(
        "current"
    )

jnxMIMstErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 3, 0, 2)
)
jnxMIMstErrTrap.setObjects(
      *(("JUNIPER-MIMSTP-MIB", "jnxMIMstBrgAddress"),
        ("JUNIPER-MIMSTP-MIB", "jnxMIMstGlobalErrTrapType"))
)
if mibBuilder.loadTexts:
    jnxMIMstErrTrap.setStatus(
        "current"
    )

jnxMIMstNewRootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 3, 0, 3)
)
jnxMIMstNewRootTrap.setObjects(
      *(("JUNIPER-MIMSTP-MIB", "jnxMIMstBrgAddress"),
        ("JUNIPER-MIMSTP-MIB", "jnxMIMstOldDesignatedRoot"),
        ("JUNIPER-MIMSTP-MIB", "jnxMIMstMstiBridgeRegionalRoot"),
        ("JUNIPER-MIMSTP-MIB", "jnxMIMstMstiInstanceIndex"))
)
if mibBuilder.loadTexts:
    jnxMIMstNewRootTrap.setStatus(
        "current"
    )

jnxMIMstTopologyChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 3, 0, 4)
)
jnxMIMstTopologyChgTrap.setObjects(
      *(("JUNIPER-MIMSTP-MIB", "jnxMIMstBrgAddress"),
        ("JUNIPER-MIMSTP-MIB", "jnxMIMstMstiInstanceIndex"))
)
if mibBuilder.loadTexts:
    jnxMIMstTopologyChgTrap.setStatus(
        "current"
    )

jnxMIMstProtocolMigrationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 3, 0, 5)
)
jnxMIMstProtocolMigrationTrap.setObjects(
      *(("JUNIPER-MIMSTP-MIB", "jnxMIMstBrgAddress"),
        ("JUNIPER-MIMSTP-MIB", "jnxMIMstPortTrapIndex"),
        ("JUNIPER-MIMSTP-MIB", "jnxMIMstForceProtocolVersion"),
        ("JUNIPER-MIMSTP-MIB", "jnxMIMstPortMigrationType"))
)
if mibBuilder.loadTexts:
    jnxMIMstProtocolMigrationTrap.setStatus(
        "current"
    )

jnxMIMstInvalidBpduRxdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 3, 0, 6)
)
jnxMIMstInvalidBpduRxdTrap.setObjects(
      *(("JUNIPER-MIMSTP-MIB", "jnxMIMstBrgAddress"),
        ("JUNIPER-MIMSTP-MIB", "jnxMIMstPortTrapIndex"),
        ("JUNIPER-MIMSTP-MIB", "jnxMIMstPktErrType"),
        ("JUNIPER-MIMSTP-MIB", "jnxMIMstPktErrVal"))
)
if mibBuilder.loadTexts:
    jnxMIMstInvalidBpduRxdTrap.setStatus(
        "current"
    )

jnxMIMstRegionConfigChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 3, 0, 7)
)
jnxMIMstRegionConfigChangeTrap.setObjects(
      *(("JUNIPER-MIMSTP-MIB", "jnxMIMstBrgAddress"),
        ("JUNIPER-MIMSTP-MIB", "jnxMIMstMstiConfigIdSel"),
        ("JUNIPER-MIMSTP-MIB", "jnxMIMstMstiRegionName"),
        ("JUNIPER-MIMSTP-MIB", "jnxMIMstMstiRegionVersion"),
        ("JUNIPER-MIMSTP-MIB", "jnxMIMstMstiConfigDigest"))
)
if mibBuilder.loadTexts:
    jnxMIMstRegionConfigChangeTrap.setStatus(
        "current"
    )

jnxMIMstCistPortRootProtectStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 3, 0, 8)
)
jnxMIMstCistPortRootProtectStateChangeTrap.setObjects(
      *(("JUNIPER-MIMSTP-MIB", "jnxMIMstBrgAddress"),
        ("JUNIPER-MIMSTP-MIB", "jnxMIMstCistPortRootProtectState"))
)
if mibBuilder.loadTexts:
    jnxMIMstCistPortRootProtectStateChangeTrap.setStatus(
        "current"
    )

jnxMIMstMstiPortRootProtectStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 3, 0, 9)
)
jnxMIMstMstiPortRootProtectStateChangeTrap.setObjects(
      *(("JUNIPER-MIMSTP-MIB", "jnxMIMstBrgAddress"),
        ("JUNIPER-MIMSTP-MIB", "jnxMIMstMstiPortRootProtectState"))
)
if mibBuilder.loadTexts:
    jnxMIMstMstiPortRootProtectStateChangeTrap.setStatus(
        "current"
    )

jnxMIMstCistPortLoopProtectStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 3, 0, 10)
)
jnxMIMstCistPortLoopProtectStateChangeTrap.setObjects(
      *(("JUNIPER-MIMSTP-MIB", "jnxMIMstBrgAddress"),
        ("JUNIPER-MIMSTP-MIB", "jnxMIMstCistPortLoopProtectState"))
)
if mibBuilder.loadTexts:
    jnxMIMstCistPortLoopProtectStateChangeTrap.setStatus(
        "current"
    )

jnxMIMstMstiPortLoopProtectStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46, 1, 3, 0, 11)
)
jnxMIMstMstiPortLoopProtectStateChangeTrap.setObjects(
      *(("JUNIPER-MIMSTP-MIB", "jnxMIMstBrgAddress"),
        ("JUNIPER-MIMSTP-MIB", "jnxMIMstMstiPortLoopProtectState"))
)
if mibBuilder.loadTexts:
    jnxMIMstMstiPortLoopProtectStateChangeTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-MIMSTP-MIB",
    **{"VlanId": VlanId,
       "BridgeId": BridgeId,
       "Timeout": Timeout,
       "EnabledStatus": EnabledStatus,
       "jnxMIMstMIB": jnxMIMstMIB,
       "jnxMIDot1sJuniperMst": jnxMIDot1sJuniperMst,
       "jnxMIMstGlobalTrace": jnxMIMstGlobalTrace,
       "jnxMIMstGlobalDebug": jnxMIMstGlobalDebug,
       "jnxMIDot1sJuniperMstTable": jnxMIDot1sJuniperMstTable,
       "jnxMIDot1sJuniperMstEntry": jnxMIDot1sJuniperMstEntry,
       "jnxMIDot1sJuniperMstContextId": jnxMIDot1sJuniperMstContextId,
       "jnxMIMstSystemControl": jnxMIMstSystemControl,
       "jnxMIMstModuleStatus": jnxMIMstModuleStatus,
       "jnxMIMstMaxMstInstanceNumber": jnxMIMstMaxMstInstanceNumber,
       "jnxMIMstNoOfMstiSupported": jnxMIMstNoOfMstiSupported,
       "jnxMIMstMaxHopCount": jnxMIMstMaxHopCount,
       "jnxMIMstBrgAddress": jnxMIMstBrgAddress,
       "jnxMIMstCistRoot": jnxMIMstCistRoot,
       "jnxMIMstCistRegionalRoot": jnxMIMstCistRegionalRoot,
       "jnxMIMstCistRootCost": jnxMIMstCistRootCost,
       "jnxMIMstCistRegionalRootCost": jnxMIMstCistRegionalRootCost,
       "jnxMIMstCistRootPort": jnxMIMstCistRootPort,
       "jnxMIMstCistBridgePriority": jnxMIMstCistBridgePriority,
       "jnxMIMstCistBridgeMaxAge": jnxMIMstCistBridgeMaxAge,
       "jnxMIMstCistBridgeForwardDelay": jnxMIMstCistBridgeForwardDelay,
       "jnxMIMstCistHoldTime": jnxMIMstCistHoldTime,
       "jnxMIMstCistMaxAge": jnxMIMstCistMaxAge,
       "jnxMIMstCistForwardDelay": jnxMIMstCistForwardDelay,
       "jnxMIMstMstpUpCount": jnxMIMstMstpUpCount,
       "jnxMIMstMstpDownCount": jnxMIMstMstpDownCount,
       "jnxMIMstPathCostDefaultType": jnxMIMstPathCostDefaultType,
       "jnxMIMstTrace": jnxMIMstTrace,
       "jnxMIMstDebug": jnxMIMstDebug,
       "jnxMIMstForceProtocolVersion": jnxMIMstForceProtocolVersion,
       "jnxMIMstTxHoldCount": jnxMIMstTxHoldCount,
       "jnxMIMstMstiConfigIdSel": jnxMIMstMstiConfigIdSel,
       "jnxMIMstMstiRegionName": jnxMIMstMstiRegionName,
       "jnxMIMstMstiRegionVersion": jnxMIMstMstiRegionVersion,
       "jnxMIMstMstiConfigDigest": jnxMIMstMstiConfigDigest,
       "jnxMIMstBufferOverFlowCount": jnxMIMstBufferOverFlowCount,
       "jnxMIMstMemAllocFailureCount": jnxMIMstMemAllocFailureCount,
       "jnxMIMstRegionConfigChangeCount": jnxMIMstRegionConfigChangeCount,
       "jnxMIMstCistBridgeRoleSelectionSemState": jnxMIMstCistBridgeRoleSelectionSemState,
       "jnxMIMstCistTimeSinceTopologyChange": jnxMIMstCistTimeSinceTopologyChange,
       "jnxMIMstCistTopChanges": jnxMIMstCistTopChanges,
       "jnxMIMstCistNewRootBridgeCount": jnxMIMstCistNewRootBridgeCount,
       "jnxMIMstCistHelloTime": jnxMIMstCistHelloTime,
       "jnxMIMstCistBridgeHelloTime": jnxMIMstCistBridgeHelloTime,
       "jnxMIMstCistDynamicPathcostCalculation": jnxMIMstCistDynamicPathcostCalculation,
       "jnxMIMstMstiBridgeTable": jnxMIMstMstiBridgeTable,
       "jnxMIMstMstiBridgeEntry": jnxMIMstMstiBridgeEntry,
       "jnxMIMstMstiInstanceIndex": jnxMIMstMstiInstanceIndex,
       "jnxMIMstMstiBridgeRegionalRoot": jnxMIMstMstiBridgeRegionalRoot,
       "jnxMIMstMstiBridgePriority": jnxMIMstMstiBridgePriority,
       "jnxMIMstMstiRootCost": jnxMIMstMstiRootCost,
       "jnxMIMstMstiRootPort": jnxMIMstMstiRootPort,
       "jnxMIMstMstiTimeSinceTopologyChange": jnxMIMstMstiTimeSinceTopologyChange,
       "jnxMIMstMstiTopChanges": jnxMIMstMstiTopChanges,
       "jnxMIMstMstiNewRootBridgeCount": jnxMIMstMstiNewRootBridgeCount,
       "jnxMIMstMstiBridgeRoleSelectionSemState": jnxMIMstMstiBridgeRoleSelectionSemState,
       "jnxMIMstInstanceUpCount": jnxMIMstInstanceUpCount,
       "jnxMIMstInstanceDownCount": jnxMIMstInstanceDownCount,
       "jnxMIMstOldDesignatedRoot": jnxMIMstOldDesignatedRoot,
       "jnxMIMstVlanInstanceMappingTable": jnxMIMstVlanInstanceMappingTable,
       "jnxMIMstVlanInstanceMappingEntry": jnxMIMstVlanInstanceMappingEntry,
       "jnxMIMstInstanceIndex": jnxMIMstInstanceIndex,
       "jnxMIMstMapVlanIndex": jnxMIMstMapVlanIndex,
       "jnxMIMstUnMapVlanIndex": jnxMIMstUnMapVlanIndex,
       "jnxMIMstSetVlanList": jnxMIMstSetVlanList,
       "jnxMIMstResetVlanList": jnxMIMstResetVlanList,
       "jnxMIMstInstanceVlanMapped": jnxMIMstInstanceVlanMapped,
       "jnxMIMstInstanceVlanMapped2k": jnxMIMstInstanceVlanMapped2k,
       "jnxMIMstInstanceVlanMapped3k": jnxMIMstInstanceVlanMapped3k,
       "jnxMIMstInstanceVlanMapped4k": jnxMIMstInstanceVlanMapped4k,
       "jnxMIMstCistPortTable": jnxMIMstCistPortTable,
       "jnxMIMstCistPortEntry": jnxMIMstCistPortEntry,
       "jnxMIMstCistPort": jnxMIMstCistPort,
       "jnxMIMstCistPortPathCost": jnxMIMstCistPortPathCost,
       "jnxMIMstCistPortPriority": jnxMIMstCistPortPriority,
       "jnxMIMstCistPortDesignatedRoot": jnxMIMstCistPortDesignatedRoot,
       "jnxMIMstCistPortDesignatedBridge": jnxMIMstCistPortDesignatedBridge,
       "jnxMIMstCistPortDesignatedPort": jnxMIMstCistPortDesignatedPort,
       "jnxMIMstCistPortAdminP2P": jnxMIMstCistPortAdminP2P,
       "jnxMIMstCistPortOperP2P": jnxMIMstCistPortOperP2P,
       "jnxMIMstCistPortAdminEdgeStatus": jnxMIMstCistPortAdminEdgeStatus,
       "jnxMIMstCistPortOperEdgeStatus": jnxMIMstCistPortOperEdgeStatus,
       "jnxMIMstCistPortProtocolMigration": jnxMIMstCistPortProtocolMigration,
       "jnxMIMstCistPortState": jnxMIMstCistPortState,
       "jnxMIMstCistForcePortState": jnxMIMstCistForcePortState,
       "jnxMIMstCistPortForwardTransitions": jnxMIMstCistPortForwardTransitions,
       "jnxMIMstCistPortRxMstBpduCount": jnxMIMstCistPortRxMstBpduCount,
       "jnxMIMstCistPortRxRstBpduCount": jnxMIMstCistPortRxRstBpduCount,
       "jnxMIMstCistPortRxConfigBpduCount": jnxMIMstCistPortRxConfigBpduCount,
       "jnxMIMstCistPortRxTcnBpduCount": jnxMIMstCistPortRxTcnBpduCount,
       "jnxMIMstCistPortTxMstBpduCount": jnxMIMstCistPortTxMstBpduCount,
       "jnxMIMstCistPortTxRstBpduCount": jnxMIMstCistPortTxRstBpduCount,
       "jnxMIMstCistPortTxConfigBpduCount": jnxMIMstCistPortTxConfigBpduCount,
       "jnxMIMstCistPortTxTcnBpduCount": jnxMIMstCistPortTxTcnBpduCount,
       "jnxMIMstCistPortInvalidMstBpduRxCount": jnxMIMstCistPortInvalidMstBpduRxCount,
       "jnxMIMstCistPortInvalidRstBpduRxCount": jnxMIMstCistPortInvalidRstBpduRxCount,
       "jnxMIMstCistPortInvalidConfigBpduRxCount": jnxMIMstCistPortInvalidConfigBpduRxCount,
       "jnxMIMstCistPortInvalidTcnBpduRxCount": jnxMIMstCistPortInvalidTcnBpduRxCount,
       "jnxMIMstCistPortTransmitSemState": jnxMIMstCistPortTransmitSemState,
       "jnxMIMstCistPortReceiveSemState": jnxMIMstCistPortReceiveSemState,
       "jnxMIMstCistPortProtMigrationSemState": jnxMIMstCistPortProtMigrationSemState,
       "jnxMIMstCistProtocolMigrationCount": jnxMIMstCistProtocolMigrationCount,
       "jnxMIMstCistPortDesignatedCost": jnxMIMstCistPortDesignatedCost,
       "jnxMIMstCistPortRegionalRoot": jnxMIMstCistPortRegionalRoot,
       "jnxMIMstCistPortRegionalPathCost": jnxMIMstCistPortRegionalPathCost,
       "jnxMIMstCistSelectedPortRole": jnxMIMstCistSelectedPortRole,
       "jnxMIMstCistCurrentPortRole": jnxMIMstCistCurrentPortRole,
       "jnxMIMstCistPortInfoSemState": jnxMIMstCistPortInfoSemState,
       "jnxMIMstCistPortRoleTransitionSemState": jnxMIMstCistPortRoleTransitionSemState,
       "jnxMIMstCistPortStateTransitionSemState": jnxMIMstCistPortStateTransitionSemState,
       "jnxMIMstCistPortTopologyChangeSemState": jnxMIMstCistPortTopologyChangeSemState,
       "jnxMIMstCistPortHelloTime": jnxMIMstCistPortHelloTime,
       "jnxMIMstCistPortOperVersion": jnxMIMstCistPortOperVersion,
       "jnxMIMstCistPortEffectivePortState": jnxMIMstCistPortEffectivePortState,
       "jnxMIMstCistPortAutoEdgeStatus": jnxMIMstCistPortAutoEdgeStatus,
       "jnxMIMstMstiPortTable": jnxMIMstMstiPortTable,
       "jnxMIMstMstiPortEntry": jnxMIMstMstiPortEntry,
       "jnxMIMstMstiPort": jnxMIMstMstiPort,
       "jnxMIMstMstiPortPathCost": jnxMIMstMstiPortPathCost,
       "jnxMIMstMstiPortPriority": jnxMIMstMstiPortPriority,
       "jnxMIMstMstiPortDesignatedRoot": jnxMIMstMstiPortDesignatedRoot,
       "jnxMIMstMstiPortDesignatedBridge": jnxMIMstMstiPortDesignatedBridge,
       "jnxMIMstMstiPortDesignatedPort": jnxMIMstMstiPortDesignatedPort,
       "jnxMIMstMstiPortState": jnxMIMstMstiPortState,
       "jnxMIMstMstiForcePortState": jnxMIMstMstiForcePortState,
       "jnxMIMstMstiPortForwardTransitions": jnxMIMstMstiPortForwardTransitions,
       "jnxMIMstMstiPortReceivedBPDUs": jnxMIMstMstiPortReceivedBPDUs,
       "jnxMIMstMstiPortTransmittedBPDUs": jnxMIMstMstiPortTransmittedBPDUs,
       "jnxMIMstMstiPortInvalidBPDUsRcvd": jnxMIMstMstiPortInvalidBPDUsRcvd,
       "jnxMIMstMstiPortDesignatedCost": jnxMIMstMstiPortDesignatedCost,
       "jnxMIMstMstiSelectedPortRole": jnxMIMstMstiSelectedPortRole,
       "jnxMIMstMstiCurrentPortRole": jnxMIMstMstiCurrentPortRole,
       "jnxMIMstMstiPortInfoSemState": jnxMIMstMstiPortInfoSemState,
       "jnxMIMstMstiPortRoleTransitionSemState": jnxMIMstMstiPortRoleTransitionSemState,
       "jnxMIMstMstiPortStateTransitionSemState": jnxMIMstMstiPortStateTransitionSemState,
       "jnxMIMstMstiPortTopologyChangeSemState": jnxMIMstMstiPortTopologyChangeSemState,
       "jnxMIMstMstiPortEffectivePortState": jnxMIMstMstiPortEffectivePortState,
       "jnxMIMstCistPortProtectTable": jnxMIMstCistPortProtectTable,
       "jnxMIMstCistPortProtectEntry": jnxMIMstCistPortProtectEntry,
       "jnxMIMstCistPortRootProtectEnabled": jnxMIMstCistPortRootProtectEnabled,
       "jnxMIMstCistPortRootProtectState": jnxMIMstCistPortRootProtectState,
       "jnxMIMstCistPortLoopProtectEnabled": jnxMIMstCistPortLoopProtectEnabled,
       "jnxMIMstCistPortLoopProtectState": jnxMIMstCistPortLoopProtectState,
       "jnxMIMstMstiPortProtectTable": jnxMIMstMstiPortProtectTable,
       "jnxMIMstMstiPortProtectEntry": jnxMIMstMstiPortProtectEntry,
       "jnxMIMstMstiPortRootProtectState": jnxMIMstMstiPortRootProtectState,
       "jnxMIMstMstiPortLoopProtectState": jnxMIMstMstiPortLoopProtectState,
       "jnxMIDot1sJnxMstTrapsControl": jnxMIDot1sJnxMstTrapsControl,
       "jnxMIDot1sJnxMstSetGlobalTrapOption": jnxMIDot1sJnxMstSetGlobalTrapOption,
       "jnxMIMstGlobalErrTrapType": jnxMIMstGlobalErrTrapType,
       "jnxMIDot1sJnxMstTrapsControlTable": jnxMIDot1sJnxMstTrapsControlTable,
       "jnxMIDot1sJnxMstTrapsControlEntry": jnxMIDot1sJnxMstTrapsControlEntry,
       "jnxMIMstSetTraps": jnxMIMstSetTraps,
       "jnxMIMstGenTrapType": jnxMIMstGenTrapType,
       "jnxMIMstPortTrapNotificationTable": jnxMIMstPortTrapNotificationTable,
       "jnxMIMstPortTrapNotificationEntry": jnxMIMstPortTrapNotificationEntry,
       "jnxMIMstPortTrapIndex": jnxMIMstPortTrapIndex,
       "jnxMIMstPortMigrationType": jnxMIMstPortMigrationType,
       "jnxMIMstPktErrType": jnxMIMstPktErrType,
       "jnxMIMstPktErrVal": jnxMIMstPktErrVal,
       "jnxMIDot1sJuniperMstTraps": jnxMIDot1sJuniperMstTraps,
       "jnxMIMstTraps": jnxMIMstTraps,
       "jnxMIMstGenTrap": jnxMIMstGenTrap,
       "jnxMIMstErrTrap": jnxMIMstErrTrap,
       "jnxMIMstNewRootTrap": jnxMIMstNewRootTrap,
       "jnxMIMstTopologyChgTrap": jnxMIMstTopologyChgTrap,
       "jnxMIMstProtocolMigrationTrap": jnxMIMstProtocolMigrationTrap,
       "jnxMIMstInvalidBpduRxdTrap": jnxMIMstInvalidBpduRxdTrap,
       "jnxMIMstRegionConfigChangeTrap": jnxMIMstRegionConfigChangeTrap,
       "jnxMIMstCistPortRootProtectStateChangeTrap": jnxMIMstCistPortRootProtectStateChangeTrap,
       "jnxMIMstMstiPortRootProtectStateChangeTrap": jnxMIMstMstiPortRootProtectStateChangeTrap,
       "jnxMIMstCistPortLoopProtectStateChangeTrap": jnxMIMstCistPortLoopProtectStateChangeTrap,
       "jnxMIMstMstiPortLoopProtectStateChangeTrap": jnxMIMstMstiPortLoopProtectStateChangeTrap}
)
