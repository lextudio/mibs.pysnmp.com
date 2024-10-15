# SNMP MIB module (H3C-VOSIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-VOSIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:52 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

h3cVoSIP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12)
)
h3cVoSIP.setRevisions(
        ("2005-03-15 00:00",)
)


# Types definitions



class SipMsgType(Integer32):
    """Custom type SipMsgType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("ack", 4),
          ("bye", 7),
          ("cancel", 6),
          ("info", 8),
          ("invite", 3),
          ("prack", 5),
          ("register", 2),
          ("unknown", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cSIPClientMIB_ObjectIdentity = ObjectIdentity
h3cSIPClientMIB = _H3cSIPClientMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1)
)
_H3cSIPClientConfigObjects_ObjectIdentity = ObjectIdentity
h3cSIPClientConfigObjects = _H3cSIPClientConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 1)
)


class _H3cSIPID_Type(OctetString):
    """Custom type h3cSIPID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_H3cSIPID_Type.__name__ = "OctetString"
_H3cSIPID_Object = MibScalar
h3cSIPID = _H3cSIPID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 1, 1),
    _H3cSIPID_Type()
)
h3cSIPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSIPID.setStatus("current")


class _H3cSIPPasswordType_Type(Integer32):
    """Custom type h3cSIPPasswordType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cipher", 2),
          ("simple", 1))
    )


_H3cSIPPasswordType_Type.__name__ = "Integer32"
_H3cSIPPasswordType_Object = MibScalar
h3cSIPPasswordType = _H3cSIPPasswordType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 1, 2),
    _H3cSIPPasswordType_Type()
)
h3cSIPPasswordType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSIPPasswordType.setStatus("current")
_H3cSIPPassword_Type = OctetString
_H3cSIPPassword_Object = MibScalar
h3cSIPPassword = _H3cSIPPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 1, 3),
    _H3cSIPPassword_Type()
)
h3cSIPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSIPPassword.setStatus("current")
_H3cSIPSourceIPAddressType_Type = InetAddressType
_H3cSIPSourceIPAddressType_Object = MibScalar
h3cSIPSourceIPAddressType = _H3cSIPSourceIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 1, 4),
    _H3cSIPSourceIPAddressType_Type()
)
h3cSIPSourceIPAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSIPSourceIPAddressType.setStatus("current")
_H3cSIPSourceIP_Type = InetAddress
_H3cSIPSourceIP_Object = MibScalar
h3cSIPSourceIP = _H3cSIPSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 1, 5),
    _H3cSIPSourceIP_Type()
)
h3cSIPSourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSIPSourceIP.setStatus("current")


class _H3cSIPRegisterMode_Type(Integer32):
    """Custom type h3cSIPRegisterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("gatewayAll", 1),
          ("gatewaySingle", 2),
          ("phoneNumber", 3))
    )


_H3cSIPRegisterMode_Type.__name__ = "Integer32"
_H3cSIPRegisterMode_Object = MibScalar
h3cSIPRegisterMode = _H3cSIPRegisterMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 1, 6),
    _H3cSIPRegisterMode_Type()
)
h3cSIPRegisterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSIPRegisterMode.setStatus("current")
_H3cSIPRegisterPhoneNumber_Type = OctetString
_H3cSIPRegisterPhoneNumber_Object = MibScalar
h3cSIPRegisterPhoneNumber = _H3cSIPRegisterPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 1, 7),
    _H3cSIPRegisterPhoneNumber_Type()
)
h3cSIPRegisterPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSIPRegisterPhoneNumber.setStatus("current")


class _H3cSIPRegisterEnable_Type(Integer32):
    """Custom type h3cSIPRegisterEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_H3cSIPRegisterEnable_Type.__name__ = "Integer32"
_H3cSIPRegisterEnable_Object = MibScalar
h3cSIPRegisterEnable = _H3cSIPRegisterEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 1, 8),
    _H3cSIPRegisterEnable_Type()
)
h3cSIPRegisterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSIPRegisterEnable.setStatus("current")


class _H3cSIPTrapsControl_Type(Integer32):
    """Custom type h3cSIPTrapsControl based on Integer32"""
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


_H3cSIPTrapsControl_Type.__name__ = "Integer32"
_H3cSIPTrapsControl_Object = MibScalar
h3cSIPTrapsControl = _H3cSIPTrapsControl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 1, 9),
    _H3cSIPTrapsControl_Type()
)
h3cSIPTrapsControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSIPTrapsControl.setStatus("current")


class _H3cSIPStatisticClear_Type(Integer32):
    """Custom type h3cSIPStatisticClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_H3cSIPStatisticClear_Type.__name__ = "Integer32"
