# SNMP MIB module (HH3C-VOICE-CALL-ACTIVE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-VOICE-CALL-ACTIVE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:16 2024
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

(hh3cVoice,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cVoice")

(Hh3cCodecType,) = mibBuilder.importSymbols(
    "HH3C-VOICE-DIAL-CONTROL-MIB",
    "Hh3cCodecType")

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

hh3cVoCallActive = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 15)
)
hh3cVoCallActive.setRevisions(
        ("2008-02-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cGUid(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cVoiceCallActiveObjects_ObjectIdentity = ObjectIdentity
hh3cVoiceCallActiveObjects = _Hh3cVoiceCallActiveObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 15, 1)
)
_Hh3cVoiceCallActiveTable_Object = MibTable
hh3cVoiceCallActiveTable = _Hh3cVoiceCallActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 15, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cVoiceCallActiveTable.setStatus("current")
_Hh3cVoiceCallActiveEntry_Object = MibTableRow
hh3cVoiceCallActiveEntry = _Hh3cVoiceCallActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 15, 1, 1, 1)
)
hh3cVoiceCallActiveEntry.setIndexNames(
    (0, "DIAL-CONTROL-MIB", "callActiveSetupTime"),
    (0, "DIAL-CONTROL-MIB", "callActiveIndex"),
)
if mibBuilder.loadTexts:
    hh3cVoiceCallActiveEntry.setStatus("current")
_Hh3cVoCallActiveConnectionId_Type = Hh3cGUid
_Hh3cVoCallActiveConnectionId_Object = MibTableColumn
hh3cVoCallActiveConnectionId = _Hh3cVoCallActiveConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 15, 1, 1, 1, 1),
    _Hh3cVoCallActiveConnectionId_Type()
)
hh3cVoCallActiveConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoCallActiveConnectionId.setStatus("current")
_Hh3cVoCallActiveTxDuration_Type = Gauge32
_Hh3cVoCallActiveTxDuration_Object = MibTableColumn
hh3cVoCallActiveTxDuration = _Hh3cVoCallActiveTxDuration_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 15, 1, 1, 1, 2),
    _Hh3cVoCallActiveTxDuration_Type()
)
hh3cVoCallActiveTxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoCallActiveTxDuration.setStatus("current")
_Hh3cVoCallActiveVoiceTxDuration_Type = Gauge32
_Hh3cVoCallActiveVoiceTxDuration_Object = MibTableColumn
hh3cVoCallActiveVoiceTxDuration = _Hh3cVoCallActiveVoiceTxDuration_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 15, 1, 1, 1, 3),
    _Hh3cVoCallActiveVoiceTxDuration_Type()
)
hh3cVoCallActiveVoiceTxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoCallActiveVoiceTxDuration.setStatus("current")
_Hh3cVoCallActiveFaxTxDuration_Type = Gauge32
_Hh3cVoCallActiveFaxTxDuration_Object = MibTableColumn
hh3cVoCallActiveFaxTxDuration = _Hh3cVoCallActiveFaxTxDuration_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 15, 1, 1, 1, 4),
    _Hh3cVoCallActiveFaxTxDuration_Type()
)
hh3cVoCallActiveFaxTxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoCallActiveFaxTxDuration.setStatus("current")
_Hh3cVoCallActiveCoderType_Type = Hh3cCodecType
_Hh3cVoCallActiveCoderType_Object = MibTableColumn
hh3cVoCallActiveCoderType = _Hh3cVoCallActiveCoderType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 15, 1, 1, 1, 5),
    _Hh3cVoCallActiveCoderType_Type()
)
hh3cVoCallActiveCoderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoCallActiveCoderType.setStatus("current")
_Hh3cVoCallActiveImgPageCount_Type = Gauge32
_Hh3cVoCallActiveImgPageCount_Object = MibTableColumn
hh3cVoCallActiveImgPageCount = _Hh3cVoCallActiveImgPageCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 15, 1, 1, 1, 6),
    _Hh3cVoCallActiveImgPageCount_Type()
)
hh3cVoCallActiveImgPageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoCallActiveImgPageCount.setStatus("current")
_Hh3cVoiceVoIPCallActiveTable_Object = MibTable
hh3cVoiceVoIPCallActiveTable = _Hh3cVoiceVoIPCallActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 15, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cVoiceVoIPCallActiveTable.setStatus("current")
_Hh3cVoiceVoIPCallActiveEntry_Object = MibTableRow
hh3cVoiceVoIPCallActiveEntry = _Hh3cVoiceVoIPCallActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 15, 1, 2, 1)
)
hh3cVoiceVoIPCallActiveEntry.setIndexNames(
    (0, "DIAL-CONTROL-MIB", "callActiveSetupTime"),
    (0, "DIAL-CONTROL-MIB", "callActiveIndex"),
)
if mibBuilder.loadTexts:
    hh3cVoiceVoIPCallActiveEntry.setStatus("current")
