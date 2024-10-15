# SNMP MIB module (HUAWEI-SIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-SIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:54 2024
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

(huawei,
 huaweiDatacomm,
 huaweiMgmt,
 voice) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "huawei",
    "huaweiDatacomm",
    "huaweiMgmt",
    "voice")

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
 enterprises,
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "enterprises",
    "iso",
    "mib-2")

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwSIPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12)
)
hwSIPMIB.setRevisions(
        ("2003-09-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwSIPServerMIB_ObjectIdentity = ObjectIdentity
hwSIPServerMIB = _HwSIPServerMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 1)
)
_HwSIPClientMIB_ObjectIdentity = ObjectIdentity
hwSIPClientMIB = _HwSIPClientMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2)
)
_HwSIPClientMIBObjects_ObjectIdentity = ObjectIdentity
hwSIPClientMIBObjects = _HwSIPClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1)
)


class _HwSIPID_Type(OctetString):
    """Custom type hwSIPID based on OctetString"""
    defaultValue = OctetString("VRP-GATEWAY")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwSIPID_Type.__name__ = "OctetString"
_HwSIPID_Object = MibScalar
hwSIPID = _HwSIPID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 1),
    _HwSIPID_Type()
)
hwSIPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSIPID.setStatus("current")


class _HwSIPPasswordType_Type(Integer32):
    """Custom type hwSIPPasswordType based on Integer32"""
    defaultValue = 1

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


_HwSIPPasswordType_Type.__name__ = "Integer32"
_HwSIPPasswordType_Object = MibScalar
hwSIPPasswordType = _HwSIPPasswordType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 2),
    _HwSIPPasswordType_Type()
)
hwSIPPasswordType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSIPPasswordType.setStatus("current")


class _HwSIPPassword_Type(OctetString):
    """Custom type hwSIPPassword based on OctetString"""
    defaultValue = OctetString("VRP-SIP")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwSIPPassword_Type.__name__ = "OctetString"
_HwSIPPassword_Object = MibScalar
hwSIPPassword = _HwSIPPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 3),
    _HwSIPPassword_Type()
)
hwSIPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSIPPassword.setStatus("current")


