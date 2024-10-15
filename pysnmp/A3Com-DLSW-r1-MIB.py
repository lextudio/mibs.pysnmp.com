# SNMP MIB module (A3COM-DLSW-R1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-DLSW-R1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:11 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class NBName(OctetString):
    """Custom type NBName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )





class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class TAddress(OctetString):
    """Custom type TAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )





class DlswTimeStamp(TimeTicks):
    """Custom type DlswTimeStamp based on TimeTicks"""




class EndStationLocation(Integer32):
    """Custom type EndStationLocation based on Integer32"""
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
        *(("internal", 2),
          ("local", 4),
          ("other", 1),
          ("remote", 3))
    )





class DlcType(Integer32):
    """Custom type DlcType based on Integer32"""
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
        *(("llc", 3),
          ("na", 2),
          ("other", 1),
          ("sdlc", 4))
    )





class LFSize(Integer32):
    """Custom type LFSize based on Integer32"""




class Truthvalue(Integer32):
    """Custom type Truthvalue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
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





class Instancepointer(Integer32):
    """Custom type Instancepointer based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_BrouterMIB_ObjectIdentity = ObjectIdentity
brouterMIB = _BrouterMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2)
)
_DlswMIB_3Com_ObjectIdentity = ObjectIdentity
dlswMIB_3Com = _DlswMIB_3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 24)
)
_DlswNode_ObjectIdentity = ObjectIdentity
dlswNode = _DlswNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 1)
)


class _DlswVersion_Type(OctetString):
    """Custom type dlswVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_DlswVersion_Type.__name__ = "OctetString"
_DlswVersion_Object = MibScalar
dlswVersion = _DlswVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 1, 1),
    _DlswVersion_Type()
)
dlswVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswVersion.setStatus("mandatory")


class _DlswVendorID_Type(OctetString):
    """Custom type dlswVendorID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_DlswVendorID_Type.__name__ = "OctetString"
_DlswVendorID_Object = MibScalar
dlswVendorID = _DlswVendorID_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 1, 2),
    _DlswVendorID_Type()
)
dlswVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswVendorID.setStatus("mandatory")


class _DlswVersionString_Type(DisplayString):
    """Custom type dlswVersionString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DlswVersionString_Type.__name__ = "DisplayString"
_DlswVersionString_Object = MibScalar
dlswVersionString = _DlswVersionString_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 1, 3),
    _DlswVersionString_Type()
)
dlswVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswVersionString.setStatus("mandatory")


class _DlswStdPacingSupport_Type(Integer32):
    """Custom type dlswStdPacingSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adaptiveRcvWindow", 2),
          ("fixedRcvWindow", 3),
          ("none", 1))
    )


_DlswStdPacingSupport_Type.__name__ = "Integer32"
_DlswStdPacingSupport_Object = MibScalar
dlswStdPacingSupport = _DlswStdPacingSupport_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 1, 4),
    _DlswStdPacingSupport_Type()
)
dlswStdPacingSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswStdPacingSupport.setStatus("mandatory")


class _DlswStatus_Type(Integer32):
    """Custom type dlswStatus based on Integer32"""
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


_DlswStatus_Type.__name__ = "Integer32"
_DlswStatus_Object = MibScalar
dlswStatus = _DlswStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 1, 5),
    _DlswStatus_Type()
)
dlswStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswStatus.setStatus("mandatory")
_DlswUpTime_Type = TimeTicks
_DlswUpTime_Object = MibScalar
dlswUpTime = _DlswUpTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 1, 6),
    _DlswUpTime_Type()
)
dlswUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswUpTime.setStatus("mandatory")
_DlswVirtualSegmentLFSize_Type = Integer32
_DlswVirtualSegmentLFSize_Object = MibScalar
dlswVirtualSegmentLFSize = _DlswVirtualSegmentLFSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 1, 7),
    _DlswVirtualSegmentLFSize_Type()
)
dlswVirtualSegmentLFSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswVirtualSegmentLFSize.setStatus("mandatory")
_DlswResourceNBExclusivity_Type = Truthvalue
_DlswResourceNBExclusivity_Object = MibScalar
dlswResourceNBExclusivity = _DlswResourceNBExclusivity_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 1, 8),
    _DlswResourceNBExclusivity_Type()
)
dlswResourceNBExclusivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswResourceNBExclusivity.setStatus("mandatory")
_DlswResourceMacExclusivity_Type = Truthvalue
_DlswResourceMacExclusivity_Object = MibScalar
dlswResourceMacExclusivity = _DlswResourceMacExclusivity_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 1, 9),
    _DlswResourceMacExclusivity_Type()
)
dlswResourceMacExclusivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswResourceMacExclusivity.setStatus("mandatory")
_DlswTrapControl_ObjectIdentity = ObjectIdentity
dlswTrapControl = _DlswTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 1, 10)
)


class _DlswTrapCntlTConn_Type(Integer32):
    """Custom type dlswTrapCntlTConn based on Integer32"""
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


_DlswTrapCntlTConn_Type.__name__ = "Integer32"
_DlswTrapCntlTConn_Object = MibScalar
dlswTrapCntlTConn = _DlswTrapCntlTConn_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 1, 10, 3),
    _DlswTrapCntlTConn_Type()
)
dlswTrapCntlTConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswTrapCntlTConn.setStatus("mandatory")


class _DlswTrapCntlCircuit_Type(Integer32):
    """Custom type dlswTrapCntlCircuit based on Integer32"""
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


_DlswTrapCntlCircuit_Type.__name__ = "Integer32"
_DlswTrapCntlCircuit_Object = MibScalar
dlswTrapCntlCircuit = _DlswTrapCntlCircuit_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 1, 10, 4),
    _DlswTrapCntlCircuit_Type()
)
dlswTrapCntlCircuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswTrapCntlCircuit.setStatus("mandatory")
_DlswTConn_ObjectIdentity = ObjectIdentity
dlswTConn = _DlswTConn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2)
)
_DlswTConnStat_ObjectIdentity = ObjectIdentity
dlswTConnStat = _DlswTConnStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 1)
)
_DlswTConnStatActiveConnections_Type = Gauge32
_DlswTConnStatActiveConnections_Object = MibScalar
dlswTConnStatActiveConnections = _DlswTConnStatActiveConnections_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 1, 1),
    _DlswTConnStatActiveConnections_Type()
)
dlswTConnStatActiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnStatActiveConnections.setStatus("mandatory")
_DlswTConnStatCloseIdles_Type = Counter32
_DlswTConnStatCloseIdles_Object = MibScalar
dlswTConnStatCloseIdles = _DlswTConnStatCloseIdles_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 1, 2),
    _DlswTConnStatCloseIdles_Type()
)
dlswTConnStatCloseIdles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnStatCloseIdles.setStatus("mandatory")
_DlswTConnStatCloseBusys_Type = Counter32
_DlswTConnStatCloseBusys_Object = MibScalar
dlswTConnStatCloseBusys = _DlswTConnStatCloseBusys_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 1, 3),
    _DlswTConnStatCloseBusys_Type()
)
dlswTConnStatCloseBusys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnStatCloseBusys.setStatus("mandatory")
_DlswTConnConfigTable_Object = MibTable
dlswTConnConfigTable = _DlswTConnConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 2)
)
if mibBuilder.loadTexts:
    dlswTConnConfigTable.setStatus("mandatory")
_DlswTConnConfigEntry_Object = MibTableRow
dlswTConnConfigEntry = _DlswTConnConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 2, 1)
)
dlswTConnConfigEntry.setIndexNames(
    (0, "A3COM-DLSW-R1-MIB", "dlswTConnConfigIndex"),
)
if mibBuilder.loadTexts:
    dlswTConnConfigEntry.setStatus("mandatory")
