# SNMP MIB module (DNOS-DCBX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DNOS-DCBX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:31:52 2024
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

(dnOS,) = mibBuilder.importSymbols(
    "DELL-REF-MIB",
    "dnOS")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fastPathDCBX = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58)
)
fastPathDCBX.setRevisions(
        ("2011-04-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DcbxPortRole(Integer32, TextualConvention):
    status = "current"
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
        *(("autodown", 3),
          ("autoup", 2),
          ("configSource", 4),
          ("manual", 1))
    )



class DcbxVersion(Integer32, TextualConvention):
    status = "current"
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
        *(("auto", 1),
          ("cee", 4),
          ("cin", 3),
          ("ieee", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AgentDcbxGroup_ObjectIdentity = ObjectIdentity
agentDcbxGroup = _AgentDcbxGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1)
)
_AgentDcbxTable_Object = MibTable
agentDcbxTable = _AgentDcbxTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 1)
)
if mibBuilder.loadTexts:
    agentDcbxTable.setStatus("current")
_AgentDcbxEntry_Object = MibTableRow
agentDcbxEntry = _AgentDcbxEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 1, 1)
)
agentDcbxEntry.setIndexNames(
    (0, "DNOS-DCBX-MIB", "agentDcbxIntfIndex"),
)
if mibBuilder.loadTexts:
    agentDcbxEntry.setStatus("current")
_AgentDcbxIntfIndex_Type = InterfaceIndex
_AgentDcbxIntfIndex_Object = MibTableColumn
agentDcbxIntfIndex = _AgentDcbxIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 1, 1, 1),
    _AgentDcbxIntfIndex_Type()
)
agentDcbxIntfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentDcbxIntfIndex.setStatus("current")


class _AgentDcbxAutoCfgPortRole_Type(DcbxPortRole):
    """Custom type agentDcbxAutoCfgPortRole based on DcbxPortRole"""
    defaultValue = 1


_AgentDcbxAutoCfgPortRole_Object = MibTableColumn
agentDcbxAutoCfgPortRole = _AgentDcbxAutoCfgPortRole_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 1, 1, 2),
    _AgentDcbxAutoCfgPortRole_Type()
)
agentDcbxAutoCfgPortRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDcbxAutoCfgPortRole.setStatus("current")


class _AgentDcbxVersion_Type(DcbxVersion):
    """Custom type agentDcbxVersion based on DcbxVersion"""
    defaultValue = 1


_AgentDcbxVersion_Object = MibTableColumn
agentDcbxVersion = _AgentDcbxVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 1, 1, 3),
    _AgentDcbxVersion_Type()
)
agentDcbxVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDcbxVersion.setStatus("deprecated")


class _AgentDcbxSupportedTLVs_Type(Bits):
    """Custom type agentDcbxSupportedTLVs based on Bits"""
    namedValues = NamedValues(
        *(("applicationPriority", 3),
          ("etsConfig", 1),
          ("etsRecom", 2),
          ("pfc", 0))
    )

_AgentDcbxSupportedTLVs_Type.__name__ = "Bits"
_AgentDcbxSupportedTLVs_Object = MibTableColumn
agentDcbxSupportedTLVs = _AgentDcbxSupportedTLVs_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 1, 1, 4),
    _AgentDcbxSupportedTLVs_Type()
)
agentDcbxSupportedTLVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDcbxSupportedTLVs.setStatus("current")


class _AgentDcbxConfigTLVsTxEnable_Type(Bits):
    """Custom type agentDcbxConfigTLVsTxEnable based on Bits"""
    namedValues = NamedValues(
        *(("applicationPriority", 3),
          ("etsConfig", 1),
          ("etsRecom", 2),
          ("pfc", 0))
    )

_AgentDcbxConfigTLVsTxEnable_Type.__name__ = "Bits"
_AgentDcbxConfigTLVsTxEnable_Object = MibTableColumn
agentDcbxConfigTLVsTxEnable = _AgentDcbxConfigTLVsTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 1, 1, 5),
    _AgentDcbxConfigTLVsTxEnable_Type()
)
agentDcbxConfigTLVsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDcbxConfigTLVsTxEnable.setStatus("current")
_AgentDcbxStatusTable_Object = MibTable
agentDcbxStatusTable = _AgentDcbxStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2)
)
if mibBuilder.loadTexts:
    agentDcbxStatusTable.setStatus("current")
