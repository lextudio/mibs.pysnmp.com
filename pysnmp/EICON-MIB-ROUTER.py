# SNMP MIB module (EICON-MIB-ROUTER) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EICON-MIB-ROUTER
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:46 2024
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



class OperState(Integer32):
    """Custom type OperState based on Integer32"""
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
        *(("active", 4),
          ("busy", 5),
          ("disabled", 2),
          ("other", 1),
          ("ready", 3))
    )





class AdminState(Integer32):
    """Custom type AdminState based on Integer32"""
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
        *(("dump", 3),
          ("invalid", 5),
          ("start", 1),
          ("stop", 2),
          ("test", 4))
    )





class ActionState(Integer32):
    """Custom type ActionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("done", 1),
          ("failed", 2),
          ("in-progress", 3))
    )





class EntryStatus(Integer32):
    """Custom type EntryStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )





class EntryStatusV2(Integer32):
    """Custom type EntryStatusV2 based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("modifyRequest", 5),
          ("underCreation", 3),
          ("underModification", 6),
          ("valid", 1))
    )





class ConnectionStatus(Integer32):
    """Custom type ConnectionStatus based on Integer32"""
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
        *(("calling", 3),
          ("connected", 4),
          ("hangingup", 5),
          ("hungup", 6),
          ("invalid", 1),
          ("listening", 2),
          ("pending-hungup", 7))
    )





class ControlOnOff(Integer32):
    """Custom type ControlOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 3),
          ("start", 2),
          ("stop", 1))
    )





class CardRef(Integer32):
    """Custom type CardRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )





class PortRef(Integer32):
    """Custom type PortRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )





class PositiveInteger(Integer32):
    """Custom type PositiveInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Eicon_ObjectIdentity = ObjectIdentity
eicon = _Eicon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434)
)
_Management_ObjectIdentity = ObjectIdentity
management = _Management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2)
)
_Mibv2_ObjectIdentity = ObjectIdentity
mibv2 = _Mibv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2, 2)
)
_Module_ObjectIdentity = ObjectIdentity
module = _Module_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4)
)
_Router_ObjectIdentity = ObjectIdentity
router = _Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8)
)


class _RtName_Type(DisplayString):
    """Custom type rtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_RtName_Type.__name__ = "DisplayString"
_RtName_Object = MibScalar
rtName = _RtName_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 1),
    _RtName_Type()
)
rtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtName.setStatus("mandatory")


class _RtProductName_Type(DisplayString):
    """Custom type rtProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_RtProductName_Type.__name__ = "DisplayString"
_RtProductName_Object = MibScalar
rtProductName = _RtProductName_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 2),
    _RtProductName_Type()
)
rtProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtProductName.setStatus("mandatory")
_RtReleaseVersion_Type = Integer32
_RtReleaseVersion_Object = MibScalar
rtReleaseVersion = _RtReleaseVersion_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 3),
    _RtReleaseVersion_Type()
)
rtReleaseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtReleaseVersion.setStatus("mandatory")
_RtReleaseDate_Type = Integer32
_RtReleaseDate_Object = MibScalar
rtReleaseDate = _RtReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 4),
    _RtReleaseDate_Type()
)
rtReleaseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtReleaseDate.setStatus("mandatory")
_RtOperState_Type = OperState
_RtOperState_Object = MibScalar
rtOperState = _RtOperState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 5),
    _RtOperState_Type()
)
rtOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtOperState.setStatus("mandatory")
_RtAdminStateCtr_Type = AdminState
_RtAdminStateCtr_Object = MibScalar
rtAdminStateCtr = _RtAdminStateCtr_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 6),
    _RtAdminStateCtr_Type()
)
rtAdminStateCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtAdminStateCtr.setStatus("mandatory")


class _RtType_Type(Integer32):
    """Custom type rtType based on Integer32"""
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
        *(("typeMadrasRouter", 6),
          ("typeNTRouter", 4),
          ("typeNetWareRouter", 1),
          ("typeOS2Router", 2),
          ("typeSynOpticsRouter", 5),
          ("typeUnixRouter", 3))
    )


_RtType_Type.__name__ = "Integer32"
_RtType_Object = MibScalar
rtType = _RtType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 7),
    _RtType_Type()
)
rtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtType.setStatus("mandatory")
_RtTimeUp_Type = TimeTicks
_RtTimeUp_Object = MibScalar
rtTimeUp = _RtTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 8),
    _RtTimeUp_Type()
)
rtTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtTimeUp.setStatus("mandatory")
_RtNumberOfPorts_Type = Integer32
_RtNumberOfPorts_Object = MibScalar
rtNumberOfPorts = _RtNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 9),
    _RtNumberOfPorts_Type()
)
rtNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtNumberOfPorts.setStatus("mandatory")
_RtMaxCircuits_Type = Integer32
_RtMaxCircuits_Object = MibScalar
rtMaxCircuits = _RtMaxCircuits_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 10),
    _RtMaxCircuits_Type()
)
rtMaxCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtMaxCircuits.setStatus("mandatory")
_RtAvailableCircuits_Type = Gauge32
_RtAvailableCircuits_Object = MibScalar
rtAvailableCircuits = _RtAvailableCircuits_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 11),
    _RtAvailableCircuits_Type()
)
rtAvailableCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtAvailableCircuits.setStatus("mandatory")
_RtAvailableLANMapping_Type = Gauge32
_RtAvailableLANMapping_Object = MibScalar
rtAvailableLANMapping = _RtAvailableLANMapping_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 12),
    _RtAvailableLANMapping_Type()
)
rtAvailableLANMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtAvailableLANMapping.setStatus("mandatory")
_RtMaxLANMapping_Type = Integer32
_RtMaxLANMapping_Object = MibScalar
rtMaxLANMapping = _RtMaxLANMapping_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 13),
    _RtMaxLANMapping_Type()
)
rtMaxLANMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtMaxLANMapping.setStatus("mandatory")
_RtGlobalTxPackets_Type = Counter32
_RtGlobalTxPackets_Object = MibScalar
rtGlobalTxPackets = _RtGlobalTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 14),
    _RtGlobalTxPackets_Type()
)
rtGlobalTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtGlobalTxPackets.setStatus("mandatory")
_RtGlobalTxBytesLow_Type = Counter32
_RtGlobalTxBytesLow_Object = MibScalar
rtGlobalTxBytesLow = _RtGlobalTxBytesLow_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 15),
    _RtGlobalTxBytesLow_Type()
)
rtGlobalTxBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtGlobalTxBytesLow.setStatus("mandatory")
_RtGlobalTxBytesHigh_Type = Counter32
_RtGlobalTxBytesHigh_Object = MibScalar
rtGlobalTxBytesHigh = _RtGlobalTxBytesHigh_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 16),
    _RtGlobalTxBytesHigh_Type()
)
rtGlobalTxBytesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtGlobalTxBytesHigh.setStatus("mandatory")
_RtGlobalRxPackets_Type = Counter32
_RtGlobalRxPackets_Object = MibScalar
rtGlobalRxPackets = _RtGlobalRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 17),
    _RtGlobalRxPackets_Type()
)
rtGlobalRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtGlobalRxPackets.setStatus("mandatory")
_RtGlobalRxBytesLow_Type = Counter32
_RtGlobalRxBytesLow_Object = MibScalar
rtGlobalRxBytesLow = _RtGlobalRxBytesLow_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 18),
    _RtGlobalRxBytesLow_Type()
)
rtGlobalRxBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtGlobalRxBytesLow.setStatus("mandatory")
_RtGlobalRxBytesHigh_Type = Counter32
_RtGlobalRxBytesHigh_Object = MibScalar
rtGlobalRxBytesHigh = _RtGlobalRxBytesHigh_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 19),
    _RtGlobalRxBytesHigh_Type()
)
rtGlobalRxBytesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtGlobalRxBytesHigh.setStatus("mandatory")
_RtGlobalTxDropNoRoute_Type = Counter32
_RtGlobalTxDropNoRoute_Object = MibScalar
rtGlobalTxDropNoRoute = _RtGlobalTxDropNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 20),
    _RtGlobalTxDropNoRoute_Type()
)
rtGlobalTxDropNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtGlobalTxDropNoRoute.setStatus("mandatory")
_RtGlobalTxDropNoResource_Type = Counter32
_RtGlobalTxDropNoResource_Object = MibScalar
rtGlobalTxDropNoResource = _RtGlobalTxDropNoResource_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 21),
    _RtGlobalTxDropNoResource_Type()
)
rtGlobalTxDropNoResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtGlobalTxDropNoResource.setStatus("mandatory")
_RtGlobalTxDropUnknownProt_Type = Counter32
_RtGlobalTxDropUnknownProt_Object = MibScalar
rtGlobalTxDropUnknownProt = _RtGlobalTxDropUnknownProt_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 22),
    _RtGlobalTxDropUnknownProt_Type()
)
rtGlobalTxDropUnknownProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtGlobalTxDropUnknownProt.setStatus("mandatory")
_RtGlobalRxDropNoResource_Type = Counter32
_RtGlobalRxDropNoResource_Object = MibScalar
rtGlobalRxDropNoResource = _RtGlobalRxDropNoResource_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 23),
    _RtGlobalRxDropNoResource_Type()
)
rtGlobalRxDropNoResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtGlobalRxDropNoResource.setStatus("mandatory")
_RtGlobalRxDropUnknownProt_Type = Counter32
_RtGlobalRxDropUnknownProt_Object = MibScalar
rtGlobalRxDropUnknownProt = _RtGlobalRxDropUnknownProt_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 24),
    _RtGlobalRxDropUnknownProt_Type()
)
rtGlobalRxDropUnknownProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtGlobalRxDropUnknownProt.setStatus("mandatory")
_RtGlobalRxError_Type = Counter32
_RtGlobalRxError_Object = MibScalar
rtGlobalRxError = _RtGlobalRxError_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 25),
    _RtGlobalRxError_Type()
)
rtGlobalRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtGlobalRxError.setStatus("mandatory")
_RtGlobalCountersReset_Type = ControlOnOff
_RtGlobalCountersReset_Object = MibScalar
rtGlobalCountersReset = _RtGlobalCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 26),
    _RtGlobalCountersReset_Type()
)
rtGlobalCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtGlobalCountersReset.setStatus("mandatory")
_RtTraceCtrl_Type = ControlOnOff
_RtTraceCtrl_Object = MibScalar
rtTraceCtrl = _RtTraceCtrl_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 27),
    _RtTraceCtrl_Type()
)
rtTraceCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtTraceCtrl.setStatus("mandatory")


class _RtTraceFileName_Type(DisplayString):
    """Custom type rtTraceFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_RtTraceFileName_Type.__name__ = "DisplayString"