_DlswTConnConfigIndex_Type = Integer32
_DlswTConnConfigIndex_Object = MibTableColumn
dlswTConnConfigIndex = _DlswTConnConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 2, 1, 1),
    _DlswTConnConfigIndex_Type()
)
dlswTConnConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnConfigIndex.setStatus("mandatory")
_DlswTConnConfigTDomain_Type = ObjectIdentifier
_DlswTConnConfigTDomain_Object = MibTableColumn
dlswTConnConfigTDomain = _DlswTConnConfigTDomain_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 2, 1, 2),
    _DlswTConnConfigTDomain_Type()
)
dlswTConnConfigTDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswTConnConfigTDomain.setStatus("mandatory")
_DlswTConnConfigLocalTAddr_Type = TAddress
_DlswTConnConfigLocalTAddr_Object = MibTableColumn
dlswTConnConfigLocalTAddr = _DlswTConnConfigLocalTAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 2, 1, 3),
    _DlswTConnConfigLocalTAddr_Type()
)
dlswTConnConfigLocalTAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswTConnConfigLocalTAddr.setStatus("mandatory")
_DlswTConnConfigRemoteTAddr_Type = TAddress
_DlswTConnConfigRemoteTAddr_Object = MibTableColumn
dlswTConnConfigRemoteTAddr = _DlswTConnConfigRemoteTAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 2, 1, 4),
    _DlswTConnConfigRemoteTAddr_Type()
)
dlswTConnConfigRemoteTAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswTConnConfigRemoteTAddr.setStatus("mandatory")
_DlswTConnConfigLastModifyTime_Type = DlswTimeStamp
_DlswTConnConfigLastModifyTime_Object = MibTableColumn
dlswTConnConfigLastModifyTime = _DlswTConnConfigLastModifyTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 2, 1, 5),
    _DlswTConnConfigLastModifyTime_Type()
)
dlswTConnConfigLastModifyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswTConnConfigLastModifyTime.setStatus("mandatory")


class _DlswTConnConfigEntryType_Type(Integer32):
    """Custom type dlswTConnConfigEntryType based on Integer32"""
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
          ("group", 3),
          ("individual", 1))
    )


_DlswTConnConfigEntryType_Type.__name__ = "Integer32"
_DlswTConnConfigEntryType_Object = MibTableColumn
dlswTConnConfigEntryType = _DlswTConnConfigEntryType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 2, 1, 6),
    _DlswTConnConfigEntryType_Type()
)
dlswTConnConfigEntryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswTConnConfigEntryType.setStatus("mandatory")
_DlswTConnConfigGroupDefinition_Type = Instancepointer
_DlswTConnConfigGroupDefinition_Object = MibTableColumn
dlswTConnConfigGroupDefinition = _DlswTConnConfigGroupDefinition_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 2, 1, 7),
    _DlswTConnConfigGroupDefinition_Type()
)
dlswTConnConfigGroupDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswTConnConfigGroupDefinition.setStatus("mandatory")


class _DlswTConnConfigSetupType_Type(Integer32):
    """Custom type dlswTConnConfigSetupType based on Integer32"""
    defaultValue = 4

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
        *(("activeOnDemand", 3),
          ("activePersistent", 2),
          ("excluded", 5),
          ("other", 1),
          ("passive", 4))
    )


_DlswTConnConfigSetupType_Type.__name__ = "Integer32"
_DlswTConnConfigSetupType_Object = MibTableColumn
dlswTConnConfigSetupType = _DlswTConnConfigSetupType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 2, 1, 8),
    _DlswTConnConfigSetupType_Type()
)
dlswTConnConfigSetupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswTConnConfigSetupType.setStatus("mandatory")


class _DlswTConnConfigSapList_Type(OctetString):
    """Custom type dlswTConnConfigSapList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_DlswTConnConfigSapList_Type.__name__ = "OctetString"
_DlswTConnConfigSapList_Object = MibTableColumn
dlswTConnConfigSapList = _DlswTConnConfigSapList_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 2, 1, 9),
    _DlswTConnConfigSapList_Type()
)
dlswTConnConfigSapList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswTConnConfigSapList.setStatus("mandatory")


class _DlswTConnConfigAdvertiseMacNB_Type(Truthvalue):
    """Custom type dlswTConnConfigAdvertiseMacNB based on Truthvalue"""


_DlswTConnConfigAdvertiseMacNB_Object = MibTableColumn
dlswTConnConfigAdvertiseMacNB = _DlswTConnConfigAdvertiseMacNB_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 2, 1, 10),
    _DlswTConnConfigAdvertiseMacNB_Type()
)
dlswTConnConfigAdvertiseMacNB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswTConnConfigAdvertiseMacNB.setStatus("mandatory")


class _DlswTConnConfigInitCirRecvWndw_Type(Integer32):
    """Custom type dlswTConnConfigInitCirRecvWndw based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DlswTConnConfigInitCirRecvWndw_Type.__name__ = "Integer32"
_DlswTConnConfigInitCirRecvWndw_Object = MibTableColumn
dlswTConnConfigInitCirRecvWndw = _DlswTConnConfigInitCirRecvWndw_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 2, 1, 11),
    _DlswTConnConfigInitCirRecvWndw_Type()
)
dlswTConnConfigInitCirRecvWndw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswTConnConfigInitCirRecvWndw.setStatus("mandatory")
_DlswTConnConfigOpens_Type = Counter32
_DlswTConnConfigOpens_Object = MibTableColumn
dlswTConnConfigOpens = _DlswTConnConfigOpens_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 2, 1, 12),
    _DlswTConnConfigOpens_Type()
)
dlswTConnConfigOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnConfigOpens.setStatus("mandatory")
_DlswTConnConfigRowStatus_Type = RowStatus
_DlswTConnConfigRowStatus_Object = MibTableColumn
dlswTConnConfigRowStatus = _DlswTConnConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 2, 1, 13),
    _DlswTConnConfigRowStatus_Type()
)
dlswTConnConfigRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswTConnConfigRowStatus.setStatus("mandatory")
_DlswTConnOperTable_Object = MibTable
dlswTConnOperTable = _DlswTConnOperTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3)
)
if mibBuilder.loadTexts:
    dlswTConnOperTable.setStatus("mandatory")
_DlswTConnOperEntry_Object = MibTableRow
dlswTConnOperEntry = _DlswTConnOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1)
)
dlswTConnOperEntry.setIndexNames(
    (0, "A3COM-DLSW-R1-MIB", "dlswTConnOperTDomain"),
    (0, "A3COM-DLSW-R1-MIB", "dlswTConnOperRemoteTAddr"),
)
if mibBuilder.loadTexts:
    dlswTConnOperEntry.setStatus("mandatory")
_DlswTConnOperTDomain_Type = ObjectIdentifier
_DlswTConnOperTDomain_Object = MibTableColumn
dlswTConnOperTDomain = _DlswTConnOperTDomain_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 1),
    _DlswTConnOperTDomain_Type()
)
dlswTConnOperTDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperTDomain.setStatus("mandatory")
_DlswTConnOperLocalTAddr_Type = TAddress
_DlswTConnOperLocalTAddr_Object = MibTableColumn
dlswTConnOperLocalTAddr = _DlswTConnOperLocalTAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 2),
    _DlswTConnOperLocalTAddr_Type()
)
dlswTConnOperLocalTAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperLocalTAddr.setStatus("mandatory")
_DlswTConnOperRemoteTAddr_Type = TAddress
_DlswTConnOperRemoteTAddr_Object = MibTableColumn
dlswTConnOperRemoteTAddr = _DlswTConnOperRemoteTAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 3),
    _DlswTConnOperRemoteTAddr_Type()
)
dlswTConnOperRemoteTAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperRemoteTAddr.setStatus("mandatory")
_DlswTConnOperEntryTime_Type = DlswTimeStamp
_DlswTConnOperEntryTime_Object = MibTableColumn
dlswTConnOperEntryTime = _DlswTConnOperEntryTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 4),
    _DlswTConnOperEntryTime_Type()
)
dlswTConnOperEntryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperEntryTime.setStatus("mandatory")
_DlswTConnOperConnectTime_Type = DlswTimeStamp
_DlswTConnOperConnectTime_Object = MibTableColumn
dlswTConnOperConnectTime = _DlswTConnOperConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 5),
    _DlswTConnOperConnectTime_Type()
)
dlswTConnOperConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperConnectTime.setStatus("mandatory")


class _DlswTConnOperState_Type(Integer32):
    """Custom type dlswTConnOperState based on Integer32"""
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
        *(("connected", 3),
          ("connecting", 1),
          ("disconnected", 6),
          ("disconnecting", 5),
          ("initCapExchange", 2),
          ("quiescing", 4))
    )


_DlswTConnOperState_Type.__name__ = "Integer32"
_DlswTConnOperState_Object = MibTableColumn
dlswTConnOperState = _DlswTConnOperState_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 6),
    _DlswTConnOperState_Type()
)
dlswTConnOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswTConnOperState.setStatus("mandatory")
_DlswTConnOperConfigIndex_Type = Integer32
_DlswTConnOperConfigIndex_Object = MibTableColumn
dlswTConnOperConfigIndex = _DlswTConnOperConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 7),
    _DlswTConnOperConfigIndex_Type()
)
dlswTConnOperConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperConfigIndex.setStatus("mandatory")