_Hh3cVoVoIPCallActiveConnectionId_Type = Hh3cGUid
_Hh3cVoVoIPCallActiveConnectionId_Object = MibTableColumn
hh3cVoVoIPCallActiveConnectionId = _Hh3cVoVoIPCallActiveConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 15, 1, 2, 1, 1),
    _Hh3cVoVoIPCallActiveConnectionId_Type()
)
hh3cVoVoIPCallActiveConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoVoIPCallActiveConnectionId.setStatus("current")
_Hh3cVoVoIPCallActiveRemSigIPType_Type = InetAddressType
_Hh3cVoVoIPCallActiveRemSigIPType_Object = MibTableColumn
hh3cVoVoIPCallActiveRemSigIPType = _Hh3cVoVoIPCallActiveRemSigIPType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 15, 1, 2, 1, 2),
    _Hh3cVoVoIPCallActiveRemSigIPType_Type()
)
hh3cVoVoIPCallActiveRemSigIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoVoIPCallActiveRemSigIPType.setStatus("current")
_Hh3cVoVoIPCallActiveRemSigIPAddr_Type = InetAddress
_Hh3cVoVoIPCallActiveRemSigIPAddr_Object = MibTableColumn
hh3cVoVoIPCallActiveRemSigIPAddr = _Hh3cVoVoIPCallActiveRemSigIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 15, 1, 2, 1, 3),
    _Hh3cVoVoIPCallActiveRemSigIPAddr_Type()
)
hh3cVoVoIPCallActiveRemSigIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoVoIPCallActiveRemSigIPAddr.setStatus("current")


class _Hh3cVoVoIPCallActiveRemSigPort_Type(Integer32):
    """Custom type hh3cVoVoIPCallActiveRemSigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cVoVoIPCallActiveRemSigPort_Type.__name__ = "Integer32"
_Hh3cVoVoIPCallActiveRemSigPort_Object = MibTableColumn
hh3cVoVoIPCallActiveRemSigPort = _Hh3cVoVoIPCallActiveRemSigPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 15, 1, 2, 1, 4),
    _Hh3cVoVoIPCallActiveRemSigPort_Type()
)
hh3cVoVoIPCallActiveRemSigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoVoIPCallActiveRemSigPort.setStatus("current")
_Hh3cVoVoIPCallActiveRemMedIPType_Type = InetAddressType
_Hh3cVoVoIPCallActiveRemMedIPType_Object = MibTableColumn
hh3cVoVoIPCallActiveRemMedIPType = _Hh3cVoVoIPCallActiveRemMedIPType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 15, 1, 2, 1, 5),
    _Hh3cVoVoIPCallActiveRemMedIPType_Type()
)
hh3cVoVoIPCallActiveRemMedIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoVoIPCallActiveRemMedIPType.setStatus("current")
_Hh3cVoVoIPCallActiveRemMedIPAddr_Type = InetAddress
_Hh3cVoVoIPCallActiveRemMedIPAddr_Object = MibTableColumn
hh3cVoVoIPCallActiveRemMedIPAddr = _Hh3cVoVoIPCallActiveRemMedIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 15, 1, 2, 1, 6),
    _Hh3cVoVoIPCallActiveRemMedIPAddr_Type()
)
hh3cVoVoIPCallActiveRemMedIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoVoIPCallActiveRemMedIPAddr.setStatus("current")


class _Hh3cVoVoIPCallActiveRemMedPort_Type(Integer32):
    """Custom type hh3cVoVoIPCallActiveRemMedPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cVoVoIPCallActiveRemMedPort_Type.__name__ = "Integer32"