_RtTraceFileName_Object = MibScalar
rtTraceFileName = _RtTraceFileName_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 28),
    _RtTraceFileName_Type()
)
rtTraceFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtTraceFileName.setStatus("mandatory")
_RtTraceInterfaceType_Type = Integer32
_RtTraceInterfaceType_Object = MibScalar
rtTraceInterfaceType = _RtTraceInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 29),
    _RtTraceInterfaceType_Type()
)
rtTraceInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtTraceInterfaceType.setStatus("mandatory")
_RtPortTable_Object = MibTable
rtPortTable = _RtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 30)
)
if mibBuilder.loadTexts:
    rtPortTable.setStatus("mandatory")
_RtPortEntry_Object = MibTableRow
rtPortEntry = _RtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 30, 1)
)
rtPortEntry.setIndexNames(
    (0, "EICON-MIB-ROUTER", "rtPortIndex"),
)
if mibBuilder.loadTexts:
    rtPortEntry.setStatus("mandatory")


class _RtPortIndex_Type(Integer32):
    """Custom type rtPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_RtPortIndex_Type.__name__ = "Integer32"
_RtPortIndex_Object = MibTableColumn
rtPortIndex = _RtPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 30, 1, 1),
    _RtPortIndex_Type()
)
rtPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtPortIndex.setStatus("mandatory")


class _RtPortNumber_Type(Integer32):
    """Custom type rtPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_RtPortNumber_Type.__name__ = "Integer32"
_RtPortNumber_Object = MibTableColumn
rtPortNumber = _RtPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 30, 1, 2),
    _RtPortNumber_Type()
)
rtPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtPortNumber.setStatus("mandatory")
_RtPortProtocol_Type = Integer32
_RtPortProtocol_Object = MibTableColumn
rtPortProtocol = _RtPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 30, 1, 3),
    _RtPortProtocol_Type()
)
rtPortProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtPortProtocol.setStatus("mandatory")
_RtPortTxThroughput_Type = Gauge32
_RtPortTxThroughput_Object = MibTableColumn
rtPortTxThroughput = _RtPortTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 30, 1, 4),
    _RtPortTxThroughput_Type()
)
rtPortTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtPortTxThroughput.setStatus("mandatory")
_RtPortRxThroughput_Type = Gauge32
_RtPortRxThroughput_Object = MibTableColumn
rtPortRxThroughput = _RtPortRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 30, 1, 5),
    _RtPortRxThroughput_Type()
)
rtPortRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtPortRxThroughput.setStatus("mandatory")
_RtPortTxPackets_Type = Counter32
_RtPortTxPackets_Object = MibTableColumn
rtPortTxPackets = _RtPortTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 30, 1, 6),
    _RtPortTxPackets_Type()
)
rtPortTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtPortTxPackets.setStatus("mandatory")
_RtPortTxBytesLow_Type = Counter32
_RtPortTxBytesLow_Object = MibTableColumn
rtPortTxBytesLow = _RtPortTxBytesLow_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 30, 1, 7),
    _RtPortTxBytesLow_Type()
)
rtPortTxBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtPortTxBytesLow.setStatus("mandatory")
_RtPortTxBytesHigh_Type = Counter32
_RtPortTxBytesHigh_Object = MibTableColumn
rtPortTxBytesHigh = _RtPortTxBytesHigh_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 30, 1, 8),
    _RtPortTxBytesHigh_Type()
)
rtPortTxBytesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtPortTxBytesHigh.setStatus("mandatory")
_RtPortRxPackets_Type = Counter32
_RtPortRxPackets_Object = MibTableColumn
rtPortRxPackets = _RtPortRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 30, 1, 9),
    _RtPortRxPackets_Type()
)
rtPortRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtPortRxPackets.setStatus("mandatory")
_RtPortRxBytesLow_Type = Counter32
_RtPortRxBytesLow_Object = MibTableColumn
rtPortRxBytesLow = _RtPortRxBytesLow_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 30, 1, 10),
    _RtPortRxBytesLow_Type()
)
rtPortRxBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtPortRxBytesLow.setStatus("mandatory")
_RtPortRxBytesHigh_Type = Counter32
_RtPortRxBytesHigh_Object = MibTableColumn
rtPortRxBytesHigh = _RtPortRxBytesHigh_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 30, 1, 11),
    _RtPortRxBytesHigh_Type()
)
rtPortRxBytesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtPortRxBytesHigh.setStatus("mandatory")
_RtPortTxDropNoResource_Type = Counter32
_RtPortTxDropNoResource_Object = MibTableColumn
rtPortTxDropNoResource = _RtPortTxDropNoResource_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 30, 1, 12),
    _RtPortTxDropNoResource_Type()
)
rtPortTxDropNoResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtPortTxDropNoResource.setStatus("mandatory")
_RtPortRxError_Type = Counter32
_RtPortRxError_Object = MibTableColumn
rtPortRxError = _RtPortRxError_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 30, 1, 13),
    _RtPortRxError_Type()
)
rtPortRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtPortRxError.setStatus("mandatory")
_RtPortCountersReset_Type = ControlOnOff
_RtPortCountersReset_Object = MibTableColumn
rtPortCountersReset = _RtPortCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 30, 1, 14),
    _RtPortCountersReset_Type()
)
rtPortCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtPortCountersReset.setStatus("mandatory")
_RtConnFreeIndex_Type = Integer32
_RtConnFreeIndex_Object = MibScalar
rtConnFreeIndex = _RtConnFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 31),
    _RtConnFreeIndex_Type()
)
rtConnFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtConnFreeIndex.setStatus("mandatory")
_RtConnTable_Object = MibTable
rtConnTable = _RtConnTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32)
)
if mibBuilder.loadTexts:
    rtConnTable.setStatus("mandatory")
_RtConnEntry_Object = MibTableRow
rtConnEntry = _RtConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1)
)
rtConnEntry.setIndexNames(
    (0, "EICON-MIB-ROUTER", "rtConnIndex"),
)
if mibBuilder.loadTexts:
    rtConnEntry.setStatus("mandatory")
_RtConnIndex_Type = Integer32
_RtConnIndex_Object = MibTableColumn
rtConnIndex = _RtConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 1),
    _RtConnIndex_Type()
)
rtConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtConnIndex.setStatus("mandatory")


class _RtConnName_Type(DisplayString):
    """Custom type rtConnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RtConnName_Type.__name__ = "DisplayString"
_RtConnName_Object = MibTableColumn
rtConnName = _RtConnName_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 2),
    _RtConnName_Type()
)
rtConnName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnName.setStatus("mandatory")


class _RtConnComment_Type(DisplayString):
    """Custom type rtConnComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RtConnComment_Type.__name__ = "DisplayString"
_RtConnComment_Object = MibTableColumn
rtConnComment = _RtConnComment_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 3),
    _RtConnComment_Type()
)
rtConnComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnComment.setStatus("mandatory")
_RtConnEntryStatus_Type = EntryStatus
_RtConnEntryStatus_Object = MibTableColumn
rtConnEntryStatus = _RtConnEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 4),
    _RtConnEntryStatus_Type()
)
rtConnEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnEntryStatus.setStatus("mandatory")
_RtConnOperState_Type = OperState
_RtConnOperState_Object = MibTableColumn
rtConnOperState = _RtConnOperState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 5),
    _RtConnOperState_Type()
)
rtConnOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtConnOperState.setStatus("mandatory")
_RtConnAdminStateCtr_Type = AdminState
_RtConnAdminStateCtr_Object = MibTableColumn
rtConnAdminStateCtr = _RtConnAdminStateCtr_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 6),
    _RtConnAdminStateCtr_Type()
)
rtConnAdminStateCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnAdminStateCtr.setStatus("mandatory")


class _RtConnAutoStart_Type(Integer32):
    """Custom type rtConnAutoStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("startNo", 2),
          ("startYes", 1))
    )


_RtConnAutoStart_Type.__name__ = "Integer32"
_RtConnAutoStart_Object = MibTableColumn
rtConnAutoStart = _RtConnAutoStart_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 7),
    _RtConnAutoStart_Type()
)
rtConnAutoStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnAutoStart.setStatus("mandatory")


class _RtConnType_Type(Integer32):
    """Custom type rtConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("typeIn", 1),
          ("typeOut", 2),
          ("typeTwoWay", 3))
    )


_RtConnType_Type.__name__ = "Integer32"
_RtConnType_Object = MibTableColumn
rtConnType = _RtConnType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 8),
    _RtConnType_Type()
)
rtConnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnType.setStatus("mandatory")
_RtConnInactivityTimeout_Type = Integer32
_RtConnInactivityTimeout_Object = MibTableColumn
rtConnInactivityTimeout = _RtConnInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 9),
    _RtConnInactivityTimeout_Type()
)
rtConnInactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnInactivityTimeout.setStatus("mandatory")
_RtConnPortNumber_Type = PortRef
_RtConnPortNumber_Object = MibTableColumn
rtConnPortNumber = _RtConnPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 10),
    _RtConnPortNumber_Type()
)
rtConnPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnPortNumber.setStatus("mandatory")


class _RtConnCompression_Type(Integer32):
    """Custom type rtConnCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("comprNo", 1),
          ("comprOther", 3),
          ("comprStac", 2))
    )


_RtConnCompression_Type.__name__ = "Integer32"
_RtConnCompression_Object = MibTableColumn
rtConnCompression = _RtConnCompression_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 11),
    _RtConnCompression_Type()
)
rtConnCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnCompression.setStatus("mandatory")
_RtConnRetryNum_Type = Integer32
_RtConnRetryNum_Object = MibTableColumn
rtConnRetryNum = _RtConnRetryNum_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 12),
    _RtConnRetryNum_Type()
)
rtConnRetryNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnRetryNum.setStatus("mandatory")
_RtConnRetryDelay_Type = Integer32
_RtConnRetryDelay_Object = MibTableColumn
rtConnRetryDelay = _RtConnRetryDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 13),
    _RtConnRetryDelay_Type()
)
rtConnRetryDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnRetryDelay.setStatus("mandatory")


class _RtConnPeerRouter_Type(Integer32):
    """Custom type rtConnPeerRouter based on Integer32"""
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
        *(("peerCISCO", 4),
          ("peerNetWareNLM", 2),
          ("peerNetWareV2", 1),
          ("peerUniversal", 3))
    )


_RtConnPeerRouter_Type.__name__ = "Integer32"
_RtConnPeerRouter_Object = MibTableColumn
rtConnPeerRouter = _RtConnPeerRouter_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 14),
    _RtConnPeerRouter_Type()
)
rtConnPeerRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnPeerRouter.setStatus("mandatory")
_RtConnLanProtocol_Type = Integer32
_RtConnLanProtocol_Object = MibTableColumn
rtConnLanProtocol = _RtConnLanProtocol_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 15),
    _RtConnLanProtocol_Type()
)
rtConnLanProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnLanProtocol.setStatus("mandatory")


class _RtConnWanProtocol_Type(Integer32):
    """Custom type rtConnWanProtocol based on Integer32"""
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
        *(("connFr", 3),
          ("connHdlc", 6),
          ("connPpp", 4),
          ("connSna", 5),
          ("connX25Pvc", 2),
          ("connX25Svc", 1))
    )


_RtConnWanProtocol_Type.__name__ = "Integer32"
_RtConnWanProtocol_Object = MibTableColumn
rtConnWanProtocol = _RtConnWanProtocol_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 16),
    _RtConnWanProtocol_Type()
)
rtConnWanProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnWanProtocol.setStatus("mandatory")


class _RtConnX25LocalDTE_Type(DisplayString):
    """Custom type rtConnX25LocalDTE based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_RtConnX25LocalDTE_Type.__name__ = "DisplayString"