_AgentDcbxStatusEntry_Object = MibTableRow
agentDcbxStatusEntry = _AgentDcbxStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2, 1)
)
agentDcbxStatusEntry.setIndexNames(
    (0, "DNOS-DCBX-MIB", "agentDcbxIntfIndex"),
)
if mibBuilder.loadTexts:
    agentDcbxStatusEntry.setStatus("current")


class _AgentDcbxOperVersion_Type(DcbxVersion):
    """Custom type agentDcbxOperVersion based on DcbxVersion"""
    defaultValue = 1


_AgentDcbxOperVersion_Object = MibTableColumn
agentDcbxOperVersion = _AgentDcbxOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2, 1, 2),
    _AgentDcbxOperVersion_Type()
)
agentDcbxOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDcbxOperVersion.setStatus("current")
_AgentDcbxPeerMACaddress_Type = MacAddress
_AgentDcbxPeerMACaddress_Object = MibTableColumn
agentDcbxPeerMACaddress = _AgentDcbxPeerMACaddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2, 1, 3),
    _AgentDcbxPeerMACaddress_Type()
)
agentDcbxPeerMACaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDcbxPeerMACaddress.setStatus("current")


class _AgentDcbxCfgSource_Type(Integer32):
    """Custom type agentDcbxCfgSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_AgentDcbxCfgSource_Type.__name__ = "Integer32"
_AgentDcbxCfgSource_Object = MibTableColumn
agentDcbxCfgSource = _AgentDcbxCfgSource_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2, 1, 4),
    _AgentDcbxCfgSource_Type()
)
agentDcbxCfgSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDcbxCfgSource.setStatus("current")
_AgentDcbxMultiplePeerCount_Type = Unsigned32
_AgentDcbxMultiplePeerCount_Object = MibTableColumn
agentDcbxMultiplePeerCount = _AgentDcbxMultiplePeerCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2, 1, 5),
    _AgentDcbxMultiplePeerCount_Type()
)
agentDcbxMultiplePeerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDcbxMultiplePeerCount.setStatus("current")
_AgentDcbxPeerRemovedCount_Type = Unsigned32
_AgentDcbxPeerRemovedCount_Object = MibTableColumn
agentDcbxPeerRemovedCount = _AgentDcbxPeerRemovedCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2, 1, 6),
    _AgentDcbxPeerRemovedCount_Type()
)
agentDcbxPeerRemovedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDcbxPeerRemovedCount.setStatus("current")
_AgentDcbxPeerOperVersionNum_Type = Unsigned32
_AgentDcbxPeerOperVersionNum_Object = MibTableColumn
agentDcbxPeerOperVersionNum = _AgentDcbxPeerOperVersionNum_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2, 1, 7),
    _AgentDcbxPeerOperVersionNum_Type()
)
agentDcbxPeerOperVersionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDcbxPeerOperVersionNum.setStatus("current")
_AgentDcbxPeerMaxVersion_Type = Unsigned32
_AgentDcbxPeerMaxVersion_Object = MibTableColumn
agentDcbxPeerMaxVersion = _AgentDcbxPeerMaxVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2, 1, 8),
    _AgentDcbxPeerMaxVersion_Type()
)
agentDcbxPeerMaxVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDcbxPeerMaxVersion.setStatus("current")
_AgentDcbxSeqNum_Type = Unsigned32
_AgentDcbxSeqNum_Object = MibTableColumn
agentDcbxSeqNum = _AgentDcbxSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2, 1, 9),
    _AgentDcbxSeqNum_Type()
)
agentDcbxSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDcbxSeqNum.setStatus("current")
_AgentDcbxAckNum_Type = Unsigned32
_AgentDcbxAckNum_Object = MibTableColumn
agentDcbxAckNum = _AgentDcbxAckNum_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2, 1, 10),
    _AgentDcbxAckNum_Type()
)
agentDcbxAckNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDcbxAckNum.setStatus("current")
_AgentDcbxPeerRcvdAckNum_Type = Unsigned32
_AgentDcbxPeerRcvdAckNum_Object = MibTableColumn
agentDcbxPeerRcvdAckNum = _AgentDcbxPeerRcvdAckNum_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2, 1, 11),
    _AgentDcbxPeerRcvdAckNum_Type()
)
agentDcbxPeerRcvdAckNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDcbxPeerRcvdAckNum.setStatus("current")
_AgentDcbxTxCount_Type = Unsigned32
_AgentDcbxTxCount_Object = MibTableColumn
agentDcbxTxCount = _AgentDcbxTxCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2, 1, 12),
    _AgentDcbxTxCount_Type()
)
agentDcbxTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDcbxTxCount.setStatus("current")
_AgentDcbxRxCount_Type = Unsigned32
_AgentDcbxRxCount_Object = MibTableColumn
agentDcbxRxCount = _AgentDcbxRxCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2, 1, 13),
    _AgentDcbxRxCount_Type()
)
agentDcbxRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDcbxRxCount.setStatus("current")
_AgentDcbxErrorFramesCount_Type = Unsigned32
_AgentDcbxErrorFramesCount_Object = MibTableColumn
agentDcbxErrorFramesCount = _AgentDcbxErrorFramesCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2, 1, 14),
    _AgentDcbxErrorFramesCount_Type()
)
agentDcbxErrorFramesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDcbxErrorFramesCount.setStatus("current")
_AgentDcbxUnknownTLVsCount_Type = Unsigned32
_AgentDcbxUnknownTLVsCount_Object = MibTableColumn
agentDcbxUnknownTLVsCount = _AgentDcbxUnknownTLVsCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2, 1, 15),
    _AgentDcbxUnknownTLVsCount_Type()
)
agentDcbxUnknownTLVsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDcbxUnknownTLVsCount.setStatus("current")
_AgentDcbxGroupGlobalConfGroup_ObjectIdentity = ObjectIdentity
agentDcbxGroupGlobalConfGroup = _AgentDcbxGroupGlobalConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 3)
)


class _AgentDcbxGlobalConfVersion_Type(DcbxVersion):
    """Custom type agentDcbxGlobalConfVersion based on DcbxVersion"""
    defaultValue = 1


_AgentDcbxGlobalConfVersion_Object = MibScalar
agentDcbxGlobalConfVersion = _AgentDcbxGlobalConfVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 3, 1),
    _AgentDcbxGlobalConfVersion_Type()
)
agentDcbxGlobalConfVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDcbxGlobalConfVersion.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNOS-DCBX-MIB",
    **{"DcbxPortRole": DcbxPortRole,
       "DcbxVersion": DcbxVersion,
       "fastPathDCBX": fastPathDCBX,
       "agentDcbxGroup": agentDcbxGroup,
       "agentDcbxTable": agentDcbxTable,
       "agentDcbxEntry": agentDcbxEntry,
       "agentDcbxIntfIndex": agentDcbxIntfIndex,
       "agentDcbxAutoCfgPortRole": agentDcbxAutoCfgPortRole,
       "agentDcbxVersion": agentDcbxVersion,
       "agentDcbxSupportedTLVs": agentDcbxSupportedTLVs,
       "agentDcbxConfigTLVsTxEnable": agentDcbxConfigTLVsTxEnable,
       "agentDcbxStatusTable": agentDcbxStatusTable,
       "agentDcbxStatusEntry": agentDcbxStatusEntry,
       "agentDcbxOperVersion": agentDcbxOperVersion,
       "agentDcbxPeerMACaddress": agentDcbxPeerMACaddress,
       "agentDcbxCfgSource": agentDcbxCfgSource,
       "agentDcbxMultiplePeerCount": agentDcbxMultiplePeerCount,
       "agentDcbxPeerRemovedCount": agentDcbxPeerRemovedCount,
       "agentDcbxPeerOperVersionNum": agentDcbxPeerOperVersionNum,
       "agentDcbxPeerMaxVersion": agentDcbxPeerMaxVersion,
       "agentDcbxSeqNum": agentDcbxSeqNum,
       "agentDcbxAckNum": agentDcbxAckNum,
       "agentDcbxPeerRcvdAckNum": agentDcbxPeerRcvdAckNum,
       "agentDcbxTxCount": agentDcbxTxCount,
       "agentDcbxRxCount": agentDcbxRxCount,
       "agentDcbxErrorFramesCount": agentDcbxErrorFramesCount,
       "agentDcbxUnknownTLVsCount": agentDcbxUnknownTLVsCount,
       "agentDcbxGroupGlobalConfGroup": agentDcbxGroupGlobalConfGroup,
       "agentDcbxGlobalConfVersion": agentDcbxGlobalConfVersion}
)