class _HwSIPTransport_Type(Integer32):
    """Custom type hwSIPTransport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 2),
          ("udp", 1))
    )


_HwSIPTransport_Type.__name__ = "Integer32"
_HwSIPTransport_Object = MibScalar
hwSIPTransport = _HwSIPTransport_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 4),
    _HwSIPTransport_Type()
)
hwSIPTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSIPTransport.setStatus("current")
_HwSIPSourceIP_Type = IpAddress
_HwSIPSourceIP_Object = MibScalar
hwSIPSourceIP = _HwSIPSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 5),
    _HwSIPSourceIP_Type()
)
hwSIPSourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSIPSourceIP.setStatus("current")


class _HwSIPCallDebugSwitch_Type(Integer32):
    """Custom type hwSIPCallDebugSwitch based on Integer32"""
    defaultValue = 2

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


_HwSIPCallDebugSwitch_Type.__name__ = "Integer32"
_HwSIPCallDebugSwitch_Object = MibScalar
hwSIPCallDebugSwitch = _HwSIPCallDebugSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 6),
    _HwSIPCallDebugSwitch_Type()
)
hwSIPCallDebugSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSIPCallDebugSwitch.setStatus("current")


class _HwSIPRegisterDebugSwitch_Type(Integer32):
    """Custom type hwSIPRegisterDebugSwitch based on Integer32"""
    defaultValue = 2

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


_HwSIPRegisterDebugSwitch_Type.__name__ = "Integer32"
_HwSIPRegisterDebugSwitch_Object = MibScalar
hwSIPRegisterDebugSwitch = _HwSIPRegisterDebugSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 7),
    _HwSIPRegisterDebugSwitch_Type()
)
hwSIPRegisterDebugSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSIPRegisterDebugSwitch.setStatus("current")


class _HwSIPRegPrimitiveDebugSwitch_Type(Integer32):
    """Custom type hwSIPRegPrimitiveDebugSwitch based on Integer32"""
    defaultValue = 2

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


_HwSIPRegPrimitiveDebugSwitch_Type.__name__ = "Integer32"
_HwSIPRegPrimitiveDebugSwitch_Object = MibScalar
hwSIPRegPrimitiveDebugSwitch = _HwSIPRegPrimitiveDebugSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 8),
    _HwSIPRegPrimitiveDebugSwitch_Type()
)
hwSIPRegPrimitiveDebugSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSIPRegPrimitiveDebugSwitch.setStatus("current")


class _HwSIPCallPrimitiveDebugSwitch_Type(Integer32):
    """Custom type hwSIPCallPrimitiveDebugSwitch based on Integer32"""
    defaultValue = 2

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


_HwSIPCallPrimitiveDebugSwitch_Type.__name__ = "Integer32"
_HwSIPCallPrimitiveDebugSwitch_Object = MibScalar
hwSIPCallPrimitiveDebugSwitch = _HwSIPCallPrimitiveDebugSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 9),
    _HwSIPCallPrimitiveDebugSwitch_Type()
)
hwSIPCallPrimitiveDebugSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSIPCallPrimitiveDebugSwitch.setStatus("current")


class _HwSIPWarningDebugSwitch_Type(Integer32):
    """Custom type hwSIPWarningDebugSwitch based on Integer32"""
    defaultValue = 2

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


_HwSIPWarningDebugSwitch_Type.__name__ = "Integer32"
_HwSIPWarningDebugSwitch_Object = MibScalar
hwSIPWarningDebugSwitch = _HwSIPWarningDebugSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 10),
    _HwSIPWarningDebugSwitch_Type()
)
hwSIPWarningDebugSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSIPWarningDebugSwitch.setStatus("current")


class _HwSIPErrorDebugSwitch_Type(Integer32):
    """Custom type hwSIPErrorDebugSwitch based on Integer32"""
    defaultValue = 2

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


_HwSIPErrorDebugSwitch_Type.__name__ = "Integer32"
_HwSIPErrorDebugSwitch_Object = MibScalar
hwSIPErrorDebugSwitch = _HwSIPErrorDebugSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 11),
    _HwSIPErrorDebugSwitch_Type()
)
hwSIPErrorDebugSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSIPErrorDebugSwitch.setStatus("current")


class _HwSIPTrapsControl_Type(Integer32):
    """Custom type hwSIPTrapsControl based on Integer32"""
    defaultValue = 2

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


_HwSIPTrapsControl_Type.__name__ = "Integer32"
_HwSIPTrapsControl_Object = MibScalar
hwSIPTrapsControl = _HwSIPTrapsControl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 12),
    _HwSIPTrapsControl_Type()
)
hwSIPTrapsControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSIPTrapsControl.setStatus("current")


class _HwSIPStatisticClear_Type(Integer32):
    """Custom type hwSIPStatisticClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_HwSIPStatisticClear_Type.__name__ = "Integer32"
_HwSIPStatisticClear_Object = MibScalar
hwSIPStatisticClear = _HwSIPStatisticClear_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 13),
    _HwSIPStatisticClear_Type()
)
hwSIPStatisticClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSIPStatisticClear.setStatus("current")
_HwSIPRegisterFailReason_Type = DisplayString
_HwSIPRegisterFailReason_Object = MibScalar
hwSIPRegisterFailReason = _HwSIPRegisterFailReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 14),
    _HwSIPRegisterFailReason_Type()
)
hwSIPRegisterFailReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwSIPRegisterFailReason.setStatus("current")


class _HwSIPAuthenticatedRequestMethord_Type(Integer32):
    """Custom type hwSIPAuthenticatedRequestMethord based on Integer32"""
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
          ("unknow", 1))
    )