_RtConnX25LocalDTE_Object = MibTableColumn
rtConnX25LocalDTE = _RtConnX25LocalDTE_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 17),
    _RtConnX25LocalDTE_Type()
)
rtConnX25LocalDTE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnX25LocalDTE.setStatus("mandatory")


class _RtConnX25RemoteDTE_Type(DisplayString):
    """Custom type rtConnX25RemoteDTE based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_RtConnX25RemoteDTE_Type.__name__ = "DisplayString"
_RtConnX25RemoteDTE_Object = MibTableColumn
rtConnX25RemoteDTE = _RtConnX25RemoteDTE_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 18),
    _RtConnX25RemoteDTE_Type()
)
rtConnX25RemoteDTE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnX25RemoteDTE.setStatus("mandatory")


class _RtConnX25CallingFacilities_Type(DisplayString):
    """Custom type rtConnX25CallingFacilities based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 218),
    )


_RtConnX25CallingFacilities_Type.__name__ = "DisplayString"
_RtConnX25CallingFacilities_Object = MibTableColumn
rtConnX25CallingFacilities = _RtConnX25CallingFacilities_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 19),
    _RtConnX25CallingFacilities_Type()
)
rtConnX25CallingFacilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnX25CallingFacilities.setStatus("mandatory")


class _RtConnX25ListeningFacilities_Type(DisplayString):
    """Custom type rtConnX25ListeningFacilities based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 218),
    )


_RtConnX25ListeningFacilities_Type.__name__ = "DisplayString"
_RtConnX25ListeningFacilities_Object = MibTableColumn
rtConnX25ListeningFacilities = _RtConnX25ListeningFacilities_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 20),
    _RtConnX25ListeningFacilities_Type()
)
rtConnX25ListeningFacilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnX25ListeningFacilities.setStatus("mandatory")


class _RtConnX25UserData_Type(DisplayString):
    """Custom type rtConnX25UserData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_RtConnX25UserData_Type.__name__ = "DisplayString"
_RtConnX25UserData_Object = MibTableColumn
rtConnX25UserData = _RtConnX25UserData_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 21),
    _RtConnX25UserData_Type()
)
rtConnX25UserData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnX25UserData.setStatus("mandatory")
_RtConnX25Pvc_Type = Integer32
_RtConnX25Pvc_Object = MibTableColumn
rtConnX25Pvc = _RtConnX25Pvc_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 22),
    _RtConnX25Pvc_Type()
)
rtConnX25Pvc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnX25Pvc.setStatus("mandatory")
_RtConnFrDlci_Type = Integer32
_RtConnFrDlci_Object = MibTableColumn
rtConnFrDlci = _RtConnFrDlci_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 23),
    _RtConnFrDlci_Type()
)
rtConnFrDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnFrDlci.setStatus("mandatory")


class _RtConnSnaPuName_Type(DisplayString):
    """Custom type rtConnSnaPuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_RtConnSnaPuName_Type.__name__ = "DisplayString"
_RtConnSnaPuName_Object = MibTableColumn
rtConnSnaPuName = _RtConnSnaPuName_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 24),
    _RtConnSnaPuName_Type()
)
rtConnSnaPuName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnSnaPuName.setStatus("mandatory")


class _RtConnSnaLocalFqName_Type(DisplayString):
    """Custom type rtConnSnaLocalFqName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 18),
    )


_RtConnSnaLocalFqName_Type.__name__ = "DisplayString"
_RtConnSnaLocalFqName_Object = MibTableColumn
rtConnSnaLocalFqName = _RtConnSnaLocalFqName_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 25),
    _RtConnSnaLocalFqName_Type()
)
rtConnSnaLocalFqName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnSnaLocalFqName.setStatus("mandatory")


class _RtConnSnaRemoteFqName_Type(DisplayString):
    """Custom type rtConnSnaRemoteFqName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 18),
    )


_RtConnSnaRemoteFqName_Type.__name__ = "DisplayString"
_RtConnSnaRemoteFqName_Object = MibTableColumn
rtConnSnaRemoteFqName = _RtConnSnaRemoteFqName_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 26),
    _RtConnSnaRemoteFqName_Type()
)
rtConnSnaRemoteFqName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnSnaRemoteFqName.setStatus("mandatory")


class _RtConnSnaModeName_Type(DisplayString):
    """Custom type rtConnSnaModeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_RtConnSnaModeName_Type.__name__ = "DisplayString"
_RtConnSnaModeName_Object = MibTableColumn
rtConnSnaModeName = _RtConnSnaModeName_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 27),
    _RtConnSnaModeName_Type()
)
rtConnSnaModeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnSnaModeName.setStatus("mandatory")


class _RtConnSnaSendPaceWindow_Type(Integer32):
    """Custom type rtConnSnaSendPaceWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RtConnSnaSendPaceWindow_Type.__name__ = "Integer32"
_RtConnSnaSendPaceWindow_Object = MibTableColumn
rtConnSnaSendPaceWindow = _RtConnSnaSendPaceWindow_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 28),
    _RtConnSnaSendPaceWindow_Type()
)
rtConnSnaSendPaceWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnSnaSendPaceWindow.setStatus("mandatory")


class _RtConnSnaReceivePaceWindow_Type(Integer32):
    """Custom type rtConnSnaReceivePaceWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RtConnSnaReceivePaceWindow_Type.__name__ = "Integer32"
_RtConnSnaReceivePaceWindow_Object = MibTableColumn
rtConnSnaReceivePaceWindow = _RtConnSnaReceivePaceWindow_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 29),
    _RtConnSnaReceivePaceWindow_Type()
)
rtConnSnaReceivePaceWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnSnaReceivePaceWindow.setStatus("mandatory")


class _RtConnSnaRuSendLow_Type(Integer32):
    """Custom type rtConnSnaRuSendLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(133, 248),
    )


_RtConnSnaRuSendLow_Type.__name__ = "Integer32"
_RtConnSnaRuSendLow_Object = MibTableColumn
rtConnSnaRuSendLow = _RtConnSnaRuSendLow_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 30),
    _RtConnSnaRuSendLow_Type()
)
rtConnSnaRuSendLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnSnaRuSendLow.setStatus("mandatory")


class _RtConnSnaRuReceiveLow_Type(Integer32):
    """Custom type rtConnSnaRuReceiveLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(133, 248),
    )


_RtConnSnaRuReceiveLow_Type.__name__ = "Integer32"
_RtConnSnaRuReceiveLow_Object = MibTableColumn
rtConnSnaRuReceiveLow = _RtConnSnaRuReceiveLow_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 31),
    _RtConnSnaRuReceiveLow_Type()
)
rtConnSnaRuReceiveLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnSnaRuReceiveLow.setStatus("mandatory")


class _RtConnSnaRuSendHigh_Type(Integer32):
    """Custom type rtConnSnaRuSendHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(133, 248),
    )


_RtConnSnaRuSendHigh_Type.__name__ = "Integer32"
_RtConnSnaRuSendHigh_Object = MibTableColumn
rtConnSnaRuSendHigh = _RtConnSnaRuSendHigh_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 32),
    _RtConnSnaRuSendHigh_Type()
)
rtConnSnaRuSendHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnSnaRuSendHigh.setStatus("mandatory")


class _RtConnSnaRuReceiveHigh_Type(Integer32):
    """Custom type rtConnSnaRuReceiveHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(133, 248),
    )


_RtConnSnaRuReceiveHigh_Type.__name__ = "Integer32"
_RtConnSnaRuReceiveHigh_Object = MibTableColumn
rtConnSnaRuReceiveHigh = _RtConnSnaRuReceiveHigh_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 33),
    _RtConnSnaRuReceiveHigh_Type()
)
rtConnSnaRuReceiveHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnSnaRuReceiveHigh.setStatus("mandatory")


class _RtConnUsage_Type(Integer32):
    """Custom type rtConnUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uSageBackup", 2),
          ("uSagePrimary", 1))
    )


_RtConnUsage_Type.__name__ = "Integer32"
_RtConnUsage_Object = MibTableColumn
rtConnUsage = _RtConnUsage_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 34),
    _RtConnUsage_Type()
)
rtConnUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnUsage.setStatus("mandatory")


class _RtConnFrSegmentation_Type(Integer32):
    """Custom type rtConnFrSegmentation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 3),
          ("no", 1),
          ("yes", 2))
    )


_RtConnFrSegmentation_Type.__name__ = "Integer32"
_RtConnFrSegmentation_Object = MibTableColumn
rtConnFrSegmentation = _RtConnFrSegmentation_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 35),
    _RtConnFrSegmentation_Type()
)
rtConnFrSegmentation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnFrSegmentation.setStatus("mandatory")


class _RtConnFrXid_Type(Integer32):
    """Custom type rtConnFrXid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 3),
          ("no", 1),
          ("yes", 2))
    )


_RtConnFrXid_Type.__name__ = "Integer32"
_RtConnFrXid_Object = MibTableColumn
rtConnFrXid = _RtConnFrXid_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 36),
    _RtConnFrXid_Type()
)
rtConnFrXid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnFrXid.setStatus("mandatory")


class _RtConnPrimOrBackName_Type(DisplayString):
    """Custom type rtConnPrimOrBackName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RtConnPrimOrBackName_Type.__name__ = "DisplayString"
_RtConnPrimOrBackName_Object = MibTableColumn
rtConnPrimOrBackName = _RtConnPrimOrBackName_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 37),
    _RtConnPrimOrBackName_Type()
)
rtConnPrimOrBackName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnPrimOrBackName.setStatus("mandatory")


