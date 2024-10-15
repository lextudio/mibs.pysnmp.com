# SNMP MIB module (ALCATEL-IND1-DCBX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-DCBX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:49 2024
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

(softentIND1Dcbx,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Dcbx")

(VfcEnableState,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB",
    "VfcEnableState")

(IEEE8021PriorityValue,) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021PriorityValue")

(LldpXdot1dcbxAppProtocol,
 LldpXdot1dcbxAppSelector,
 LldpXdot1dcbxSupportedCapacity,
 LldpXdot1dcbxTrafficClassBandwidthValue,
 LldpXdot1dcbxTrafficClassValue,
 LldpXdot1dcbxTrafficSelectionAlgorithm,
 lldpXdot1dcbxAdminApplicationPriorityAEProtocol,
 lldpXdot1dcbxAdminApplicationPriorityAESelector) = mibBuilder.importSymbols(
    "LLDP-EXT-DOT1-V2-MIB",
    "LldpXdot1dcbxAppProtocol",
    "LldpXdot1dcbxAppSelector",
    "LldpXdot1dcbxSupportedCapacity",
    "LldpXdot1dcbxTrafficClassBandwidthValue",
    "LldpXdot1dcbxTrafficClassValue",
    "LldpXdot1dcbxTrafficSelectionAlgorithm",
    "lldpXdot1dcbxAdminApplicationPriorityAEProtocol",
    "lldpXdot1dcbxAdminApplicationPriorityAESelector")

(lldpV2LocPortIfIndex,) = mibBuilder.importSymbols(
    "LLDP-V2-MIB",
    "lldpV2LocPortIfIndex")

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

alcatelIND1DcbxMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1)
)
alcatelIND1DcbxMIB.setRevisions(
        ("2011-06-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DcbxTrafficFlow(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tfLossless", 1),
          ("tfLossy", 0))
    )



class DcbxPriorityTCMap(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )



class DcbxStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("etsPfcTlvMismatch", 4),
          ("etsTlvMismatch", 3),
          ("ok", 0),
          ("pfcResourcesExhausted", 1),
          ("pfcTlvMismatch", 2))
    )



class DcbxActionTaken(Integer32, TextualConvention):
    status = "current"
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
        *(("cfgLocalAdmin", 5),
          ("cfgLocalRecom", 6),
          ("cfgRemoteAdmin", 7),
          ("cfgRemoteRecom", 8),
          ("disabledPfc", 3),
          ("na", 0),
          ("restEtsAdminCfg", 1),
          ("restEtsPfcAdminCfg", 4),
          ("restPfcAdminCfg", 2))
    )



class DcbxTCsPresent(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )



class DcbxVersion(Integer32, TextualConvention):
    status = "current"
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
          ("cee", 1),
          ("ieee", 0))
    )



class RemoteDcbxVersion(Integer32, TextualConvention):
    status = "current"
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
        *(("auto", 2),
          ("cee", 1),
          ("ieee", 0),
          ("unknown", 3))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1DcbxMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1DcbxMIBObjects = _AlcatelIND1DcbxMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1DcbxMIBObjects.setStatus("current")
_AlaDcbxConfig_ObjectIdentity = ObjectIdentity
alaDcbxConfig = _AlaDcbxConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1)
)
_AlaDcbxDCProfileTable_Object = MibTable
alaDcbxDCProfileTable = _AlaDcbxDCProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaDcbxDCProfileTable.setStatus("current")
_AlaDcbxDCProfileEntry_Object = MibTableRow
alaDcbxDCProfileEntry = _AlaDcbxDCProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 1, 1)
)
alaDcbxDCProfileEntry.setIndexNames(
    (0, "ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPId"),
)
if mibBuilder.loadTexts:
    alaDcbxDCProfileEntry.setStatus("current")


class _AlaDcbxDCPId_Type(Unsigned32):
    """Custom type alaDcbxDCPId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_AlaDcbxDCPId_Type.__name__ = "Unsigned32"
_AlaDcbxDCPId_Object = MibTableColumn
alaDcbxDCPId = _AlaDcbxDCPId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 1, 1, 1),
    _AlaDcbxDCPId_Type()
)
alaDcbxDCPId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDcbxDCPId.setStatus("current")


class _AlaDcbxDCPName_Type(SnmpAdminString):
    """Custom type alaDcbxDCPName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDcbxDCPName_Type.__name__ = "SnmpAdminString"
_AlaDcbxDCPName_Object = MibTableColumn
alaDcbxDCPName = _AlaDcbxDCPName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 1, 1, 2),
    _AlaDcbxDCPName_Type()
)
alaDcbxDCPName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDcbxDCPName.setStatus("current")
_AlaDcbxDCPETSTrafficClassesSupported_Type = LldpXdot1dcbxSupportedCapacity
_AlaDcbxDCPETSTrafficClassesSupported_Object = MibTableColumn
alaDcbxDCPETSTrafficClassesSupported = _AlaDcbxDCPETSTrafficClassesSupported_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 1, 1, 3),
    _AlaDcbxDCPETSTrafficClassesSupported_Type()
)
alaDcbxDCPETSTrafficClassesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDcbxDCPETSTrafficClassesSupported.setStatus("current")
_AlaDcbxDCPPFCCap_Type = LldpXdot1dcbxSupportedCapacity
_AlaDcbxDCPPFCCap_Object = MibTableColumn
alaDcbxDCPPFCCap = _AlaDcbxDCPPFCCap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 1, 1, 4),
    _AlaDcbxDCPPFCCap_Type()
)
alaDcbxDCPPFCCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDcbxDCPPFCCap.setStatus("current")
_AlaDcbxDCPPriorityTCMap_Type = DcbxPriorityTCMap
_AlaDcbxDCPPriorityTCMap_Object = MibTableColumn
alaDcbxDCPPriorityTCMap = _AlaDcbxDCPPriorityTCMap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 1, 1, 5),
    _AlaDcbxDCPPriorityTCMap_Type()
)
alaDcbxDCPPriorityTCMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDcbxDCPPriorityTCMap.setStatus("current")