_HwSIPAuthenticatedRequestMethord_Type.__name__ = "Integer32"
_HwSIPAuthenticatedRequestMethord_Object = MibScalar
hwSIPAuthenticatedRequestMethord = _HwSIPAuthenticatedRequestMethord_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 15),
    _HwSIPAuthenticatedRequestMethord_Type()
)
hwSIPAuthenticatedRequestMethord.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwSIPAuthenticatedRequestMethord.setStatus("current")
_HwSIPStatisticObjects_ObjectIdentity = ObjectIdentity
hwSIPStatisticObjects = _HwSIPStatisticObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16)
)
_HwSIPRegisters_Type = Integer32
_HwSIPRegisters_Object = MibScalar
hwSIPRegisters = _HwSIPRegisters_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 1),
    _HwSIPRegisters_Type()
)
hwSIPRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPRegisters.setStatus("current")
_HwSIPInvites_Type = Integer32
_HwSIPInvites_Object = MibScalar
hwSIPInvites = _HwSIPInvites_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 2),
    _HwSIPInvites_Type()
)
hwSIPInvites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPInvites.setStatus("current")
_HwSIPAcks_Type = Integer32
_HwSIPAcks_Object = MibScalar
hwSIPAcks = _HwSIPAcks_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 3),
    _HwSIPAcks_Type()
)
hwSIPAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPAcks.setStatus("current")
_HwSIPPracks_Type = Integer32
_HwSIPPracks_Object = MibScalar
hwSIPPracks = _HwSIPPracks_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 4),
    _HwSIPPracks_Type()
)
hwSIPPracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPPracks.setStatus("current")
_HwSIPByes_Type = Integer32
_HwSIPByes_Object = MibScalar
hwSIPByes = _HwSIPByes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 5),
    _HwSIPByes_Type()
)
hwSIPByes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPByes.setStatus("current")
_HwSIPCancels_Type = Integer32
_HwSIPCancels_Object = MibScalar
hwSIPCancels = _HwSIPCancels_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 6),
    _HwSIPCancels_Type()
)
hwSIPCancels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPCancels.setStatus("current")
_HwSIPInfos_Type = Integer32
_HwSIPInfos_Object = MibScalar
hwSIPInfos = _HwSIPInfos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 7),
    _HwSIPInfos_Type()
)
hwSIPInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPInfos.setStatus("current")
_HwSIPOKRegisters_Type = Integer32
_HwSIPOKRegisters_Object = MibScalar
hwSIPOKRegisters = _HwSIPOKRegisters_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 8),
    _HwSIPOKRegisters_Type()
)
hwSIPOKRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPOKRegisters.setStatus("current")
_HwSIPOKInvites_Type = Integer32
_HwSIPOKInvites_Object = MibScalar
hwSIPOKInvites = _HwSIPOKInvites_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 9),
    _HwSIPOKInvites_Type()
)
hwSIPOKInvites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPOKInvites.setStatus("current")
_HwSIPOKAcks_Type = Integer32
_HwSIPOKAcks_Object = MibScalar
hwSIPOKAcks = _HwSIPOKAcks_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 10),
    _HwSIPOKAcks_Type()
)
hwSIPOKAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPOKAcks.setStatus("current")
_HwSIPOKPracks_Type = Integer32
_HwSIPOKPracks_Object = MibScalar
hwSIPOKPracks = _HwSIPOKPracks_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 11),
    _HwSIPOKPracks_Type()
)
hwSIPOKPracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPOKPracks.setStatus("current")
_HwSIPOKByes_Type = Integer32
_HwSIPOKByes_Object = MibScalar
hwSIPOKByes = _HwSIPOKByes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 12),
    _HwSIPOKByes_Type()
)
hwSIPOKByes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPOKByes.setStatus("current")
_HwSIPOKCancels_Type = Integer32
_HwSIPOKCancels_Object = MibScalar
hwSIPOKCancels = _HwSIPOKCancels_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 13),
    _HwSIPOKCancels_Type()
)
hwSIPOKCancels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPOKCancels.setStatus("current")
_HwSIPOKInfos_Type = Integer32
_HwSIPOKInfos_Object = MibScalar
hwSIPOKInfos = _HwSIPOKInfos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 14),
    _HwSIPOKInfos_Type()
)
hwSIPOKInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPOKInfos.setStatus("current")
_HwSIPResp3MultipleChoice_Type = Integer32
_HwSIPResp3MultipleChoice_Object = MibScalar
hwSIPResp3MultipleChoice = _HwSIPResp3MultipleChoice_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 15),
    _HwSIPResp3MultipleChoice_Type()
)
hwSIPResp3MultipleChoice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp3MultipleChoice.setStatus("current")
_HwSIPResp3MovedPermanently_Type = Integer32
_HwSIPResp3MovedPermanently_Object = MibScalar
hwSIPResp3MovedPermanently = _HwSIPResp3MovedPermanently_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 16),
    _HwSIPResp3MovedPermanently_Type()
)
hwSIPResp3MovedPermanently.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp3MovedPermanently.setStatus("current")
_HwSIPResp3MovedTemporarily_Type = Integer32
_HwSIPResp3MovedTemporarily_Object = MibScalar
hwSIPResp3MovedTemporarily = _HwSIPResp3MovedTemporarily_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 17),
    _HwSIPResp3MovedTemporarily_Type()
)
hwSIPResp3MovedTemporarily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp3MovedTemporarily.setStatus("current")
_HwSIPResp3UseProxy_Type = Integer32
_HwSIPResp3UseProxy_Object = MibScalar
hwSIPResp3UseProxy = _HwSIPResp3UseProxy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 18),
    _HwSIPResp3UseProxy_Type()
)
hwSIPResp3UseProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp3UseProxy.setStatus("current")
_HwSIPResp3Other_Type = Integer32
_HwSIPResp3Other_Object = MibScalar
hwSIPResp3Other = _HwSIPResp3Other_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 19),
    _HwSIPResp3Other_Type()
)
hwSIPResp3Other.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp3Other.setStatus("current")
_HwSIPResp4BadRequest_Type = Integer32
_HwSIPResp4BadRequest_Object = MibScalar
hwSIPResp4BadRequest = _HwSIPResp4BadRequest_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 20),
    _HwSIPResp4BadRequest_Type()
)
hwSIPResp4BadRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp4BadRequest.setStatus("current")
_HwSIPResp4Unauthorized_Type = Integer32
_HwSIPResp4Unauthorized_Object = MibScalar
hwSIPResp4Unauthorized = _HwSIPResp4Unauthorized_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 21),
    _HwSIPResp4Unauthorized_Type()
)
hwSIPResp4Unauthorized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp4Unauthorized.setStatus("current")
_HwSIPResp4Forbidden_Type = Integer32
_HwSIPResp4Forbidden_Object = MibScalar
hwSIPResp4Forbidden = _HwSIPResp4Forbidden_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 22),
    _HwSIPResp4Forbidden_Type()
)
hwSIPResp4Forbidden.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp4Forbidden.setStatus("current")
_HwSIPResp4NotFound_Type = Integer32
_HwSIPResp4NotFound_Object = MibScalar
hwSIPResp4NotFound = _HwSIPResp4NotFound_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 23),
    _HwSIPResp4NotFound_Type()
)
hwSIPResp4NotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp4NotFound.setStatus("current")
_HwSIPResp4MethodNotAllowed_Type = Integer32
_HwSIPResp4MethodNotAllowed_Object = MibScalar
hwSIPResp4MethodNotAllowed = _HwSIPResp4MethodNotAllowed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 24),
    _HwSIPResp4MethodNotAllowed_Type()
)
hwSIPResp4MethodNotAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp4MethodNotAllowed.setStatus("current")
_HwSIPResp4NotAcceptable_Type = Integer32
_HwSIPResp4NotAcceptable_Object = MibScalar
hwSIPResp4NotAcceptable = _HwSIPResp4NotAcceptable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 25),
    _HwSIPResp4NotAcceptable_Type()
)
hwSIPResp4NotAcceptable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp4NotAcceptable.setStatus("current")
_HwSIPResp4ProxyAuthRequired_Type = Integer32
_HwSIPResp4ProxyAuthRequired_Object = MibScalar
hwSIPResp4ProxyAuthRequired = _HwSIPResp4ProxyAuthRequired_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 26),
    _HwSIPResp4ProxyAuthRequired_Type()
)
hwSIPResp4ProxyAuthRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp4ProxyAuthRequired.setStatus("current")
_HwSIPResp4ReqTimeout_Type = Integer32
_HwSIPResp4ReqTimeout_Object = MibScalar
hwSIPResp4ReqTimeout = _HwSIPResp4ReqTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 27),
    _HwSIPResp4ReqTimeout_Type()
)
hwSIPResp4ReqTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp4ReqTimeout.setStatus("current")
_HwSIPResp4ReqEntityTooLarge_Type = Integer32
_HwSIPResp4ReqEntityTooLarge_Object = MibScalar
hwSIPResp4ReqEntityTooLarge = _HwSIPResp4ReqEntityTooLarge_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 28),
    _HwSIPResp4ReqEntityTooLarge_Type()
)
hwSIPResp4ReqEntityTooLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp4ReqEntityTooLarge.setStatus("current")
_HwSIPResp4ReqURITooLarge_Type = Integer32
_HwSIPResp4ReqURITooLarge_Object = MibScalar
hwSIPResp4ReqURITooLarge = _HwSIPResp4ReqURITooLarge_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 29),
    _HwSIPResp4ReqURITooLarge_Type()
)
hwSIPResp4ReqURITooLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp4ReqURITooLarge.setStatus("current")
_HwSIPResp4UnsupportedMediaType_Type = Integer32
_HwSIPResp4UnsupportedMediaType_Object = MibScalar
hwSIPResp4UnsupportedMediaType = _HwSIPResp4UnsupportedMediaType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 30),
    _HwSIPResp4UnsupportedMediaType_Type()
)
hwSIPResp4UnsupportedMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp4UnsupportedMediaType.setStatus("current")
_HwSIPResp4UnsupportedURIScheme_Type = Integer32
_HwSIPResp4UnsupportedURIScheme_Object = MibScalar
hwSIPResp4UnsupportedURIScheme = _HwSIPResp4UnsupportedURIScheme_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 31),
    _HwSIPResp4UnsupportedURIScheme_Type()
)
hwSIPResp4UnsupportedURIScheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp4UnsupportedURIScheme.setStatus("current")
_HwSIPResp4BadExtension_Type = Integer32
_HwSIPResp4BadExtension_Object = MibScalar
hwSIPResp4BadExtension = _HwSIPResp4BadExtension_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 32),
    _HwSIPResp4BadExtension_Type()
)
hwSIPResp4BadExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp4BadExtension.setStatus("current")
_HwSIPResp4ExtensionRequired_Type = Integer32
_HwSIPResp4ExtensionRequired_Object = MibScalar
hwSIPResp4ExtensionRequired = _HwSIPResp4ExtensionRequired_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 33),
    _HwSIPResp4ExtensionRequired_Type()
)
hwSIPResp4ExtensionRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp4ExtensionRequired.setStatus("current")
_HwSIPResp4AddrIncomplete_Type = Integer32
_HwSIPResp4AddrIncomplete_Object = MibScalar
hwSIPResp4AddrIncomplete = _HwSIPResp4AddrIncomplete_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 34),
    _HwSIPResp4AddrIncomplete_Type()
)
hwSIPResp4AddrIncomplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp4AddrIncomplete.setStatus("current")
_HwSIPResp4BusyHere_Type = Integer32
_HwSIPResp4BusyHere_Object = MibScalar
hwSIPResp4BusyHere = _HwSIPResp4BusyHere_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 35),
    _HwSIPResp4BusyHere_Type()
)
hwSIPResp4BusyHere.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp4BusyHere.setStatus("current")
_HwSIPResp4RequestTerminated_Type = Integer32
_HwSIPResp4RequestTerminated_Object = MibScalar
hwSIPResp4RequestTerminated = _HwSIPResp4RequestTerminated_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 36),
    _HwSIPResp4RequestTerminated_Type()
)
hwSIPResp4RequestTerminated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp4RequestTerminated.setStatus("current")
_HwSIPResp4Other_Type = Integer32
_HwSIPResp4Other_Object = MibScalar
hwSIPResp4Other = _HwSIPResp4Other_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 37),
    _HwSIPResp4Other_Type()
)
hwSIPResp4Other.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp4Other.setStatus("current")
_HwSIPResp5InternalError_Type = Integer32
_HwSIPResp5InternalError_Object = MibScalar
hwSIPResp5InternalError = _HwSIPResp5InternalError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 38),
    _HwSIPResp5InternalError_Type()
)
hwSIPResp5InternalError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp5InternalError.setStatus("current")
_HwSIPResp5NotImplemented_Type = Integer32
_HwSIPResp5NotImplemented_Object = MibScalar
hwSIPResp5NotImplemented = _HwSIPResp5NotImplemented_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 39),
    _HwSIPResp5NotImplemented_Type()
)
hwSIPResp5NotImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp5NotImplemented.setStatus("current")
_HwSIPResp5BadGateway_Type = Integer32
_HwSIPResp5BadGateway_Object = MibScalar
hwSIPResp5BadGateway = _HwSIPResp5BadGateway_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 40),
    _HwSIPResp5BadGateway_Type()
)
hwSIPResp5BadGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp5BadGateway.setStatus("current")
_HwSIPResp5ServiceUnavailable_Type = Integer32
_HwSIPResp5ServiceUnavailable_Object = MibScalar
hwSIPResp5ServiceUnavailable = _HwSIPResp5ServiceUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 41),
    _HwSIPResp5ServiceUnavailable_Type()
)
hwSIPResp5ServiceUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp5ServiceUnavailable.setStatus("current")
_HwSIPResp5GatewayTimeout_Type = Integer32
_HwSIPResp5GatewayTimeout_Object = MibScalar
hwSIPResp5GatewayTimeout = _HwSIPResp5GatewayTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 42),
    _HwSIPResp5GatewayTimeout_Type()
)
hwSIPResp5GatewayTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp5GatewayTimeout.setStatus("current")
_HwSIPResp5BadSipVersion_Type = Integer32
_HwSIPResp5BadSipVersion_Object = MibScalar
hwSIPResp5BadSipVersion = _HwSIPResp5BadSipVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 43),
    _HwSIPResp5BadSipVersion_Type()
)
hwSIPResp5BadSipVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp5BadSipVersion.setStatus("current")
_HwSIPResp5MessageTooLarge_Type = Integer32
_HwSIPResp5MessageTooLarge_Object = MibScalar
hwSIPResp5MessageTooLarge = _HwSIPResp5MessageTooLarge_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 44),
    _HwSIPResp5MessageTooLarge_Type()
)
hwSIPResp5MessageTooLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp5MessageTooLarge.setStatus("current")
_HwSIPResp5Other_Type = Integer32
_HwSIPResp5Other_Object = MibScalar
hwSIPResp5Other = _HwSIPResp5Other_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 45),
    _HwSIPResp5Other_Type()
)
hwSIPResp5Other.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp5Other.setStatus("current")
_HwSIPResp6xx_Type = Integer32
_HwSIPResp6xx_Object = MibScalar
hwSIPResp6xx = _HwSIPResp6xx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 16, 46),
    _HwSIPResp6xx_Type()
)
hwSIPResp6xx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSIPResp6xx.setStatus("current")
_HwSIPServerConfigTable_Object = MibTable
hwSIPServerConfigTable = _HwSIPServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 21)
)
if mibBuilder.loadTexts:
    hwSIPServerConfigTable.setStatus("current")