class _RtConnRipSapUpdateType_Type(Integer32):
    """Custom type rtConnRipSapUpdateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("onchange", 2),
          ("periodic", 3))
    )


_RtConnRipSapUpdateType_Type.__name__ = "Integer32"
_RtConnRipSapUpdateType_Object = MibTableColumn
rtConnRipSapUpdateType = _RtConnRipSapUpdateType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 38),
    _RtConnRipSapUpdateType_Type()
)
rtConnRipSapUpdateType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnRipSapUpdateType.setStatus("mandatory")
_RtConnSAPDelay_Type = Integer32
_RtConnSAPDelay_Object = MibTableColumn
rtConnSAPDelay = _RtConnSAPDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 39),
    _RtConnSAPDelay_Type()
)
rtConnSAPDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnSAPDelay.setStatus("mandatory")
_RtConnRIPDelay_Type = Integer32
_RtConnRIPDelay_Object = MibTableColumn
rtConnRIPDelay = _RtConnRIPDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 32, 1, 40),
    _RtConnRIPDelay_Type()
)
rtConnRIPDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtConnRIPDelay.setStatus("mandatory")
_RtIPMapFreeIndex_Type = Integer32
_RtIPMapFreeIndex_Object = MibScalar
rtIPMapFreeIndex = _RtIPMapFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 33),
    _RtIPMapFreeIndex_Type()
)
rtIPMapFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIPMapFreeIndex.setStatus("mandatory")
_RtIPMappingTable_Object = MibTable
rtIPMappingTable = _RtIPMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 34)
)
if mibBuilder.loadTexts:
    rtIPMappingTable.setStatus("mandatory")
_RtIPMappingEntry_Object = MibTableRow
rtIPMappingEntry = _RtIPMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 34, 1)
)
rtIPMappingEntry.setIndexNames(
    (0, "EICON-MIB-ROUTER", "rtIPMapConnIndex"),
    (0, "EICON-MIB-ROUTER", "rtIPMapIndex"),
)
if mibBuilder.loadTexts:
    rtIPMappingEntry.setStatus("mandatory")
_RtIPMapIndex_Type = Integer32
_RtIPMapIndex_Object = MibTableColumn
rtIPMapIndex = _RtIPMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 34, 1, 1),
    _RtIPMapIndex_Type()
)
rtIPMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIPMapIndex.setStatus("mandatory")
_RtIPMapConnIndex_Type = Integer32
_RtIPMapConnIndex_Object = MibTableColumn
rtIPMapConnIndex = _RtIPMapConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 34, 1, 2),
    _RtIPMapConnIndex_Type()
)
rtIPMapConnIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIPMapConnIndex.setStatus("mandatory")
_RtIPMapEntryStatus_Type = EntryStatus
_RtIPMapEntryStatus_Object = MibTableColumn
rtIPMapEntryStatus = _RtIPMapEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 34, 1, 3),
    _RtIPMapEntryStatus_Type()
)
rtIPMapEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIPMapEntryStatus.setStatus("mandatory")
_RtIPMapNextHop_Type = IpAddress
_RtIPMapNextHop_Object = MibTableColumn
rtIPMapNextHop = _RtIPMapNextHop_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 34, 1, 4),
    _RtIPMapNextHop_Type()
)
rtIPMapNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIPMapNextHop.setStatus("mandatory")


class _RtIPMapBroadcast_Type(Integer32):
    """Custom type rtIPMapBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadNo", 1),
          ("broadYes", 2))
    )


_RtIPMapBroadcast_Type.__name__ = "Integer32"
_RtIPMapBroadcast_Object = MibTableColumn
rtIPMapBroadcast = _RtIPMapBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 34, 1, 5),
    _RtIPMapBroadcast_Type()
)
rtIPMapBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIPMapBroadcast.setStatus("mandatory")
_RtIPMapIPMask_Type = IpAddress
_RtIPMapIPMask_Object = MibTableColumn
rtIPMapIPMask = _RtIPMapIPMask_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 34, 1, 6),
    _RtIPMapIPMask_Type()
)
rtIPMapIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIPMapIPMask.setStatus("mandatory")


class _RtIPMapVJCompress_Type(Integer32):
    """Custom type rtIPMapVJCompress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vjNo", 1),
          ("vjYes", 2))
    )


_RtIPMapVJCompress_Type.__name__ = "Integer32"
_RtIPMapVJCompress_Object = MibTableColumn
rtIPMapVJCompress = _RtIPMapVJCompress_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 34, 1, 7),
    _RtIPMapVJCompress_Type()
)
rtIPMapVJCompress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIPMapVJCompress.setStatus("mandatory")
_RtCircuitTable_Object = MibTable
rtCircuitTable = _RtCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35)
)
if mibBuilder.loadTexts:
    rtCircuitTable.setStatus("mandatory")
_RtCircuitEntry_Object = MibTableRow
rtCircuitEntry = _RtCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35, 1)
)
rtCircuitEntry.setIndexNames(
    (0, "EICON-MIB-ROUTER", "rtCircuitConnIndex"),
)
if mibBuilder.loadTexts:
    rtCircuitEntry.setStatus("mandatory")
_RtCircuitConnIndex_Type = Integer32
_RtCircuitConnIndex_Object = MibTableColumn
rtCircuitConnIndex = _RtCircuitConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35, 1, 1),
    _RtCircuitConnIndex_Type()
)
rtCircuitConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitConnIndex.setStatus("mandatory")


class _RtCircuitStatus_Type(Integer32):
    """Custom type rtCircuitStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 6),
          ("calling", 2),
          ("connected", 3),
          ("hangingup", 4),
          ("hungup", 5),
          ("idle", 7),
          ("listening", 1),
          ("notbound", 9),
          ("portdisconnected", 8),
          ("unknown", 10))
    )


_RtCircuitStatus_Type.__name__ = "Integer32"
_RtCircuitStatus_Object = MibTableColumn
rtCircuitStatus = _RtCircuitStatus_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35, 1, 2),
    _RtCircuitStatus_Type()
)
rtCircuitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitStatus.setStatus("mandatory")
_RtCircuitTimeUp_Type = TimeTicks
_RtCircuitTimeUp_Object = MibTableColumn
rtCircuitTimeUp = _RtCircuitTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35, 1, 3),
    _RtCircuitTimeUp_Type()
)
rtCircuitTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitTimeUp.setStatus("mandatory")
_RtCircuitErrCode_Type = Integer32
_RtCircuitErrCode_Object = MibTableColumn
rtCircuitErrCode = _RtCircuitErrCode_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35, 1, 4),
    _RtCircuitErrCode_Type()
)
rtCircuitErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitErrCode.setStatus("mandatory")
_RtCircuitSessionType_Type = Integer32
_RtCircuitSessionType_Object = MibTableColumn
rtCircuitSessionType = _RtCircuitSessionType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35, 1, 5),
    _RtCircuitSessionType_Type()
)
rtCircuitSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitSessionType.setStatus("mandatory")
_RtCircuitConnLSN_Type = Integer32
_RtCircuitConnLSN_Object = MibTableColumn
rtCircuitConnLSN = _RtCircuitConnLSN_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35, 1, 6),
    _RtCircuitConnLSN_Type()
)
rtCircuitConnLSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitConnLSN.setStatus("mandatory")
_RtCircuitDataLSN_Type = Integer32
_RtCircuitDataLSN_Object = MibTableColumn
rtCircuitDataLSN = _RtCircuitDataLSN_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35, 1, 7),
    _RtCircuitDataLSN_Type()
)
rtCircuitDataLSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitDataLSN.setStatus("mandatory")
_RtCircuitCmSelector_Type = Integer32
_RtCircuitCmSelector_Object = MibTableColumn
rtCircuitCmSelector = _RtCircuitCmSelector_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35, 1, 8),
    _RtCircuitCmSelector_Type()
)
rtCircuitCmSelector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitCmSelector.setStatus("mandatory")
_RtCircuitCompression_Type = Integer32
_RtCircuitCompression_Object = MibTableColumn
rtCircuitCompression = _RtCircuitCompression_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35, 1, 9),
    _RtCircuitCompression_Type()
)
rtCircuitCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitCompression.setStatus("mandatory")
_RtCircuitCompAlgorithm_Type = Integer32
_RtCircuitCompAlgorithm_Object = MibTableColumn
rtCircuitCompAlgorithm = _RtCircuitCompAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35, 1, 10),
    _RtCircuitCompAlgorithm_Type()
)
rtCircuitCompAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitCompAlgorithm.setStatus("mandatory")
_RtCircuitBeforeComp_Type = Gauge32
_RtCircuitBeforeComp_Object = MibTableColumn
rtCircuitBeforeComp = _RtCircuitBeforeComp_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35, 1, 11),
    _RtCircuitBeforeComp_Type()
)
rtCircuitBeforeComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitBeforeComp.setStatus("mandatory")
_RtCircuitAfterComp_Type = Gauge32
_RtCircuitAfterComp_Object = MibTableColumn
rtCircuitAfterComp = _RtCircuitAfterComp_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35, 1, 12),
    _RtCircuitAfterComp_Type()
)
rtCircuitAfterComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitAfterComp.setStatus("mandatory")
_RtCircuitTxErr_Type = Integer32
_RtCircuitTxErr_Object = MibTableColumn
rtCircuitTxErr = _RtCircuitTxErr_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35, 1, 13),
    _RtCircuitTxErr_Type()
)
rtCircuitTxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitTxErr.setStatus("mandatory")
_RtCircuitBoundLANProtocol_Type = Integer32
_RtCircuitBoundLANProtocol_Object = MibTableColumn
rtCircuitBoundLANProtocol = _RtCircuitBoundLANProtocol_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35, 1, 14),
    _RtCircuitBoundLANProtocol_Type()
)
rtCircuitBoundLANProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitBoundLANProtocol.setStatus("mandatory")