class _DlswTConnOperFlowCntlMode_Type(Integer32):
    """Custom type dlswTConnOperFlowCntlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 3),
          ("pacing", 2),
          ("undetermined", 1))
    )


_DlswTConnOperFlowCntlMode_Type.__name__ = "Integer32"
_DlswTConnOperFlowCntlMode_Object = MibTableColumn
dlswTConnOperFlowCntlMode = _DlswTConnOperFlowCntlMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 8),
    _DlswTConnOperFlowCntlMode_Type()
)
dlswTConnOperFlowCntlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperFlowCntlMode.setStatus("mandatory")


class _DlswTConnOperPartnerVersion_Type(OctetString):
    """Custom type dlswTConnOperPartnerVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_DlswTConnOperPartnerVersion_Type.__name__ = "OctetString"
_DlswTConnOperPartnerVersion_Object = MibTableColumn
dlswTConnOperPartnerVersion = _DlswTConnOperPartnerVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 9),
    _DlswTConnOperPartnerVersion_Type()
)
dlswTConnOperPartnerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperPartnerVersion.setStatus("mandatory")


class _DlswTConnOperPartnerVendorID_Type(OctetString):
    """Custom type dlswTConnOperPartnerVendorID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_DlswTConnOperPartnerVendorID_Type.__name__ = "OctetString"
_DlswTConnOperPartnerVendorID_Object = MibTableColumn
dlswTConnOperPartnerVendorID = _DlswTConnOperPartnerVendorID_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 10),
    _DlswTConnOperPartnerVendorID_Type()
)
dlswTConnOperPartnerVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperPartnerVendorID.setStatus("mandatory")


class _DlswTConnOperPartnerVersionStr_Type(DisplayString):
    """Custom type dlswTConnOperPartnerVersionStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )


_DlswTConnOperPartnerVersionStr_Type.__name__ = "DisplayString"
_DlswTConnOperPartnerVersionStr_Object = MibTableColumn
dlswTConnOperPartnerVersionStr = _DlswTConnOperPartnerVersionStr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 11),
    _DlswTConnOperPartnerVersionStr_Type()
)
dlswTConnOperPartnerVersionStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperPartnerVersionStr.setStatus("mandatory")


class _DlswTConnOperPartnerInitPacingWndw_Type(Integer32):
    """Custom type dlswTConnOperPartnerInitPacingWndw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DlswTConnOperPartnerInitPacingWndw_Type.__name__ = "Integer32"
_DlswTConnOperPartnerInitPacingWndw_Object = MibTableColumn
dlswTConnOperPartnerInitPacingWndw = _DlswTConnOperPartnerInitPacingWndw_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 12),
    _DlswTConnOperPartnerInitPacingWndw_Type()
)
dlswTConnOperPartnerInitPacingWndw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperPartnerInitPacingWndw.setStatus("mandatory")


class _DlswTConnOperPartnerSapList_Type(OctetString):
    """Custom type dlswTConnOperPartnerSapList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DlswTConnOperPartnerSapList_Type.__name__ = "OctetString"
_DlswTConnOperPartnerSapList_Object = MibTableColumn
dlswTConnOperPartnerSapList = _DlswTConnOperPartnerSapList_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 13),
    _DlswTConnOperPartnerSapList_Type()
)
dlswTConnOperPartnerSapList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswTConnOperPartnerSapList.setStatus("mandatory")
_DlswTConnOperPartnerNBExcl_Type = Truthvalue
_DlswTConnOperPartnerNBExcl_Object = MibTableColumn
dlswTConnOperPartnerNBExcl = _DlswTConnOperPartnerNBExcl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 14),
    _DlswTConnOperPartnerNBExcl_Type()
)
dlswTConnOperPartnerNBExcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperPartnerNBExcl.setStatus("mandatory")
_DlswTConnOperPartnerMacExcl_Type = Truthvalue
_DlswTConnOperPartnerMacExcl_Object = MibTableColumn
dlswTConnOperPartnerMacExcl = _DlswTConnOperPartnerMacExcl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 15),
    _DlswTConnOperPartnerMacExcl_Type()
)
dlswTConnOperPartnerMacExcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperPartnerMacExcl.setStatus("mandatory")


class _DlswTConnOperPartnerNBInfo_Type(Integer32):
    """Custom type dlswTConnOperPartnerNBInfo based on Integer32"""
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
        *(("complete", 3),
          ("none", 1),
          ("notApplicable", 4),
          ("partial", 2))
    )


_DlswTConnOperPartnerNBInfo_Type.__name__ = "Integer32"
_DlswTConnOperPartnerNBInfo_Object = MibTableColumn
dlswTConnOperPartnerNBInfo = _DlswTConnOperPartnerNBInfo_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 16),
    _DlswTConnOperPartnerNBInfo_Type()
)
dlswTConnOperPartnerNBInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperPartnerNBInfo.setStatus("mandatory")


class _DlswTConnOperPartnerMacInfo_Type(Integer32):
    """Custom type dlswTConnOperPartnerMacInfo based on Integer32"""
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
        *(("complete", 3),
          ("none", 1),
          ("notApplicable", 4),
          ("partial", 2))
    )


_DlswTConnOperPartnerMacInfo_Type.__name__ = "Integer32"
_DlswTConnOperPartnerMacInfo_Object = MibTableColumn
dlswTConnOperPartnerMacInfo = _DlswTConnOperPartnerMacInfo_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 17),
    _DlswTConnOperPartnerMacInfo_Type()
)
dlswTConnOperPartnerMacInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperPartnerMacInfo.setStatus("mandatory")
_DlswTConnOperDiscTime_Type = DlswTimeStamp
_DlswTConnOperDiscTime_Object = MibTableColumn
dlswTConnOperDiscTime = _DlswTConnOperDiscTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 18),
    _DlswTConnOperDiscTime_Type()
)
dlswTConnOperDiscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperDiscTime.setStatus("mandatory")


class _DlswTConnOperDiscReason_Type(Integer32):
    """Custom type dlswTConnOperDiscReason based on Integer32"""
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
        *(("capExFailed", 2),
          ("lastCircuitDiscd", 5),
          ("operatorCommand", 4),
          ("other", 1),
          ("protocolError", 6),
          ("transportLayerDisc", 3))
    )


