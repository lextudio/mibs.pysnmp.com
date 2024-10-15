# SNMP MIB module (ONEACCESS-ETHOAM-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ONEACCESS-ETHOAM-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:52 2024
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

(Dot1agCfmCcmInterval,
 Dot1agCfmConfigErrors,
 Dot1agCfmIdPermission,
 Dot1agCfmMDLevel,
 Dot1agCfmMDLevelOrNone,
 Dot1agCfmMepIdOrZero,
 Dot1agCfmMhfCreation,
 Dot1agCfmMpDirection,
 dot1agCfmConfigErrorList,
 dot1agCfmDefaultMd,
 dot1agCfmMa,
 dot1agCfmMaIndex,
 dot1agCfmMaMepListRowStatus,
 dot1agCfmMaNetRowStatus,
 dot1agCfmMdIndex,
 dot1agCfmMdRowStatus,
 dot1agCfmMepEntry,
 dot1agCfmMepIdentifier,
 dot1agCfmMepLbrBadMsdu,
 dot1agCfmMepRowStatus,
 dot1agCfmStack,
 dot1agCfmVlan) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmCcmInterval",
    "Dot1agCfmConfigErrors",
    "Dot1agCfmIdPermission",
    "Dot1agCfmMDLevel",
    "Dot1agCfmMDLevelOrNone",
    "Dot1agCfmMepIdOrZero",
    "Dot1agCfmMhfCreation",
    "Dot1agCfmMpDirection",
    "dot1agCfmConfigErrorList",
    "dot1agCfmDefaultMd",
    "dot1agCfmMa",
    "dot1agCfmMaIndex",
    "dot1agCfmMaMepListRowStatus",
    "dot1agCfmMaNetRowStatus",
    "dot1agCfmMdIndex",
    "dot1agCfmMdRowStatus",
    "dot1agCfmMepEntry",
    "dot1agCfmMepIdentifier",
    "dot1agCfmMepLbrBadMsdu",
    "dot1agCfmMepRowStatus",
    "dot1agCfmStack",
    "dot1agCfmVlan")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(oacExpIMEthernet,
 oacMIBModules) = mibBuilder.importSymbols(
    "ONEACCESS-GLOBAL-REG",
    "oacExpIMEthernet",
    "oacMIBModules")

(VlanIdOrNone,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIdOrNone")

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

oacEthOamExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 100, 689)
)
oacEthOamExtMib.setRevisions(
        ("2011-07-29 00:00",
         "2011-06-15 00:00",
         "2011-01-05 00:01",
         "2010-08-12 00:01")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EthOamExtMipMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode8021ag", 2),
          ("modey1731", 1))
    )



class EthOamExtMepMode(Integer32, TextualConvention):
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
        *(("mode8021ag", 2),
          ("modehybrid", 3),
          ("modey1731", 1))
    )



class EthOamEfdState(Integer32, TextualConvention):
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
        *(("efdDisabled", 1),
          ("efdIdle", 2),
          ("efdTriggered", 3))
    )



# MIB Managed Objects in the order of their OIDs

_OacEthOamExtMIBObjects_ObjectIdentity = ObjectIdentity
oacEthOamExtMIBObjects = _OacEthOamExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2)
)
_OacEthOamExtIfObjects_ObjectIdentity = ObjectIdentity
oacEthOamExtIfObjects = _OacEthOamExtIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1)
)
_OacEthOamExtMipTable_Object = MibTable
oacEthOamExtMipTable = _OacEthOamExtMipTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 1)
)
if mibBuilder.loadTexts:
    oacEthOamExtMipTable.setStatus("current")
_OacEthOamExtMipEntry_Object = MibTableRow
oacEthOamExtMipEntry = _OacEthOamExtMipEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 1, 1)
)
oacEthOamExtMipEntry.setIndexNames(
    (0, "ONEACCESS-ETHOAM-EXT-MIB", "oacEthOamMipIfIndex"),
    (0, "ONEACCESS-ETHOAM-EXT-MIB", "oacEthOamMipMegLevel"),
    (0, "ONEACCESS-ETHOAM-EXT-MIB", "oacEthOamMipVlanIndex"),
)
if mibBuilder.loadTexts:
    oacEthOamExtMipEntry.setStatus("current")