class _RtCircuitRemoteRouter_Type(DisplayString):
    """Custom type rtCircuitRemoteRouter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_RtCircuitRemoteRouter_Type.__name__ = "DisplayString"
_RtCircuitRemoteRouter_Object = MibTableColumn
rtCircuitRemoteRouter = _RtCircuitRemoteRouter_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35, 1, 15),
    _RtCircuitRemoteRouter_Type()
)
rtCircuitRemoteRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitRemoteRouter.setStatus("mandatory")
_RtCircuitCountersReset_Type = ControlOnOff
_RtCircuitCountersReset_Object = MibTableColumn
rtCircuitCountersReset = _RtCircuitCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35, 1, 16),
    _RtCircuitCountersReset_Type()
)
rtCircuitCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtCircuitCountersReset.setStatus("mandatory")


class _RtCircuitWanProtocol_Type(Integer32):
    """Custom type rtCircuitWanProtocol based on Integer32"""
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
        *(("connFr", 3),
          ("connHdlc", 6),
          ("connPpp", 4),
          ("connSna", 5),
          ("connX25Pvc", 2),
          ("connX25Svc", 1))
    )


_RtCircuitWanProtocol_Type.__name__ = "Integer32"
_RtCircuitWanProtocol_Object = MibTableColumn
rtCircuitWanProtocol = _RtCircuitWanProtocol_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35, 1, 17),
    _RtCircuitWanProtocol_Type()
)
rtCircuitWanProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitWanProtocol.setStatus("mandatory")


class _RtCircuitX25LocalDTE_Type(DisplayString):
    """Custom type rtCircuitX25LocalDTE based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_RtCircuitX25LocalDTE_Type.__name__ = "DisplayString"
_RtCircuitX25LocalDTE_Object = MibTableColumn
rtCircuitX25LocalDTE = _RtCircuitX25LocalDTE_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35, 1, 18),
    _RtCircuitX25LocalDTE_Type()
)
rtCircuitX25LocalDTE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitX25LocalDTE.setStatus("mandatory")


class _RtCircuitX25RemoteDTE_Type(DisplayString):
    """Custom type rtCircuitX25RemoteDTE based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_RtCircuitX25RemoteDTE_Type.__name__ = "DisplayString"
_RtCircuitX25RemoteDTE_Object = MibTableColumn
rtCircuitX25RemoteDTE = _RtCircuitX25RemoteDTE_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35, 1, 19),
    _RtCircuitX25RemoteDTE_Type()
)
rtCircuitX25RemoteDTE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitX25RemoteDTE.setStatus("mandatory")


class _RtCircuitX25CallingFacilities_Type(DisplayString):
    """Custom type rtCircuitX25CallingFacilities based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 218),
    )


_RtCircuitX25CallingFacilities_Type.__name__ = "DisplayString"
_RtCircuitX25CallingFacilities_Object = MibTableColumn
rtCircuitX25CallingFacilities = _RtCircuitX25CallingFacilities_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35, 1, 20),
    _RtCircuitX25CallingFacilities_Type()
)
rtCircuitX25CallingFacilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitX25CallingFacilities.setStatus("mandatory")


class _RtCircuitX25ListeningFacilities_Type(DisplayString):
    """Custom type rtCircuitX25ListeningFacilities based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 218),
    )


_RtCircuitX25ListeningFacilities_Type.__name__ = "DisplayString"
_RtCircuitX25ListeningFacilities_Object = MibTableColumn
rtCircuitX25ListeningFacilities = _RtCircuitX25ListeningFacilities_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35, 1, 21),
    _RtCircuitX25ListeningFacilities_Type()
)
rtCircuitX25ListeningFacilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitX25ListeningFacilities.setStatus("mandatory")


class _RtCircuitX25UserData_Type(DisplayString):
    """Custom type rtCircuitX25UserData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_RtCircuitX25UserData_Type.__name__ = "DisplayString"
_RtCircuitX25UserData_Object = MibTableColumn
rtCircuitX25UserData = _RtCircuitX25UserData_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35, 1, 22),
    _RtCircuitX25UserData_Type()
)
rtCircuitX25UserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitX25UserData.setStatus("mandatory")
_RtCircuitX25Cause_Type = Integer32
_RtCircuitX25Cause_Object = MibTableColumn
rtCircuitX25Cause = _RtCircuitX25Cause_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35, 1, 23),
    _RtCircuitX25Cause_Type()
)
rtCircuitX25Cause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitX25Cause.setStatus("mandatory")
_RtCircuitX25Diag_Type = Integer32
_RtCircuitX25Diag_Object = MibTableColumn
rtCircuitX25Diag = _RtCircuitX25Diag_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35, 1, 24),
    _RtCircuitX25Diag_Type()
)
rtCircuitX25Diag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitX25Diag.setStatus("mandatory")
_RtCircuitX25Pvc_Type = Integer32
_RtCircuitX25Pvc_Object = MibTableColumn
rtCircuitX25Pvc = _RtCircuitX25Pvc_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35, 1, 25),
    _RtCircuitX25Pvc_Type()
)
rtCircuitX25Pvc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitX25Pvc.setStatus("mandatory")
_RtCircuitFrDlci_Type = Integer32
_RtCircuitFrDlci_Object = MibTableColumn
rtCircuitFrDlci = _RtCircuitFrDlci_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35, 1, 26),
    _RtCircuitFrDlci_Type()
)
rtCircuitFrDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitFrDlci.setStatus("mandatory")


class _RtCircuitFrSegmentation_Type(Integer32):
    """Custom type rtCircuitFrSegmentation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 3),
          ("no", 1),
          ("yes", 2))
    )


_RtCircuitFrSegmentation_Type.__name__ = "Integer32"
_RtCircuitFrSegmentation_Object = MibTableColumn
rtCircuitFrSegmentation = _RtCircuitFrSegmentation_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35, 1, 27),
    _RtCircuitFrSegmentation_Type()
)
rtCircuitFrSegmentation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitFrSegmentation.setStatus("mandatory")


class _RtCircuitFrXIDNegot_Type(Integer32):
    """Custom type rtCircuitFrXIDNegot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 3),
          ("no", 1),
          ("yes", 2))
    )


_RtCircuitFrXIDNegot_Type.__name__ = "Integer32"
_RtCircuitFrXIDNegot_Object = MibTableColumn
rtCircuitFrXIDNegot = _RtCircuitFrXIDNegot_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35, 1, 28),
    _RtCircuitFrXIDNegot_Type()
)
rtCircuitFrXIDNegot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitFrXIDNegot.setStatus("mandatory")
_RtCircuitFrXIDPacketSize_Type = Integer32
_RtCircuitFrXIDPacketSize_Object = MibTableColumn
rtCircuitFrXIDPacketSize = _RtCircuitFrXIDPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35, 1, 29),
    _RtCircuitFrXIDPacketSize_Type()
)
rtCircuitFrXIDPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitFrXIDPacketSize.setStatus("mandatory")


class _RtCircuitFrCongestion_Type(Integer32):
    """Custom type rtCircuitFrCongestion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("congested", 2),
          ("noCongestion", 1))
    )


_RtCircuitFrCongestion_Type.__name__ = "Integer32"
_RtCircuitFrCongestion_Object = MibTableColumn
rtCircuitFrCongestion = _RtCircuitFrCongestion_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 35, 1, 30),
    _RtCircuitFrCongestion_Type()
)
rtCircuitFrCongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitFrCongestion.setStatus("mandatory")
_RtCircuitIPTable_Object = MibTable
rtCircuitIPTable = _RtCircuitIPTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 36)
)
if mibBuilder.loadTexts:
    rtCircuitIPTable.setStatus("mandatory")
_RtCircuitIPEntry_Object = MibTableRow
rtCircuitIPEntry = _RtCircuitIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 36, 1)
)
rtCircuitIPEntry.setIndexNames(
    (0, "EICON-MIB-ROUTER", "rtCircuitIPConnIndex"),
)
if mibBuilder.loadTexts:
    rtCircuitIPEntry.setStatus("mandatory")
_RtCircuitIPConnIndex_Type = Integer32
_RtCircuitIPConnIndex_Object = MibTableColumn
rtCircuitIPConnIndex = _RtCircuitIPConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 36, 1, 1),
    _RtCircuitIPConnIndex_Type()
)
rtCircuitIPConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitIPConnIndex.setStatus("mandatory")
_RtCircuitIPRemoteAddress_Type = IpAddress
_RtCircuitIPRemoteAddress_Object = MibTableColumn
rtCircuitIPRemoteAddress = _RtCircuitIPRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 36, 1, 2),
    _RtCircuitIPRemoteAddress_Type()
)
rtCircuitIPRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitIPRemoteAddress.setStatus("mandatory")
_RtCircuitIPLocalAddress_Type = IpAddress
_RtCircuitIPLocalAddress_Object = MibTableColumn
rtCircuitIPLocalAddress = _RtCircuitIPLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 36, 1, 3),
    _RtCircuitIPLocalAddress_Type()
)
rtCircuitIPLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitIPLocalAddress.setStatus("mandatory")
_RtCircuitIPTxPackets_Type = Counter32
_RtCircuitIPTxPackets_Object = MibTableColumn
rtCircuitIPTxPackets = _RtCircuitIPTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 36, 1, 4),
    _RtCircuitIPTxPackets_Type()
)
rtCircuitIPTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitIPTxPackets.setStatus("mandatory")
_RtCircuitIPTxBytes_Type = Counter32
_RtCircuitIPTxBytes_Object = MibTableColumn
rtCircuitIPTxBytes = _RtCircuitIPTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 36, 1, 5),
    _RtCircuitIPTxBytes_Type()
)
rtCircuitIPTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitIPTxBytes.setStatus("mandatory")
_RtCircuitIPRxPackets_Type = Counter32
_RtCircuitIPRxPackets_Object = MibTableColumn
rtCircuitIPRxPackets = _RtCircuitIPRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 36, 1, 6),
    _RtCircuitIPRxPackets_Type()
)
rtCircuitIPRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitIPRxPackets.setStatus("mandatory")
_RtCircuitIPRxBytes_Type = Counter32
_RtCircuitIPRxBytes_Object = MibTableColumn
rtCircuitIPRxBytes = _RtCircuitIPRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 36, 1, 7),
    _RtCircuitIPRxBytes_Type()
)
rtCircuitIPRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitIPRxBytes.setStatus("mandatory")
_RtCircuitIPXTable_Object = MibTable
rtCircuitIPXTable = _RtCircuitIPXTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 37)
)
if mibBuilder.loadTexts:
    rtCircuitIPXTable.setStatus("mandatory")
_RtCircuitIPXEntry_Object = MibTableRow
rtCircuitIPXEntry = _RtCircuitIPXEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 37, 1)
)
rtCircuitIPXEntry.setIndexNames(
    (0, "EICON-MIB-ROUTER", "rtCircuitIPXConnIndex"),
)
if mibBuilder.loadTexts:
    rtCircuitIPXEntry.setStatus("mandatory")
_RtCircuitIPXConnIndex_Type = Integer32
_RtCircuitIPXConnIndex_Object = MibTableColumn
rtCircuitIPXConnIndex = _RtCircuitIPXConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 37, 1, 1),
    _RtCircuitIPXConnIndex_Type()
)
rtCircuitIPXConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitIPXConnIndex.setStatus("mandatory")


class _RtCircuitIPXRemoteNode_Type(OctetString):
    """Custom type rtCircuitIPXRemoteNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_RtCircuitIPXRemoteNode_Type.__name__ = "OctetString"