class _AlaDcbxDCPTemplateDCPId_Type(Unsigned32):
    """Custom type alaDcbxDCPTemplateDCPId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_AlaDcbxDCPTemplateDCPId_Type.__name__ = "Unsigned32"
_AlaDcbxDCPTemplateDCPId_Object = MibTableColumn
alaDcbxDCPTemplateDCPId = _AlaDcbxDCPTemplateDCPId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 1, 1, 6),
    _AlaDcbxDCPTemplateDCPId_Type()
)
alaDcbxDCPTemplateDCPId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDcbxDCPTemplateDCPId.setStatus("current")


class _AlaDcbxDCPTemplateDCPName_Type(SnmpAdminString):
    """Custom type alaDcbxDCPTemplateDCPName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDcbxDCPTemplateDCPName_Type.__name__ = "SnmpAdminString"
_AlaDcbxDCPTemplateDCPName_Object = MibTableColumn
alaDcbxDCPTemplateDCPName = _AlaDcbxDCPTemplateDCPName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 1, 1, 7),
    _AlaDcbxDCPTemplateDCPName_Type()
)
alaDcbxDCPTemplateDCPName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDcbxDCPTemplateDCPName.setStatus("current")
_AlaDcbxDCPTCsPresent_Type = DcbxTCsPresent
_AlaDcbxDCPTCsPresent_Object = MibTableColumn
alaDcbxDCPTCsPresent = _AlaDcbxDCPTCsPresent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 1, 1, 8),
    _AlaDcbxDCPTCsPresent_Type()
)
alaDcbxDCPTCsPresent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDcbxDCPTCsPresent.setStatus("current")


class _AlaDcbxDCP8023xPauseReady_Type(VfcEnableState):
    """Custom type alaDcbxDCP8023xPauseReady based on VfcEnableState"""


_AlaDcbxDCP8023xPauseReady_Object = MibTableColumn
alaDcbxDCP8023xPauseReady = _AlaDcbxDCP8023xPauseReady_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 1, 1, 9),
    _AlaDcbxDCP8023xPauseReady_Type()
)
alaDcbxDCP8023xPauseReady.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDcbxDCP8023xPauseReady.setStatus("current")
_AlaDcbxDCPRowStatus_Type = RowStatus
_AlaDcbxDCPRowStatus_Object = MibTableColumn
alaDcbxDCPRowStatus = _AlaDcbxDCPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 1, 1, 10),
    _AlaDcbxDCPRowStatus_Type()
)
alaDcbxDCPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDcbxDCPRowStatus.setStatus("current")
_AlaDcbxDCPTrafficClassTable_Object = MibTable
alaDcbxDCPTrafficClassTable = _AlaDcbxDCPTrafficClassTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaDcbxDCPTrafficClassTable.setStatus("current")
_AlaDcbxDCPTCEntry_Object = MibTableRow
alaDcbxDCPTCEntry = _AlaDcbxDCPTCEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 2, 1)
)
alaDcbxDCPTCEntry.setIndexNames(
    (0, "ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPTCDCPId"),
    (0, "ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPTCTrafficClass"),
)
if mibBuilder.loadTexts:
    alaDcbxDCPTCEntry.setStatus("current")


class _AlaDcbxDCPTCDCPId_Type(Unsigned32):
    """Custom type alaDcbxDCPTCDCPId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_AlaDcbxDCPTCDCPId_Type.__name__ = "Unsigned32"
_AlaDcbxDCPTCDCPId_Object = MibTableColumn
alaDcbxDCPTCDCPId = _AlaDcbxDCPTCDCPId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 2, 1, 1),
    _AlaDcbxDCPTCDCPId_Type()
)
alaDcbxDCPTCDCPId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDcbxDCPTCDCPId.setStatus("current")
_AlaDcbxDCPTCTrafficClass_Type = LldpXdot1dcbxTrafficClassValue
_AlaDcbxDCPTCTrafficClass_Object = MibTableColumn
alaDcbxDCPTCTrafficClass = _AlaDcbxDCPTCTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 2, 1, 2),
    _AlaDcbxDCPTCTrafficClass_Type()
)
alaDcbxDCPTCTrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDcbxDCPTCTrafficClass.setStatus("current")


class _AlaDcbxDCPTCDCPName_Type(SnmpAdminString):
    """Custom type alaDcbxDCPTCDCPName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDcbxDCPTCDCPName_Type.__name__ = "SnmpAdminString"