_H3cSIPStatisticClear_Object = MibScalar
h3cSIPStatisticClear = _H3cSIPStatisticClear_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 1, 10),
    _H3cSIPStatisticClear_Type()
)
h3cSIPStatisticClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSIPStatisticClear.setStatus("current")
_H3cSIPServerConfigTable_Object = MibTable
h3cSIPServerConfigTable = _H3cSIPServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 2)
)
if mibBuilder.loadTexts:
    h3cSIPServerConfigTable.setStatus("current")
_H3cSIPServerConfigEntry_Object = MibTableRow
h3cSIPServerConfigEntry = _H3cSIPServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 2, 1)
)
h3cSIPServerConfigEntry.setIndexNames(
    (0, "H3C-VOSIP-MIB", "h3cSIPServerIPAddressType"),
    (0, "H3C-VOSIP-MIB", "h3cSIPServerIPAddress"),
    (0, "H3C-VOSIP-MIB", "h3cSIPServerPort"),
)
if mibBuilder.loadTexts:
    h3cSIPServerConfigEntry.setStatus("current")
_H3cSIPServerIPAddressType_Type = InetAddressType
_H3cSIPServerIPAddressType_Object = MibTableColumn
h3cSIPServerIPAddressType = _H3cSIPServerIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 2, 1, 1),
    _H3cSIPServerIPAddressType_Type()
)
h3cSIPServerIPAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSIPServerIPAddressType.setStatus("current")
_H3cSIPServerIPAddress_Type = InetAddress
_H3cSIPServerIPAddress_Object = MibTableColumn
h3cSIPServerIPAddress = _H3cSIPServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 2, 1, 2),
    _H3cSIPServerIPAddress_Type()
)
h3cSIPServerIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSIPServerIPAddress.setStatus("current")


class _H3cSIPServerPort_Type(Integer32):
    """Custom type h3cSIPServerPort based on Integer32"""
    defaultValue = 5060

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cSIPServerPort_Type.__name__ = "Integer32"
_H3cSIPServerPort_Object = MibTableColumn
h3cSIPServerPort = _H3cSIPServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 2, 1, 3),
    _H3cSIPServerPort_Type()
)
h3cSIPServerPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSIPServerPort.setStatus("current")


class _H3cSIPServerType_Type(Integer32):
    """Custom type h3cSIPServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_H3cSIPServerType_Type.__name__ = "Integer32"
_H3cSIPServerType_Object = MibTableColumn
h3cSIPServerType = _H3cSIPServerType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 2, 1, 4),
    _H3cSIPServerType_Type()
)
h3cSIPServerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSIPServerType.setStatus("current")


class _H3cSIPAcceptType_Type(Integer32):
    """Custom type h3cSIPAcceptType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("inbound", 1))
    )


_H3cSIPAcceptType_Type.__name__ = "Integer32"
_H3cSIPAcceptType_Object = MibTableColumn
h3cSIPAcceptType = _H3cSIPAcceptType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 2, 1, 5),
    _H3cSIPAcceptType_Type()
)
h3cSIPAcceptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSIPAcceptType.setStatus("current")
_H3cSIPServerStatus_Type = RowStatus
_H3cSIPServerStatus_Object = MibTableColumn
h3cSIPServerStatus = _H3cSIPServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 2, 1, 6),
    _H3cSIPServerStatus_Type()
)
h3cSIPServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSIPServerStatus.setStatus("current")
_H3cSIPMsgStatTable_Object = MibTable
h3cSIPMsgStatTable = _H3cSIPMsgStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 3)
)
if mibBuilder.loadTexts:
    h3cSIPMsgStatTable.setStatus("current")
_H3cSIPMsgStatEntry_Object = MibTableRow
h3cSIPMsgStatEntry = _H3cSIPMsgStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 3, 1)
)
h3cSIPMsgStatEntry.setIndexNames(
    (0, "H3C-VOSIP-MIB", "h3cSIPMsgIndex"),
)
if mibBuilder.loadTexts:
    h3cSIPMsgStatEntry.setStatus("current")