_RtCircuitIPXRemoteNode_Object = MibTableColumn
rtCircuitIPXRemoteNode = _RtCircuitIPXRemoteNode_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 37, 1, 2),
    _RtCircuitIPXRemoteNode_Type()
)
rtCircuitIPXRemoteNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitIPXRemoteNode.setStatus("mandatory")


class _RtCircuitIPXRemoteNetwork_Type(OctetString):
    """Custom type rtCircuitIPXRemoteNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_RtCircuitIPXRemoteNetwork_Type.__name__ = "OctetString"
_RtCircuitIPXRemoteNetwork_Object = MibTableColumn
rtCircuitIPXRemoteNetwork = _RtCircuitIPXRemoteNetwork_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 37, 1, 3),
    _RtCircuitIPXRemoteNetwork_Type()
)
rtCircuitIPXRemoteNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitIPXRemoteNetwork.setStatus("mandatory")


class _RtCircuitIPXLocalNode_Type(OctetString):
    """Custom type rtCircuitIPXLocalNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_RtCircuitIPXLocalNode_Type.__name__ = "OctetString"
_RtCircuitIPXLocalNode_Object = MibTableColumn
rtCircuitIPXLocalNode = _RtCircuitIPXLocalNode_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 37, 1, 4),
    _RtCircuitIPXLocalNode_Type()
)
rtCircuitIPXLocalNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitIPXLocalNode.setStatus("mandatory")


class _RtCircuitIPXLocalNetwork_Type(OctetString):
    """Custom type rtCircuitIPXLocalNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_RtCircuitIPXLocalNetwork_Type.__name__ = "OctetString"
_RtCircuitIPXLocalNetwork_Object = MibTableColumn
rtCircuitIPXLocalNetwork = _RtCircuitIPXLocalNetwork_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 37, 1, 5),
    _RtCircuitIPXLocalNetwork_Type()
)
rtCircuitIPXLocalNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitIPXLocalNetwork.setStatus("mandatory")
_RtCircuitIPXTxPackets_Type = Counter32
_RtCircuitIPXTxPackets_Object = MibTableColumn
rtCircuitIPXTxPackets = _RtCircuitIPXTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 37, 1, 6),
    _RtCircuitIPXTxPackets_Type()
)
rtCircuitIPXTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitIPXTxPackets.setStatus("mandatory")
_RtCircuitIPXTxBytes_Type = Counter32
_RtCircuitIPXTxBytes_Object = MibTableColumn
rtCircuitIPXTxBytes = _RtCircuitIPXTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 37, 1, 7),
    _RtCircuitIPXTxBytes_Type()
)
rtCircuitIPXTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitIPXTxBytes.setStatus("mandatory")
_RtCircuitIPXRxPackets_Type = Counter32
_RtCircuitIPXRxPackets_Object = MibTableColumn
rtCircuitIPXRxPackets = _RtCircuitIPXRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 37, 1, 8),
    _RtCircuitIPXRxPackets_Type()
)
rtCircuitIPXRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitIPXRxPackets.setStatus("mandatory")
_RtCircuitIPXRxBytes_Type = Counter32
_RtCircuitIPXRxBytes_Object = MibTableColumn
rtCircuitIPXRxBytes = _RtCircuitIPXRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 37, 1, 9),
    _RtCircuitIPXRxBytes_Type()
)
rtCircuitIPXRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitIPXRxBytes.setStatus("mandatory")
_RtCircuitATTable_Object = MibTable
rtCircuitATTable = _RtCircuitATTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 38)
)
if mibBuilder.loadTexts:
    rtCircuitATTable.setStatus("mandatory")
_RtCircuitATEntry_Object = MibTableRow
rtCircuitATEntry = _RtCircuitATEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 38, 1)
)
rtCircuitATEntry.setIndexNames(
    (0, "EICON-MIB-ROUTER", "rtCircuitATConnIndex"),
)
if mibBuilder.loadTexts:
    rtCircuitATEntry.setStatus("mandatory")
_RtCircuitATConnIndex_Type = Integer32
_RtCircuitATConnIndex_Object = MibTableColumn
rtCircuitATConnIndex = _RtCircuitATConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 38, 1, 1),
    _RtCircuitATConnIndex_Type()
)
rtCircuitATConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitATConnIndex.setStatus("mandatory")


class _RtCircuitATRemoteNet_Type(OctetString):
    """Custom type rtCircuitATRemoteNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_RtCircuitATRemoteNet_Type.__name__ = "OctetString"
_RtCircuitATRemoteNet_Object = MibTableColumn
rtCircuitATRemoteNet = _RtCircuitATRemoteNet_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 38, 1, 2),
    _RtCircuitATRemoteNet_Type()
)
rtCircuitATRemoteNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitATRemoteNet.setStatus("mandatory")


class _RtCircuitATRemoteNode_Type(OctetString):
    """Custom type rtCircuitATRemoteNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RtCircuitATRemoteNode_Type.__name__ = "OctetString"
_RtCircuitATRemoteNode_Object = MibTableColumn
rtCircuitATRemoteNode = _RtCircuitATRemoteNode_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 38, 1, 3),
    _RtCircuitATRemoteNode_Type()
)
rtCircuitATRemoteNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitATRemoteNode.setStatus("mandatory")


class _RtCircuitATLocalNet_Type(OctetString):
    """Custom type rtCircuitATLocalNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_RtCircuitATLocalNet_Type.__name__ = "OctetString"
_RtCircuitATLocalNet_Object = MibTableColumn
rtCircuitATLocalNet = _RtCircuitATLocalNet_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 38, 1, 4),
    _RtCircuitATLocalNet_Type()
)
rtCircuitATLocalNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitATLocalNet.setStatus("mandatory")


class _RtCircuitATLocalNode_Type(OctetString):
    """Custom type rtCircuitATLocalNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RtCircuitATLocalNode_Type.__name__ = "OctetString"
_RtCircuitATLocalNode_Object = MibTableColumn
rtCircuitATLocalNode = _RtCircuitATLocalNode_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 38, 1, 5),
    _RtCircuitATLocalNode_Type()
)
rtCircuitATLocalNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitATLocalNode.setStatus("mandatory")
_RtCircuitATTxPackets_Type = Counter32
_RtCircuitATTxPackets_Object = MibTableColumn
rtCircuitATTxPackets = _RtCircuitATTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 38, 1, 6),
    _RtCircuitATTxPackets_Type()
)
rtCircuitATTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitATTxPackets.setStatus("mandatory")
_RtCircuitATTxBytes_Type = Counter32
_RtCircuitATTxBytes_Object = MibTableColumn
rtCircuitATTxBytes = _RtCircuitATTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 38, 1, 7),
    _RtCircuitATTxBytes_Type()
)
rtCircuitATTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitATTxBytes.setStatus("mandatory")
_RtCircuitATRxPackets_Type = Counter32
_RtCircuitATRxPackets_Object = MibTableColumn
rtCircuitATRxPackets = _RtCircuitATRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 38, 1, 8),
    _RtCircuitATRxPackets_Type()
)
rtCircuitATRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitATRxPackets.setStatus("mandatory")
_RtCircuitATRxBytes_Type = Counter32
_RtCircuitATRxBytes_Object = MibTableColumn
rtCircuitATRxBytes = _RtCircuitATRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 38, 1, 9),
    _RtCircuitATRxBytes_Type()
)
rtCircuitATRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtCircuitATRxBytes.setStatus("mandatory")
_RtMaxIPFilter_Type = Integer32
_RtMaxIPFilter_Object = MibScalar
rtMaxIPFilter = _RtMaxIPFilter_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 39),
    _RtMaxIPFilter_Type()
)
rtMaxIPFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtMaxIPFilter.setStatus("mandatory")
_RtAvailableIPFilter_Type = Gauge32
_RtAvailableIPFilter_Object = MibScalar
rtAvailableIPFilter = _RtAvailableIPFilter_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 40),
    _RtAvailableIPFilter_Type()
)
rtAvailableIPFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtAvailableIPFilter.setStatus("mandatory")
_RtIPFilterDropStatsIn_Type = Counter32
_RtIPFilterDropStatsIn_Object = MibScalar
rtIPFilterDropStatsIn = _RtIPFilterDropStatsIn_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 41),
    _RtIPFilterDropStatsIn_Type()
)
rtIPFilterDropStatsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIPFilterDropStatsIn.setStatus("mandatory")
_RtIPFilterDropStatsOut_Type = Counter32
_RtIPFilterDropStatsOut_Object = MibScalar
rtIPFilterDropStatsOut = _RtIPFilterDropStatsOut_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 42),
    _RtIPFilterDropStatsOut_Type()
)
rtIPFilterDropStatsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIPFilterDropStatsOut.setStatus("mandatory")
_RtIPFilterForwardStatsIn_Type = Counter32
_RtIPFilterForwardStatsIn_Object = MibScalar
rtIPFilterForwardStatsIn = _RtIPFilterForwardStatsIn_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 43),
    _RtIPFilterForwardStatsIn_Type()
)
rtIPFilterForwardStatsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIPFilterForwardStatsIn.setStatus("mandatory")
_RtIPFilterForwardStatsOut_Type = Counter32
_RtIPFilterForwardStatsOut_Object = MibScalar
rtIPFilterForwardStatsOut = _RtIPFilterForwardStatsOut_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 44),
    _RtIPFilterForwardStatsOut_Type()
)
rtIPFilterForwardStatsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIPFilterForwardStatsOut.setStatus("mandatory")
_RtIPFilterFreeIndex_Type = Integer32
_RtIPFilterFreeIndex_Object = MibScalar
rtIPFilterFreeIndex = _RtIPFilterFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 45),
    _RtIPFilterFreeIndex_Type()
)
rtIPFilterFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIPFilterFreeIndex.setStatus("mandatory")
_RtIPFilterTable_Object = MibTable
rtIPFilterTable = _RtIPFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 46)
)
if mibBuilder.loadTexts:
    rtIPFilterTable.setStatus("mandatory")
_RtIPFilterEntry_Object = MibTableRow
rtIPFilterEntry = _RtIPFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 46, 1)
)
rtIPFilterEntry.setIndexNames(
    (0, "EICON-MIB-ROUTER", "rtIPFilterConnIndex"),
    (0, "EICON-MIB-ROUTER", "rtIPFilterIndex"),
)
if mibBuilder.loadTexts:
    rtIPFilterEntry.setStatus("mandatory")
_RtIPFilterConnIndex_Type = Integer32
_RtIPFilterConnIndex_Object = MibTableColumn
rtIPFilterConnIndex = _RtIPFilterConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 46, 1, 1),
    _RtIPFilterConnIndex_Type()
)
rtIPFilterConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIPFilterConnIndex.setStatus("mandatory")
_RtIPFilterIndex_Type = Integer32
_RtIPFilterIndex_Object = MibTableColumn
rtIPFilterIndex = _RtIPFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 46, 1, 2),
    _RtIPFilterIndex_Type()
)
rtIPFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIPFilterIndex.setStatus("mandatory")
_RtIPFilterEntryStatus_Type = EntryStatusV2
_RtIPFilterEntryStatus_Object = MibTableColumn
rtIPFilterEntryStatus = _RtIPFilterEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 46, 1, 3),
    _RtIPFilterEntryStatus_Type()
)
rtIPFilterEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIPFilterEntryStatus.setStatus("mandatory")
_RtIPFilterOperState_Type = OperState
_RtIPFilterOperState_Object = MibTableColumn
rtIPFilterOperState = _RtIPFilterOperState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 46, 1, 4),
    _RtIPFilterOperState_Type()
)
rtIPFilterOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIPFilterOperState.setStatus("mandatory")
_RtIPFilterAdminStateCtr_Type = AdminState
_RtIPFilterAdminStateCtr_Object = MibTableColumn
rtIPFilterAdminStateCtr = _RtIPFilterAdminStateCtr_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 46, 1, 5),
    _RtIPFilterAdminStateCtr_Type()
)
rtIPFilterAdminStateCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIPFilterAdminStateCtr.setStatus("mandatory")
_RtIPFilterPosition_Type = Integer32
_RtIPFilterPosition_Object = MibTableColumn
rtIPFilterPosition = _RtIPFilterPosition_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 46, 1, 6),
    _RtIPFilterPosition_Type()
)
rtIPFilterPosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIPFilterPosition.setStatus("mandatory")


class _RtIPFilterAction_Type(Integer32):
    """Custom type rtIPFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("forward", 2))
    )


