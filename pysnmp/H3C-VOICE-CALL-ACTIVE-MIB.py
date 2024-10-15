# SNMP MIB module (H3C-VOICE-CALL-ACTIVE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-VOICE-CALL-ACTIVE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:47 2024
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

(H3cCodecType,) = mibBuilder.importSymbols(
    "H3C-VOICE-DIAL-CONTROL-MIB",
    "H3cCodecType")

(h3cVoice,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cVoice")

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

h3cVoCallActive = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 15)
)
h3cVoCallActive.setRevisions(
        ("2008-02-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cGUid(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



# MIB Managed Objects in the order of their OIDs

_H3cVoiceCallActiveObjects_ObjectIdentity = ObjectIdentity
h3cVoiceCallActiveObjects = _H3cVoiceCallActiveObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 15, 1)
)
_H3cVoiceCallActiveTable_Object = MibTable
h3cVoiceCallActiveTable = _H3cVoiceCallActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 15, 1, 1)
)
if mibBuilder.loadTexts:
    h3cVoiceCallActiveTable.setStatus("current")
_H3cVoiceCallActiveEntry_Object = MibTableRow
h3cVoiceCallActiveEntry = _H3cVoiceCallActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 15, 1, 1, 1)
)
h3cVoiceCallActiveEntry.setIndexNames(
    (0, "DIAL-CONTROL-MIB", "callActiveSetupTime"),
    (0, "DIAL-CONTROL-MIB", "callActiveIndex"),
)
if mibBuilder.loadTexts:
    h3cVoiceCallActiveEntry.setStatus("current")
_H3cVoCallActiveConnectionId_Type = H3cGUid
_H3cVoCallActiveConnectionId_Object = MibTableColumn
h3cVoCallActiveConnectionId = _H3cVoCallActiveConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 15, 1, 1, 1, 1),
    _H3cVoCallActiveConnectionId_Type()
)
h3cVoCallActiveConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallActiveConnectionId.setStatus("current")
_H3cVoCallActiveTxDuration_Type = Gauge32
_H3cVoCallActiveTxDuration_Object = MibTableColumn
h3cVoCallActiveTxDuration = _H3cVoCallActiveTxDuration_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 15, 1, 1, 1, 2),
    _H3cVoCallActiveTxDuration_Type()
)
h3cVoCallActiveTxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallActiveTxDuration.setStatus("current")
_H3cVoCallActiveVoiceTxDuration_Type = Gauge32
_H3cVoCallActiveVoiceTxDuration_Object = MibTableColumn
h3cVoCallActiveVoiceTxDuration = _H3cVoCallActiveVoiceTxDuration_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 15, 1, 1, 1, 3),
    _H3cVoCallActiveVoiceTxDuration_Type()
)
h3cVoCallActiveVoiceTxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallActiveVoiceTxDuration.setStatus("current")
_H3cVoCallActiveFaxTxDuration_Type = Gauge32
_H3cVoCallActiveFaxTxDuration_Object = MibTableColumn
h3cVoCallActiveFaxTxDuration = _H3cVoCallActiveFaxTxDuration_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 15, 1, 1, 1, 4),
    _H3cVoCallActiveFaxTxDuration_Type()
)
h3cVoCallActiveFaxTxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallActiveFaxTxDuration.setStatus("current")
_H3cVoCallActiveCoderType_Type = H3cCodecType
_H3cVoCallActiveCoderType_Object = MibTableColumn
h3cVoCallActiveCoderType = _H3cVoCallActiveCoderType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 15, 1, 1, 1, 5),
    _H3cVoCallActiveCoderType_Type()
)
h3cVoCallActiveCoderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallActiveCoderType.setStatus("current")
_H3cVoCallActiveImgPageCount_Type = Gauge32
_H3cVoCallActiveImgPageCount_Object = MibTableColumn
h3cVoCallActiveImgPageCount = _H3cVoCallActiveImgPageCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 15, 1, 1, 1, 6),
    _H3cVoCallActiveImgPageCount_Type()
)
h3cVoCallActiveImgPageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallActiveImgPageCount.setStatus("current")
_H3cVoiceVoIPCallActiveTable_Object = MibTable
h3cVoiceVoIPCallActiveTable = _H3cVoiceVoIPCallActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 15, 1, 2)
)
if mibBuilder.loadTexts:
    h3cVoiceVoIPCallActiveTable.setStatus("current")
