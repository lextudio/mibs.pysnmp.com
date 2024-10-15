# SNMP MIB module (CISCO-CDMA-AHDLC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CDMA-AHDLC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:10 2024
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

(EntPhysicalIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "EntPhysicalIndexOrZero")

(ZeroBasedCounter32,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "ZeroBasedCounter32")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cCdmaAhdlcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 997)
)
cCdmaAhdlcMIB.setRevisions(
        ("2005-11-14 00:00",
         "2002-01-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CCdmaAhdlcMIBNotif_ObjectIdentity = ObjectIdentity
cCdmaAhdlcMIBNotif = _CCdmaAhdlcMIBNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 0)
)
_CCdmaAhdlcMIBObjects_ObjectIdentity = ObjectIdentity
cCdmaAhdlcMIBObjects = _CCdmaAhdlcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1)
)
_CCdmaAhdlcEngineInfo_ObjectIdentity = ObjectIdentity
cCdmaAhdlcEngineInfo = _CCdmaAhdlcEngineInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1)
)
_CCdmaAhdlcEngineTable_Object = MibTable
cCdmaAhdlcEngineTable = _CCdmaAhdlcEngineTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cCdmaAhdlcEngineTable.setStatus("current")
_CCdmaAhdlcEngineEntry_Object = MibTableRow
cCdmaAhdlcEngineEntry = _CCdmaAhdlcEngineEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 1, 1)
)
cCdmaAhdlcEngineEntry.setIndexNames(
    (0, "CISCO-CDMA-AHDLC-MIB", "cCdmaAhdlcEngineIndex"),
)
if mibBuilder.loadTexts:
    cCdmaAhdlcEngineEntry.setStatus("current")
_CCdmaAhdlcEngineIndex_Type = Unsigned32
_CCdmaAhdlcEngineIndex_Object = MibTableColumn
cCdmaAhdlcEngineIndex = _CCdmaAhdlcEngineIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 1, 1, 1),
    _CCdmaAhdlcEngineIndex_Type()
)
cCdmaAhdlcEngineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCdmaAhdlcEngineIndex.setStatus("current")
_CCdmaAhdlcEngineName_Type = SnmpAdminString
_CCdmaAhdlcEngineName_Object = MibTableColumn
cCdmaAhdlcEngineName = _CCdmaAhdlcEngineName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 1, 1, 2),
    _CCdmaAhdlcEngineName_Type()
)
cCdmaAhdlcEngineName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAhdlcEngineName.setStatus("current")


class _CCdmaAhdlcEngineType_Type(Integer32):
    """Custom type cCdmaAhdlcEngineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("software", 1),
          ("unknown", 0))
    )


_CCdmaAhdlcEngineType_Type.__name__ = "Integer32"
_CCdmaAhdlcEngineType_Object = MibTableColumn
cCdmaAhdlcEngineType = _CCdmaAhdlcEngineType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 1, 1, 3),
    _CCdmaAhdlcEngineType_Type()
)
cCdmaAhdlcEngineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAhdlcEngineType.setStatus("current")
_CCdmaAhdlcEngineChannelsInUse_Type = Gauge32
_CCdmaAhdlcEngineChannelsInUse_Object = MibTableColumn
cCdmaAhdlcEngineChannelsInUse = _CCdmaAhdlcEngineChannelsInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 1, 1, 4),
    _CCdmaAhdlcEngineChannelsInUse_Type()
)
cCdmaAhdlcEngineChannelsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAhdlcEngineChannelsInUse.setStatus("current")
_CCdmaAhdlcEngineMaxChannels_Type = Unsigned32
_CCdmaAhdlcEngineMaxChannels_Object = MibTableColumn
cCdmaAhdlcEngineMaxChannels = _CCdmaAhdlcEngineMaxChannels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 1, 1, 5),
    _CCdmaAhdlcEngineMaxChannels_Type()
)
cCdmaAhdlcEngineMaxChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAhdlcEngineMaxChannels.setStatus("current")
_CCdmaAhdlcEngineConfMaxChannels_Type = Unsigned32
_CCdmaAhdlcEngineConfMaxChannels_Object = MibTableColumn
cCdmaAhdlcEngineConfMaxChannels = _CCdmaAhdlcEngineConfMaxChannels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 1, 1, 6),
    _CCdmaAhdlcEngineConfMaxChannels_Type()
)
cCdmaAhdlcEngineConfMaxChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cCdmaAhdlcEngineConfMaxChannels.setStatus("current")


class _CCdmaAhdlcEngineOperState_Type(Integer32):
    """Custom type cCdmaAhdlcEngineOperState based on Integer32"""
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
          ("unknown", 0),
          ("up", 1))
    )


_CCdmaAhdlcEngineOperState_Type.__name__ = "Integer32"
_CCdmaAhdlcEngineOperState_Object = MibTableColumn
cCdmaAhdlcEngineOperState = _CCdmaAhdlcEngineOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 1, 1, 7),
    _CCdmaAhdlcEngineOperState_Type()
)
cCdmaAhdlcEngineOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAhdlcEngineOperState.setStatus("current")


class _CCdmaAhdlcEngineAdminState_Type(Integer32):
    """Custom type cCdmaAhdlcEngineAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CCdmaAhdlcEngineAdminState_Type.__name__ = "Integer32"