_RtIPFilterAction_Type.__name__ = "Integer32"
_RtIPFilterAction_Object = MibTableColumn
rtIPFilterAction = _RtIPFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 46, 1, 7),
    _RtIPFilterAction_Type()
)
rtIPFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIPFilterAction.setStatus("mandatory")


class _RtIPFilterDirection_Type(Integer32):
    """Custom type rtIPFilterDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 3),
          ("in", 1),
          ("out", 2))
    )


_RtIPFilterDirection_Type.__name__ = "Integer32"
_RtIPFilterDirection_Object = MibTableColumn
rtIPFilterDirection = _RtIPFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 46, 1, 8),
    _RtIPFilterDirection_Type()
)
rtIPFilterDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIPFilterDirection.setStatus("mandatory")


class _RtIPFilterPortType_Type(Integer32):
    """Custom type rtIPFilterPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 3),
          ("tcp", 1),
          ("udp", 2))
    )


_RtIPFilterPortType_Type.__name__ = "Integer32"
_RtIPFilterPortType_Object = MibTableColumn
rtIPFilterPortType = _RtIPFilterPortType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 46, 1, 9),
    _RtIPFilterPortType_Type()
)
rtIPFilterPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIPFilterPortType.setStatus("mandatory")
_RtIPFilterLowSrcPort_Type = Integer32
_RtIPFilterLowSrcPort_Object = MibTableColumn
rtIPFilterLowSrcPort = _RtIPFilterLowSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 46, 1, 10),
    _RtIPFilterLowSrcPort_Type()
)
rtIPFilterLowSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIPFilterLowSrcPort.setStatus("mandatory")
_RtIPFilterHighSrcPort_Type = Integer32
_RtIPFilterHighSrcPort_Object = MibTableColumn
rtIPFilterHighSrcPort = _RtIPFilterHighSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 46, 1, 11),
    _RtIPFilterHighSrcPort_Type()
)
rtIPFilterHighSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIPFilterHighSrcPort.setStatus("mandatory")
_RtIPFilterLowDestPort_Type = Integer32
_RtIPFilterLowDestPort_Object = MibTableColumn
rtIPFilterLowDestPort = _RtIPFilterLowDestPort_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 46, 1, 12),
    _RtIPFilterLowDestPort_Type()
)
rtIPFilterLowDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIPFilterLowDestPort.setStatus("mandatory")
_RtIPFilterHighDestPort_Type = Integer32
_RtIPFilterHighDestPort_Object = MibTableColumn
rtIPFilterHighDestPort = _RtIPFilterHighDestPort_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 46, 1, 13),
    _RtIPFilterHighDestPort_Type()
)
rtIPFilterHighDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIPFilterHighDestPort.setStatus("mandatory")
_RtIPFilterIPAddressSrc_Type = IpAddress
_RtIPFilterIPAddressSrc_Object = MibTableColumn
rtIPFilterIPAddressSrc = _RtIPFilterIPAddressSrc_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 46, 1, 14),
    _RtIPFilterIPAddressSrc_Type()
)
rtIPFilterIPAddressSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIPFilterIPAddressSrc.setStatus("mandatory")
_RtIPFilterIPMaskSrc_Type = IpAddress
_RtIPFilterIPMaskSrc_Object = MibTableColumn
rtIPFilterIPMaskSrc = _RtIPFilterIPMaskSrc_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 46, 1, 15),
    _RtIPFilterIPMaskSrc_Type()
)
rtIPFilterIPMaskSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIPFilterIPMaskSrc.setStatus("mandatory")
_RtIPFilterIPAddressDest_Type = IpAddress
_RtIPFilterIPAddressDest_Object = MibTableColumn
rtIPFilterIPAddressDest = _RtIPFilterIPAddressDest_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 46, 1, 16),
    _RtIPFilterIPAddressDest_Type()
)
rtIPFilterIPAddressDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIPFilterIPAddressDest.setStatus("mandatory")
_RtIPFilterIPMaskDest_Type = IpAddress
_RtIPFilterIPMaskDest_Object = MibTableColumn
rtIPFilterIPMaskDest = _RtIPFilterIPMaskDest_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 46, 1, 17),
    _RtIPFilterIPMaskDest_Type()
)
rtIPFilterIPMaskDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtIPFilterIPMaskDest.setStatus("mandatory")
_RtIPFilterStatsIn_Type = Counter32
_RtIPFilterStatsIn_Object = MibTableColumn
rtIPFilterStatsIn = _RtIPFilterStatsIn_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 46, 1, 18),
    _RtIPFilterStatsIn_Type()
)
rtIPFilterStatsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIPFilterStatsIn.setStatus("mandatory")
_RtIPFilterStatsOut_Type = Counter32
_RtIPFilterStatsOut_Object = MibTableColumn
rtIPFilterStatsOut = _RtIPFilterStatsOut_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 46, 1, 19),
    _RtIPFilterStatsOut_Type()
)
rtIPFilterStatsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIPFilterStatsOut.setStatus("mandatory")
_RtActionState_Type = ActionState
_RtActionState_Object = MibScalar
rtActionState = _RtActionState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 47),
    _RtActionState_Type()
)
rtActionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtActionState.setStatus("mandatory")