_OacEthOamMipIfIndex_Type = InterfaceIndex
_OacEthOamMipIfIndex_Object = MibTableColumn
oacEthOamMipIfIndex = _OacEthOamMipIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 1, 1, 1),
    _OacEthOamMipIfIndex_Type()
)
oacEthOamMipIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacEthOamMipIfIndex.setStatus("current")
_OacEthOamMipMegLevel_Type = Unsigned32
_OacEthOamMipMegLevel_Object = MibTableColumn
oacEthOamMipMegLevel = _OacEthOamMipMegLevel_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 1, 1, 2),
    _OacEthOamMipMegLevel_Type()
)
oacEthOamMipMegLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacEthOamMipMegLevel.setStatus("current")
_OacEthOamMipVlanIndex_Type = VlanIdOrNone
_OacEthOamMipVlanIndex_Object = MibTableColumn
oacEthOamMipVlanIndex = _OacEthOamMipVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 1, 1, 3),
    _OacEthOamMipVlanIndex_Type()
)
oacEthOamMipVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacEthOamMipVlanIndex.setStatus("current")


class _OacEthOamMipMode_Type(EthOamExtMipMode):
    """Custom type oacEthOamMipMode based on EthOamExtMipMode"""


_OacEthOamMipMode_Object = MibTableColumn
oacEthOamMipMode = _OacEthOamMipMode_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 1, 1, 4),
    _OacEthOamMipMode_Type()
)
oacEthOamMipMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacEthOamMipMode.setStatus("current")
_OacEthOamMipRowStatus_Type = RowStatus
_OacEthOamMipRowStatus_Object = MibTableColumn
oacEthOamMipRowStatus = _OacEthOamMipRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 1, 1, 5),
    _OacEthOamMipRowStatus_Type()
)
oacEthOamMipRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacEthOamMipRowStatus.setStatus("current")
_OacEthOamExtMepTable_Object = MibTable
oacEthOamExtMepTable = _OacEthOamExtMepTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2)
)
if mibBuilder.loadTexts:
    oacEthOamExtMepTable.setStatus("current")
_OacEthOamExtMepEntry_Object = MibTableRow
oacEthOamExtMepEntry = _OacEthOamExtMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    oacEthOamExtMepEntry.setStatus("current")


class _OacEthOamMepMode_Type(EthOamExtMepMode):
    """Custom type oacEthOamMepMode based on EthOamExtMepMode"""


_OacEthOamMepMode_Object = MibTableColumn
oacEthOamMepMode = _OacEthOamMepMode_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 1),
    _OacEthOamMepMode_Type()
)
oacEthOamMepMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacEthOamMepMode.setStatus("current")
_OacEthOamMepLossDestMacAddress_Type = MacAddress
_OacEthOamMepLossDestMacAddress_Object = MibTableColumn
oacEthOamMepLossDestMacAddress = _OacEthOamMepLossDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 10),
    _OacEthOamMepLossDestMacAddress_Type()
)
oacEthOamMepLossDestMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacEthOamMepLossDestMacAddress.setStatus("current")
_OacEthOamMepLossDestMepId_Type = Dot1agCfmMepIdOrZero
_OacEthOamMepLossDestMepId_Object = MibTableColumn
oacEthOamMepLossDestMepId = _OacEthOamMepLossDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 11),
    _OacEthOamMepLossDestMepId_Type()
)
oacEthOamMepLossDestMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacEthOamMepLossDestMepId.setStatus("current")
_OacEthOamMepLossDestIsMepId_Type = TruthValue
_OacEthOamMepLossDestIsMepId_Object = MibTableColumn
oacEthOamMepLossDestIsMepId = _OacEthOamMepLossDestIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 12),
    _OacEthOamMepLossDestIsMepId_Type()
)
oacEthOamMepLossDestIsMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacEthOamMepLossDestIsMepId.setStatus("current")
_OacEthOamMepLossVlanPriority_Type = Unsigned32
_OacEthOamMepLossVlanPriority_Object = MibTableColumn
oacEthOamMepLossVlanPriority = _OacEthOamMepLossVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 13),
    _OacEthOamMepLossVlanPriority_Type()
)
oacEthOamMepLossVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacEthOamMepLossVlanPriority.setStatus("current")


class _OacEthOamMepLossInterval_Type(Dot1agCfmCcmInterval):
    """Custom type oacEthOamMepLossInterval based on Dot1agCfmCcmInterval"""