_CCdmaAhdlcEngineAdminState_Object = MibTableColumn
cCdmaAhdlcEngineAdminState = _CCdmaAhdlcEngineAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 1, 1, 8),
    _CCdmaAhdlcEngineAdminState_Type()
)
cCdmaAhdlcEngineAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cCdmaAhdlcEngineAdminState.setStatus("current")
_CCdmaAhdlcEngineDownNotifEnabled_Type = TruthValue
_CCdmaAhdlcEngineDownNotifEnabled_Object = MibTableColumn
cCdmaAhdlcEngineDownNotifEnabled = _CCdmaAhdlcEngineDownNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 1, 1, 9),
    _CCdmaAhdlcEngineDownNotifEnabled_Type()
)
cCdmaAhdlcEngineDownNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cCdmaAhdlcEngineDownNotifEnabled.setStatus("current")
_CCdmaAhdlcPhysicalIndex_Type = EntPhysicalIndexOrZero
_CCdmaAhdlcPhysicalIndex_Object = MibTableColumn
cCdmaAhdlcPhysicalIndex = _CCdmaAhdlcPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 1, 1, 10),
    _CCdmaAhdlcPhysicalIndex_Type()
)
cCdmaAhdlcPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAhdlcPhysicalIndex.setStatus("current")
_CCdmaAhdlcPerfTable_Object = MibTable
cCdmaAhdlcPerfTable = _CCdmaAhdlcPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cCdmaAhdlcPerfTable.setStatus("current")
_CCdmaAhdlcPerfEntry_Object = MibTableRow
cCdmaAhdlcPerfEntry = _CCdmaAhdlcPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cCdmaAhdlcPerfEntry.setStatus("current")
_CCdmaAhdlcOutgoingOctetsToEncode_Type = ZeroBasedCounter32
_CCdmaAhdlcOutgoingOctetsToEncode_Object = MibTableColumn
cCdmaAhdlcOutgoingOctetsToEncode = _CCdmaAhdlcOutgoingOctetsToEncode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 2, 1, 1),
    _CCdmaAhdlcOutgoingOctetsToEncode_Type()
)
cCdmaAhdlcOutgoingOctetsToEncode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAhdlcOutgoingOctetsToEncode.setStatus("current")
_CCdmaAhdlcOutgoingOctetsEncoded_Type = ZeroBasedCounter32
_CCdmaAhdlcOutgoingOctetsEncoded_Object = MibTableColumn
cCdmaAhdlcOutgoingOctetsEncoded = _CCdmaAhdlcOutgoingOctetsEncoded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 2, 1, 2),
    _CCdmaAhdlcOutgoingOctetsEncoded_Type()
)
cCdmaAhdlcOutgoingOctetsEncoded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAhdlcOutgoingOctetsEncoded.setStatus("current")
_CCdmaAhdlcOutgoingPktsToEncode_Type = ZeroBasedCounter32
_CCdmaAhdlcOutgoingPktsToEncode_Object = MibTableColumn
cCdmaAhdlcOutgoingPktsToEncode = _CCdmaAhdlcOutgoingPktsToEncode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 2, 1, 3),
    _CCdmaAhdlcOutgoingPktsToEncode_Type()
)
cCdmaAhdlcOutgoingPktsToEncode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAhdlcOutgoingPktsToEncode.setStatus("current")
_CCdmaAhdlcOutgoingPktsEncoded_Type = ZeroBasedCounter32
_CCdmaAhdlcOutgoingPktsEncoded_Object = MibTableColumn
cCdmaAhdlcOutgoingPktsEncoded = _CCdmaAhdlcOutgoingPktsEncoded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 2, 1, 4),
    _CCdmaAhdlcOutgoingPktsEncoded_Type()
)
cCdmaAhdlcOutgoingPktsEncoded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAhdlcOutgoingPktsEncoded.setStatus("current")
_CCdmaAhdlcIncomingOctetsToDecode_Type = ZeroBasedCounter32
_CCdmaAhdlcIncomingOctetsToDecode_Object = MibTableColumn
cCdmaAhdlcIncomingOctetsToDecode = _CCdmaAhdlcIncomingOctetsToDecode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 2, 1, 5),
    _CCdmaAhdlcIncomingOctetsToDecode_Type()
)
cCdmaAhdlcIncomingOctetsToDecode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAhdlcIncomingOctetsToDecode.setStatus("current")
_CCdmaAhdlcIncomingOctetsDecoded_Type = ZeroBasedCounter32
_CCdmaAhdlcIncomingOctetsDecoded_Object = MibTableColumn
cCdmaAhdlcIncomingOctetsDecoded = _CCdmaAhdlcIncomingOctetsDecoded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 2, 1, 6),
    _CCdmaAhdlcIncomingOctetsDecoded_Type()
)
cCdmaAhdlcIncomingOctetsDecoded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAhdlcIncomingOctetsDecoded.setStatus("current")
_CCdmaAhdlcIncomingPktsToDecode_Type = ZeroBasedCounter32
_CCdmaAhdlcIncomingPktsToDecode_Object = MibTableColumn
cCdmaAhdlcIncomingPktsToDecode = _CCdmaAhdlcIncomingPktsToDecode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 2, 1, 7),
    _CCdmaAhdlcIncomingPktsToDecode_Type()
)
cCdmaAhdlcIncomingPktsToDecode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAhdlcIncomingPktsToDecode.setStatus("current")
_CCdmaAhdlcIncomingPktsDecoded_Type = ZeroBasedCounter32
_CCdmaAhdlcIncomingPktsDecoded_Object = MibTableColumn
cCdmaAhdlcIncomingPktsDecoded = _CCdmaAhdlcIncomingPktsDecoded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 2, 1, 8),
    _CCdmaAhdlcIncomingPktsDecoded_Type()
)
cCdmaAhdlcIncomingPktsDecoded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAhdlcIncomingPktsDecoded.setStatus("current")
_CCdmaAhdlcDropPktsDec_Type = ZeroBasedCounter32
_CCdmaAhdlcDropPktsDec_Object = MibTableColumn
cCdmaAhdlcDropPktsDec = _CCdmaAhdlcDropPktsDec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 2, 1, 9),
    _CCdmaAhdlcDropPktsDec_Type()
)
cCdmaAhdlcDropPktsDec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAhdlcDropPktsDec.setStatus("current")
_CCdmaAhdlcDropPktsEnc_Type = ZeroBasedCounter32
_CCdmaAhdlcDropPktsEnc_Object = MibTableColumn
cCdmaAhdlcDropPktsEnc = _CCdmaAhdlcDropPktsEnc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 2, 1, 10),
    _CCdmaAhdlcDropPktsEnc_Type()
)
cCdmaAhdlcDropPktsEnc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAhdlcDropPktsEnc.setStatus("current")
_CCdmaAhdlcCRCDropPkts_Type = ZeroBasedCounter32
_CCdmaAhdlcCRCDropPkts_Object = MibTableColumn
cCdmaAhdlcCRCDropPkts = _CCdmaAhdlcCRCDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 2, 1, 11),
    _CCdmaAhdlcCRCDropPkts_Type()
)
cCdmaAhdlcCRCDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAhdlcCRCDropPkts.setStatus("current")
_CCdmaAhdlcMemDropPktsDec_Type = ZeroBasedCounter32
_CCdmaAhdlcMemDropPktsDec_Object = MibTableColumn
cCdmaAhdlcMemDropPktsDec = _CCdmaAhdlcMemDropPktsDec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 2, 1, 12),
    _CCdmaAhdlcMemDropPktsDec_Type()
)
cCdmaAhdlcMemDropPktsDec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAhdlcMemDropPktsDec.setStatus("current")
_CCdmaAhdlcMemDropPktsEnc_Type = ZeroBasedCounter32
_CCdmaAhdlcMemDropPktsEnc_Object = MibTableColumn
cCdmaAhdlcMemDropPktsEnc = _CCdmaAhdlcMemDropPktsEnc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 2, 1, 13),
    _CCdmaAhdlcMemDropPktsEnc_Type()
)
cCdmaAhdlcMemDropPktsEnc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAhdlcMemDropPktsEnc.setStatus("current")
_CCdmaAhdlcOverflowDropPktsDec_Type = ZeroBasedCounter32
_CCdmaAhdlcOverflowDropPktsDec_Object = MibTableColumn
cCdmaAhdlcOverflowDropPktsDec = _CCdmaAhdlcOverflowDropPktsDec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 2, 1, 14),
    _CCdmaAhdlcOverflowDropPktsDec_Type()
)
cCdmaAhdlcOverflowDropPktsDec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAhdlcOverflowDropPktsDec.setStatus("current")
_CCdmaAhdlcOverflowDropPktsEnc_Type = ZeroBasedCounter32
_CCdmaAhdlcOverflowDropPktsEnc_Object = MibTableColumn
cCdmaAhdlcOverflowDropPktsEnc = _CCdmaAhdlcOverflowDropPktsEnc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 2, 1, 15),
    _CCdmaAhdlcOverflowDropPktsEnc_Type()
)
cCdmaAhdlcOverflowDropPktsEnc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAhdlcOverflowDropPktsEnc.setStatus("current")
_CCdmaAhdlcInvSizeDropPktsDec_Type = ZeroBasedCounter32
_CCdmaAhdlcInvSizeDropPktsDec_Object = MibTableColumn
cCdmaAhdlcInvSizeDropPktsDec = _CCdmaAhdlcInvSizeDropPktsDec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 2, 1, 16),
    _CCdmaAhdlcInvSizeDropPktsDec_Type()
)
cCdmaAhdlcInvSizeDropPktsDec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAhdlcInvSizeDropPktsDec.setStatus("current")
_CCdmaAhdlcInvSizeDropPktsEnc_Type = ZeroBasedCounter32
_CCdmaAhdlcInvSizeDropPktsEnc_Object = MibTableColumn
cCdmaAhdlcInvSizeDropPktsEnc = _CCdmaAhdlcInvSizeDropPktsEnc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 2, 1, 17),
    _CCdmaAhdlcInvSizeDropPktsEnc_Type()
)
cCdmaAhdlcInvSizeDropPktsEnc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAhdlcInvSizeDropPktsEnc.setStatus("current")
_CCdmaAhdlcDiscontinuityTime_Type = TimeStamp
_CCdmaAhdlcDiscontinuityTime_Object = MibTableColumn
cCdmaAhdlcDiscontinuityTime = _CCdmaAhdlcDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 1, 1, 2, 1, 18),
    _CCdmaAhdlcDiscontinuityTime_Type()
)
cCdmaAhdlcDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAhdlcDiscontinuityTime.setStatus("current")
_CCdmaAhdlcMIBConformance_ObjectIdentity = ObjectIdentity
cCdmaAhdlcMIBConformance = _CCdmaAhdlcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 3)
)
_CCdmaAhdlcMIBCompliances_ObjectIdentity = ObjectIdentity
cCdmaAhdlcMIBCompliances = _CCdmaAhdlcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 3, 1)
)
_CCdmaAhdlcMIBGroups_ObjectIdentity = ObjectIdentity
cCdmaAhdlcMIBGroups = _CCdmaAhdlcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 3, 2)
)
cCdmaAhdlcEngineEntry.registerAugmentions(
    ("CISCO-CDMA-AHDLC-MIB",
     "cCdmaAhdlcPerfEntry")
)
cCdmaAhdlcPerfEntry.setIndexNames(*cCdmaAhdlcEngineEntry.getIndexNames())