_DlswTConnOperDiscReason_Type.__name__ = "Integer32"
_DlswTConnOperDiscReason_Object = MibTableColumn
dlswTConnOperDiscReason = _DlswTConnOperDiscReason_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 19),
    _DlswTConnOperDiscReason_Type()
)
dlswTConnOperDiscReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperDiscReason.setStatus("mandatory")
_DlswTConnOperDiscActiveCir_Type = Integer32
_DlswTConnOperDiscActiveCir_Object = MibTableColumn
dlswTConnOperDiscActiveCir = _DlswTConnOperDiscActiveCir_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 20),
    _DlswTConnOperDiscActiveCir_Type()
)
dlswTConnOperDiscActiveCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperDiscActiveCir.setStatus("mandatory")
_DlswTConnOperInDataPkts_Type = Counter32
_DlswTConnOperInDataPkts_Object = MibTableColumn
dlswTConnOperInDataPkts = _DlswTConnOperInDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 21),
    _DlswTConnOperInDataPkts_Type()
)
dlswTConnOperInDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperInDataPkts.setStatus("mandatory")
_DlswTConnOperOutDataPkts_Type = Counter32
_DlswTConnOperOutDataPkts_Object = MibTableColumn
dlswTConnOperOutDataPkts = _DlswTConnOperOutDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 22),
    _DlswTConnOperOutDataPkts_Type()
)
dlswTConnOperOutDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperOutDataPkts.setStatus("mandatory")
_DlswTConnOperInDataOctets_Type = Counter32
_DlswTConnOperInDataOctets_Object = MibTableColumn
dlswTConnOperInDataOctets = _DlswTConnOperInDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 23),
    _DlswTConnOperInDataOctets_Type()
)
dlswTConnOperInDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperInDataOctets.setStatus("mandatory")
_DlswTConnOperOutDataOctets_Type = Counter32
_DlswTConnOperOutDataOctets_Object = MibTableColumn
dlswTConnOperOutDataOctets = _DlswTConnOperOutDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 24),
    _DlswTConnOperOutDataOctets_Type()
)
dlswTConnOperOutDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperOutDataOctets.setStatus("mandatory")
_DlswTConnOperInCntlPkts_Type = Counter32
_DlswTConnOperInCntlPkts_Object = MibTableColumn
dlswTConnOperInCntlPkts = _DlswTConnOperInCntlPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 25),
    _DlswTConnOperInCntlPkts_Type()
)
dlswTConnOperInCntlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperInCntlPkts.setStatus("mandatory")
_DlswTConnOperOutCntlPkts_Type = Counter32
_DlswTConnOperOutCntlPkts_Object = MibTableColumn
dlswTConnOperOutCntlPkts = _DlswTConnOperOutCntlPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 26),
    _DlswTConnOperOutCntlPkts_Type()
)
dlswTConnOperOutCntlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperOutCntlPkts.setStatus("mandatory")
_DlswTConnOperCURexSents_Type = Counter32
_DlswTConnOperCURexSents_Object = MibTableColumn
dlswTConnOperCURexSents = _DlswTConnOperCURexSents_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 27),
    _DlswTConnOperCURexSents_Type()
)
dlswTConnOperCURexSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperCURexSents.setStatus("mandatory")
_DlswTConnOperICRexRcvds_Type = Counter32
_DlswTConnOperICRexRcvds_Object = MibTableColumn
dlswTConnOperICRexRcvds = _DlswTConnOperICRexRcvds_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 28),
    _DlswTConnOperICRexRcvds_Type()
)
dlswTConnOperICRexRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperICRexRcvds.setStatus("mandatory")
_DlswTConnOperCURexRcvds_Type = Counter32
_DlswTConnOperCURexRcvds_Object = MibTableColumn
dlswTConnOperCURexRcvds = _DlswTConnOperCURexRcvds_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 29),
    _DlswTConnOperCURexRcvds_Type()
)
dlswTConnOperCURexRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperCURexRcvds.setStatus("mandatory")
_DlswTConnOperICRexSents_Type = Counter32
_DlswTConnOperICRexSents_Object = MibTableColumn
dlswTConnOperICRexSents = _DlswTConnOperICRexSents_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 30),
    _DlswTConnOperICRexSents_Type()
)
dlswTConnOperICRexSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperICRexSents.setStatus("mandatory")
_DlswTConnOperNQexSents_Type = Counter32
_DlswTConnOperNQexSents_Object = MibTableColumn
dlswTConnOperNQexSents = _DlswTConnOperNQexSents_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 31),
    _DlswTConnOperNQexSents_Type()
)
dlswTConnOperNQexSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperNQexSents.setStatus("mandatory")
_DlswTConnOperNRexRcvds_Type = Counter32
_DlswTConnOperNRexRcvds_Object = MibTableColumn
dlswTConnOperNRexRcvds = _DlswTConnOperNRexRcvds_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 32),
    _DlswTConnOperNRexRcvds_Type()
)
dlswTConnOperNRexRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperNRexRcvds.setStatus("mandatory")
_DlswTConnOperNQexRcvds_Type = Counter32
_DlswTConnOperNQexRcvds_Object = MibTableColumn
dlswTConnOperNQexRcvds = _DlswTConnOperNQexRcvds_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 33),
    _DlswTConnOperNQexRcvds_Type()
)
dlswTConnOperNQexRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperNQexRcvds.setStatus("mandatory")
_DlswTConnOperNRexSents_Type = Counter32
_DlswTConnOperNRexSents_Object = MibTableColumn
dlswTConnOperNRexSents = _DlswTConnOperNRexSents_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 34),
    _DlswTConnOperNRexSents_Type()
)
dlswTConnOperNRexSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperNRexSents.setStatus("mandatory")
_DlswTConnOperCirCreates_Type = Counter32
_DlswTConnOperCirCreates_Object = MibTableColumn
dlswTConnOperCirCreates = _DlswTConnOperCirCreates_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 35),
    _DlswTConnOperCirCreates_Type()
)
dlswTConnOperCirCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperCirCreates.setStatus("mandatory")
_DlswTConnOperCircuits_Type = Gauge32
_DlswTConnOperCircuits_Object = MibTableColumn
dlswTConnOperCircuits = _DlswTConnOperCircuits_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 2, 3, 1, 36),
    _DlswTConnOperCircuits_Type()
)
dlswTConnOperCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperCircuits.setStatus("mandatory")
_DlswInterface_ObjectIdentity = ObjectIdentity
dlswInterface = _DlswInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 3)
)
_DlswDirectory_ObjectIdentity = ObjectIdentity
dlswDirectory = _DlswDirectory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 4)
)
_DlswDirStat_ObjectIdentity = ObjectIdentity
dlswDirStat = _DlswDirStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 4, 1)
)
_DlswDirMacEntries_Type = Gauge32
_DlswDirMacEntries_Object = MibScalar
dlswDirMacEntries = _DlswDirMacEntries_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 4, 1, 1),
    _DlswDirMacEntries_Type()
)
dlswDirMacEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswDirMacEntries.setStatus("mandatory")
_DlswDirNBEntries_Type = Gauge32
_DlswDirNBEntries_Object = MibScalar
dlswDirNBEntries = _DlswDirNBEntries_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 4, 1, 4),
    _DlswDirNBEntries_Type()
)
dlswDirNBEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswDirNBEntries.setStatus("mandatory")
_DlswDirCache_ObjectIdentity = ObjectIdentity
dlswDirCache = _DlswDirCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 4, 2)
)
_DlswDirMacTable_Object = MibTable
dlswDirMacTable = _DlswDirMacTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 4, 2, 1)
)
if mibBuilder.loadTexts:
    dlswDirMacTable.setStatus("mandatory")
_DlswDirMacEntry_Object = MibTableRow
dlswDirMacEntry = _DlswDirMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 4, 2, 1, 1)
)
dlswDirMacEntry.setIndexNames(
    (0, "A3COM-DLSW-R1-MIB", "dlswDirMacIndex"),
)
if mibBuilder.loadTexts:
    dlswDirMacEntry.setStatus("mandatory")
_DlswDirMacIndex_Type = Integer32
_DlswDirMacIndex_Object = MibTableColumn
dlswDirMacIndex = _DlswDirMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 4, 2, 1, 1, 1),
    _DlswDirMacIndex_Type()
)
dlswDirMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswDirMacIndex.setStatus("mandatory")
_DlswDirMacMac_Type = MacAddress
_DlswDirMacMac_Object = MibTableColumn
dlswDirMacMac = _DlswDirMacMac_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 4, 2, 1, 1, 2),
    _DlswDirMacMac_Type()
)
dlswDirMacMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswDirMacMac.setStatus("mandatory")


class _DlswDirMacMask_Type(MacAddress):
    """Custom type dlswDirMacMask based on MacAddress"""
    defaultHexValue = "FFFFFFFFFFFF"


_DlswDirMacMask_Object = MibTableColumn
dlswDirMacMask = _DlswDirMacMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 4, 2, 1, 1, 3),
    _DlswDirMacMask_Type()
)
dlswDirMacMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswDirMacMask.setStatus("mandatory")


class _DlswDirMacEntryType_Type(Integer32):
    """Custom type dlswDirMacEntryType based on Integer32"""
    defaultValue = 2

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
        *(("dynamic", 5),
          ("other", 1),
          ("partnerCapExMsg", 4),
          ("userConfiguredPrivate", 3),
          ("userConfiguredPublic", 2))
    )


_DlswDirMacEntryType_Type.__name__ = "Integer32"
_DlswDirMacEntryType_Object = MibTableColumn
dlswDirMacEntryType = _DlswDirMacEntryType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 4, 2, 1, 1, 4),
    _DlswDirMacEntryType_Type()
)
dlswDirMacEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswDirMacEntryType.setStatus("mandatory")


class _DlswDirMacLocationType_Type(Integer32):
    """Custom type dlswDirMacLocationType based on Integer32"""
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
        *(("local", 2),
          ("other", 1),
          ("remote", 3))
    )


_DlswDirMacLocationType_Type.__name__ = "Integer32"
_DlswDirMacLocationType_Object = MibTableColumn
dlswDirMacLocationType = _DlswDirMacLocationType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 4, 2, 1, 1, 5),
    _DlswDirMacLocationType_Type()
)
dlswDirMacLocationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswDirMacLocationType.setStatus("mandatory")
_DlswDirMacLocation_Type = Instancepointer
_DlswDirMacLocation_Object = MibTableColumn
dlswDirMacLocation = _DlswDirMacLocation_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 4, 2, 1, 1, 6),
    _DlswDirMacLocation_Type()
)
dlswDirMacLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswDirMacLocation.setStatus("mandatory")


class _DlswDirMacStatus_Type(Integer32):
    """Custom type dlswDirMacStatus based on Integer32"""
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
        *(("notReachable", 3),
          ("reachable", 2),
          ("unknown", 1))
    )