_Hh3cVoVoIPCallActiveRemMedPort_Object = MibTableColumn
hh3cVoVoIPCallActiveRemMedPort = _Hh3cVoVoIPCallActiveRemMedPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 15, 1, 2, 1, 7),
    _Hh3cVoVoIPCallActiveRemMedPort_Type()
)
hh3cVoVoIPCallActiveRemMedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoVoIPCallActiveRemMedPort.setStatus("current")


class _Hh3cVoVoIPCallActiveSessProtocol_Type(Integer32):
    """Custom type hh3cVoVoIPCallActiveSessProtocol based on Integer32"""
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


_Hh3cVoVoIPCallActiveSessProtocol_Type.__name__ = "Integer32"
_Hh3cVoVoIPCallActiveSessProtocol_Object = MibTableColumn
hh3cVoVoIPCallActiveSessProtocol = _Hh3cVoVoIPCallActiveSessProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 15, 1, 2, 1, 8),
    _Hh3cVoVoIPCallActiveSessProtocol_Type()
)
hh3cVoVoIPCallActiveSessProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoVoIPCallActiveSessProtocol.setStatus("current")
_Hh3cVoVoIPCallActiveCoderType_Type = Hh3cCodecType
_Hh3cVoVoIPCallActiveCoderType_Object = MibTableColumn
hh3cVoVoIPCallActiveCoderType = _Hh3cVoVoIPCallActiveCoderType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 15, 1, 2, 1, 9),
    _Hh3cVoVoIPCallActiveCoderType_Type()
)
hh3cVoVoIPCallActiveCoderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoVoIPCallActiveCoderType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-VOICE-CALL-ACTIVE-MIB",
    **{"Hh3cGUid": Hh3cGUid,
       "hh3cVoCallActive": hh3cVoCallActive,
       "hh3cVoiceCallActiveObjects": hh3cVoiceCallActiveObjects,
       "hh3cVoiceCallActiveTable": hh3cVoiceCallActiveTable,
       "hh3cVoiceCallActiveEntry": hh3cVoiceCallActiveEntry,
       "hh3cVoCallActiveConnectionId": hh3cVoCallActiveConnectionId,
       "hh3cVoCallActiveTxDuration": hh3cVoCallActiveTxDuration,
       "hh3cVoCallActiveVoiceTxDuration": hh3cVoCallActiveVoiceTxDuration,
       "hh3cVoCallActiveFaxTxDuration": hh3cVoCallActiveFaxTxDuration,
       "hh3cVoCallActiveCoderType": hh3cVoCallActiveCoderType,
       "hh3cVoCallActiveImgPageCount": hh3cVoCallActiveImgPageCount,
       "hh3cVoiceVoIPCallActiveTable": hh3cVoiceVoIPCallActiveTable,
       "hh3cVoiceVoIPCallActiveEntry": hh3cVoiceVoIPCallActiveEntry,
       "hh3cVoVoIPCallActiveConnectionId": hh3cVoVoIPCallActiveConnectionId,
       "hh3cVoVoIPCallActiveRemSigIPType": hh3cVoVoIPCallActiveRemSigIPType,
       "hh3cVoVoIPCallActiveRemSigIPAddr": hh3cVoVoIPCallActiveRemSigIPAddr,
       "hh3cVoVoIPCallActiveRemSigPort": hh3cVoVoIPCallActiveRemSigPort,
       "hh3cVoVoIPCallActiveRemMedIPType": hh3cVoVoIPCallActiveRemMedIPType,
       "hh3cVoVoIPCallActiveRemMedIPAddr": hh3cVoVoIPCallActiveRemMedIPAddr,
       "hh3cVoVoIPCallActiveRemMedPort": hh3cVoVoIPCallActiveRemMedPort,
       "hh3cVoVoIPCallActiveSessProtocol": hh3cVoVoIPCallActiveSessProtocol,
       "hh3cVoVoIPCallActiveCoderType": hh3cVoVoIPCallActiveCoderType}
)