_H3cSIPMsgIndex_Type = SipMsgType
_H3cSIPMsgIndex_Object = MibTableColumn
h3cSIPMsgIndex = _H3cSIPMsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 3, 1, 1),
    _H3cSIPMsgIndex_Type()
)
h3cSIPMsgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSIPMsgIndex.setStatus("current")
_H3cSIPMsgName_Type = OctetString
_H3cSIPMsgName_Object = MibTableColumn
h3cSIPMsgName = _H3cSIPMsgName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 3, 1, 2),
    _H3cSIPMsgName_Type()
)
h3cSIPMsgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSIPMsgName.setStatus("current")
_H3cSIPMsgSend_Type = Counter32
_H3cSIPMsgSend_Object = MibTableColumn
h3cSIPMsgSend = _H3cSIPMsgSend_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 3, 1, 3),
    _H3cSIPMsgSend_Type()
)
h3cSIPMsgSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSIPMsgSend.setStatus("current")
_H3cSIPMsgOKSend_Type = Counter32
_H3cSIPMsgOKSend_Object = MibTableColumn
h3cSIPMsgOKSend = _H3cSIPMsgOKSend_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 3, 1, 4),
    _H3cSIPMsgOKSend_Type()
)
h3cSIPMsgOKSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSIPMsgOKSend.setStatus("current")
_H3cSIPMsgReceive_Type = Counter32
_H3cSIPMsgReceive_Object = MibTableColumn
h3cSIPMsgReceive = _H3cSIPMsgReceive_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 3, 1, 5),
    _H3cSIPMsgReceive_Type()
)
h3cSIPMsgReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSIPMsgReceive.setStatus("current")
_H3cSIPMsgOKReceive_Type = Counter32
_H3cSIPMsgOKReceive_Object = MibTableColumn
h3cSIPMsgOKReceive = _H3cSIPMsgOKReceive_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 3, 1, 6),
    _H3cSIPMsgOKReceive_Type()
)
h3cSIPMsgOKReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSIPMsgOKReceive.setStatus("current")
_H3cSIPMsgResponseStatTable_Object = MibTable
h3cSIPMsgResponseStatTable = _H3cSIPMsgResponseStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 4)
)
if mibBuilder.loadTexts:
    h3cSIPMsgResponseStatTable.setStatus("current")
_H3cSIPMsgResponseStatEntry_Object = MibTableRow
h3cSIPMsgResponseStatEntry = _H3cSIPMsgResponseStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 4, 1)
)
h3cSIPMsgResponseStatEntry.setIndexNames(
    (0, "H3C-VOSIP-MIB", "h3cSIPMsgResponseIndex"),
)
if mibBuilder.loadTexts:
    h3cSIPMsgResponseStatEntry.setStatus("current")
_H3cSIPMsgResponseIndex_Type = Integer32
_H3cSIPMsgResponseIndex_Object = MibTableColumn
h3cSIPMsgResponseIndex = _H3cSIPMsgResponseIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 4, 1, 1),
    _H3cSIPMsgResponseIndex_Type()
)
h3cSIPMsgResponseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSIPMsgResponseIndex.setStatus("current")
_H3cSIPMsgResponseCode_Type = OctetString
_H3cSIPMsgResponseCode_Object = MibTableColumn
h3cSIPMsgResponseCode = _H3cSIPMsgResponseCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 4, 1, 2),
    _H3cSIPMsgResponseCode_Type()
)
h3cSIPMsgResponseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSIPMsgResponseCode.setStatus("current")
_H3cSIPResCodeRecvCount_Type = Counter32
_H3cSIPResCodeRecvCount_Object = MibTableColumn
h3cSIPResCodeRecvCount = _H3cSIPResCodeRecvCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 4, 1, 3),
    _H3cSIPResCodeRecvCount_Type()
)
h3cSIPResCodeRecvCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSIPResCodeRecvCount.setStatus("current")
_H3cSIPResCodeSendCount_Type = Counter32
_H3cSIPResCodeSendCount_Object = MibTableColumn
h3cSIPResCodeSendCount = _H3cSIPResCodeSendCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 1, 4, 1, 4),
    _H3cSIPResCodeSendCount_Type()
)
h3cSIPResCodeSendCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSIPResCodeSendCount.setStatus("current")
_H3cSIPTrapStubObjects_ObjectIdentity = ObjectIdentity
h3cSIPTrapStubObjects = _H3cSIPTrapStubObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 3)
)