_OacEthOamMepLossInterval_Object = MibTableColumn
oacEthOamMepLossInterval = _OacEthOamMepLossInterval_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 14),
    _OacEthOamMepLossInterval_Type()
)
oacEthOamMepLossInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacEthOamMepLossInterval.setStatus("current")


class _OacEthOamMepLossStatus_Type(TruthValue):
    """Custom type oacEthOamMepLossStatus based on TruthValue"""


_OacEthOamMepLossStatus_Object = MibTableColumn
oacEthOamMepLossStatus = _OacEthOamMepLossStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 15),
    _OacEthOamMepLossStatus_Type()
)
oacEthOamMepLossStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacEthOamMepLossStatus.setStatus("current")
_OacEthOamMepLossMessagesStart_Type = TruthValue
_OacEthOamMepLossMessagesStart_Object = MibTableColumn
oacEthOamMepLossMessagesStart = _OacEthOamMepLossMessagesStart_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 16),
    _OacEthOamMepLossMessagesStart_Type()
)
oacEthOamMepLossMessagesStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacEthOamMepLossMessagesStart.setStatus("current")
_OacEthOamMepLossResultOK_Type = TruthValue
_OacEthOamMepLossResultOK_Object = MibTableColumn
oacEthOamMepLossResultOK = _OacEthOamMepLossResultOK_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 17),
    _OacEthOamMepLossResultOK_Type()
)
oacEthOamMepLossResultOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacEthOamMepLossResultOK.setStatus("current")
_OacEthOamMepLossNbrOfTxFrames_Type = Counter32
_OacEthOamMepLossNbrOfTxFrames_Object = MibTableColumn
oacEthOamMepLossNbrOfTxFrames = _OacEthOamMepLossNbrOfTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 18),
    _OacEthOamMepLossNbrOfTxFrames_Type()
)
oacEthOamMepLossNbrOfTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacEthOamMepLossNbrOfTxFrames.setStatus("current")
_OacEthOamMepLossNbrOfRxFrames_Type = Counter32
_OacEthOamMepLossNbrOfRxFrames_Object = MibTableColumn
oacEthOamMepLossNbrOfRxFrames = _OacEthOamMepLossNbrOfRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 19),
    _OacEthOamMepLossNbrOfRxFrames_Type()
)
oacEthOamMepLossNbrOfRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacEthOamMepLossNbrOfRxFrames.setStatus("current")
_OacEthOamMepLossReplyLoss_Type = Counter32
_OacEthOamMepLossReplyLoss_Object = MibTableColumn
oacEthOamMepLossReplyLoss = _OacEthOamMepLossReplyLoss_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 20),
    _OacEthOamMepLossReplyLoss_Type()
)
oacEthOamMepLossReplyLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacEthOamMepLossReplyLoss.setStatus("current")
_OacEthOamMepLossNearEndDrops_Type = Counter32
_OacEthOamMepLossNearEndDrops_Object = MibTableColumn
oacEthOamMepLossNearEndDrops = _OacEthOamMepLossNearEndDrops_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 21),
    _OacEthOamMepLossNearEndDrops_Type()
)
oacEthOamMepLossNearEndDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacEthOamMepLossNearEndDrops.setStatus("current")
_OacEthOamMepLossFarEndDrops_Type = Counter32
_OacEthOamMepLossFarEndDrops_Object = MibTableColumn
oacEthOamMepLossFarEndDrops = _OacEthOamMepLossFarEndDrops_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 22),
    _OacEthOamMepLossFarEndDrops_Type()
)
oacEthOamMepLossFarEndDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacEthOamMepLossFarEndDrops.setStatus("current")
_OacEthOamMepDelayDestMacAddress_Type = MacAddress
_OacEthOamMepDelayDestMacAddress_Object = MibTableColumn
oacEthOamMepDelayDestMacAddress = _OacEthOamMepDelayDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 30),
    _OacEthOamMepDelayDestMacAddress_Type()
)
oacEthOamMepDelayDestMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacEthOamMepDelayDestMacAddress.setStatus("current")
_OacEthOamMepDelayDestMepId_Type = Dot1agCfmMepIdOrZero
_OacEthOamMepDelayDestMepId_Object = MibTableColumn
oacEthOamMepDelayDestMepId = _OacEthOamMepDelayDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 31),
    _OacEthOamMepDelayDestMepId_Type()
)
oacEthOamMepDelayDestMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacEthOamMepDelayDestMepId.setStatus("current")
_OacEthOamMepDelayDestIsMepId_Type = TruthValue
_OacEthOamMepDelayDestIsMepId_Object = MibTableColumn
oacEthOamMepDelayDestIsMepId = _OacEthOamMepDelayDestIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 32),
    _OacEthOamMepDelayDestIsMepId_Type()
)
oacEthOamMepDelayDestIsMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacEthOamMepDelayDestIsMepId.setStatus("current")
_OacEthOamMepDelayVlanPriority_Type = Unsigned32
_OacEthOamMepDelayVlanPriority_Object = MibTableColumn
oacEthOamMepDelayVlanPriority = _OacEthOamMepDelayVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 33),
    _OacEthOamMepDelayVlanPriority_Type()
)
oacEthOamMepDelayVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacEthOamMepDelayVlanPriority.setStatus("current")


