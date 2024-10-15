# SNMP MIB module (HPN-ICF-VOICE-CALL-ACTIVE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-VOICE-CALL-ACTIVE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:09 2024
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

(callActiveIndex,
 callActiveSetupTime) = mibBuilder.importSymbols(
    "DIAL-CONTROL-MIB",
    "callActiveIndex",
    "callActiveSetupTime")

(hpnicfVoice,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfVoice")

(HpnicfCodecType,) = mibBuilder.importSymbols(
    "HPN-ICF-VOICE-DIAL-CONTROL-MIB",
    "HpnicfCodecType")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hpnicfVoCallActive = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15)
)
hpnicfVoCallActive.setRevisions(
        ("2008-02-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfGUid(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



# MIB Managed Objects in the order of their OIDs

_HpnicfVoiceCallActiveObjects_ObjectIdentity = ObjectIdentity
hpnicfVoiceCallActiveObjects = _HpnicfVoiceCallActiveObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1)
)
_HpnicfVoiceCallActiveTable_Object = MibTable
hpnicfVoiceCallActiveTable = _HpnicfVoiceCallActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfVoiceCallActiveTable.setStatus("current")
_HpnicfVoiceCallActiveEntry_Object = MibTableRow
hpnicfVoiceCallActiveEntry = _HpnicfVoiceCallActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 1, 1)
)
hpnicfVoiceCallActiveEntry.setIndexNames(
    (0, "DIAL-CONTROL-MIB", "callActiveSetupTime"),
    (0, "DIAL-CONTROL-MIB", "callActiveIndex"),
)
if mibBuilder.loadTexts:
    hpnicfVoiceCallActiveEntry.setStatus("current")
_HpnicfVoCallActiveConnectionId_Type = HpnicfGUid
_HpnicfVoCallActiveConnectionId_Object = MibTableColumn
hpnicfVoCallActiveConnectionId = _HpnicfVoCallActiveConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 1, 1, 1),
    _HpnicfVoCallActiveConnectionId_Type()
)
hpnicfVoCallActiveConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoCallActiveConnectionId.setStatus("current")
_HpnicfVoCallActiveTxDuration_Type = Gauge32
_HpnicfVoCallActiveTxDuration_Object = MibTableColumn
hpnicfVoCallActiveTxDuration = _HpnicfVoCallActiveTxDuration_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 1, 1, 2),
    _HpnicfVoCallActiveTxDuration_Type()
)
hpnicfVoCallActiveTxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoCallActiveTxDuration.setStatus("current")
_HpnicfVoCallActiveVoiceTxDuration_Type = Gauge32
_HpnicfVoCallActiveVoiceTxDuration_Object = MibTableColumn
hpnicfVoCallActiveVoiceTxDuration = _HpnicfVoCallActiveVoiceTxDuration_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 1, 1, 3),
    _HpnicfVoCallActiveVoiceTxDuration_Type()
)
hpnicfVoCallActiveVoiceTxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoCallActiveVoiceTxDuration.setStatus("current")
_HpnicfVoCallActiveFaxTxDuration_Type = Gauge32
_HpnicfVoCallActiveFaxTxDuration_Object = MibTableColumn
hpnicfVoCallActiveFaxTxDuration = _HpnicfVoCallActiveFaxTxDuration_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 1, 1, 4),
    _HpnicfVoCallActiveFaxTxDuration_Type()
)
hpnicfVoCallActiveFaxTxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoCallActiveFaxTxDuration.setStatus("current")
_HpnicfVoCallActiveCoderType_Type = HpnicfCodecType
_HpnicfVoCallActiveCoderType_Object = MibTableColumn
hpnicfVoCallActiveCoderType = _HpnicfVoCallActiveCoderType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 1, 1, 5),
    _HpnicfVoCallActiveCoderType_Type()
)
hpnicfVoCallActiveCoderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoCallActiveCoderType.setStatus("current")
_HpnicfVoCallActiveImgPageCount_Type = Gauge32
_HpnicfVoCallActiveImgPageCount_Object = MibTableColumn
hpnicfVoCallActiveImgPageCount = _HpnicfVoCallActiveImgPageCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 1, 1, 6),
    _HpnicfVoCallActiveImgPageCount_Type()
)
hpnicfVoCallActiveImgPageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoCallActiveImgPageCount.setStatus("current")
_HpnicfVoiceVoIPCallActiveTable_Object = MibTable
hpnicfVoiceVoIPCallActiveTable = _HpnicfVoiceVoIPCallActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfVoiceVoIPCallActiveTable.setStatus("current")
_HpnicfVoiceVoIPCallActiveEntry_Object = MibTableRow
hpnicfVoiceVoIPCallActiveEntry = _HpnicfVoiceVoIPCallActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 2, 1)
)
hpnicfVoiceVoIPCallActiveEntry.setIndexNames(
    (0, "DIAL-CONTROL-MIB", "callActiveSetupTime"),
    (0, "DIAL-CONTROL-MIB", "callActiveIndex"),
)
if mibBuilder.loadTexts:
    hpnicfVoiceVoIPCallActiveEntry.setStatus("current")