_AlaDcbxDCPTCDCPName_Object = MibTableColumn
alaDcbxDCPTCDCPName = _AlaDcbxDCPTCDCPName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 2, 1, 3),
    _AlaDcbxDCPTCDCPName_Type()
)
alaDcbxDCPTCDCPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDcbxDCPTCDCPName.setStatus("current")
_AlaDcbxDCPTCMaximumBandwidth_Type = LldpXdot1dcbxTrafficClassBandwidthValue
_AlaDcbxDCPTCMaximumBandwidth_Object = MibTableColumn
alaDcbxDCPTCMaximumBandwidth = _AlaDcbxDCPTCMaximumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 2, 1, 4),
    _AlaDcbxDCPTCMaximumBandwidth_Type()
)
alaDcbxDCPTCMaximumBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDcbxDCPTCMaximumBandwidth.setStatus("current")
_AlaDcbxDCPTCMinimumBandwidth_Type = LldpXdot1dcbxTrafficClassBandwidthValue
_AlaDcbxDCPTCMinimumBandwidth_Object = MibTableColumn
alaDcbxDCPTCMinimumBandwidth = _AlaDcbxDCPTCMinimumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 2, 1, 5),
    _AlaDcbxDCPTCMinimumBandwidth_Type()
)
alaDcbxDCPTCMinimumBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDcbxDCPTCMinimumBandwidth.setStatus("current")


class _AlaDcbxDCPTCPFCLinkDelay_Type(Unsigned32):
    """Custom type alaDcbxDCPTCPFCLinkDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 100),
    )


_AlaDcbxDCPTCPFCLinkDelay_Type.__name__ = "Unsigned32"
_AlaDcbxDCPTCPFCLinkDelay_Object = MibTableColumn
alaDcbxDCPTCPFCLinkDelay = _AlaDcbxDCPTCPFCLinkDelay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 2, 1, 6),
    _AlaDcbxDCPTCPFCLinkDelay_Type()
)
alaDcbxDCPTCPFCLinkDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDcbxDCPTCPFCLinkDelay.setStatus("current")


class _AlaDcbxDCPTCPFCLinkDelayUserModified_Type(TruthValue):
    """Custom type alaDcbxDCPTCPFCLinkDelayUserModified based on TruthValue"""


_AlaDcbxDCPTCPFCLinkDelayUserModified_Object = MibTableColumn
alaDcbxDCPTCPFCLinkDelayUserModified = _AlaDcbxDCPTCPFCLinkDelayUserModified_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 2, 1, 7),
    _AlaDcbxDCPTCPFCLinkDelayUserModified_Type()
)
alaDcbxDCPTCPFCLinkDelayUserModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDcbxDCPTCPFCLinkDelayUserModified.setStatus("current")
_AlaDcbxDCPTCPFCTrafficFlow_Type = DcbxTrafficFlow
_AlaDcbxDCPTCPFCTrafficFlow_Object = MibTableColumn
alaDcbxDCPTCPFCTrafficFlow = _AlaDcbxDCPTCPFCTrafficFlow_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 2, 1, 8),
    _AlaDcbxDCPTCPFCTrafficFlow_Type()
)
alaDcbxDCPTCPFCTrafficFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDcbxDCPTCPFCTrafficFlow.setStatus("current")
_AlaDcbxDCPTCPriorityMap_Type = Unsigned32
_AlaDcbxDCPTCPriorityMap_Object = MibTableColumn
alaDcbxDCPTCPriorityMap = _AlaDcbxDCPTCPriorityMap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 2, 1, 9),
    _AlaDcbxDCPTCPriorityMap_Type()
)
alaDcbxDCPTCPriorityMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDcbxDCPTCPriorityMap.setStatus("current")
_AlaDcbxDCPTCTrafficScheduler_Type = LldpXdot1dcbxTrafficSelectionAlgorithm
_AlaDcbxDCPTCTrafficScheduler_Object = MibTableColumn
alaDcbxDCPTCTrafficScheduler = _AlaDcbxDCPTCTrafficScheduler_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 2, 1, 10),
    _AlaDcbxDCPTCTrafficScheduler_Type()
)
alaDcbxDCPTCTrafficScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDcbxDCPTCTrafficScheduler.setStatus("current")
_AlaDcbxDCPTCRecommendedBandwidth_Type = LldpXdot1dcbxTrafficClassBandwidthValue
_AlaDcbxDCPTCRecommendedBandwidth_Object = MibTableColumn
alaDcbxDCPTCRecommendedBandwidth = _AlaDcbxDCPTCRecommendedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 2, 1, 11),
    _AlaDcbxDCPTCRecommendedBandwidth_Type()
)
alaDcbxDCPTCRecommendedBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDcbxDCPTCRecommendedBandwidth.setStatus("current")
_AlaDcbxDCPTCRecommendedTrafficScheduler_Type = LldpXdot1dcbxTrafficSelectionAlgorithm
_AlaDcbxDCPTCRecommendedTrafficScheduler_Object = MibTableColumn
alaDcbxDCPTCRecommendedTrafficScheduler = _AlaDcbxDCPTCRecommendedTrafficScheduler_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 2, 1, 12),
    _AlaDcbxDCPTCRecommendedTrafficScheduler_Type()
)
alaDcbxDCPTCRecommendedTrafficScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDcbxDCPTCRecommendedTrafficScheduler.setStatus("current")
_AlaDcbxPortInstanceTable_Object = MibTable
alaDcbxPortInstanceTable = _AlaDcbxPortInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alaDcbxPortInstanceTable.setStatus("current")
_AlaDcbxPortInstanceEntry_Object = MibTableRow
alaDcbxPortInstanceEntry = _AlaDcbxPortInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3, 1)
)
alaDcbxPortInstanceEntry.setIndexNames(
    (0, "ALCATEL-IND1-DCBX-MIB", "alaDcbxPIIfIndex"),
)
if mibBuilder.loadTexts:
    alaDcbxPortInstanceEntry.setStatus("current")
_AlaDcbxPIIfIndex_Type = Unsigned32
_AlaDcbxPIIfIndex_Object = MibTableColumn
alaDcbxPIIfIndex = _AlaDcbxPIIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3, 1, 1),
    _AlaDcbxPIIfIndex_Type()
)
alaDcbxPIIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDcbxPIIfIndex.setStatus("current")


class _AlaDcbxPIDCBXAdmin_Type(VfcEnableState):
    """Custom type alaDcbxPIDCBXAdmin based on VfcEnableState"""


_AlaDcbxPIDCBXAdmin_Object = MibTableColumn
alaDcbxPIDCBXAdmin = _AlaDcbxPIDCBXAdmin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3, 1, 2),
    _AlaDcbxPIDCBXAdmin_Type()
)
alaDcbxPIDCBXAdmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDcbxPIDCBXAdmin.setStatus("current")


class _AlaDcbxPIDCBXOper_Type(VfcEnableState):
    """Custom type alaDcbxPIDCBXOper based on VfcEnableState"""


_AlaDcbxPIDCBXOper_Object = MibTableColumn
alaDcbxPIDCBXOper = _AlaDcbxPIDCBXOper_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3, 1, 3),
    _AlaDcbxPIDCBXOper_Type()
)
alaDcbxPIDCBXOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDcbxPIDCBXOper.setStatus("current")


class _AlaDcbxPIAdminDCPId_Type(Unsigned32):
    """Custom type alaDcbxPIAdminDCPId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_AlaDcbxPIAdminDCPId_Type.__name__ = "Unsigned32"