class _RtActionError_Type(Integer32):
    """Custom type rtActionError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("err-ALREADY-STARTED", 1),
          ("err-General", 99),
          ("err-NOT-STARTED", 2),
          ("err-SHUTDOWN-FAILURE", 4),
          ("err-STACK-NOT-BOUND", 3),
          ("no-error", 0))
    )


_RtActionError_Type.__name__ = "Integer32"
_RtActionError_Object = MibScalar
rtActionError = _RtActionError_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 8, 48),
    _RtActionError_Type()
)
rtActionError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtActionError.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EICON-MIB-ROUTER",
    **{"OperState": OperState,
       "AdminState": AdminState,
       "ActionState": ActionState,
       "EntryStatus": EntryStatus,
       "EntryStatusV2": EntryStatusV2,
       "ConnectionStatus": ConnectionStatus,
       "ControlOnOff": ControlOnOff,
       "CardRef": CardRef,
       "PortRef": PortRef,
       "PositiveInteger": PositiveInteger,
       "eicon": eicon,
       "management": management,
       "mibv2": mibv2,
       "module": module,
       "router": router,
       "rtName": rtName,
       "rtProductName": rtProductName,
       "rtReleaseVersion": rtReleaseVersion,
       "rtReleaseDate": rtReleaseDate,
       "rtOperState": rtOperState,
       "rtAdminStateCtr": rtAdminStateCtr,
       "rtType": rtType,
       "rtTimeUp": rtTimeUp,
       "rtNumberOfPorts": rtNumberOfPorts,
       "rtMaxCircuits": rtMaxCircuits,
       "rtAvailableCircuits": rtAvailableCircuits,
       "rtAvailableLANMapping": rtAvailableLANMapping,
       "rtMaxLANMapping": rtMaxLANMapping,
       "rtGlobalTxPackets": rtGlobalTxPackets,
       "rtGlobalTxBytesLow": rtGlobalTxBytesLow,
       "rtGlobalTxBytesHigh": rtGlobalTxBytesHigh,
       "rtGlobalRxPackets": rtGlobalRxPackets,
       "rtGlobalRxBytesLow": rtGlobalRxBytesLow,
       "rtGlobalRxBytesHigh": rtGlobalRxBytesHigh,
       "rtGlobalTxDropNoRoute": rtGlobalTxDropNoRoute,
       "rtGlobalTxDropNoResource": rtGlobalTxDropNoResource,
       "rtGlobalTxDropUnknownProt": rtGlobalTxDropUnknownProt,
       "rtGlobalRxDropNoResource": rtGlobalRxDropNoResource,
       "rtGlobalRxDropUnknownProt": rtGlobalRxDropUnknownProt,
       "rtGlobalRxError": rtGlobalRxError,
       "rtGlobalCountersReset": rtGlobalCountersReset,
       "rtTraceCtrl": rtTraceCtrl,
       "rtTraceFileName": rtTraceFileName,
       "rtTraceInterfaceType": rtTraceInterfaceType,
       "rtPortTable": rtPortTable,
       "rtPortEntry": rtPortEntry,
       "rtPortIndex": rtPortIndex,
       "rtPortNumber": rtPortNumber,
       "rtPortProtocol": rtPortProtocol,
       "rtPortTxThroughput": rtPortTxThroughput,
       "rtPortRxThroughput": rtPortRxThroughput,
       "rtPortTxPackets": rtPortTxPackets,
       "rtPortTxBytesLow": rtPortTxBytesLow,
       "rtPortTxBytesHigh": rtPortTxBytesHigh,
       "rtPortRxPackets": rtPortRxPackets,
       "rtPortRxBytesLow": rtPortRxBytesLow,
       "rtPortRxBytesHigh": rtPortRxBytesHigh,
       "rtPortTxDropNoResource": rtPortTxDropNoResource,
       "rtPortRxError": rtPortRxError,
       "rtPortCountersReset": rtPortCountersReset,
       "rtConnFreeIndex": rtConnFreeIndex,
       "rtConnTable": rtConnTable,
       "rtConnEntry": rtConnEntry,
       "rtConnIndex": rtConnIndex,
       "rtConnName": rtConnName,
       "rtConnComment": rtConnComment,
       "rtConnEntryStatus": rtConnEntryStatus,
       "rtConnOperState": rtConnOperState,
       "rtConnAdminStateCtr": rtConnAdminStateCtr,
       "rtConnAutoStart": rtConnAutoStart,
       "rtConnType": rtConnType,
       "rtConnInactivityTimeout": rtConnInactivityTimeout,
       "rtConnPortNumber": rtConnPortNumber,
       "rtConnCompression": rtConnCompression,
       "rtConnRetryNum": rtConnRetryNum,
       "rtConnRetryDelay": rtConnRetryDelay,
       "rtConnPeerRouter": rtConnPeerRouter,
       "rtConnLanProtocol": rtConnLanProtocol,
       "rtConnWanProtocol": rtConnWanProtocol,
       "rtConnX25LocalDTE": rtConnX25LocalDTE,
       "rtConnX25RemoteDTE": rtConnX25RemoteDTE,
       "rtConnX25CallingFacilities": rtConnX25CallingFacilities,
       "rtConnX25ListeningFacilities": rtConnX25ListeningFacilities,
       "rtConnX25UserData": rtConnX25UserData,
       "rtConnX25Pvc": rtConnX25Pvc,
       "rtConnFrDlci": rtConnFrDlci,
       "rtConnSnaPuName": rtConnSnaPuName,
       "rtConnSnaLocalFqName": rtConnSnaLocalFqName,
       "rtConnSnaRemoteFqName": rtConnSnaRemoteFqName,
       "rtConnSnaModeName": rtConnSnaModeName,
       "rtConnSnaSendPaceWindow": rtConnSnaSendPaceWindow,
       "rtConnSnaReceivePaceWindow": rtConnSnaReceivePaceWindow,
       "rtConnSnaRuSendLow": rtConnSnaRuSendLow,
       "rtConnSnaRuReceiveLow": rtConnSnaRuReceiveLow,
       "rtConnSnaRuSendHigh": rtConnSnaRuSendHigh,
       "rtConnSnaRuReceiveHigh": rtConnSnaRuReceiveHigh,
       "rtConnUsage": rtConnUsage,
       "rtConnFrSegmentation": rtConnFrSegmentation,
       "rtConnFrXid": rtConnFrXid,
       "rtConnPrimOrBackName": rtConnPrimOrBackName,
       "rtConnRipSapUpdateType": rtConnRipSapUpdateType,
       "rtConnSAPDelay": rtConnSAPDelay,
       "rtConnRIPDelay": rtConnRIPDelay,
       "rtIPMapFreeIndex": rtIPMapFreeIndex,
       "rtIPMappingTable": rtIPMappingTable,
       "rtIPMappingEntry": rtIPMappingEntry,
       "rtIPMapIndex": rtIPMapIndex,
       "rtIPMapConnIndex": rtIPMapConnIndex,
       "rtIPMapEntryStatus": rtIPMapEntryStatus,
       "rtIPMapNextHop": rtIPMapNextHop,
       "rtIPMapBroadcast": rtIPMapBroadcast,
       "rtIPMapIPMask": rtIPMapIPMask,
       "rtIPMapVJCompress": rtIPMapVJCompress,
       "rtCircuitTable": rtCircuitTable,
       "rtCircuitEntry": rtCircuitEntry,
       "rtCircuitConnIndex": rtCircuitConnIndex,
       "rtCircuitStatus": rtCircuitStatus,
       "rtCircuitTimeUp": rtCircuitTimeUp,
       "rtCircuitErrCode": rtCircuitErrCode,
       "rtCircuitSessionType": rtCircuitSessionType,
       "rtCircuitConnLSN": rtCircuitConnLSN,
       "rtCircuitDataLSN": rtCircuitDataLSN,
       "rtCircuitCmSelector": rtCircuitCmSelector,
       "rtCircuitCompression": rtCircuitCompression,
       "rtCircuitCompAlgorithm": rtCircuitCompAlgorithm,
       "rtCircuitBeforeComp": rtCircuitBeforeComp,
       "rtCircuitAfterComp": rtCircuitAfterComp,
       "rtCircuitTxErr": rtCircuitTxErr,
       "rtCircuitBoundLANProtocol": rtCircuitBoundLANProtocol,
       "rtCircuitRemoteRouter": rtCircuitRemoteRouter,
       "rtCircuitCountersReset": rtCircuitCountersReset,
       "rtCircuitWanProtocol": rtCircuitWanProtocol,
       "rtCircuitX25LocalDTE": rtCircuitX25LocalDTE,
       "rtCircuitX25RemoteDTE": rtCircuitX25RemoteDTE,
       "rtCircuitX25CallingFacilities": rtCircuitX25CallingFacilities,
       "rtCircuitX25ListeningFacilities": rtCircuitX25ListeningFacilities,
       "rtCircuitX25UserData": rtCircuitX25UserData,
       "rtCircuitX25Cause": rtCircuitX25Cause,
       "rtCircuitX25Diag": rtCircuitX25Diag,
       "rtCircuitX25Pvc": rtCircuitX25Pvc,
       "rtCircuitFrDlci": rtCircuitFrDlci,
       "rtCircuitFrSegmentation": rtCircuitFrSegmentation,
       "rtCircuitFrXIDNegot": rtCircuitFrXIDNegot,
       "rtCircuitFrXIDPacketSize": rtCircuitFrXIDPacketSize,
       "rtCircuitFrCongestion": rtCircuitFrCongestion,
       "rtCircuitIPTable": rtCircuitIPTable,
       "rtCircuitIPEntry": rtCircuitIPEntry,
       "rtCircuitIPConnIndex": rtCircuitIPConnIndex,
       "rtCircuitIPRemoteAddress": rtCircuitIPRemoteAddress,
       "rtCircuitIPLocalAddress": rtCircuitIPLocalAddress,
       "rtCircuitIPTxPackets": rtCircuitIPTxPackets,
       "rtCircuitIPTxBytes": rtCircuitIPTxBytes,
       "rtCircuitIPRxPackets": rtCircuitIPRxPackets,
       "rtCircuitIPRxBytes": rtCircuitIPRxBytes,
       "rtCircuitIPXTable": rtCircuitIPXTable,
       "rtCircuitIPXEntry": rtCircuitIPXEntry,
       "rtCircuitIPXConnIndex": rtCircuitIPXConnIndex,
       "rtCircuitIPXRemoteNode": rtCircuitIPXRemoteNode,
       "rtCircuitIPXRemoteNetwork": rtCircuitIPXRemoteNetwork,
       "rtCircuitIPXLocalNode": rtCircuitIPXLocalNode,
       "rtCircuitIPXLocalNetwork": rtCircuitIPXLocalNetwork,
       "rtCircuitIPXTxPackets": rtCircuitIPXTxPackets,
       "rtCircuitIPXTxBytes": rtCircuitIPXTxBytes,
       "rtCircuitIPXRxPackets": rtCircuitIPXRxPackets,
       "rtCircuitIPXRxBytes": rtCircuitIPXRxBytes,
       "rtCircuitATTable": rtCircuitATTable,
       "rtCircuitATEntry": rtCircuitATEntry,
       "rtCircuitATConnIndex": rtCircuitATConnIndex,
       "rtCircuitATRemoteNet": rtCircuitATRemoteNet,
       "rtCircuitATRemoteNode": rtCircuitATRemoteNode,
       "rtCircuitATLocalNet": rtCircuitATLocalNet,
       "rtCircuitATLocalNode": rtCircuitATLocalNode,
       "rtCircuitATTxPackets": rtCircuitATTxPackets,
       "rtCircuitATTxBytes": rtCircuitATTxBytes,
       "rtCircuitATRxPackets": rtCircuitATRxPackets,
       "rtCircuitATRxBytes": rtCircuitATRxBytes,
       "rtMaxIPFilter": rtMaxIPFilter,
       "rtAvailableIPFilter": rtAvailableIPFilter,
       "rtIPFilterDropStatsIn": rtIPFilterDropStatsIn,
       "rtIPFilterDropStatsOut": rtIPFilterDropStatsOut,
       "rtIPFilterForwardStatsIn": rtIPFilterForwardStatsIn,
       "rtIPFilterForwardStatsOut": rtIPFilterForwardStatsOut,
       "rtIPFilterFreeIndex": rtIPFilterFreeIndex,
       "rtIPFilterTable": rtIPFilterTable,
       "rtIPFilterEntry": rtIPFilterEntry,
       "rtIPFilterConnIndex": rtIPFilterConnIndex,
       "rtIPFilterIndex": rtIPFilterIndex,
       "rtIPFilterEntryStatus": rtIPFilterEntryStatus,
       "rtIPFilterOperState": rtIPFilterOperState,
       "rtIPFilterAdminStateCtr": rtIPFilterAdminStateCtr,
       "rtIPFilterPosition": rtIPFilterPosition,
       "rtIPFilterAction": rtIPFilterAction,
       "rtIPFilterDirection": rtIPFilterDirection,
       "rtIPFilterPortType": rtIPFilterPortType,
       "rtIPFilterLowSrcPort": rtIPFilterLowSrcPort,
       "rtIPFilterHighSrcPort": rtIPFilterHighSrcPort,
       "rtIPFilterLowDestPort": rtIPFilterLowDestPort,
       "rtIPFilterHighDestPort": rtIPFilterHighDestPort,
       "rtIPFilterIPAddressSrc": rtIPFilterIPAddressSrc,
       "rtIPFilterIPMaskSrc": rtIPFilterIPMaskSrc,
       "rtIPFilterIPAddressDest": rtIPFilterIPAddressDest,
       "rtIPFilterIPMaskDest": rtIPFilterIPMaskDest,
       "rtIPFilterStatsIn": rtIPFilterStatsIn,
       "rtIPFilterStatsOut": rtIPFilterStatsOut,
       "rtActionState": rtActionState,
       "rtActionError": rtActionError}
)