_DlswDirMacStatus_Type.__name__ = "Integer32"
_DlswDirMacStatus_Object = MibTableColumn
dlswDirMacStatus = _DlswDirMacStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 4, 2, 1, 1, 7),
    _DlswDirMacStatus_Type()
)
dlswDirMacStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswDirMacStatus.setStatus("mandatory")
_DlswDirMacLFSize_Type = LFSize
_DlswDirMacLFSize_Object = MibTableColumn
dlswDirMacLFSize = _DlswDirMacLFSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 4, 2, 1, 1, 8),
    _DlswDirMacLFSize_Type()
)
dlswDirMacLFSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswDirMacLFSize.setStatus("mandatory")
_DlswDirMacRowStatus_Type = RowStatus
_DlswDirMacRowStatus_Object = MibTableColumn
dlswDirMacRowStatus = _DlswDirMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 4, 2, 1, 1, 9),
    _DlswDirMacRowStatus_Type()
)
dlswDirMacRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswDirMacRowStatus.setStatus("mandatory")
_DlswDirNBTable_Object = MibTable
dlswDirNBTable = _DlswDirNBTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 4, 2, 2)
)
if mibBuilder.loadTexts:
    dlswDirNBTable.setStatus("mandatory")
_DlswDirNBEntry_Object = MibTableRow
dlswDirNBEntry = _DlswDirNBEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 4, 2, 2, 1)
)
dlswDirNBEntry.setIndexNames(
    (0, "A3COM-DLSW-R1-MIB", "dlswDirNBIndex"),
)
if mibBuilder.loadTexts:
    dlswDirNBEntry.setStatus("mandatory")
_DlswDirNBIndex_Type = Integer32
_DlswDirNBIndex_Object = MibTableColumn
dlswDirNBIndex = _DlswDirNBIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 4, 2, 2, 1, 1),
    _DlswDirNBIndex_Type()
)
dlswDirNBIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswDirNBIndex.setStatus("mandatory")
_DlswDirNBName_Type = NBName
_DlswDirNBName_Object = MibTableColumn
dlswDirNBName = _DlswDirNBName_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 4, 2, 2, 1, 2),
    _DlswDirNBName_Type()
)
dlswDirNBName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswDirNBName.setStatus("mandatory")


class _DlswDirNBNameType_Type(Integer32):
    """Custom type dlswDirNBNameType based on Integer32"""
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
        *(("group", 3),
          ("individual", 2),
          ("unknown", 1))
    )


_DlswDirNBNameType_Type.__name__ = "Integer32"
_DlswDirNBNameType_Object = MibTableColumn
dlswDirNBNameType = _DlswDirNBNameType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 4, 2, 2, 1, 3),
    _DlswDirNBNameType_Type()
)
dlswDirNBNameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswDirNBNameType.setStatus("mandatory")


class _DlswDirNBEntryType_Type(Integer32):
    """Custom type dlswDirNBEntryType based on Integer32"""
    defaultValue = 2

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
        *(("dynamic", 5),
          ("other", 1),
          ("partnerCapExMsg", 4),
          ("userConfiguredPrivate", 3),
          ("userConfiguredPublic", 2))
    )


_DlswDirNBEntryType_Type.__name__ = "Integer32"
_DlswDirNBEntryType_Object = MibTableColumn
dlswDirNBEntryType = _DlswDirNBEntryType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 4, 2, 2, 1, 4),
    _DlswDirNBEntryType_Type()
)
dlswDirNBEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswDirNBEntryType.setStatus("mandatory")


class _DlswDirNBLocationType_Type(Integer32):
    """Custom type dlswDirNBLocationType based on Integer32"""
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
        *(("local", 2),
          ("other", 1),
          ("remote", 3))
    )


_DlswDirNBLocationType_Type.__name__ = "Integer32"
_DlswDirNBLocationType_Object = MibTableColumn
dlswDirNBLocationType = _DlswDirNBLocationType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 4, 2, 2, 1, 5),
    _DlswDirNBLocationType_Type()
)
dlswDirNBLocationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswDirNBLocationType.setStatus("mandatory")
_DlswDirNBLocation_Type = Instancepointer
_DlswDirNBLocation_Object = MibTableColumn
dlswDirNBLocation = _DlswDirNBLocation_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 4, 2, 2, 1, 6),
    _DlswDirNBLocation_Type()
)
dlswDirNBLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswDirNBLocation.setStatus("mandatory")


class _DlswDirNBStatus_Type(Integer32):
    """Custom type dlswDirNBStatus based on Integer32"""
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
        *(("notReachable", 3),
          ("reachable", 2),
          ("unknown", 1))
    )


_DlswDirNBStatus_Type.__name__ = "Integer32"
_DlswDirNBStatus_Object = MibTableColumn
dlswDirNBStatus = _DlswDirNBStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 4, 2, 2, 1, 7),
    _DlswDirNBStatus_Type()
)
dlswDirNBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswDirNBStatus.setStatus("mandatory")
_DlswDirNBLFSize_Type = LFSize
_DlswDirNBLFSize_Object = MibTableColumn
dlswDirNBLFSize = _DlswDirNBLFSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 4, 2, 2, 1, 8),
    _DlswDirNBLFSize_Type()
)
dlswDirNBLFSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswDirNBLFSize.setStatus("mandatory")
_DlswDirNBRowStatus_Type = RowStatus
_DlswDirNBRowStatus_Object = MibTableColumn
dlswDirNBRowStatus = _DlswDirNBRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 4, 2, 2, 1, 9),
    _DlswDirNBRowStatus_Type()
)
dlswDirNBRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswDirNBRowStatus.setStatus("mandatory")
_DlswCircuit_ObjectIdentity = ObjectIdentity
dlswCircuit = _DlswCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5)
)
_DlswCircuitStat_ObjectIdentity = ObjectIdentity
dlswCircuitStat = _DlswCircuitStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 1)
)
_DlswActiveCircuits_Type = Gauge32
_DlswActiveCircuits_Object = MibScalar
dlswActiveCircuits = _DlswActiveCircuits_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 1, 1),
    _DlswActiveCircuits_Type()
)
dlswActiveCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswActiveCircuits.setStatus("mandatory")
_DlswCircuitCreates_Type = Counter32
_DlswCircuitCreates_Object = MibScalar
dlswCircuitCreates = _DlswCircuitCreates_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 1, 2),
    _DlswCircuitCreates_Type()
)
dlswCircuitCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitCreates.setStatus("mandatory")
_DlswCircuitTable_Object = MibTable
dlswCircuitTable = _DlswCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2)
)
if mibBuilder.loadTexts:
    dlswCircuitTable.setStatus("mandatory")
_DlswCircuitEntry_Object = MibTableRow
dlswCircuitEntry = _DlswCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1)
)
dlswCircuitEntry.setIndexNames(
    (0, "A3COM-DLSW-R1-MIB", "dlswCircuitS1Mac"),
    (0, "A3COM-DLSW-R1-MIB", "dlswCircuitS1Sap"),
    (0, "A3COM-DLSW-R1-MIB", "dlswCircuitS2Mac"),
    (0, "A3COM-DLSW-R1-MIB", "dlswCircuitS2Sap"),
)
if mibBuilder.loadTexts:
    dlswCircuitEntry.setStatus("mandatory")
_DlswCircuitS1Mac_Type = MacAddress
_DlswCircuitS1Mac_Object = MibTableColumn
dlswCircuitS1Mac = _DlswCircuitS1Mac_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1, 1),
    _DlswCircuitS1Mac_Type()
)
dlswCircuitS1Mac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS1Mac.setStatus("mandatory")


class _DlswCircuitS1Sap_Type(OctetString):
    """Custom type dlswCircuitS1Sap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DlswCircuitS1Sap_Type.__name__ = "OctetString"
_DlswCircuitS1Sap_Object = MibTableColumn
dlswCircuitS1Sap = _DlswCircuitS1Sap_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1, 2),
    _DlswCircuitS1Sap_Type()
)
dlswCircuitS1Sap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS1Sap.setStatus("mandatory")
_DlswCircuitS1IfIndex_Type = Integer32
_DlswCircuitS1IfIndex_Object = MibTableColumn
dlswCircuitS1IfIndex = _DlswCircuitS1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1, 3),
    _DlswCircuitS1IfIndex_Type()
)
dlswCircuitS1IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS1IfIndex.setStatus("mandatory")
_DlswCircuitS1DlcType_Type = DlcType
_DlswCircuitS1DlcType_Object = MibTableColumn
dlswCircuitS1DlcType = _DlswCircuitS1DlcType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1, 4),
    _DlswCircuitS1DlcType_Type()
)
dlswCircuitS1DlcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS1DlcType.setStatus("mandatory")


class _DlswCircuitS1RouteInfo_Type(OctetString):
    """Custom type dlswCircuitS1RouteInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DlswCircuitS1RouteInfo_Type.__name__ = "OctetString"
_DlswCircuitS1RouteInfo_Object = MibTableColumn
dlswCircuitS1RouteInfo = _DlswCircuitS1RouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1, 5),
    _DlswCircuitS1RouteInfo_Type()
)
dlswCircuitS1RouteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS1RouteInfo.setStatus("mandatory")