_H3cVoiceVoIPCallActiveEntry_Object = MibTableRow
h3cVoiceVoIPCallActiveEntry = _H3cVoiceVoIPCallActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 15, 1, 2, 1)
)
h3cVoiceVoIPCallActiveEntry.setIndexNames(
    (0, "DIAL-CONTROL-MIB", "callActiveSetupTime"),
    (0, "DIAL-CONTROL-MIB", "callActiveIndex"),
)
if mibBuilder.loadTexts:
    h3cVoiceVoIPCallActiveEntry.setStatus("current")
_H3cVoVoIPCallActiveConnectionId_Type = H3cGUid
_H3cVoVoIPCallActiveConnectionId_Object = MibTableColumn
h3cVoVoIPCallActiveConnectionId = _H3cVoVoIPCallActiveConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 15, 1, 2, 1, 1),
    _H3cVoVoIPCallActiveConnectionId_Type()
)
h3cVoVoIPCallActiveConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoVoIPCallActiveConnectionId.setStatus("current")
_H3cVoVoIPCallActiveRemSigIPType_Type = InetAddressType
_H3cVoVoIPCallActiveRemSigIPType_Object = MibTableColumn
h3cVoVoIPCallActiveRemSigIPType = _H3cVoVoIPCallActiveRemSigIPType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 15, 1, 2, 1, 2),
    _H3cVoVoIPCallActiveRemSigIPType_Type()
)
h3cVoVoIPCallActiveRemSigIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoVoIPCallActiveRemSigIPType.setStatus("current")
_H3cVoVoIPCallActiveRemSigIPAddr_Type = InetAddress
_H3cVoVoIPCallActiveRemSigIPAddr_Object = MibTableColumn
h3cVoVoIPCallActiveRemSigIPAddr = _H3cVoVoIPCallActiveRemSigIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 15, 1, 2, 1, 3),
    _H3cVoVoIPCallActiveRemSigIPAddr_Type()
)
h3cVoVoIPCallActiveRemSigIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoVoIPCallActiveRemSigIPAddr.setStatus("current")


class _H3cVoVoIPCallActiveRemSigPort_Type(Integer32):
    """Custom type h3cVoVoIPCallActiveRemSigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cVoVoIPCallActiveRemSigPort_Type.__name__ = "Integer32"
_H3cVoVoIPCallActiveRemSigPort_Object = MibTableColumn
h3cVoVoIPCallActiveRemSigPort = _H3cVoVoIPCallActiveRemSigPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 15, 1, 2, 1, 4),
    _H3cVoVoIPCallActiveRemSigPort_Type()
)
h3cVoVoIPCallActiveRemSigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoVoIPCallActiveRemSigPort.setStatus("current")
_H3cVoVoIPCallActiveRemMedIPType_Type = InetAddressType
_H3cVoVoIPCallActiveRemMedIPType_Object = MibTableColumn
h3cVoVoIPCallActiveRemMedIPType = _H3cVoVoIPCallActiveRemMedIPType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 15, 1, 2, 1, 5),
    _H3cVoVoIPCallActiveRemMedIPType_Type()
)
h3cVoVoIPCallActiveRemMedIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoVoIPCallActiveRemMedIPType.setStatus("current")
_H3cVoVoIPCallActiveRemMedIPAddr_Type = InetAddress
_H3cVoVoIPCallActiveRemMedIPAddr_Object = MibTableColumn
h3cVoVoIPCallActiveRemMedIPAddr = _H3cVoVoIPCallActiveRemMedIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 15, 1, 2, 1, 6),
    _H3cVoVoIPCallActiveRemMedIPAddr_Type()
)
h3cVoVoIPCallActiveRemMedIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoVoIPCallActiveRemMedIPAddr.setStatus("current")


class _H3cVoVoIPCallActiveRemMedPort_Type(Integer32):
    """Custom type h3cVoVoIPCallActiveRemMedPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cVoVoIPCallActiveRemMedPort_Type.__name__ = "Integer32"