_AlaDcbxPIAdminDCPId_Object = MibTableColumn
alaDcbxPIAdminDCPId = _AlaDcbxPIAdminDCPId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3, 1, 4),
    _AlaDcbxPIAdminDCPId_Type()
)
alaDcbxPIAdminDCPId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDcbxPIAdminDCPId.setStatus("current")


class _AlaDcbxPIAdminDCPName_Type(SnmpAdminString):
    """Custom type alaDcbxPIAdminDCPName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDcbxPIAdminDCPName_Type.__name__ = "SnmpAdminString"
_AlaDcbxPIAdminDCPName_Object = MibTableColumn
alaDcbxPIAdminDCPName = _AlaDcbxPIAdminDCPName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3, 1, 5),
    _AlaDcbxPIAdminDCPName_Type()
)
alaDcbxPIAdminDCPName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDcbxPIAdminDCPName.setStatus("current")


class _AlaDcbxPILocalModified_Type(TruthValue):
    """Custom type alaDcbxPILocalModified based on TruthValue"""


_AlaDcbxPILocalModified_Object = MibTableColumn
alaDcbxPILocalModified = _AlaDcbxPILocalModified_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3, 1, 6),
    _AlaDcbxPILocalModified_Type()
)
alaDcbxPILocalModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDcbxPILocalModified.setStatus("current")


class _AlaDcbxPIPFCDefense_Type(VfcEnableState):
    """Custom type alaDcbxPIPFCDefense based on VfcEnableState"""


_AlaDcbxPIPFCDefense_Object = MibTableColumn
alaDcbxPIPFCDefense = _AlaDcbxPIPFCDefense_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3, 1, 7),
    _AlaDcbxPIPFCDefense_Type()
)
alaDcbxPIPFCDefense.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDcbxPIPFCDefense.setStatus("current")


class _AlaDcbxPIPFCStatsClear_Type(VfcEnableState):
    """Custom type alaDcbxPIPFCStatsClear based on VfcEnableState"""


_AlaDcbxPIPFCStatsClear_Object = MibTableColumn
alaDcbxPIPFCStatsClear = _AlaDcbxPIPFCStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3, 1, 8),
    _AlaDcbxPIPFCStatsClear_Type()
)
alaDcbxPIPFCStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDcbxPIPFCStatsClear.setStatus("current")


class _AlaDcbxPIStatus_Type(DcbxStatus):
    """Custom type alaDcbxPIStatus based on DcbxStatus"""


_AlaDcbxPIStatus_Object = MibTableColumn
alaDcbxPIStatus = _AlaDcbxPIStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3, 1, 9),
    _AlaDcbxPIStatus_Type()
)
alaDcbxPIStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDcbxPIStatus.setStatus("current")


class _AlaDcbxPIActionTaken_Type(DcbxActionTaken):
    """Custom type alaDcbxPIActionTaken based on DcbxActionTaken"""


_AlaDcbxPIActionTaken_Object = MibTableColumn
alaDcbxPIActionTaken = _AlaDcbxPIActionTaken_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3, 1, 10),
    _AlaDcbxPIActionTaken_Type()
)
alaDcbxPIActionTaken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDcbxPIActionTaken.setStatus("current")
_AlaDcbxPIRowStatus_Type = RowStatus
_AlaDcbxPIRowStatus_Object = MibTableColumn
alaDcbxPIRowStatus = _AlaDcbxPIRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3, 1, 11),
    _AlaDcbxPIRowStatus_Type()
)
alaDcbxPIRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDcbxPIRowStatus.setStatus("current")
_AlaDcbxPIDCBXVersion_Type = DcbxVersion
_AlaDcbxPIDCBXVersion_Object = MibTableColumn
alaDcbxPIDCBXVersion = _AlaDcbxPIDCBXVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3, 1, 12),
    _AlaDcbxPIDCBXVersion_Type()
)
alaDcbxPIDCBXVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDcbxPIDCBXVersion.setStatus("current")
_AlaDcbxPIDCBXOperVersion_Type = DcbxVersion
_AlaDcbxPIDCBXOperVersion_Object = MibTableColumn
alaDcbxPIDCBXOperVersion = _AlaDcbxPIDCBXOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3, 1, 13),
    _AlaDcbxPIDCBXOperVersion_Type()
)
alaDcbxPIDCBXOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDcbxPIDCBXOperVersion.setStatus("current")
_AlaDcbxPIDCBXRemoteOperVersion_Type = RemoteDcbxVersion
_AlaDcbxPIDCBXRemoteOperVersion_Object = MibTableColumn
alaDcbxPIDCBXRemoteOperVersion = _AlaDcbxPIDCBXRemoteOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3, 1, 14),
    _AlaDcbxPIDCBXRemoteOperVersion_Type()
)
alaDcbxPIDCBXRemoteOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDcbxPIDCBXRemoteOperVersion.setStatus("current")
_AlaDcbxPIPriorityTable_Object = MibTable
alaDcbxPIPriorityTable = _AlaDcbxPIPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alaDcbxPIPriorityTable.setStatus("current")
_AlaDcbxPIPrioEntry_Object = MibTableRow
alaDcbxPIPrioEntry = _AlaDcbxPIPrioEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 4, 1)
)
alaDcbxPIPrioEntry.setIndexNames(
    (0, "ALCATEL-IND1-DCBX-MIB", "alaDcbxPIPrioIfIndex"),
    (0, "ALCATEL-IND1-DCBX-MIB", "alaDcbxPIPrioPriority"),
)
if mibBuilder.loadTexts:
    alaDcbxPIPrioEntry.setStatus("current")
_AlaDcbxPIPrioIfIndex_Type = Unsigned32
_AlaDcbxPIPrioIfIndex_Object = MibTableColumn
alaDcbxPIPrioIfIndex = _AlaDcbxPIPrioIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 4, 1, 1),
    _AlaDcbxPIPrioIfIndex_Type()
)
alaDcbxPIPrioIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDcbxPIPrioIfIndex.setStatus("current")
_AlaDcbxPIPrioPriority_Type = IEEE8021PriorityValue
_AlaDcbxPIPrioPriority_Object = MibTableColumn
alaDcbxPIPrioPriority = _AlaDcbxPIPrioPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 4, 1, 2),
    _AlaDcbxPIPrioPriority_Type()
)
alaDcbxPIPrioPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDcbxPIPrioPriority.setStatus("current")
_AlaDcbxPIPrioTC_Type = LldpXdot1dcbxTrafficClassValue
_AlaDcbxPIPrioTC_Object = MibTableColumn
alaDcbxPIPrioTC = _AlaDcbxPIPrioTC_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 4, 1, 3),
    _AlaDcbxPIPrioTC_Type()
)
alaDcbxPIPrioTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDcbxPIPrioTC.setStatus("current")
_AlaDcbxPIPrioPFCPacketsReceived_Type = Counter64
_AlaDcbxPIPrioPFCPacketsReceived_Object = MibTableColumn
alaDcbxPIPrioPFCPacketsReceived = _AlaDcbxPIPrioPFCPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 4, 1, 4),
    _AlaDcbxPIPrioPFCPacketsReceived_Type()
)
alaDcbxPIPrioPFCPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDcbxPIPrioPFCPacketsReceived.setStatus("current")
_AlaDcbxPIPrioPFCPacketsTransmitted_Type = Counter64
_AlaDcbxPIPrioPFCPacketsTransmitted_Object = MibTableColumn
alaDcbxPIPrioPFCPacketsTransmitted = _AlaDcbxPIPrioPFCPacketsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 4, 1, 5),
    _AlaDcbxPIPrioPFCPacketsTransmitted_Type()
)
alaDcbxPIPrioPFCPacketsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDcbxPIPrioPFCPacketsTransmitted.setStatus("current")
_AlaDcbxPfcLLPrioritiesUsed_Type = Unsigned32
_AlaDcbxPfcLLPrioritiesUsed_Object = MibScalar
alaDcbxPfcLLPrioritiesUsed = _AlaDcbxPfcLLPrioritiesUsed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 5),
    _AlaDcbxPfcLLPrioritiesUsed_Type()
)
alaDcbxPfcLLPrioritiesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDcbxPfcLLPrioritiesUsed.setStatus("deprecated")
_AlaDcbxPfcLLPrioritiesReserved_Type = Unsigned32
_AlaDcbxPfcLLPrioritiesReserved_Object = MibScalar
alaDcbxPfcLLPrioritiesReserved = _AlaDcbxPfcLLPrioritiesReserved_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 6),
    _AlaDcbxPfcLLPrioritiesReserved_Type()
)
alaDcbxPfcLLPrioritiesReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDcbxPfcLLPrioritiesReserved.setStatus("deprecated")
_AlaDcbxPfcLLPrioritiesAvailable_Type = Unsigned32
_AlaDcbxPfcLLPrioritiesAvailable_Object = MibScalar
alaDcbxPfcLLPrioritiesAvailable = _AlaDcbxPfcLLPrioritiesAvailable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 7),
    _AlaDcbxPfcLLPrioritiesAvailable_Type()
)
alaDcbxPfcLLPrioritiesAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDcbxPfcLLPrioritiesAvailable.setStatus("deprecated")
_AlaDcbxPfcUsageTable_Object = MibTable
alaDcbxPfcUsageTable = _AlaDcbxPfcUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    alaDcbxPfcUsageTable.setStatus("current")
_AlaDcbxPfcUsageEntry_Object = MibTableRow
alaDcbxPfcUsageEntry = _AlaDcbxPfcUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 8, 1)
)
alaDcbxPfcUsageEntry.setIndexNames(
    (0, "ALCATEL-IND1-DCBX-MIB", "alaDcbxPfcUsageChassisId"),
)
if mibBuilder.loadTexts:
    alaDcbxPfcUsageEntry.setStatus("current")
_AlaDcbxPfcUsageChassisId_Type = Unsigned32
_AlaDcbxPfcUsageChassisId_Object = MibTableColumn
alaDcbxPfcUsageChassisId = _AlaDcbxPfcUsageChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 8, 1, 1),
    _AlaDcbxPfcUsageChassisId_Type()
)
alaDcbxPfcUsageChassisId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDcbxPfcUsageChassisId.setStatus("current")
_AlaDcbxPfcUsagePrioritiesUsed_Type = Unsigned32
_AlaDcbxPfcUsagePrioritiesUsed_Object = MibTableColumn
alaDcbxPfcUsagePrioritiesUsed = _AlaDcbxPfcUsagePrioritiesUsed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 8, 1, 2),
    _AlaDcbxPfcUsagePrioritiesUsed_Type()
)
alaDcbxPfcUsagePrioritiesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDcbxPfcUsagePrioritiesUsed.setStatus("current")
_AlaDcbxPfcUsagePrioritiesReserved_Type = Unsigned32
_AlaDcbxPfcUsagePrioritiesReserved_Object = MibTableColumn
alaDcbxPfcUsagePrioritiesReserved = _AlaDcbxPfcUsagePrioritiesReserved_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 8, 1, 3),
    _AlaDcbxPfcUsagePrioritiesReserved_Type()
)
alaDcbxPfcUsagePrioritiesReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDcbxPfcUsagePrioritiesReserved.setStatus("current")
_AlaDcbxPfcUsagePrioritiesAvailable_Type = Unsigned32
_AlaDcbxPfcUsagePrioritiesAvailable_Object = MibTableColumn
alaDcbxPfcUsagePrioritiesAvailable = _AlaDcbxPfcUsagePrioritiesAvailable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 8, 1, 4),
    _AlaDcbxPfcUsagePrioritiesAvailable_Type()
)
alaDcbxPfcUsagePrioritiesAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDcbxPfcUsagePrioritiesAvailable.setStatus("current")
_AlaXdot1dcbxAdminApplicationPriorityAppTable_Object = MibTable
alaXdot1dcbxAdminApplicationPriorityAppTable = _AlaXdot1dcbxAdminApplicationPriorityAppTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    alaXdot1dcbxAdminApplicationPriorityAppTable.setStatus("current")
_AlaXdot1dcbxAdminApplicationPriorityAppEntry_Object = MibTableRow
alaXdot1dcbxAdminApplicationPriorityAppEntry = _AlaXdot1dcbxAdminApplicationPriorityAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 9, 1)
)
alaXdot1dcbxAdminApplicationPriorityAppEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxAdminApplicationPriorityAESelector"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxAdminApplicationPriorityAEProtocol"),
)
if mibBuilder.loadTexts:
    alaXdot1dcbxAdminApplicationPriorityAppEntry.setStatus("current")
_AlaXdot1dcbxAdminApplicationPriorityAEPriority_Type = IEEE8021PriorityValue
_AlaXdot1dcbxAdminApplicationPriorityAEPriority_Object = MibTableColumn
alaXdot1dcbxAdminApplicationPriorityAEPriority = _AlaXdot1dcbxAdminApplicationPriorityAEPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 9, 1, 1),
    _AlaXdot1dcbxAdminApplicationPriorityAEPriority_Type()
)
alaXdot1dcbxAdminApplicationPriorityAEPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaXdot1dcbxAdminApplicationPriorityAEPriority.setStatus("current")
_AlaXdot1dcbxAdminApplicationPriorityAppRowStatus_Type = RowStatus
_AlaXdot1dcbxAdminApplicationPriorityAppRowStatus_Object = MibTableColumn
alaXdot1dcbxAdminApplicationPriorityAppRowStatus = _AlaXdot1dcbxAdminApplicationPriorityAppRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 9, 1, 2),
    _AlaXdot1dcbxAdminApplicationPriorityAppRowStatus_Type()
)
alaXdot1dcbxAdminApplicationPriorityAppRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaXdot1dcbxAdminApplicationPriorityAppRowStatus.setStatus("current")
_AlaDcbxConformance_ObjectIdentity = ObjectIdentity
alaDcbxConformance = _AlaDcbxConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 2)
)
_AlcatelIND1DcbxMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1DcbxMIBConformance = _AlcatelIND1DcbxMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1DcbxMIBConformance.setStatus("current")
_AlcatelIND1DcbxMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1DcbxMIBGroups = _AlcatelIND1DcbxMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1DcbxMIBGroups.setStatus("current")
_AlcatelIND1DcbxMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1DcbxMIBCompliances = _AlcatelIND1DcbxMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1DcbxMIBCompliances.setStatus("current")

# Managed Objects groups

alaDcbxDCProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 2, 1, 1)
)
alaDcbxDCProfileGroup.setObjects(
      *(("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPName"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPETSTrafficClassesSupported"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPPFCCap"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPPriorityTCMap"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPTemplateDCPId"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPTemplateDCPName"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPTCsPresent"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCP8023xPauseReady"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPRowStatus"))
)
if mibBuilder.loadTexts:
    alaDcbxDCProfileGroup.setStatus("current")

alaDcbxDCPTrafficClassGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 2, 1, 2)
)
alaDcbxDCPTrafficClassGroup.setObjects(
      *(("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPTCDCPName"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPTCMaximumBandwidth"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPTCMinimumBandwidth"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPTCPFCLinkDelay"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPTCPFCLinkDelayUserModified"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPTCPFCTrafficFlow"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPTCPriorityMap"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPTCTrafficScheduler"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPTCRecommendedBandwidth"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPTCRecommendedTrafficScheduler"))
)
if mibBuilder.loadTexts:
    alaDcbxDCPTrafficClassGroup.setStatus("current")

alaDcbxPortInstanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 2, 1, 3)
)
alaDcbxPortInstanceGroup.setObjects(
      *(("ALCATEL-IND1-DCBX-MIB", "alaDcbxPIDCBXAdmin"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPIDCBXOper"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPIAdminDCPId"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPIAdminDCPName"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPILocalModified"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPIPFCDefense"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPIPFCStatsClear"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPIStatus"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPIActionTaken"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPIRowStatus"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPIDCBXVersion"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPIDCBXOperVersion"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPIDCBXRemoteOperVersion"))
)
if mibBuilder.loadTexts:
    alaDcbxPortInstanceGroup.setStatus("current")

alaDcbxPortInstancePriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 2, 1, 4)
)
alaDcbxPortInstancePriorityGroup.setObjects(
      *(("ALCATEL-IND1-DCBX-MIB", "alaDcbxPIPrioTC"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPIPrioPFCPacketsReceived"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPIPrioPFCPacketsTransmitted"))
)
if mibBuilder.loadTexts:
    alaDcbxPortInstancePriorityGroup.setStatus("current")

alaDcbxPfcUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 2, 1, 5)
)
alaDcbxPfcUsageGroup.setObjects(
      *(("ALCATEL-IND1-DCBX-MIB", "alaDcbxPfcLLPrioritiesUsed"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPfcLLPrioritiesReserved"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPfcLLPrioritiesAvailable"))
)
if mibBuilder.loadTexts:
    alaDcbxPfcUsageGroup.setStatus("current")

alaDcbxPfcUsageNewGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 2, 1, 6)
)
alaDcbxPfcUsageNewGroup.setObjects(
      *(("ALCATEL-IND1-DCBX-MIB", "alaDcbxPfcUsagePrioritiesUsed"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPfcUsagePrioritiesReserved"),
        ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPfcUsagePrioritiesAvailable"))
)
if mibBuilder.loadTexts:
    alaDcbxPfcUsageNewGroup.setStatus("current")

alaXdot1dcbxAdminApplicationPriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 2, 1, 7)
)
alaXdot1dcbxAdminApplicationPriorityGroup.setObjects(
      *(("ALCATEL-IND1-DCBX-MIB", "alaXdot1dcbxAdminApplicationPriorityAEPriority"),
        ("ALCATEL-IND1-DCBX-MIB", "alaXdot1dcbxAdminApplicationPriorityAppRowStatus"))
)
if mibBuilder.loadTexts:
    alaXdot1dcbxAdminApplicationPriorityGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1DcbxMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1DcbxMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-DCBX-MIB",
    **{"DcbxTrafficFlow": DcbxTrafficFlow,
       "DcbxPriorityTCMap": DcbxPriorityTCMap,
       "DcbxStatus": DcbxStatus,
       "DcbxActionTaken": DcbxActionTaken,
       "DcbxTCsPresent": DcbxTCsPresent,
       "DcbxVersion": DcbxVersion,
       "RemoteDcbxVersion": RemoteDcbxVersion,
       "alcatelIND1DcbxMIB": alcatelIND1DcbxMIB,
       "alcatelIND1DcbxMIBObjects": alcatelIND1DcbxMIBObjects,
       "alaDcbxConfig": alaDcbxConfig,
       "alaDcbxDCProfileTable": alaDcbxDCProfileTable,
       "alaDcbxDCProfileEntry": alaDcbxDCProfileEntry,
       "alaDcbxDCPId": alaDcbxDCPId,
       "alaDcbxDCPName": alaDcbxDCPName,
       "alaDcbxDCPETSTrafficClassesSupported": alaDcbxDCPETSTrafficClassesSupported,
       "alaDcbxDCPPFCCap": alaDcbxDCPPFCCap,
       "alaDcbxDCPPriorityTCMap": alaDcbxDCPPriorityTCMap,
       "alaDcbxDCPTemplateDCPId": alaDcbxDCPTemplateDCPId,
       "alaDcbxDCPTemplateDCPName": alaDcbxDCPTemplateDCPName,
       "alaDcbxDCPTCsPresent": alaDcbxDCPTCsPresent,
       "alaDcbxDCP8023xPauseReady": alaDcbxDCP8023xPauseReady,
       "alaDcbxDCPRowStatus": alaDcbxDCPRowStatus,
       "alaDcbxDCPTrafficClassTable": alaDcbxDCPTrafficClassTable,
       "alaDcbxDCPTCEntry": alaDcbxDCPTCEntry,
       "alaDcbxDCPTCDCPId": alaDcbxDCPTCDCPId,
       "alaDcbxDCPTCTrafficClass": alaDcbxDCPTCTrafficClass,
       "alaDcbxDCPTCDCPName": alaDcbxDCPTCDCPName,
       "alaDcbxDCPTCMaximumBandwidth": alaDcbxDCPTCMaximumBandwidth,
       "alaDcbxDCPTCMinimumBandwidth": alaDcbxDCPTCMinimumBandwidth,
       "alaDcbxDCPTCPFCLinkDelay": alaDcbxDCPTCPFCLinkDelay,
       "alaDcbxDCPTCPFCLinkDelayUserModified": alaDcbxDCPTCPFCLinkDelayUserModified,
       "alaDcbxDCPTCPFCTrafficFlow": alaDcbxDCPTCPFCTrafficFlow,
       "alaDcbxDCPTCPriorityMap": alaDcbxDCPTCPriorityMap,
       "alaDcbxDCPTCTrafficScheduler": alaDcbxDCPTCTrafficScheduler,
       "alaDcbxDCPTCRecommendedBandwidth": alaDcbxDCPTCRecommendedBandwidth,
       "alaDcbxDCPTCRecommendedTrafficScheduler": alaDcbxDCPTCRecommendedTrafficScheduler,
       "alaDcbxPortInstanceTable": alaDcbxPortInstanceTable,
       "alaDcbxPortInstanceEntry": alaDcbxPortInstanceEntry,
       "alaDcbxPIIfIndex": alaDcbxPIIfIndex,
       "alaDcbxPIDCBXAdmin": alaDcbxPIDCBXAdmin,
       "alaDcbxPIDCBXOper": alaDcbxPIDCBXOper,
       "alaDcbxPIAdminDCPId": alaDcbxPIAdminDCPId,
       "alaDcbxPIAdminDCPName": alaDcbxPIAdminDCPName,
       "alaDcbxPILocalModified": alaDcbxPILocalModified,
       "alaDcbxPIPFCDefense": alaDcbxPIPFCDefense,
       "alaDcbxPIPFCStatsClear": alaDcbxPIPFCStatsClear,
       "alaDcbxPIStatus": alaDcbxPIStatus,
       "alaDcbxPIActionTaken": alaDcbxPIActionTaken,
       "alaDcbxPIRowStatus": alaDcbxPIRowStatus,
       "alaDcbxPIDCBXVersion": alaDcbxPIDCBXVersion,
       "alaDcbxPIDCBXOperVersion": alaDcbxPIDCBXOperVersion,
       "alaDcbxPIDCBXRemoteOperVersion": alaDcbxPIDCBXRemoteOperVersion,
       "alaDcbxPIPriorityTable": alaDcbxPIPriorityTable,
       "alaDcbxPIPrioEntry": alaDcbxPIPrioEntry,
       "alaDcbxPIPrioIfIndex": alaDcbxPIPrioIfIndex,
       "alaDcbxPIPrioPriority": alaDcbxPIPrioPriority,
       "alaDcbxPIPrioTC": alaDcbxPIPrioTC,
       "alaDcbxPIPrioPFCPacketsReceived": alaDcbxPIPrioPFCPacketsReceived,
       "alaDcbxPIPrioPFCPacketsTransmitted": alaDcbxPIPrioPFCPacketsTransmitted,
       "alaDcbxPfcLLPrioritiesUsed": alaDcbxPfcLLPrioritiesUsed,
       "alaDcbxPfcLLPrioritiesReserved": alaDcbxPfcLLPrioritiesReserved,
       "alaDcbxPfcLLPrioritiesAvailable": alaDcbxPfcLLPrioritiesAvailable,
       "alaDcbxPfcUsageTable": alaDcbxPfcUsageTable,
       "alaDcbxPfcUsageEntry": alaDcbxPfcUsageEntry,
       "alaDcbxPfcUsageChassisId": alaDcbxPfcUsageChassisId,
       "alaDcbxPfcUsagePrioritiesUsed": alaDcbxPfcUsagePrioritiesUsed,
       "alaDcbxPfcUsagePrioritiesReserved": alaDcbxPfcUsagePrioritiesReserved,
       "alaDcbxPfcUsagePrioritiesAvailable": alaDcbxPfcUsagePrioritiesAvailable,
       "alaXdot1dcbxAdminApplicationPriorityAppTable": alaXdot1dcbxAdminApplicationPriorityAppTable,
       "alaXdot1dcbxAdminApplicationPriorityAppEntry": alaXdot1dcbxAdminApplicationPriorityAppEntry,
       "alaXdot1dcbxAdminApplicationPriorityAEPriority": alaXdot1dcbxAdminApplicationPriorityAEPriority,
       "alaXdot1dcbxAdminApplicationPriorityAppRowStatus": alaXdot1dcbxAdminApplicationPriorityAppRowStatus,
       "alaDcbxConformance": alaDcbxConformance,
       "alcatelIND1DcbxMIBConformance": alcatelIND1DcbxMIBConformance,
       "alcatelIND1DcbxMIBGroups": alcatelIND1DcbxMIBGroups,
       "alaDcbxDCProfileGroup": alaDcbxDCProfileGroup,
       "alaDcbxDCPTrafficClassGroup": alaDcbxDCPTrafficClassGroup,
       "alaDcbxPortInstanceGroup": alaDcbxPortInstanceGroup,
       "alaDcbxPortInstancePriorityGroup": alaDcbxPortInstancePriorityGroup,
       "alaDcbxPfcUsageGroup": alaDcbxPfcUsageGroup,
       "alaDcbxPfcUsageNewGroup": alaDcbxPfcUsageNewGroup,
       "alaXdot1dcbxAdminApplicationPriorityGroup": alaXdot1dcbxAdminApplicationPriorityGroup,
       "alcatelIND1DcbxMIBCompliances": alcatelIND1DcbxMIBCompliances,
       "alcatelIND1DcbxMIBCompliance": alcatelIND1DcbxMIBCompliance}
)