_HpnicfVoVoIPCallActiveConnectionId_Type = HpnicfGUid
_HpnicfVoVoIPCallActiveConnectionId_Object = MibTableColumn
hpnicfVoVoIPCallActiveConnectionId = _HpnicfVoVoIPCallActiveConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 2, 1, 1),
    _HpnicfVoVoIPCallActiveConnectionId_Type()
)
hpnicfVoVoIPCallActiveConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoVoIPCallActiveConnectionId.setStatus("current")
_HpnicfVoVoIPCallActiveRemSigIPType_Type = InetAddressType
_HpnicfVoVoIPCallActiveRemSigIPType_Object = MibTableColumn
hpnicfVoVoIPCallActiveRemSigIPType = _HpnicfVoVoIPCallActiveRemSigIPType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 2, 1, 2),
    _HpnicfVoVoIPCallActiveRemSigIPType_Type()
)
hpnicfVoVoIPCallActiveRemSigIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoVoIPCallActiveRemSigIPType.setStatus("current")
_HpnicfVoVoIPCallActiveRemSigIPAddr_Type = InetAddress
_HpnicfVoVoIPCallActiveRemSigIPAddr_Object = MibTableColumn
hpnicfVoVoIPCallActiveRemSigIPAddr = _HpnicfVoVoIPCallActiveRemSigIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 2, 1, 3),
    _HpnicfVoVoIPCallActiveRemSigIPAddr_Type()
)
hpnicfVoVoIPCallActiveRemSigIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoVoIPCallActiveRemSigIPAddr.setStatus("current")


class _HpnicfVoVoIPCallActiveRemSigPort_Type(Integer32):
    """Custom type hpnicfVoVoIPCallActiveRemSigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfVoVoIPCallActiveRemSigPort_Type.__name__ = "Integer32"
_HpnicfVoVoIPCallActiveRemSigPort_Object = MibTableColumn
hpnicfVoVoIPCallActiveRemSigPort = _HpnicfVoVoIPCallActiveRemSigPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 2, 1, 4),
    _HpnicfVoVoIPCallActiveRemSigPort_Type()
)
hpnicfVoVoIPCallActiveRemSigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoVoIPCallActiveRemSigPort.setStatus("current")
_HpnicfVoVoIPCallActiveRemMedIPType_Type = InetAddressType
_HpnicfVoVoIPCallActiveRemMedIPType_Object = MibTableColumn
hpnicfVoVoIPCallActiveRemMedIPType = _HpnicfVoVoIPCallActiveRemMedIPType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 2, 1, 5),
    _HpnicfVoVoIPCallActiveRemMedIPType_Type()
)
hpnicfVoVoIPCallActiveRemMedIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoVoIPCallActiveRemMedIPType.setStatus("current")
_HpnicfVoVoIPCallActiveRemMedIPAddr_Type = InetAddress
_HpnicfVoVoIPCallActiveRemMedIPAddr_Object = MibTableColumn
hpnicfVoVoIPCallActiveRemMedIPAddr = _HpnicfVoVoIPCallActiveRemMedIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 2, 1, 6),
    _HpnicfVoVoIPCallActiveRemMedIPAddr_Type()
)
hpnicfVoVoIPCallActiveRemMedIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoVoIPCallActiveRemMedIPAddr.setStatus("current")


class _HpnicfVoVoIPCallActiveRemMedPort_Type(Integer32):
    """Custom type hpnicfVoVoIPCallActiveRemMedPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfVoVoIPCallActiveRemMedPort_Type.__name__ = "Integer32"