# Managed Objects groups

cCdmaAhdlcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 3, 2, 1)
)
cCdmaAhdlcGroup.setObjects(
      *(("CISCO-CDMA-AHDLC-MIB", "cCdmaAhdlcEngineName"),
        ("CISCO-CDMA-AHDLC-MIB", "cCdmaAhdlcEngineType"),
        ("CISCO-CDMA-AHDLC-MIB", "cCdmaAhdlcEngineMaxChannels"),
        ("CISCO-CDMA-AHDLC-MIB", "cCdmaAhdlcEngineConfMaxChannels"),
        ("CISCO-CDMA-AHDLC-MIB", "cCdmaAhdlcEngineChannelsInUse"),
        ("CISCO-CDMA-AHDLC-MIB", "cCdmaAhdlcEngineOperState"),
        ("CISCO-CDMA-AHDLC-MIB", "cCdmaAhdlcEngineAdminState"),
        ("CISCO-CDMA-AHDLC-MIB", "cCdmaAhdlcEngineDownNotifEnabled"),
        ("CISCO-CDMA-AHDLC-MIB", "cCdmaAhdlcPhysicalIndex"),
        ("CISCO-CDMA-AHDLC-MIB", "cCdmaAhdlcOutgoingOctetsToEncode"),
        ("CISCO-CDMA-AHDLC-MIB", "cCdmaAhdlcOutgoingOctetsEncoded"),
        ("CISCO-CDMA-AHDLC-MIB", "cCdmaAhdlcOutgoingPktsToEncode"),
        ("CISCO-CDMA-AHDLC-MIB", "cCdmaAhdlcOutgoingPktsEncoded"),
        ("CISCO-CDMA-AHDLC-MIB", "cCdmaAhdlcIncomingOctetsToDecode"),
        ("CISCO-CDMA-AHDLC-MIB", "cCdmaAhdlcIncomingOctetsDecoded"),
        ("CISCO-CDMA-AHDLC-MIB", "cCdmaAhdlcIncomingPktsToDecode"),
        ("CISCO-CDMA-AHDLC-MIB", "cCdmaAhdlcIncomingPktsDecoded"),
        ("CISCO-CDMA-AHDLC-MIB", "cCdmaAhdlcDropPktsDec"),
        ("CISCO-CDMA-AHDLC-MIB", "cCdmaAhdlcDropPktsEnc"),
        ("CISCO-CDMA-AHDLC-MIB", "cCdmaAhdlcCRCDropPkts"),
        ("CISCO-CDMA-AHDLC-MIB", "cCdmaAhdlcMemDropPktsDec"),
        ("CISCO-CDMA-AHDLC-MIB", "cCdmaAhdlcMemDropPktsEnc"),
        ("CISCO-CDMA-AHDLC-MIB", "cCdmaAhdlcOverflowDropPktsDec"),
        ("CISCO-CDMA-AHDLC-MIB", "cCdmaAhdlcOverflowDropPktsEnc"),
        ("CISCO-CDMA-AHDLC-MIB", "cCdmaAhdlcInvSizeDropPktsDec"),
        ("CISCO-CDMA-AHDLC-MIB", "cCdmaAhdlcInvSizeDropPktsEnc"),
        ("CISCO-CDMA-AHDLC-MIB", "cCdmaAhdlcDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    cCdmaAhdlcGroup.setStatus("current")


# Notification objects

cCdmaAhdlcEngineDownNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 0, 1)
)
cCdmaAhdlcEngineDownNotif.setObjects(
      *(("CISCO-CDMA-AHDLC-MIB", "cCdmaAhdlcEngineOperState"),
        ("CISCO-CDMA-AHDLC-MIB", "cCdmaAhdlcEngineAdminState"))
)
if mibBuilder.loadTexts:
    cCdmaAhdlcEngineDownNotif.setStatus(
        "current"
    )


# Notifications groups

cCdmaAhdlcNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 3, 2, 2)
)
cCdmaAhdlcNotifGroup.setObjects(
    ("CISCO-CDMA-AHDLC-MIB", "cCdmaAhdlcEngineDownNotif")
)
if mibBuilder.loadTexts:
    cCdmaAhdlcNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cCdmaAhdlcMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 997, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cCdmaAhdlcMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CDMA-AHDLC-MIB",
    **{"cCdmaAhdlcMIB": cCdmaAhdlcMIB,
       "cCdmaAhdlcMIBNotif": cCdmaAhdlcMIBNotif,
       "cCdmaAhdlcEngineDownNotif": cCdmaAhdlcEngineDownNotif,
       "cCdmaAhdlcMIBObjects": cCdmaAhdlcMIBObjects,
       "cCdmaAhdlcEngineInfo": cCdmaAhdlcEngineInfo,
       "cCdmaAhdlcEngineTable": cCdmaAhdlcEngineTable,
       "cCdmaAhdlcEngineEntry": cCdmaAhdlcEngineEntry,
       "cCdmaAhdlcEngineIndex": cCdmaAhdlcEngineIndex,
       "cCdmaAhdlcEngineName": cCdmaAhdlcEngineName,
       "cCdmaAhdlcEngineType": cCdmaAhdlcEngineType,
       "cCdmaAhdlcEngineChannelsInUse": cCdmaAhdlcEngineChannelsInUse,
       "cCdmaAhdlcEngineMaxChannels": cCdmaAhdlcEngineMaxChannels,
       "cCdmaAhdlcEngineConfMaxChannels": cCdmaAhdlcEngineConfMaxChannels,
       "cCdmaAhdlcEngineOperState": cCdmaAhdlcEngineOperState,
       "cCdmaAhdlcEngineAdminState": cCdmaAhdlcEngineAdminState,
       "cCdmaAhdlcEngineDownNotifEnabled": cCdmaAhdlcEngineDownNotifEnabled,
       "cCdmaAhdlcPhysicalIndex": cCdmaAhdlcPhysicalIndex,
       "cCdmaAhdlcPerfTable": cCdmaAhdlcPerfTable,
       "cCdmaAhdlcPerfEntry": cCdmaAhdlcPerfEntry,
       "cCdmaAhdlcOutgoingOctetsToEncode": cCdmaAhdlcOutgoingOctetsToEncode,
       "cCdmaAhdlcOutgoingOctetsEncoded": cCdmaAhdlcOutgoingOctetsEncoded,
       "cCdmaAhdlcOutgoingPktsToEncode": cCdmaAhdlcOutgoingPktsToEncode,
       "cCdmaAhdlcOutgoingPktsEncoded": cCdmaAhdlcOutgoingPktsEncoded,
       "cCdmaAhdlcIncomingOctetsToDecode": cCdmaAhdlcIncomingOctetsToDecode,
       "cCdmaAhdlcIncomingOctetsDecoded": cCdmaAhdlcIncomingOctetsDecoded,
       "cCdmaAhdlcIncomingPktsToDecode": cCdmaAhdlcIncomingPktsToDecode,
       "cCdmaAhdlcIncomingPktsDecoded": cCdmaAhdlcIncomingPktsDecoded,
       "cCdmaAhdlcDropPktsDec": cCdmaAhdlcDropPktsDec,
       "cCdmaAhdlcDropPktsEnc": cCdmaAhdlcDropPktsEnc,
       "cCdmaAhdlcCRCDropPkts": cCdmaAhdlcCRCDropPkts,
       "cCdmaAhdlcMemDropPktsDec": cCdmaAhdlcMemDropPktsDec,
       "cCdmaAhdlcMemDropPktsEnc": cCdmaAhdlcMemDropPktsEnc,
       "cCdmaAhdlcOverflowDropPktsDec": cCdmaAhdlcOverflowDropPktsDec,
       "cCdmaAhdlcOverflowDropPktsEnc": cCdmaAhdlcOverflowDropPktsEnc,
       "cCdmaAhdlcInvSizeDropPktsDec": cCdmaAhdlcInvSizeDropPktsDec,
       "cCdmaAhdlcInvSizeDropPktsEnc": cCdmaAhdlcInvSizeDropPktsEnc,
       "cCdmaAhdlcDiscontinuityTime": cCdmaAhdlcDiscontinuityTime,
       "cCdmaAhdlcMIBConformance": cCdmaAhdlcMIBConformance,
       "cCdmaAhdlcMIBCompliances": cCdmaAhdlcMIBCompliances,
       "cCdmaAhdlcMIBCompliance": cCdmaAhdlcMIBCompliance,
       "cCdmaAhdlcMIBGroups": cCdmaAhdlcMIBGroups,
       "cCdmaAhdlcGroup": cCdmaAhdlcGroup,
       "cCdmaAhdlcNotifGroup": cCdmaAhdlcNotifGroup}
)