class _DlswCircuitS1CircuitId_Type(OctetString):
    """Custom type dlswCircuitS1CircuitId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DlswCircuitS1CircuitId_Type.__name__ = "OctetString"
_DlswCircuitS1CircuitId_Object = MibTableColumn
dlswCircuitS1CircuitId = _DlswCircuitS1CircuitId_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1, 6),
    _DlswCircuitS1CircuitId_Type()
)
dlswCircuitS1CircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS1CircuitId.setStatus("mandatory")
_DlswCircuitS1Dlc_Type = Instancepointer
_DlswCircuitS1Dlc_Object = MibTableColumn
dlswCircuitS1Dlc = _DlswCircuitS1Dlc_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1, 7),
    _DlswCircuitS1Dlc_Type()
)
dlswCircuitS1Dlc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS1Dlc.setStatus("mandatory")
_DlswCircuitS2Mac_Type = MacAddress
_DlswCircuitS2Mac_Object = MibTableColumn
dlswCircuitS2Mac = _DlswCircuitS2Mac_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1, 8),
    _DlswCircuitS2Mac_Type()
)
dlswCircuitS2Mac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS2Mac.setStatus("mandatory")


class _DlswCircuitS2Sap_Type(OctetString):
    """Custom type dlswCircuitS2Sap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DlswCircuitS2Sap_Type.__name__ = "OctetString"
_DlswCircuitS2Sap_Object = MibTableColumn
dlswCircuitS2Sap = _DlswCircuitS2Sap_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1, 9),
    _DlswCircuitS2Sap_Type()
)
dlswCircuitS2Sap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS2Sap.setStatus("mandatory")
_DlswCircuitS2Location_Type = EndStationLocation
_DlswCircuitS2Location_Object = MibTableColumn
dlswCircuitS2Location = _DlswCircuitS2Location_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1, 10),
    _DlswCircuitS2Location_Type()
)
dlswCircuitS2Location.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS2Location.setStatus("mandatory")
_DlswCircuitS2TDomain_Type = ObjectIdentifier
_DlswCircuitS2TDomain_Object = MibTableColumn
dlswCircuitS2TDomain = _DlswCircuitS2TDomain_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1, 11),
    _DlswCircuitS2TDomain_Type()
)
dlswCircuitS2TDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS2TDomain.setStatus("mandatory")
_DlswCircuitS2TAddress_Type = TAddress
_DlswCircuitS2TAddress_Object = MibTableColumn
dlswCircuitS2TAddress = _DlswCircuitS2TAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1, 12),
    _DlswCircuitS2TAddress_Type()
)
dlswCircuitS2TAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS2TAddress.setStatus("mandatory")


class _DlswCircuitS2CircuitId_Type(OctetString):
    """Custom type dlswCircuitS2CircuitId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DlswCircuitS2CircuitId_Type.__name__ = "OctetString"
_DlswCircuitS2CircuitId_Object = MibTableColumn
dlswCircuitS2CircuitId = _DlswCircuitS2CircuitId_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1, 13),
    _DlswCircuitS2CircuitId_Type()
)
dlswCircuitS2CircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS2CircuitId.setStatus("mandatory")


class _DlswCircuitOrigin_Type(Integer32):
    """Custom type dlswCircuitOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("s1", 1),
          ("s2", 2))
    )


_DlswCircuitOrigin_Type.__name__ = "Integer32"
_DlswCircuitOrigin_Object = MibTableColumn
dlswCircuitOrigin = _DlswCircuitOrigin_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1, 14),
    _DlswCircuitOrigin_Type()
)
dlswCircuitOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitOrigin.setStatus("mandatory")
_DlswCircuitEntryTime_Type = DlswTimeStamp
_DlswCircuitEntryTime_Object = MibTableColumn
dlswCircuitEntryTime = _DlswCircuitEntryTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1, 15),
    _DlswCircuitEntryTime_Type()
)
dlswCircuitEntryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitEntryTime.setStatus("mandatory")
_DlswCircuitStateTime_Type = DlswTimeStamp
_DlswCircuitStateTime_Object = MibTableColumn
dlswCircuitStateTime = _DlswCircuitStateTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1, 16),
    _DlswCircuitStateTime_Type()
)
dlswCircuitStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitStateTime.setStatus("mandatory")


class _DlswCircuitState_Type(Integer32):
    """Custom type dlswCircuitState based on Integer32"""
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
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("circuitEstablished", 5),
          ("circuitPending", 4),
          ("circuitRestart", 12),
          ("circuitStart", 2),
          ("connectPending", 6),
          ("connected", 8),
          ("contactPending", 7),
          ("disconnectPending", 9),
          ("disconnected", 1),
          ("haltPending", 10),
          ("haltPendingNoack", 11),
          ("resolvePending", 3),
          ("restartPending", 13))
    )


_DlswCircuitState_Type.__name__ = "Integer32"
_DlswCircuitState_Object = MibTableColumn
dlswCircuitState = _DlswCircuitState_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1, 17),
    _DlswCircuitState_Type()
)
dlswCircuitState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswCircuitState.setStatus("mandatory")


class _DlswCircuitPriority_Type(Integer32):
    """Custom type dlswCircuitPriority based on Integer32"""
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
        *(("high", 3),
          ("highest", 4),
          ("low", 1),
          ("medium", 2),
          ("unsupported", 0))
    )


_DlswCircuitPriority_Type.__name__ = "Integer32"
_DlswCircuitPriority_Object = MibTableColumn
dlswCircuitPriority = _DlswCircuitPriority_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1, 18),
    _DlswCircuitPriority_Type()
)
dlswCircuitPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitPriority.setStatus("mandatory")


class _DlswCircuitFCSendGrantedUnits_Type(Integer32):
    """Custom type dlswCircuitFCSendGrantedUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DlswCircuitFCSendGrantedUnits_Type.__name__ = "Integer32"
_DlswCircuitFCSendGrantedUnits_Object = MibTableColumn
dlswCircuitFCSendGrantedUnits = _DlswCircuitFCSendGrantedUnits_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1, 19),
    _DlswCircuitFCSendGrantedUnits_Type()
)
dlswCircuitFCSendGrantedUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitFCSendGrantedUnits.setStatus("mandatory")


class _DlswCircuitFCSendCurrentWndw_Type(Integer32):
    """Custom type dlswCircuitFCSendCurrentWndw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DlswCircuitFCSendCurrentWndw_Type.__name__ = "Integer32"
_DlswCircuitFCSendCurrentWndw_Object = MibTableColumn
dlswCircuitFCSendCurrentWndw = _DlswCircuitFCSendCurrentWndw_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1, 20),
    _DlswCircuitFCSendCurrentWndw_Type()
)
dlswCircuitFCSendCurrentWndw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitFCSendCurrentWndw.setStatus("mandatory")


class _DlswCircuitFCRecvGrantedUnits_Type(Integer32):
    """Custom type dlswCircuitFCRecvGrantedUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DlswCircuitFCRecvGrantedUnits_Type.__name__ = "Integer32"
_DlswCircuitFCRecvGrantedUnits_Object = MibTableColumn
dlswCircuitFCRecvGrantedUnits = _DlswCircuitFCRecvGrantedUnits_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1, 21),
    _DlswCircuitFCRecvGrantedUnits_Type()
)
dlswCircuitFCRecvGrantedUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitFCRecvGrantedUnits.setStatus("mandatory")


class _DlswCircuitFCRecvCurrentWndw_Type(Integer32):
    """Custom type dlswCircuitFCRecvCurrentWndw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DlswCircuitFCRecvCurrentWndw_Type.__name__ = "Integer32"