_HwSIPServerConfigEntry_Object = MibTableRow
hwSIPServerConfigEntry = _HwSIPServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 21, 1)
)
hwSIPServerConfigEntry.setIndexNames(
    (0, "HUAWEI-SIP-MIB", "hwSIPServerIPAddress"),
    (0, "HUAWEI-SIP-MIB", "hwSIPServerPort"),
)
if mibBuilder.loadTexts:
    hwSIPServerConfigEntry.setStatus("current")
_HwSIPServerIPAddress_Type = IpAddress
_HwSIPServerIPAddress_Object = MibTableColumn
hwSIPServerIPAddress = _HwSIPServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 21, 1, 1),
    _HwSIPServerIPAddress_Type()
)
hwSIPServerIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSIPServerIPAddress.setStatus("current")


class _HwSIPServerPort_Type(Integer32):
    """Custom type hwSIPServerPort based on Integer32"""
    defaultValue = 5060


_HwSIPServerPort_Object = MibTableColumn
hwSIPServerPort = _HwSIPServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 21, 1, 2),
    _HwSIPServerPort_Type()
)
hwSIPServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSIPServerPort.setStatus("current")


class _HwSIPServerType_Type(Integer32):
    """Custom type hwSIPServerType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slaver", 2))
    )


_HwSIPServerType_Type.__name__ = "Integer32"
_HwSIPServerType_Object = MibTableColumn
hwSIPServerType = _HwSIPServerType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 21, 1, 3),
    _HwSIPServerType_Type()
)
hwSIPServerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSIPServerType.setStatus("current")


class _HwSIPAcceptType_Type(Integer32):
    """Custom type hwSIPAcceptType based on Integer32"""
    defaultValue = 2

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


_HwSIPAcceptType_Type.__name__ = "Integer32"
_HwSIPAcceptType_Object = MibTableColumn
hwSIPAcceptType = _HwSIPAcceptType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 21, 1, 4),
    _HwSIPAcceptType_Type()
)
hwSIPAcceptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSIPAcceptType.setStatus("current")
_HwSIPServerStatus_Type = RowStatus
_HwSIPServerStatus_Object = MibTableColumn
hwSIPServerStatus = _HwSIPServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 1, 21, 1, 5),
    _HwSIPServerStatus_Type()
)
hwSIPServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSIPServerStatus.setStatus("current")
_HwSIPClientNotifications_ObjectIdentity = ObjectIdentity
hwSIPClientNotifications = _HwSIPClientNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 2)
)

# Managed Objects groups


# Notification objects

hwSIPRegisterFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 2, 1)
)
hwSIPRegisterFailure.setObjects(
      *(("HUAWEI-SIP-MIB", "hwSIPServerIPAddress"),
        ("HUAWEI-SIP-MIB", "hwSIPServerPort"),
        ("HUAWEI-SIP-MIB", "hwSIPRegisterFailReason"),
        ("HUAWEI-SIP-MIB", "hwSIPID"))
)
if mibBuilder.loadTexts:
    hwSIPRegisterFailure.setStatus(
        "current"
    )

hwSIPAuthenticateFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 2, 2)
)
hwSIPAuthenticateFailure.setObjects(
      *(("HUAWEI-SIP-MIB", "hwSIPID"),
        ("HUAWEI-SIP-MIB", "hwSIPAuthenticatedRequestMethord"))
)
if mibBuilder.loadTexts:
    hwSIPAuthenticateFailure.setStatus(
        "current"
    )

hwSIPServerSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 12, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hwSIPServerSwitch.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-SIP-MIB",
    **{"hwSIPMIB": hwSIPMIB,
       "hwSIPServerMIB": hwSIPServerMIB,
       "hwSIPClientMIB": hwSIPClientMIB,
       "hwSIPClientMIBObjects": hwSIPClientMIBObjects,
       "hwSIPID": hwSIPID,
       "hwSIPPasswordType": hwSIPPasswordType,
       "hwSIPPassword": hwSIPPassword,
       "hwSIPTransport": hwSIPTransport,
       "hwSIPSourceIP": hwSIPSourceIP,
       "hwSIPCallDebugSwitch": hwSIPCallDebugSwitch,
       "hwSIPRegisterDebugSwitch": hwSIPRegisterDebugSwitch,
       "hwSIPRegPrimitiveDebugSwitch": hwSIPRegPrimitiveDebugSwitch,
       "hwSIPCallPrimitiveDebugSwitch": hwSIPCallPrimitiveDebugSwitch,
       "hwSIPWarningDebugSwitch": hwSIPWarningDebugSwitch,
       "hwSIPErrorDebugSwitch": hwSIPErrorDebugSwitch,
       "hwSIPTrapsControl": hwSIPTrapsControl,
       "hwSIPStatisticClear": hwSIPStatisticClear,
       "hwSIPRegisterFailReason": hwSIPRegisterFailReason,
       "hwSIPAuthenticatedRequestMethord": hwSIPAuthenticatedRequestMethord,
       "hwSIPStatisticObjects": hwSIPStatisticObjects,
       "hwSIPRegisters": hwSIPRegisters,
       "hwSIPInvites": hwSIPInvites,
       "hwSIPAcks": hwSIPAcks,
       "hwSIPPracks": hwSIPPracks,
       "hwSIPByes": hwSIPByes,
       "hwSIPCancels": hwSIPCancels,
       "hwSIPInfos": hwSIPInfos,
       "hwSIPOKRegisters": hwSIPOKRegisters,
       "hwSIPOKInvites": hwSIPOKInvites,
       "hwSIPOKAcks": hwSIPOKAcks,
       "hwSIPOKPracks": hwSIPOKPracks,
       "hwSIPOKByes": hwSIPOKByes,
       "hwSIPOKCancels": hwSIPOKCancels,
       "hwSIPOKInfos": hwSIPOKInfos,
       "hwSIPResp3MultipleChoice": hwSIPResp3MultipleChoice,
       "hwSIPResp3MovedPermanently": hwSIPResp3MovedPermanently,
       "hwSIPResp3MovedTemporarily": hwSIPResp3MovedTemporarily,
       "hwSIPResp3UseProxy": hwSIPResp3UseProxy,
       "hwSIPResp3Other": hwSIPResp3Other,
       "hwSIPResp4BadRequest": hwSIPResp4BadRequest,
       "hwSIPResp4Unauthorized": hwSIPResp4Unauthorized,
       "hwSIPResp4Forbidden": hwSIPResp4Forbidden,
       "hwSIPResp4NotFound": hwSIPResp4NotFound,
       "hwSIPResp4MethodNotAllowed": hwSIPResp4MethodNotAllowed,
       "hwSIPResp4NotAcceptable": hwSIPResp4NotAcceptable,
       "hwSIPResp4ProxyAuthRequired": hwSIPResp4ProxyAuthRequired,
       "hwSIPResp4ReqTimeout": hwSIPResp4ReqTimeout,
       "hwSIPResp4ReqEntityTooLarge": hwSIPResp4ReqEntityTooLarge,
       "hwSIPResp4ReqURITooLarge": hwSIPResp4ReqURITooLarge,
       "hwSIPResp4UnsupportedMediaType": hwSIPResp4UnsupportedMediaType,
       "hwSIPResp4UnsupportedURIScheme": hwSIPResp4UnsupportedURIScheme,
       "hwSIPResp4BadExtension": hwSIPResp4BadExtension,
       "hwSIPResp4ExtensionRequired": hwSIPResp4ExtensionRequired,
       "hwSIPResp4AddrIncomplete": hwSIPResp4AddrIncomplete,
       "hwSIPResp4BusyHere": hwSIPResp4BusyHere,
       "hwSIPResp4RequestTerminated": hwSIPResp4RequestTerminated,
       "hwSIPResp4Other": hwSIPResp4Other,
       "hwSIPResp5InternalError": hwSIPResp5InternalError,
       "hwSIPResp5NotImplemented": hwSIPResp5NotImplemented,
       "hwSIPResp5BadGateway": hwSIPResp5BadGateway,
       "hwSIPResp5ServiceUnavailable": hwSIPResp5ServiceUnavailable,
       "hwSIPResp5GatewayTimeout": hwSIPResp5GatewayTimeout,
       "hwSIPResp5BadSipVersion": hwSIPResp5BadSipVersion,
       "hwSIPResp5MessageTooLarge": hwSIPResp5MessageTooLarge,
       "hwSIPResp5Other": hwSIPResp5Other,
       "hwSIPResp6xx": hwSIPResp6xx,
       "hwSIPServerConfigTable": hwSIPServerConfigTable,
       "hwSIPServerConfigEntry": hwSIPServerConfigEntry,
       "hwSIPServerIPAddress": hwSIPServerIPAddress,
       "hwSIPServerPort": hwSIPServerPort,
       "hwSIPServerType": hwSIPServerType,
       "hwSIPAcceptType": hwSIPAcceptType,
       "hwSIPServerStatus": hwSIPServerStatus,
       "hwSIPClientNotifications": hwSIPClientNotifications,
       "hwSIPRegisterFailure": hwSIPRegisterFailure,
       "hwSIPAuthenticateFailure": hwSIPAuthenticateFailure,
       "hwSIPServerSwitch": hwSIPServerSwitch}
)