class _OacEthOamMepDelayInterval_Type(Dot1agCfmCcmInterval):
    """Custom type oacEthOamMepDelayInterval based on Dot1agCfmCcmInterval"""


_OacEthOamMepDelayInterval_Object = MibTableColumn
oacEthOamMepDelayInterval = _OacEthOamMepDelayInterval_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 34),
    _OacEthOamMepDelayInterval_Type()
)
oacEthOamMepDelayInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacEthOamMepDelayInterval.setStatus("current")


class _OacEthOamMepDelayStatus_Type(TruthValue):
    """Custom type oacEthOamMepDelayStatus based on TruthValue"""


_OacEthOamMepDelayStatus_Object = MibTableColumn
oacEthOamMepDelayStatus = _OacEthOamMepDelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 35),
    _OacEthOamMepDelayStatus_Type()
)
oacEthOamMepDelayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacEthOamMepDelayStatus.setStatus("current")
_OacEthOamMepDelayTimeOut_Type = Unsigned32
_OacEthOamMepDelayTimeOut_Object = MibTableColumn
oacEthOamMepDelayTimeOut = _OacEthOamMepDelayTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 36),
    _OacEthOamMepDelayTimeOut_Type()
)
oacEthOamMepDelayTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacEthOamMepDelayTimeOut.setStatus("current")
_OacEthOamMepDelayMessagesStart_Type = TruthValue
_OacEthOamMepDelayMessagesStart_Object = MibTableColumn
oacEthOamMepDelayMessagesStart = _OacEthOamMepDelayMessagesStart_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 37),
    _OacEthOamMepDelayMessagesStart_Type()
)
oacEthOamMepDelayMessagesStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacEthOamMepDelayMessagesStart.setStatus("current")
_OacEthOamMepDelayResultOK_Type = TruthValue
_OacEthOamMepDelayResultOK_Object = MibTableColumn
oacEthOamMepDelayResultOK = _OacEthOamMepDelayResultOK_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 38),
    _OacEthOamMepDelayResultOK_Type()
)
oacEthOamMepDelayResultOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacEthOamMepDelayResultOK.setStatus("current")
_OacEthOamMepDelayNbrOfTxFrames_Type = Counter32
_OacEthOamMepDelayNbrOfTxFrames_Object = MibTableColumn
oacEthOamMepDelayNbrOfTxFrames = _OacEthOamMepDelayNbrOfTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 39),
    _OacEthOamMepDelayNbrOfTxFrames_Type()
)
oacEthOamMepDelayNbrOfTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacEthOamMepDelayNbrOfTxFrames.setStatus("current")
_OacEthOamMepDelayNbrOfRxFrames_Type = Counter32
_OacEthOamMepDelayNbrOfRxFrames_Object = MibTableColumn
oacEthOamMepDelayNbrOfRxFrames = _OacEthOamMepDelayNbrOfRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 40),
    _OacEthOamMepDelayNbrOfRxFrames_Type()
)
oacEthOamMepDelayNbrOfRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacEthOamMepDelayNbrOfRxFrames.setStatus("current")
_OacEthOamMepDelayLoss_Type = Counter32
_OacEthOamMepDelayLoss_Object = MibTableColumn
oacEthOamMepDelayLoss = _OacEthOamMepDelayLoss_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 41),
    _OacEthOamMepDelayLoss_Type()
)
oacEthOamMepDelayLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacEthOamMepDelayLoss.setStatus("current")
_OacEthOamMepDelayMin_Type = Unsigned32
_OacEthOamMepDelayMin_Object = MibTableColumn
oacEthOamMepDelayMin = _OacEthOamMepDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 42),
    _OacEthOamMepDelayMin_Type()
)
oacEthOamMepDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacEthOamMepDelayMin.setStatus("current")
_OacEthOamMepDelayMax_Type = Unsigned32
_OacEthOamMepDelayMax_Object = MibTableColumn
oacEthOamMepDelayMax = _OacEthOamMepDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 43),
    _OacEthOamMepDelayMax_Type()
)
oacEthOamMepDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacEthOamMepDelayMax.setStatus("current")
_OacEthOamMepDelayAvrg_Type = Unsigned32
_OacEthOamMepDelayAvrg_Object = MibTableColumn
oacEthOamMepDelayAvrg = _OacEthOamMepDelayAvrg_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 44),
    _OacEthOamMepDelayAvrg_Type()
)
oacEthOamMepDelayAvrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacEthOamMepDelayAvrg.setStatus("current")
_OacEthOamMepDelayJitterNegMax_Type = Unsigned32
_OacEthOamMepDelayJitterNegMax_Object = MibTableColumn
oacEthOamMepDelayJitterNegMax = _OacEthOamMepDelayJitterNegMax_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 45),
    _OacEthOamMepDelayJitterNegMax_Type()
)
oacEthOamMepDelayJitterNegMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacEthOamMepDelayJitterNegMax.setStatus("current")
_OacEthOamMepDelayJitterAvrgMax_Type = Unsigned32
_OacEthOamMepDelayJitterAvrgMax_Object = MibTableColumn
oacEthOamMepDelayJitterAvrgMax = _OacEthOamMepDelayJitterAvrgMax_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 46),
    _OacEthOamMepDelayJitterAvrgMax_Type()
)
oacEthOamMepDelayJitterAvrgMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacEthOamMepDelayJitterAvrgMax.setStatus("current")
_OacEthOamMepDelayJitterPosMax_Type = Unsigned32
_OacEthOamMepDelayJitterPosMax_Object = MibTableColumn
oacEthOamMepDelayJitterPosMax = _OacEthOamMepDelayJitterPosMax_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 47),
    _OacEthOamMepDelayJitterPosMax_Type()
)
oacEthOamMepDelayJitterPosMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacEthOamMepDelayJitterPosMax.setStatus("current")
_OacEthOamMepRdiTxEnable_Type = TruthValue
_OacEthOamMepRdiTxEnable_Object = MibTableColumn
oacEthOamMepRdiTxEnable = _OacEthOamMepRdiTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 60),
    _OacEthOamMepRdiTxEnable_Type()
)
oacEthOamMepRdiTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacEthOamMepRdiTxEnable.setStatus("current")
_OacEthOamMepMcastLbmStatus_Type = TruthValue
_OacEthOamMepMcastLbmStatus_Object = MibTableColumn
oacEthOamMepMcastLbmStatus = _OacEthOamMepMcastLbmStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 70),
    _OacEthOamMepMcastLbmStatus_Type()
)
oacEthOamMepMcastLbmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacEthOamMepMcastLbmStatus.setStatus("current")
_OacEthOamMepMcastLbmResult_Type = TruthValue
_OacEthOamMepMcastLbmResult_Object = MibTableColumn
oacEthOamMepMcastLbmResult = _OacEthOamMepMcastLbmResult_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 71),
    _OacEthOamMepMcastLbmResult_Type()
)
oacEthOamMepMcastLbmResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacEthOamMepMcastLbmResult.setStatus("current")
_OacEthOamMepMcastLbmSeqNumber_Type = Unsigned32
_OacEthOamMepMcastLbmSeqNumber_Object = MibTableColumn
oacEthOamMepMcastLbmSeqNumber = _OacEthOamMepMcastLbmSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 72),
    _OacEthOamMepMcastLbmSeqNumber_Type()
)
oacEthOamMepMcastLbmSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacEthOamMepMcastLbmSeqNumber.setStatus("current")
_OacEthOamMepMcastLbmDataTlv_Type = OctetString
_OacEthOamMepMcastLbmDataTlv_Object = MibTableColumn
oacEthOamMepMcastLbmDataTlv = _OacEthOamMepMcastLbmDataTlv_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 73),
    _OacEthOamMepMcastLbmDataTlv_Type()
)
oacEthOamMepMcastLbmDataTlv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacEthOamMepMcastLbmDataTlv.setStatus("current")
_OacEthOamMepAisInterval_Type = Unsigned32
_OacEthOamMepAisInterval_Object = MibTableColumn
oacEthOamMepAisInterval = _OacEthOamMepAisInterval_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 80),
    _OacEthOamMepAisInterval_Type()
)
oacEthOamMepAisInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacEthOamMepAisInterval.setStatus("current")
_OacEthOamMepAisVlanPriority_Type = Unsigned32
_OacEthOamMepAisVlanPriority_Object = MibTableColumn
oacEthOamMepAisVlanPriority = _OacEthOamMepAisVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 81),
    _OacEthOamMepAisVlanPriority_Type()
)
oacEthOamMepAisVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacEthOamMepAisVlanPriority.setStatus("current")
_OacEthOamMepAisTxEnable_Type = TruthValue
_OacEthOamMepAisTxEnable_Object = MibTableColumn
oacEthOamMepAisTxEnable = _OacEthOamMepAisTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 82),
    _OacEthOamMepAisTxEnable_Type()
)
oacEthOamMepAisTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacEthOamMepAisTxEnable.setStatus("current")
_OacEthOamMepAisClientMegLevel_Type = Unsigned32
_OacEthOamMepAisClientMegLevel_Object = MibTableColumn
oacEthOamMepAisClientMegLevel = _OacEthOamMepAisClientMegLevel_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 83),
    _OacEthOamMepAisClientMegLevel_Type()
)
oacEthOamMepAisClientMegLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacEthOamMepAisClientMegLevel.setStatus("current")
_OacEthOamMepEfdEnable_Type = TruthValue
_OacEthOamMepEfdEnable_Object = MibTableColumn
oacEthOamMepEfdEnable = _OacEthOamMepEfdEnable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 90),
    _OacEthOamMepEfdEnable_Type()
)
oacEthOamMepEfdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacEthOamMepEfdEnable.setStatus("current")
_OacEthOamMepEfdState_Type = EthOamEfdState
_OacEthOamMepEfdState_Object = MibTableColumn
oacEthOamMepEfdState = _OacEthOamMepEfdState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 2, 1, 91),
    _OacEthOamMepEfdState_Type()
)
oacEthOamMepEfdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacEthOamMepEfdState.setStatus("current")
_OacEthOamExtGlobal_ObjectIdentity = ObjectIdentity
oacEthOamExtGlobal = _OacEthOamExtGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 3)
)
_OacEthOamExtEnable_Type = TruthValue
_OacEthOamExtEnable_Object = MibScalar
oacEthOamExtEnable = _OacEthOamExtEnable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 3, 1),
    _OacEthOamExtEnable_Type()
)
oacEthOamExtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacEthOamExtEnable.setStatus("current")
_OacEthOamExtLbrTable_Object = MibTable
oacEthOamExtLbrTable = _OacEthOamExtLbrTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 4)
)
if mibBuilder.loadTexts:
    oacEthOamExtLbrTable.setStatus("current")