_DlswCircuitFCRecvCurrentWndw_Object = MibTableColumn
dlswCircuitFCRecvCurrentWndw = _DlswCircuitFCRecvCurrentWndw_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1, 22),
    _DlswCircuitFCRecvCurrentWndw_Type()
)
dlswCircuitFCRecvCurrentWndw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitFCRecvCurrentWndw.setStatus("mandatory")
_DlswCircuitFCLargestRecvGranted_Type = Gauge32
_DlswCircuitFCLargestRecvGranted_Object = MibTableColumn
dlswCircuitFCLargestRecvGranted = _DlswCircuitFCLargestRecvGranted_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1, 23),
    _DlswCircuitFCLargestRecvGranted_Type()
)
dlswCircuitFCLargestRecvGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitFCLargestRecvGranted.setStatus("mandatory")
_DlswCircuitFCLargestSendGranted_Type = Gauge32
_DlswCircuitFCLargestSendGranted_Object = MibTableColumn
dlswCircuitFCLargestSendGranted = _DlswCircuitFCLargestSendGranted_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1, 24),
    _DlswCircuitFCLargestSendGranted_Type()
)
dlswCircuitFCLargestSendGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitFCLargestSendGranted.setStatus("mandatory")
_DlswCircuitFCHalveWndwSents_Type = Counter32
_DlswCircuitFCHalveWndwSents_Object = MibTableColumn
dlswCircuitFCHalveWndwSents = _DlswCircuitFCHalveWndwSents_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1, 25),
    _DlswCircuitFCHalveWndwSents_Type()
)
dlswCircuitFCHalveWndwSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitFCHalveWndwSents.setStatus("mandatory")
_DlswCircuitFCResetOpSents_Type = Counter32
_DlswCircuitFCResetOpSents_Object = MibTableColumn
dlswCircuitFCResetOpSents = _DlswCircuitFCResetOpSents_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1, 26),
    _DlswCircuitFCResetOpSents_Type()
)
dlswCircuitFCResetOpSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitFCResetOpSents.setStatus("mandatory")
_DlswCircuitFCHalveWndwRcvds_Type = Counter32
_DlswCircuitFCHalveWndwRcvds_Object = MibTableColumn
dlswCircuitFCHalveWndwRcvds = _DlswCircuitFCHalveWndwRcvds_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1, 27),
    _DlswCircuitFCHalveWndwRcvds_Type()
)
dlswCircuitFCHalveWndwRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitFCHalveWndwRcvds.setStatus("mandatory")
_DlswCircuitFCResetOpRcvds_Type = Counter32
_DlswCircuitFCResetOpRcvds_Object = MibTableColumn
dlswCircuitFCResetOpRcvds = _DlswCircuitFCResetOpRcvds_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1, 28),
    _DlswCircuitFCResetOpRcvds_Type()
)
dlswCircuitFCResetOpRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitFCResetOpRcvds.setStatus("mandatory")


class _DlswCircuitDiscReasonLocal_Type(Integer32):
    """Custom type dlswCircuitDiscReasonLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("endStationDiscRcvd", 1),
          ("endStationDlcError", 2),
          ("haltDlNoAckRcvd", 6),
          ("haltDlRcvd", 5),
          ("operatorCommand", 4),
          ("protocolError", 3),
          ("transportConnClosed", 7))
    )


_DlswCircuitDiscReasonLocal_Type.__name__ = "Integer32"
_DlswCircuitDiscReasonLocal_Object = MibTableColumn
dlswCircuitDiscReasonLocal = _DlswCircuitDiscReasonLocal_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1, 29),
    _DlswCircuitDiscReasonLocal_Type()
)
dlswCircuitDiscReasonLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitDiscReasonLocal.setStatus("mandatory")


class _DlswCircuitDiscReasonRemote_Type(Integer32):
    """Custom type dlswCircuitDiscReasonRemote based on Integer32"""
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
        *(("endStationDiscRcvd", 1),
          ("endStationDlcError", 2),
          ("operatorCommand", 4),
          ("protocolError", 3),
          ("unknown", 0))
    )


_DlswCircuitDiscReasonRemote_Type.__name__ = "Integer32"
_DlswCircuitDiscReasonRemote_Object = MibTableColumn
dlswCircuitDiscReasonRemote = _DlswCircuitDiscReasonRemote_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1, 30),
    _DlswCircuitDiscReasonRemote_Type()
)
dlswCircuitDiscReasonRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitDiscReasonRemote.setStatus("mandatory")


class _DlswCircuitDiscReasonRemoteData_Type(OctetString):
    """Custom type dlswCircuitDiscReasonRemoteData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_DlswCircuitDiscReasonRemoteData_Type.__name__ = "OctetString"
_DlswCircuitDiscReasonRemoteData_Object = MibTableColumn
dlswCircuitDiscReasonRemoteData = _DlswCircuitDiscReasonRemoteData_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 5, 2, 1, 31),
    _DlswCircuitDiscReasonRemoteData_Type()
)
dlswCircuitDiscReasonRemoteData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitDiscReasonRemoteData.setStatus("mandatory")
_DlswSdlc_ObjectIdentity = ObjectIdentity
dlswSdlc = _DlswSdlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 6)
)
_DlswTraps_ObjectIdentity = ObjectIdentity
dlswTraps = _DlswTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 7)
)

# Managed Objects groups


# Notification objects

dlswTrapTConnUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 0, 1)
)
dlswTrapTConnUp.setObjects(
      *(("A3COM-DLSW-R1-MIB", "dlswTConnOperTDomain"),
        ("A3COM-DLSW-R1-MIB", "dlswTConnOperRemoteTAddr"))
)
if mibBuilder.loadTexts:
    dlswTrapTConnUp.setStatus(
        ""
    )

dlswTrapTConnDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 0, 2)
)
dlswTrapTConnDown.setObjects(
      *(("A3COM-DLSW-R1-MIB", "dlswTConnOperTDomain"),
        ("A3COM-DLSW-R1-MIB", "dlswTConnOperRemoteTAddr"))
)
if mibBuilder.loadTexts:
    dlswTrapTConnDown.setStatus(
        ""
    )

dlswTrapCircuitUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 0, 3)
)
dlswTrapCircuitUp.setObjects(
      *(("A3COM-DLSW-R1-MIB", "dlswCircuitS1Mac"),
        ("A3COM-DLSW-R1-MIB", "dlswCircuitS1Sap"),
        ("A3COM-DLSW-R1-MIB", "dlswCircuitS2Mac"),
        ("A3COM-DLSW-R1-MIB", "dlswCircuitS2Sap"))
)
if mibBuilder.loadTexts:
    dlswTrapCircuitUp.setStatus(
        ""
    )

dlswTrapCircuitDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 2, 24, 0, 4)
)
dlswTrapCircuitDown.setObjects(
      *(("A3COM-DLSW-R1-MIB", "dlswCircuitS1Mac"),
        ("A3COM-DLSW-R1-MIB", "dlswCircuitS1Sap"),
        ("A3COM-DLSW-R1-MIB", "dlswCircuitS2Mac"),
        ("A3COM-DLSW-R1-MIB", "dlswCircuitS2Sap"))
)
if mibBuilder.loadTexts:
    dlswTrapCircuitDown.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-DLSW-R1-MIB",
    **{"NBName": NBName,
       "MacAddress": MacAddress,
       "TAddress": TAddress,
       "DlswTimeStamp": DlswTimeStamp,
       "EndStationLocation": EndStationLocation,
       "DlcType": DlcType,
       "LFSize": LFSize,
       "Truthvalue": Truthvalue,
       "RowStatus": RowStatus,
       "Instancepointer": Instancepointer,
       "a3Com": a3Com,
       "brouterMIB": brouterMIB,
       "dlswMIB-3Com": dlswMIB_3Com,
       "dlswTrapTConnUp": dlswTrapTConnUp,
       "dlswTrapTConnDown": dlswTrapTConnDown,
       "dlswTrapCircuitUp": dlswTrapCircuitUp,
       "dlswTrapCircuitDown": dlswTrapCircuitDown,
       "dlswNode": dlswNode,
       "dlswVersion": dlswVersion,
       "dlswVendorID": dlswVendorID,
       "dlswVersionString": dlswVersionString,
       "dlswStdPacingSupport": dlswStdPacingSupport,
       "dlswStatus": dlswStatus,
       "dlswUpTime": dlswUpTime,
       "dlswVirtualSegmentLFSize": dlswVirtualSegmentLFSize,
       "dlswResourceNBExclusivity": dlswResourceNBExclusivity,
       "dlswResourceMacExclusivity": dlswResourceMacExclusivity,
       "dlswTrapControl": dlswTrapControl,
       "dlswTrapCntlTConn": dlswTrapCntlTConn,
       "dlswTrapCntlCircuit": dlswTrapCntlCircuit,
       "dlswTConn": dlswTConn,
       "dlswTConnStat": dlswTConnStat,
       "dlswTConnStatActiveConnections": dlswTConnStatActiveConnections,
       "dlswTConnStatCloseIdles": dlswTConnStatCloseIdles,
       "dlswTConnStatCloseBusys": dlswTConnStatCloseBusys,
       "dlswTConnConfigTable": dlswTConnConfigTable,
       "dlswTConnConfigEntry": dlswTConnConfigEntry,
       "dlswTConnConfigIndex": dlswTConnConfigIndex,
       "dlswTConnConfigTDomain": dlswTConnConfigTDomain,
       "dlswTConnConfigLocalTAddr": dlswTConnConfigLocalTAddr,
       "dlswTConnConfigRemoteTAddr": dlswTConnConfigRemoteTAddr,
       "dlswTConnConfigLastModifyTime": dlswTConnConfigLastModifyTime,
       "dlswTConnConfigEntryType": dlswTConnConfigEntryType,
       "dlswTConnConfigGroupDefinition": dlswTConnConfigGroupDefinition,
       "dlswTConnConfigSetupType": dlswTConnConfigSetupType,
       "dlswTConnConfigSapList": dlswTConnConfigSapList,
       "dlswTConnConfigAdvertiseMacNB": dlswTConnConfigAdvertiseMacNB,
       "dlswTConnConfigInitCirRecvWndw": dlswTConnConfigInitCirRecvWndw,
       "dlswTConnConfigOpens": dlswTConnConfigOpens,
       "dlswTConnConfigRowStatus": dlswTConnConfigRowStatus,
       "dlswTConnOperTable": dlswTConnOperTable,
       "dlswTConnOperEntry": dlswTConnOperEntry,
       "dlswTConnOperTDomain": dlswTConnOperTDomain,
       "dlswTConnOperLocalTAddr": dlswTConnOperLocalTAddr,
       "dlswTConnOperRemoteTAddr": dlswTConnOperRemoteTAddr,
       "dlswTConnOperEntryTime": dlswTConnOperEntryTime,
       "dlswTConnOperConnectTime": dlswTConnOperConnectTime,
       "dlswTConnOperState": dlswTConnOperState,
       "dlswTConnOperConfigIndex": dlswTConnOperConfigIndex,
       "dlswTConnOperFlowCntlMode": dlswTConnOperFlowCntlMode,
       "dlswTConnOperPartnerVersion": dlswTConnOperPartnerVersion,
       "dlswTConnOperPartnerVendorID": dlswTConnOperPartnerVendorID,
       "dlswTConnOperPartnerVersionStr": dlswTConnOperPartnerVersionStr,
       "dlswTConnOperPartnerInitPacingWndw": dlswTConnOperPartnerInitPacingWndw,
       "dlswTConnOperPartnerSapList": dlswTConnOperPartnerSapList,
       "dlswTConnOperPartnerNBExcl": dlswTConnOperPartnerNBExcl,
       "dlswTConnOperPartnerMacExcl": dlswTConnOperPartnerMacExcl,
       "dlswTConnOperPartnerNBInfo": dlswTConnOperPartnerNBInfo,
       "dlswTConnOperPartnerMacInfo": dlswTConnOperPartnerMacInfo,
       "dlswTConnOperDiscTime": dlswTConnOperDiscTime,
       "dlswTConnOperDiscReason": dlswTConnOperDiscReason,
       "dlswTConnOperDiscActiveCir": dlswTConnOperDiscActiveCir,
       "dlswTConnOperInDataPkts": dlswTConnOperInDataPkts,
       "dlswTConnOperOutDataPkts": dlswTConnOperOutDataPkts,
       "dlswTConnOperInDataOctets": dlswTConnOperInDataOctets,
       "dlswTConnOperOutDataOctets": dlswTConnOperOutDataOctets,
       "dlswTConnOperInCntlPkts": dlswTConnOperInCntlPkts,
       "dlswTConnOperOutCntlPkts": dlswTConnOperOutCntlPkts,
       "dlswTConnOperCURexSents": dlswTConnOperCURexSents,
       "dlswTConnOperICRexRcvds": dlswTConnOperICRexRcvds,
       "dlswTConnOperCURexRcvds": dlswTConnOperCURexRcvds,
       "dlswTConnOperICRexSents": dlswTConnOperICRexSents,
       "dlswTConnOperNQexSents": dlswTConnOperNQexSents,
       "dlswTConnOperNRexRcvds": dlswTConnOperNRexRcvds,
       "dlswTConnOperNQexRcvds": dlswTConnOperNQexRcvds,
       "dlswTConnOperNRexSents": dlswTConnOperNRexSents,
       "dlswTConnOperCirCreates": dlswTConnOperCirCreates,
       "dlswTConnOperCircuits": dlswTConnOperCircuits,
       "dlswInterface": dlswInterface,
       "dlswDirectory": dlswDirectory,
       "dlswDirStat": dlswDirStat,
       "dlswDirMacEntries": dlswDirMacEntries,
       "dlswDirNBEntries": dlswDirNBEntries,
       "dlswDirCache": dlswDirCache,
       "dlswDirMacTable": dlswDirMacTable,
       "dlswDirMacEntry": dlswDirMacEntry,
       "dlswDirMacIndex": dlswDirMacIndex,
       "dlswDirMacMac": dlswDirMacMac,
       "dlswDirMacMask": dlswDirMacMask,
       "dlswDirMacEntryType": dlswDirMacEntryType,
       "dlswDirMacLocationType": dlswDirMacLocationType,
       "dlswDirMacLocation": dlswDirMacLocation,
       "dlswDirMacStatus": dlswDirMacStatus,
       "dlswDirMacLFSize": dlswDirMacLFSize,
       "dlswDirMacRowStatus": dlswDirMacRowStatus,
       "dlswDirNBTable": dlswDirNBTable,
       "dlswDirNBEntry": dlswDirNBEntry,
       "dlswDirNBIndex": dlswDirNBIndex,
       "dlswDirNBName": dlswDirNBName,
       "dlswDirNBNameType": dlswDirNBNameType,
       "dlswDirNBEntryType": dlswDirNBEntryType,
       "dlswDirNBLocationType": dlswDirNBLocationType,
       "dlswDirNBLocation": dlswDirNBLocation,
       "dlswDirNBStatus": dlswDirNBStatus,
       "dlswDirNBLFSize": dlswDirNBLFSize,
       "dlswDirNBRowStatus": dlswDirNBRowStatus,
       "dlswCircuit": dlswCircuit,
       "dlswCircuitStat": dlswCircuitStat,
       "dlswActiveCircuits": dlswActiveCircuits,
       "dlswCircuitCreates": dlswCircuitCreates,
       "dlswCircuitTable": dlswCircuitTable,
       "dlswCircuitEntry": dlswCircuitEntry,
       "dlswCircuitS1Mac": dlswCircuitS1Mac,
       "dlswCircuitS1Sap": dlswCircuitS1Sap,
       "dlswCircuitS1IfIndex": dlswCircuitS1IfIndex,
       "dlswCircuitS1DlcType": dlswCircuitS1DlcType,
       "dlswCircuitS1RouteInfo": dlswCircuitS1RouteInfo,
       "dlswCircuitS1CircuitId": dlswCircuitS1CircuitId,
       "dlswCircuitS1Dlc": dlswCircuitS1Dlc,
       "dlswCircuitS2Mac": dlswCircuitS2Mac,
       "dlswCircuitS2Sap": dlswCircuitS2Sap,
       "dlswCircuitS2Location": dlswCircuitS2Location,
       "dlswCircuitS2TDomain": dlswCircuitS2TDomain,
       "dlswCircuitS2TAddress": dlswCircuitS2TAddress,
       "dlswCircuitS2CircuitId": dlswCircuitS2CircuitId,
       "dlswCircuitOrigin": dlswCircuitOrigin,
       "dlswCircuitEntryTime": dlswCircuitEntryTime,
       "dlswCircuitStateTime": dlswCircuitStateTime,
       "dlswCircuitState": dlswCircuitState,
       "dlswCircuitPriority": dlswCircuitPriority,
       "dlswCircuitFCSendGrantedUnits": dlswCircuitFCSendGrantedUnits,
       "dlswCircuitFCSendCurrentWndw": dlswCircuitFCSendCurrentWndw,
       "dlswCircuitFCRecvGrantedUnits": dlswCircuitFCRecvGrantedUnits,
       "dlswCircuitFCRecvCurrentWndw": dlswCircuitFCRecvCurrentWndw,
       "dlswCircuitFCLargestRecvGranted": dlswCircuitFCLargestRecvGranted,
       "dlswCircuitFCLargestSendGranted": dlswCircuitFCLargestSendGranted,
       "dlswCircuitFCHalveWndwSents": dlswCircuitFCHalveWndwSents,
       "dlswCircuitFCResetOpSents": dlswCircuitFCResetOpSents,
       "dlswCircuitFCHalveWndwRcvds": dlswCircuitFCHalveWndwRcvds,
       "dlswCircuitFCResetOpRcvds": dlswCircuitFCResetOpRcvds,
       "dlswCircuitDiscReasonLocal": dlswCircuitDiscReasonLocal,
       "dlswCircuitDiscReasonRemote": dlswCircuitDiscReasonRemote,
       "dlswCircuitDiscReasonRemoteData": dlswCircuitDiscReasonRemoteData,
       "dlswSdlc": dlswSdlc,
       "dlswTraps": dlswTraps}
)