_HpnicfVoVoIPCallActiveRemMedPort_Object = MibTableColumn
hpnicfVoVoIPCallActiveRemMedPort = _HpnicfVoVoIPCallActiveRemMedPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 2, 1, 7),
    _HpnicfVoVoIPCallActiveRemMedPort_Type()
)
hpnicfVoVoIPCallActiveRemMedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoVoIPCallActiveRemMedPort.setStatus("current")


class _HpnicfVoVoIPCallActiveSessProtocol_Type(Integer32):
    """Custom type hpnicfVoVoIPCallActiveSessProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("h323", 2),
          ("sip", 3),
          ("unknown", 1))
    )


_HpnicfVoVoIPCallActiveSessProtocol_Type.__name__ = "Integer32"
_HpnicfVoVoIPCallActiveSessProtocol_Object = MibTableColumn
hpnicfVoVoIPCallActiveSessProtocol = _HpnicfVoVoIPCallActiveSessProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 2, 1, 8),
    _HpnicfVoVoIPCallActiveSessProtocol_Type()
)
hpnicfVoVoIPCallActiveSessProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoVoIPCallActiveSessProtocol.setStatus("current")
_HpnicfVoVoIPCallActiveCoderType_Type = HpnicfCodecType
_HpnicfVoVoIPCallActiveCoderType_Object = MibTableColumn
hpnicfVoVoIPCallActiveCoderType = _HpnicfVoVoIPCallActiveCoderType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 2, 1, 9),
    _HpnicfVoVoIPCallActiveCoderType_Type()
)
hpnicfVoVoIPCallActiveCoderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoVoIPCallActiveCoderType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-VOICE-CALL-ACTIVE-MIB",
    **{"HpnicfGUid": HpnicfGUid,
       "hpnicfVoCallActive": hpnicfVoCallActive,
       "hpnicfVoiceCallActiveObjects": hpnicfVoiceCallActiveObjects,
       "hpnicfVoiceCallActiveTable": hpnicfVoiceCallActiveTable,
       "hpnicfVoiceCallActiveEntry": hpnicfVoiceCallActiveEntry,
       "hpnicfVoCallActiveConnectionId": hpnicfVoCallActiveConnectionId,
       "hpnicfVoCallActiveTxDuration": hpnicfVoCallActiveTxDuration,
       "hpnicfVoCallActiveVoiceTxDuration": hpnicfVoCallActiveVoiceTxDuration,
       "hpnicfVoCallActiveFaxTxDuration": hpnicfVoCallActiveFaxTxDuration,
       "hpnicfVoCallActiveCoderType": hpnicfVoCallActiveCoderType,
       "hpnicfVoCallActiveImgPageCount": hpnicfVoCallActiveImgPageCount,
       "hpnicfVoiceVoIPCallActiveTable": hpnicfVoiceVoIPCallActiveTable,
       "hpnicfVoiceVoIPCallActiveEntry": hpnicfVoiceVoIPCallActiveEntry,
       "hpnicfVoVoIPCallActiveConnectionId": hpnicfVoVoIPCallActiveConnectionId,
       "hpnicfVoVoIPCallActiveRemSigIPType": hpnicfVoVoIPCallActiveRemSigIPType,
       "hpnicfVoVoIPCallActiveRemSigIPAddr": hpnicfVoVoIPCallActiveRemSigIPAddr,
       "hpnicfVoVoIPCallActiveRemSigPort": hpnicfVoVoIPCallActiveRemSigPort,
       "hpnicfVoVoIPCallActiveRemMedIPType": hpnicfVoVoIPCallActiveRemMedIPType,
       "hpnicfVoVoIPCallActiveRemMedIPAddr": hpnicfVoVoIPCallActiveRemMedIPAddr,
       "hpnicfVoVoIPCallActiveRemMedPort": hpnicfVoVoIPCallActiveRemMedPort,
       "hpnicfVoVoIPCallActiveSessProtocol": hpnicfVoVoIPCallActiveSessProtocol,
       "hpnicfVoVoIPCallActiveCoderType": hpnicfVoVoIPCallActiveCoderType}
)