_OacEthOamExtLbrEntry_Object = MibTableRow
oacEthOamExtLbrEntry = _OacEthOamExtLbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 4, 1)
)
oacEthOamExtLbrEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "ONEACCESS-ETHOAM-EXT-MIB", "oacEthOamLbrReceiveOrder"),
)
if mibBuilder.loadTexts:
    oacEthOamExtLbrEntry.setStatus("current")


class _OacEthOamLbrReceiveOrder_Type(Unsigned32):
    """Custom type oacEthOamLbrReceiveOrder based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_OacEthOamLbrReceiveOrder_Type.__name__ = "Unsigned32"
_OacEthOamLbrReceiveOrder_Object = MibTableColumn
oacEthOamLbrReceiveOrder = _OacEthOamLbrReceiveOrder_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 4, 1, 1),
    _OacEthOamLbrReceiveOrder_Type()
)
oacEthOamLbrReceiveOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacEthOamLbrReceiveOrder.setStatus("current")
_OacEthOamLbrPeerMacAddress_Type = MacAddress
_OacEthOamLbrPeerMacAddress_Object = MibTableColumn
oacEthOamLbrPeerMacAddress = _OacEthOamLbrPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 4, 1, 2),
    _OacEthOamLbrPeerMacAddress_Type()
)
oacEthOamLbrPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacEthOamLbrPeerMacAddress.setStatus("current")
_OacEthOamLbrMepId_Type = Dot1agCfmMepIdOrZero
_OacEthOamLbrMepId_Object = MibTableColumn
oacEthOamLbrMepId = _OacEthOamLbrMepId_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 4, 1, 3),
    _OacEthOamLbrMepId_Type()
)
oacEthOamLbrMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacEthOamLbrMepId.setStatus("current")
_OacEthOamLbrNotRespTable_Object = MibTable
oacEthOamLbrNotRespTable = _OacEthOamLbrNotRespTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 5)
)
if mibBuilder.loadTexts:
    oacEthOamLbrNotRespTable.setStatus("current")
_OacEthOamLbrNotRespEntry_Object = MibTableRow
oacEthOamLbrNotRespEntry = _OacEthOamLbrNotRespEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 5, 1)
)
oacEthOamLbrNotRespEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "ONEACCESS-ETHOAM-EXT-MIB", "oacEthOamLbrNotRespMepId"),
)
if mibBuilder.loadTexts:
    oacEthOamLbrNotRespEntry.setStatus("current")
_OacEthOamLbrNotRespMepId_Type = Dot1agCfmMepIdOrZero
_OacEthOamLbrNotRespMepId_Object = MibTableColumn
oacEthOamLbrNotRespMepId = _OacEthOamLbrNotRespMepId_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 5, 1, 1),
    _OacEthOamLbrNotRespMepId_Type()
)
oacEthOamLbrNotRespMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacEthOamLbrNotRespMepId.setStatus("current")
_OacEthOamLbrNotRespPeerMacAddress_Type = MacAddress
_OacEthOamLbrNotRespPeerMacAddress_Object = MibTableColumn
oacEthOamLbrNotRespPeerMacAddress = _OacEthOamLbrNotRespPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10, 2, 1, 5, 1, 2),
    _OacEthOamLbrNotRespPeerMacAddress_Type()
)
oacEthOamLbrNotRespPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacEthOamLbrNotRespPeerMacAddress.setStatus("current")
dot1agCfmMepEntry.registerAugmentions(
    ("ONEACCESS-ETHOAM-EXT-MIB",
     "oacEthOamExtMepEntry")
)
oacEthOamExtMepEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONEACCESS-ETHOAM-EXT-MIB",
    **{"EthOamExtMipMode": EthOamExtMipMode,
       "EthOamExtMepMode": EthOamExtMepMode,
       "EthOamEfdState": EthOamEfdState,
       "oacEthOamExtMib": oacEthOamExtMib,
       "oacEthOamExtMIBObjects": oacEthOamExtMIBObjects,
       "oacEthOamExtIfObjects": oacEthOamExtIfObjects,
       "oacEthOamExtMipTable": oacEthOamExtMipTable,
       "oacEthOamExtMipEntry": oacEthOamExtMipEntry,
       "oacEthOamMipIfIndex": oacEthOamMipIfIndex,
       "oacEthOamMipMegLevel": oacEthOamMipMegLevel,
       "oacEthOamMipVlanIndex": oacEthOamMipVlanIndex,
       "oacEthOamMipMode": oacEthOamMipMode,
       "oacEthOamMipRowStatus": oacEthOamMipRowStatus,
       "oacEthOamExtMepTable": oacEthOamExtMepTable,
       "oacEthOamExtMepEntry": oacEthOamExtMepEntry,
       "oacEthOamMepMode": oacEthOamMepMode,
       "oacEthOamMepLossDestMacAddress": oacEthOamMepLossDestMacAddress,
       "oacEthOamMepLossDestMepId": oacEthOamMepLossDestMepId,
       "oacEthOamMepLossDestIsMepId": oacEthOamMepLossDestIsMepId,
       "oacEthOamMepLossVlanPriority": oacEthOamMepLossVlanPriority,
       "oacEthOamMepLossInterval": oacEthOamMepLossInterval,
       "oacEthOamMepLossStatus": oacEthOamMepLossStatus,
       "oacEthOamMepLossMessagesStart": oacEthOamMepLossMessagesStart,
       "oacEthOamMepLossResultOK": oacEthOamMepLossResultOK,
       "oacEthOamMepLossNbrOfTxFrames": oacEthOamMepLossNbrOfTxFrames,
       "oacEthOamMepLossNbrOfRxFrames": oacEthOamMepLossNbrOfRxFrames,
       "oacEthOamMepLossReplyLoss": oacEthOamMepLossReplyLoss,
       "oacEthOamMepLossNearEndDrops": oacEthOamMepLossNearEndDrops,
       "oacEthOamMepLossFarEndDrops": oacEthOamMepLossFarEndDrops,
       "oacEthOamMepDelayDestMacAddress": oacEthOamMepDelayDestMacAddress,
       "oacEthOamMepDelayDestMepId": oacEthOamMepDelayDestMepId,
       "oacEthOamMepDelayDestIsMepId": oacEthOamMepDelayDestIsMepId,
       "oacEthOamMepDelayVlanPriority": oacEthOamMepDelayVlanPriority,
       "oacEthOamMepDelayInterval": oacEthOamMepDelayInterval,
       "oacEthOamMepDelayStatus": oacEthOamMepDelayStatus,
       "oacEthOamMepDelayTimeOut": oacEthOamMepDelayTimeOut,
       "oacEthOamMepDelayMessagesStart": oacEthOamMepDelayMessagesStart,
       "oacEthOamMepDelayResultOK": oacEthOamMepDelayResultOK,
       "oacEthOamMepDelayNbrOfTxFrames": oacEthOamMepDelayNbrOfTxFrames,
       "oacEthOamMepDelayNbrOfRxFrames": oacEthOamMepDelayNbrOfRxFrames,
       "oacEthOamMepDelayLoss": oacEthOamMepDelayLoss,
       "oacEthOamMepDelayMin": oacEthOamMepDelayMin,
       "oacEthOamMepDelayMax": oacEthOamMepDelayMax,
       "oacEthOamMepDelayAvrg": oacEthOamMepDelayAvrg,
       "oacEthOamMepDelayJitterNegMax": oacEthOamMepDelayJitterNegMax,
       "oacEthOamMepDelayJitterAvrgMax": oacEthOamMepDelayJitterAvrgMax,
       "oacEthOamMepDelayJitterPosMax": oacEthOamMepDelayJitterPosMax,
       "oacEthOamMepRdiTxEnable": oacEthOamMepRdiTxEnable,
       "oacEthOamMepMcastLbmStatus": oacEthOamMepMcastLbmStatus,
       "oacEthOamMepMcastLbmResult": oacEthOamMepMcastLbmResult,
       "oacEthOamMepMcastLbmSeqNumber": oacEthOamMepMcastLbmSeqNumber,
       "oacEthOamMepMcastLbmDataTlv": oacEthOamMepMcastLbmDataTlv,
       "oacEthOamMepAisInterval": oacEthOamMepAisInterval,
       "oacEthOamMepAisVlanPriority": oacEthOamMepAisVlanPriority,
       "oacEthOamMepAisTxEnable": oacEthOamMepAisTxEnable,
       "oacEthOamMepAisClientMegLevel": oacEthOamMepAisClientMegLevel,
       "oacEthOamMepEfdEnable": oacEthOamMepEfdEnable,
       "oacEthOamMepEfdState": oacEthOamMepEfdState,
       "oacEthOamExtGlobal": oacEthOamExtGlobal,
       "oacEthOamExtEnable": oacEthOamExtEnable,
       "oacEthOamExtLbrTable": oacEthOamExtLbrTable,
       "oacEthOamExtLbrEntry": oacEthOamExtLbrEntry,
       "oacEthOamLbrReceiveOrder": oacEthOamLbrReceiveOrder,
       "oacEthOamLbrPeerMacAddress": oacEthOamLbrPeerMacAddress,
       "oacEthOamLbrMepId": oacEthOamLbrMepId,
       "oacEthOamLbrNotRespTable": oacEthOamLbrNotRespTable,
       "oacEthOamLbrNotRespEntry": oacEthOamLbrNotRespEntry,
       "oacEthOamLbrNotRespMepId": oacEthOamLbrNotRespMepId,
       "oacEthOamLbrNotRespPeerMacAddress": oacEthOamLbrNotRespPeerMacAddress}
)