_H3cVoVoIPCallActiveRemMedPort_Object = MibTableColumn
h3cVoVoIPCallActiveRemMedPort = _H3cVoVoIPCallActiveRemMedPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 15, 1, 2, 1, 7),
    _H3cVoVoIPCallActiveRemMedPort_Type()
)
h3cVoVoIPCallActiveRemMedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoVoIPCallActiveRemMedPort.setStatus("current")


class _H3cVoVoIPCallActiveSessProtocol_Type(Integer32):
    """Custom type h3cVoVoIPCallActiveSessProtocol based on Integer32"""
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


_H3cVoVoIPCallActiveSessProtocol_Type.__name__ = "Integer32"
_H3cVoVoIPCallActiveSessProtocol_Object = MibTableColumn
h3cVoVoIPCallActiveSessProtocol = _H3cVoVoIPCallActiveSessProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 15, 1, 2, 1, 8),
    _H3cVoVoIPCallActiveSessProtocol_Type()
)
h3cVoVoIPCallActiveSessProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoVoIPCallActiveSessProtocol.setStatus("current")
_H3cVoVoIPCallActiveCoderType_Type = H3cCodecType
_H3cVoVoIPCallActiveCoderType_Object = MibTableColumn
h3cVoVoIPCallActiveCoderType = _H3cVoVoIPCallActiveCoderType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 15, 1, 2, 1, 9),
    _H3cVoVoIPCallActiveCoderType_Type()
)
h3cVoVoIPCallActiveCoderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoVoIPCallActiveCoderType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-VOICE-CALL-ACTIVE-MIB",
    **{"H3cGUid": H3cGUid,
       "h3cVoCallActive": h3cVoCallActive,
       "h3cVoiceCallActiveObjects": h3cVoiceCallActiveObjects,
       "h3cVoiceCallActiveTable": h3cVoiceCallActiveTable,
       "h3cVoiceCallActiveEntry": h3cVoiceCallActiveEntry,
       "h3cVoCallActiveConnectionId": h3cVoCallActiveConnectionId,
       "h3cVoCallActiveTxDuration": h3cVoCallActiveTxDuration,
       "h3cVoCallActiveVoiceTxDuration": h3cVoCallActiveVoiceTxDuration,
       "h3cVoCallActiveFaxTxDuration": h3cVoCallActiveFaxTxDuration,
       "h3cVoCallActiveCoderType": h3cVoCallActiveCoderType,
       "h3cVoCallActiveImgPageCount": h3cVoCallActiveImgPageCount,
       "h3cVoiceVoIPCallActiveTable": h3cVoiceVoIPCallActiveTable,
       "h3cVoiceVoIPCallActiveEntry": h3cVoiceVoIPCallActiveEntry,
       "h3cVoVoIPCallActiveConnectionId": h3cVoVoIPCallActiveConnectionId,
       "h3cVoVoIPCallActiveRemSigIPType": h3cVoVoIPCallActiveRemSigIPType,
       "h3cVoVoIPCallActiveRemSigIPAddr": h3cVoVoIPCallActiveRemSigIPAddr,
       "h3cVoVoIPCallActiveRemSigPort": h3cVoVoIPCallActiveRemSigPort,
       "h3cVoVoIPCallActiveRemMedIPType": h3cVoVoIPCallActiveRemMedIPType,
       "h3cVoVoIPCallActiveRemMedIPAddr": h3cVoVoIPCallActiveRemMedIPAddr,
       "h3cVoVoIPCallActiveRemMedPort": h3cVoVoIPCallActiveRemMedPort,
       "h3cVoVoIPCallActiveSessProtocol": h3cVoVoIPCallActiveSessProtocol,
       "h3cVoVoIPCallActiveCoderType": h3cVoVoIPCallActiveCoderType}
)