class _H3cSIPRegisterFailReason_Type(OctetString):
    """Custom type h3cSIPRegisterFailReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_H3cSIPRegisterFailReason_Type.__name__ = "OctetString"
_H3cSIPRegisterFailReason_Object = MibScalar
h3cSIPRegisterFailReason = _H3cSIPRegisterFailReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 3, 1),
    _H3cSIPRegisterFailReason_Type()
)
h3cSIPRegisterFailReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSIPRegisterFailReason.setStatus("current")
_H3cSIPAuthenReqMethod_Type = SipMsgType
_H3cSIPAuthenReqMethod_Object = MibScalar
h3cSIPAuthenReqMethod = _H3cSIPAuthenReqMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 3, 2),
    _H3cSIPAuthenReqMethod_Type()
)
h3cSIPAuthenReqMethod.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSIPAuthenReqMethod.setStatus("current")
_H3cSIPClientNotifications_ObjectIdentity = ObjectIdentity
h3cSIPClientNotifications = _H3cSIPClientNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 4)
)

# Managed Objects groups


# Notification objects

h3cSIPRegisterFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 4, 1)
)
h3cSIPRegisterFailure.setObjects(
      *(("H3C-VOSIP-MIB", "h3cSIPID"),
        ("H3C-VOSIP-MIB", "h3cSIPServerIPAddressType"),
        ("H3C-VOSIP-MIB", "h3cSIPServerIPAddress"),
        ("H3C-VOSIP-MIB", "h3cSIPServerPort"),
        ("H3C-VOSIP-MIB", "h3cSIPRegisterFailReason"))
)
if mibBuilder.loadTexts:
    h3cSIPRegisterFailure.setStatus(
        "current"
    )

h3cSIPAuthenticateFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 4, 2)
)
h3cSIPAuthenticateFailure.setObjects(
      *(("H3C-VOSIP-MIB", "h3cSIPID"),
        ("H3C-VOSIP-MIB", "h3cSIPAuthenReqMethod"))
)
if mibBuilder.loadTexts:
    h3cSIPAuthenticateFailure.setStatus(
        "current"
    )

h3cSIPServerSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 12, 4, 3)
)
if mibBuilder.loadTexts:
    h3cSIPServerSwitch.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-VOSIP-MIB",
    **{"SipMsgType": SipMsgType,
       "h3cVoSIP": h3cVoSIP,
       "h3cSIPClientMIB": h3cSIPClientMIB,
       "h3cSIPClientConfigObjects": h3cSIPClientConfigObjects,
       "h3cSIPID": h3cSIPID,
       "h3cSIPPasswordType": h3cSIPPasswordType,
       "h3cSIPPassword": h3cSIPPassword,
       "h3cSIPSourceIPAddressType": h3cSIPSourceIPAddressType,
       "h3cSIPSourceIP": h3cSIPSourceIP,
       "h3cSIPRegisterMode": h3cSIPRegisterMode,
       "h3cSIPRegisterPhoneNumber": h3cSIPRegisterPhoneNumber,
       "h3cSIPRegisterEnable": h3cSIPRegisterEnable,
       "h3cSIPTrapsControl": h3cSIPTrapsControl,
       "h3cSIPStatisticClear": h3cSIPStatisticClear,
       "h3cSIPServerConfigTable": h3cSIPServerConfigTable,
       "h3cSIPServerConfigEntry": h3cSIPServerConfigEntry,
       "h3cSIPServerIPAddressType": h3cSIPServerIPAddressType,
       "h3cSIPServerIPAddress": h3cSIPServerIPAddress,
       "h3cSIPServerPort": h3cSIPServerPort,
       "h3cSIPServerType": h3cSIPServerType,
       "h3cSIPAcceptType": h3cSIPAcceptType,
       "h3cSIPServerStatus": h3cSIPServerStatus,
       "h3cSIPMsgStatTable": h3cSIPMsgStatTable,
       "h3cSIPMsgStatEntry": h3cSIPMsgStatEntry,
       "h3cSIPMsgIndex": h3cSIPMsgIndex,
       "h3cSIPMsgName": h3cSIPMsgName,
       "h3cSIPMsgSend": h3cSIPMsgSend,
       "h3cSIPMsgOKSend": h3cSIPMsgOKSend,
       "h3cSIPMsgReceive": h3cSIPMsgReceive,
       "h3cSIPMsgOKReceive": h3cSIPMsgOKReceive,
       "h3cSIPMsgResponseStatTable": h3cSIPMsgResponseStatTable,
       "h3cSIPMsgResponseStatEntry": h3cSIPMsgResponseStatEntry,
       "h3cSIPMsgResponseIndex": h3cSIPMsgResponseIndex,
       "h3cSIPMsgResponseCode": h3cSIPMsgResponseCode,
       "h3cSIPResCodeRecvCount": h3cSIPResCodeRecvCount,
       "h3cSIPResCodeSendCount": h3cSIPResCodeSendCount,
       "h3cSIPTrapStubObjects": h3cSIPTrapStubObjects,
       "h3cSIPRegisterFailReason": h3cSIPRegisterFailReason,
       "h3cSIPAuthenReqMethod": h3cSIPAuthenReqMethod,
       "h3cSIPClientNotifications": h3cSIPClientNotifications,
       "h3cSIPRegisterFailure": h3cSIPRegisterFailure,
       "h3cSIPAuthenticateFailure": h3cSIPAuthenticateFailure,
       "h3cSIPServerSwitch": h3cSIPServerSwitch}
)
