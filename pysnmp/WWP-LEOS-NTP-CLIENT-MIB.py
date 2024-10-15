# SNMP MIB module (WWP-LEOS-NTP-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-NTP-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:58 2024
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

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosNtpClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18)
)
wwpLeosNtpClientMIB.setRevisions(
        ("2012-09-12 00:00",
         "2012-05-31 00:00",
         "2012-03-27 00:00",
         "2011-07-05 00:00",
         "2011-03-29 12:00",
         "2008-05-20 00:00",
         "2007-12-20 00:00",
         "2007-07-15 10:00",
         "2003-04-11 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Md5Key(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



# MIB Managed Objects in the order of their OIDs

_WwpLeosNtpClientMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosNtpClientMIBObjects = _WwpLeosNtpClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1)
)
_WwpLeosNtpClient_ObjectIdentity = ObjectIdentity
wwpLeosNtpClient = _WwpLeosNtpClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1)
)


class _WwpLeosNtpClientState_Type(Integer32):
    """Custom type wwpLeosNtpClientState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WwpLeosNtpClientState_Type.__name__ = "Integer32"
_WwpLeosNtpClientState_Object = MibScalar
wwpLeosNtpClientState = _WwpLeosNtpClientState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 1),
    _WwpLeosNtpClientState_Type()
)
wwpLeosNtpClientState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosNtpClientState.setStatus("current")


class _WwpLeosNtpClientMode_Type(Integer32):
    """Custom type wwpLeosNtpClientMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 2),
          ("polling", 1))
    )


_WwpLeosNtpClientMode_Type.__name__ = "Integer32"
_WwpLeosNtpClientMode_Object = MibScalar
wwpLeosNtpClientMode = _WwpLeosNtpClientMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 2),
    _WwpLeosNtpClientMode_Type()
)
wwpLeosNtpClientMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosNtpClientMode.setStatus("current")


class _WwpLeosNtpClientPollFreq_Type(Integer32):
    """Custom type wwpLeosNtpClientPollFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 4096),
    )


_WwpLeosNtpClientPollFreq_Type.__name__ = "Integer32"
_WwpLeosNtpClientPollFreq_Object = MibScalar
wwpLeosNtpClientPollFreq = _WwpLeosNtpClientPollFreq_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 3),
    _WwpLeosNtpClientPollFreq_Type()
)
wwpLeosNtpClientPollFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosNtpClientPollFreq.setStatus("current")
_WwpLeosNtpClientTable_Object = MibTable
wwpLeosNtpClientTable = _WwpLeosNtpClientTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 4)
)
if mibBuilder.loadTexts:
    wwpLeosNtpClientTable.setStatus("current")
_WwpLeosNtpClientEntry_Object = MibTableRow
wwpLeosNtpClientEntry = _WwpLeosNtpClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 4, 1)
)
wwpLeosNtpClientEntry.setIndexNames(
    (0, "WWP-LEOS-NTP-CLIENT-MIB", "wwpLeosNtpServerIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosNtpClientEntry.setStatus("current")


class _WwpLeosNtpServerIndex_Type(Integer32):
    """Custom type wwpLeosNtpServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WwpLeosNtpServerIndex_Type.__name__ = "Integer32"
_WwpLeosNtpServerIndex_Object = MibTableColumn
wwpLeosNtpServerIndex = _WwpLeosNtpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 4, 1, 1),
    _WwpLeosNtpServerIndex_Type()
)
wwpLeosNtpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosNtpServerIndex.setStatus("current")
_WwpLeosNtpServerAddrType_Type = AddressFamilyNumbers
_WwpLeosNtpServerAddrType_Object = MibTableColumn
wwpLeosNtpServerAddrType = _WwpLeosNtpServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 4, 1, 2),
    _WwpLeosNtpServerAddrType_Type()
)
wwpLeosNtpServerAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosNtpServerAddrType.setStatus("current")
_WwpLeosNtpServerAddr_Type = DisplayString
_WwpLeosNtpServerAddr_Object = MibTableColumn
wwpLeosNtpServerAddr = _WwpLeosNtpServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 4, 1, 3),
    _WwpLeosNtpServerAddr_Type()
)
wwpLeosNtpServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosNtpServerAddr.setStatus("current")
_WwpLeosNtpServerResolvedAddr_Type = IpAddress
_WwpLeosNtpServerResolvedAddr_Object = MibTableColumn
wwpLeosNtpServerResolvedAddr = _WwpLeosNtpServerResolvedAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 4, 1, 4),
    _WwpLeosNtpServerResolvedAddr_Type()
)
wwpLeosNtpServerResolvedAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosNtpServerResolvedAddr.setStatus("current")


class _WwpLeosNtpServerUserPri_Type(Integer32):
    """Custom type wwpLeosNtpServerUserPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WwpLeosNtpServerUserPri_Type.__name__ = "Integer32"
_WwpLeosNtpServerUserPri_Object = MibTableColumn
wwpLeosNtpServerUserPri = _WwpLeosNtpServerUserPri_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 4, 1, 5),
    _WwpLeosNtpServerUserPri_Type()
)
wwpLeosNtpServerUserPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosNtpServerUserPri.setStatus("deprecated")


class _WwpLeosNtpServerDhcpPri_Type(Integer32):
    """Custom type wwpLeosNtpServerDhcpPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WwpLeosNtpServerDhcpPri_Type.__name__ = "Integer32"
_WwpLeosNtpServerDhcpPri_Object = MibTableColumn
wwpLeosNtpServerDhcpPri = _WwpLeosNtpServerDhcpPri_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 4, 1, 6),
    _WwpLeosNtpServerDhcpPri_Type()
)
wwpLeosNtpServerDhcpPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosNtpServerDhcpPri.setStatus("deprecated")


class _WwpLeosNtpServerUserAdminState_Type(Integer32):
    """Custom type wwpLeosNtpServerUserAdminState based on Integer32"""
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


_WwpLeosNtpServerUserAdminState_Type.__name__ = "Integer32"
_WwpLeosNtpServerUserAdminState_Object = MibTableColumn
wwpLeosNtpServerUserAdminState = _WwpLeosNtpServerUserAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 4, 1, 7),
    _WwpLeosNtpServerUserAdminState_Type()
)
wwpLeosNtpServerUserAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosNtpServerUserAdminState.setStatus("current")


class _WwpLeosNtpServerScope_Type(Integer32):
    """Custom type wwpLeosNtpServerScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("dhcp", 2),
          ("user", 1))
    )


_WwpLeosNtpServerScope_Type.__name__ = "Integer32"
_WwpLeosNtpServerScope_Object = MibTableColumn
wwpLeosNtpServerScope = _WwpLeosNtpServerScope_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 4, 1, 8),
    _WwpLeosNtpServerScope_Type()
)
wwpLeosNtpServerScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosNtpServerScope.setStatus("current")


class _WwpLeosNtpServerOperState_Type(Integer32):
    """Custom type wwpLeosNtpServerOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notConfigured", 3))
    )


_WwpLeosNtpServerOperState_Type.__name__ = "Integer32"
_WwpLeosNtpServerOperState_Object = MibTableColumn
wwpLeosNtpServerOperState = _WwpLeosNtpServerOperState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 4, 1, 9),
    _WwpLeosNtpServerOperState_Type()
)
wwpLeosNtpServerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosNtpServerOperState.setStatus("current")
_WwpLeosNtpServerStatus_Type = RowStatus
_WwpLeosNtpServerStatus_Object = MibTableColumn
wwpLeosNtpServerStatus = _WwpLeosNtpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 4, 1, 10),
    _WwpLeosNtpServerStatus_Type()
)
wwpLeosNtpServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosNtpServerStatus.setStatus("current")


class _WwpLeosNtpServerKeyId_Type(Unsigned32):
    """Custom type wwpLeosNtpServerKeyId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_WwpLeosNtpServerKeyId_Type.__name__ = "Unsigned32"
_WwpLeosNtpServerKeyId_Object = MibTableColumn
wwpLeosNtpServerKeyId = _WwpLeosNtpServerKeyId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 4, 1, 11),
    _WwpLeosNtpServerKeyId_Type()
)
wwpLeosNtpServerKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosNtpServerKeyId.setStatus("current")


class _WwpLeosNtpServerState_Type(Integer32):
    """Custom type wwpLeosNtpServerState based on Integer32"""
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
              255,
              256)
        )
    )
    namedValues = NamedValues(
        *(("candidate", 5),
          ("correct", 3),
          ("error", 256),
          ("insane", 2),
          ("ppspeer", 8),
          ("reaching", 255),
          ("reject", 1),
          ("selected", 6),
          ("standby", 4),
          ("syspeer", 7))
    )


_WwpLeosNtpServerState_Type.__name__ = "Integer32"
_WwpLeosNtpServerState_Object = MibTableColumn
wwpLeosNtpServerState = _WwpLeosNtpServerState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 4, 1, 12),
    _WwpLeosNtpServerState_Type()
)
wwpLeosNtpServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosNtpServerState.setStatus("current")
_WwpLeosNtpServerResolvedInetAddrType_Type = InetAddressType
_WwpLeosNtpServerResolvedInetAddrType_Object = MibTableColumn
wwpLeosNtpServerResolvedInetAddrType = _WwpLeosNtpServerResolvedInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 4, 1, 13),
    _WwpLeosNtpServerResolvedInetAddrType_Type()
)
wwpLeosNtpServerResolvedInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosNtpServerResolvedInetAddrType.setStatus("current")
_WwpLeosNtpServerResolvedInetAddr_Type = InetAddress
_WwpLeosNtpServerResolvedInetAddr_Object = MibTableColumn
wwpLeosNtpServerResolvedInetAddr = _WwpLeosNtpServerResolvedInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 4, 1, 14),
    _WwpLeosNtpServerResolvedInetAddr_Type()
)
wwpLeosNtpServerResolvedInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosNtpServerResolvedInetAddr.setStatus("current")
_WwpLeosNtpAuthTable_Object = MibTable
wwpLeosNtpAuthTable = _WwpLeosNtpAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 5)
)
if mibBuilder.loadTexts:
    wwpLeosNtpAuthTable.setStatus("current")
_WwpLeosNtpAuthEntry_Object = MibTableRow
wwpLeosNtpAuthEntry = _WwpLeosNtpAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 5, 1)
)
wwpLeosNtpAuthEntry.setIndexNames(
    (0, "WWP-LEOS-NTP-CLIENT-MIB", "wwpLeosNtpAuthKeyId"),
)
if mibBuilder.loadTexts:
    wwpLeosNtpAuthEntry.setStatus("current")


class _WwpLeosNtpAuthKeyId_Type(Unsigned32):
    """Custom type wwpLeosNtpAuthKeyId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_WwpLeosNtpAuthKeyId_Type.__name__ = "Unsigned32"
_WwpLeosNtpAuthKeyId_Object = MibTableColumn
wwpLeosNtpAuthKeyId = _WwpLeosNtpAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 5, 1, 1),
    _WwpLeosNtpAuthKeyId_Type()
)
wwpLeosNtpAuthKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosNtpAuthKeyId.setStatus("current")


class _WwpLeosNtpAuthMd5Key_Type(Md5Key):
    """Custom type wwpLeosNtpAuthMd5Key based on Md5Key"""
    subtypeSpec = Md5Key.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosNtpAuthMd5Key_Type.__name__ = "Md5Key"
_WwpLeosNtpAuthMd5Key_Object = MibTableColumn
wwpLeosNtpAuthMd5Key = _WwpLeosNtpAuthMd5Key_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 5, 1, 2),
    _WwpLeosNtpAuthMd5Key_Type()
)
wwpLeosNtpAuthMd5Key.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosNtpAuthMd5Key.setStatus("current")
_WwpLeosNtpAuthRowStatus_Type = RowStatus
_WwpLeosNtpAuthRowStatus_Object = MibTableColumn
wwpLeosNtpAuthRowStatus = _WwpLeosNtpAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 5, 1, 3),
    _WwpLeosNtpAuthRowStatus_Type()
)
wwpLeosNtpAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosNtpAuthRowStatus.setStatus("current")


class _WwpLeosNtpAuthMD5KeyEnc_Type(Md5Key):
    """Custom type wwpLeosNtpAuthMD5KeyEnc based on Md5Key"""
    subtypeSpec = Md5Key.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_WwpLeosNtpAuthMD5KeyEnc_Type.__name__ = "Md5Key"
_WwpLeosNtpAuthMD5KeyEnc_Object = MibTableColumn
wwpLeosNtpAuthMD5KeyEnc = _WwpLeosNtpAuthMD5KeyEnc_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 5, 1, 4),
    _WwpLeosNtpAuthMD5KeyEnc_Type()
)
wwpLeosNtpAuthMD5KeyEnc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosNtpAuthMD5KeyEnc.setStatus("current")
_WwpLeosNtpClientMD5State_Type = TruthValue
_WwpLeosNtpClientMD5State_Object = MibScalar
wwpLeosNtpClientMD5State = _WwpLeosNtpClientMD5State_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 6),
    _WwpLeosNtpClientMD5State_Type()
)
wwpLeosNtpClientMD5State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosNtpClientMD5State.setStatus("current")
_WwpLeosNtpClientDrift_Type = Integer32
_WwpLeosNtpClientDrift_Object = MibScalar
wwpLeosNtpClientDrift = _WwpLeosNtpClientDrift_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 7),
    _WwpLeosNtpClientDrift_Type()
)
wwpLeosNtpClientDrift.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosNtpClientDrift.setStatus("current")
_WwpLeosNtpClientFastOffset_Type = Integer32
_WwpLeosNtpClientFastOffset_Object = MibScalar
wwpLeosNtpClientFastOffset = _WwpLeosNtpClientFastOffset_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 9),
    _WwpLeosNtpClientFastOffset_Type()
)
wwpLeosNtpClientFastOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosNtpClientFastOffset.setStatus("current")
_WwpLeosNtpClientSlowOffset_Type = Integer32
_WwpLeosNtpClientSlowOffset_Object = MibScalar
wwpLeosNtpClientSlowOffset = _WwpLeosNtpClientSlowOffset_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 10),
    _WwpLeosNtpClientSlowOffset_Type()
)
wwpLeosNtpClientSlowOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosNtpClientSlowOffset.setStatus("current")


class _WwpLeosNtpClientMinPollFreq_Type(Integer32):
    """Custom type wwpLeosNtpClientMinPollFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 4096),
    )


_WwpLeosNtpClientMinPollFreq_Type.__name__ = "Integer32"
_WwpLeosNtpClientMinPollFreq_Object = MibScalar
wwpLeosNtpClientMinPollFreq = _WwpLeosNtpClientMinPollFreq_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 11),
    _WwpLeosNtpClientMinPollFreq_Type()
)
wwpLeosNtpClientMinPollFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosNtpClientMinPollFreq.setStatus("current")


class _WwpLeosNtpClientMaxPollFreq_Type(Integer32):
    """Custom type wwpLeosNtpClientMaxPollFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 4096),
    )


_WwpLeosNtpClientMaxPollFreq_Type.__name__ = "Integer32"
_WwpLeosNtpClientMaxPollFreq_Object = MibScalar
wwpLeosNtpClientMaxPollFreq = _WwpLeosNtpClientMaxPollFreq_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 12),
    _WwpLeosNtpClientMaxPollFreq_Type()
)
wwpLeosNtpClientMaxPollFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosNtpClientMaxPollFreq.setStatus("current")
_WwpLeosNtpClientOffset_Type = Integer32
_WwpLeosNtpClientOffset_Object = MibScalar
wwpLeosNtpClientOffset = _WwpLeosNtpClientOffset_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 13),
    _WwpLeosNtpClientOffset_Type()
)
wwpLeosNtpClientOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosNtpClientOffset.setStatus("deprecated")
_WwpLeosNtpClientDelay_Type = Integer32
_WwpLeosNtpClientDelay_Object = MibScalar
wwpLeosNtpClientDelay = _WwpLeosNtpClientDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 14),
    _WwpLeosNtpClientDelay_Type()
)
wwpLeosNtpClientDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosNtpClientDelay.setStatus("current")
_WwpLeosNtpClientJitter_Type = Integer32
_WwpLeosNtpClientJitter_Object = MibScalar
wwpLeosNtpClientJitter = _WwpLeosNtpClientJitter_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 15),
    _WwpLeosNtpClientJitter_Type()
)
wwpLeosNtpClientJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosNtpClientJitter.setStatus("current")
_WwpLeosNtpClientNtpOffset_Type = Integer32
_WwpLeosNtpClientNtpOffset_Object = MibScalar
wwpLeosNtpClientNtpOffset = _WwpLeosNtpClientNtpOffset_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 16),
    _WwpLeosNtpClientNtpOffset_Type()
)
wwpLeosNtpClientNtpOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosNtpClientNtpOffset.setStatus("current")


class _WwpLeosNtpClientNtpFastStartMode_Type(Integer32):
    """Custom type wwpLeosNtpClientNtpFastStartMode based on Integer32"""
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


_WwpLeosNtpClientNtpFastStartMode_Type.__name__ = "Integer32"
_WwpLeosNtpClientNtpFastStartMode_Object = MibScalar
wwpLeosNtpClientNtpFastStartMode = _WwpLeosNtpClientNtpFastStartMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 17),
    _WwpLeosNtpClientNtpFastStartMode_Type()
)
wwpLeosNtpClientNtpFastStartMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosNtpClientNtpFastStartMode.setStatus("current")
_WwpLeosNtpMulticastTable_Object = MibTable
wwpLeosNtpMulticastTable = _WwpLeosNtpMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 18)
)
if mibBuilder.loadTexts:
    wwpLeosNtpMulticastTable.setStatus("current")
_WwpLeosNtpMulticastEntry_Object = MibTableRow
wwpLeosNtpMulticastEntry = _WwpLeosNtpMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 18, 1)
)
wwpLeosNtpMulticastEntry.setIndexNames(
    (0, "WWP-LEOS-NTP-CLIENT-MIB", "wwpLeosNtpMulticastIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosNtpMulticastEntry.setStatus("current")


class _WwpLeosNtpMulticastIndex_Type(Integer32):
    """Custom type wwpLeosNtpMulticastIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WwpLeosNtpMulticastIndex_Type.__name__ = "Integer32"
_WwpLeosNtpMulticastIndex_Object = MibTableColumn
wwpLeosNtpMulticastIndex = _WwpLeosNtpMulticastIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 18, 1, 1),
    _WwpLeosNtpMulticastIndex_Type()
)
wwpLeosNtpMulticastIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosNtpMulticastIndex.setStatus("current")
_WwpLeosNtpMulticastInetAddrType_Type = InetAddressType
_WwpLeosNtpMulticastInetAddrType_Object = MibTableColumn
wwpLeosNtpMulticastInetAddrType = _WwpLeosNtpMulticastInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 18, 1, 2),
    _WwpLeosNtpMulticastInetAddrType_Type()
)
wwpLeosNtpMulticastInetAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosNtpMulticastInetAddrType.setStatus("current")
_WwpLeosNtpMulticastInetAddr_Type = InetAddress
_WwpLeosNtpMulticastInetAddr_Object = MibTableColumn
wwpLeosNtpMulticastInetAddr = _WwpLeosNtpMulticastInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 18, 1, 3),
    _WwpLeosNtpMulticastInetAddr_Type()
)
wwpLeosNtpMulticastInetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosNtpMulticastInetAddr.setStatus("current")
_WwpLeosNtpMulticastRowStatus_Type = RowStatus
_WwpLeosNtpMulticastRowStatus_Object = MibTableColumn
wwpLeosNtpMulticastRowStatus = _WwpLeosNtpMulticastRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 18, 1, 4),
    _WwpLeosNtpMulticastRowStatus_Type()
)
wwpLeosNtpMulticastRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosNtpMulticastRowStatus.setStatus("current")


class _WwpLeosNtpClientSyncChangeNotifAdminState_Type(Integer32):
    """Custom type wwpLeosNtpClientSyncChangeNotifAdminState based on Integer32"""
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


_WwpLeosNtpClientSyncChangeNotifAdminState_Type.__name__ = "Integer32"
_WwpLeosNtpClientSyncChangeNotifAdminState_Object = MibScalar
wwpLeosNtpClientSyncChangeNotifAdminState = _WwpLeosNtpClientSyncChangeNotifAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 1, 19),
    _WwpLeosNtpClientSyncChangeNotifAdminState_Type()
)
wwpLeosNtpClientSyncChangeNotifAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosNtpClientSyncChangeNotifAdminState.setStatus("current")
_WwpLeosNtpClientNotifAttrs_ObjectIdentity = ObjectIdentity
wwpLeosNtpClientNotifAttrs = _WwpLeosNtpClientNotifAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 2)
)


class _WwpLeosNtpClientSyncState_Type(Integer32):
    """Custom type wwpLeosNtpClientSyncState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-synchronized", 2),
          ("synchronized", 1))
    )


_WwpLeosNtpClientSyncState_Type.__name__ = "Integer32"
_WwpLeosNtpClientSyncState_Object = MibScalar
wwpLeosNtpClientSyncState = _WwpLeosNtpClientSyncState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 1, 2, 1),
    _WwpLeosNtpClientSyncState_Type()
)
wwpLeosNtpClientSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosNtpClientSyncState.setStatus("current")
_WwpLeosNtpClientMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosNtpClientMIBNotificationPrefix = _WwpLeosNtpClientMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 2)
)
_WwpLeosNtpClientMIBNotifications_ObjectIdentity = ObjectIdentity
wwpLeosNtpClientMIBNotifications = _WwpLeosNtpClientMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 2, 0)
)
_WwpLeosNtpClientMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosNtpClientMIBConformance = _WwpLeosNtpClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 3)
)
_WwpLeosNtpClientMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosNtpClientMIBCompliances = _WwpLeosNtpClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 3, 1)
)
_WwpLeosNtpClientMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosNtpClientMIBGroups = _WwpLeosNtpClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 3, 2)
)

# Managed Objects groups


# Notification objects

wwpLeosNtpClientSyncStatusChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 18, 2, 0, 1)
)
wwpLeosNtpClientSyncStatusChangeNotification.setObjects(
    ("WWP-LEOS-NTP-CLIENT-MIB", "wwpLeosNtpClientSyncState")
)
if mibBuilder.loadTexts:
    wwpLeosNtpClientSyncStatusChangeNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-NTP-CLIENT-MIB",
    **{"Md5Key": Md5Key,
       "wwpLeosNtpClientMIB": wwpLeosNtpClientMIB,
       "wwpLeosNtpClientMIBObjects": wwpLeosNtpClientMIBObjects,
       "wwpLeosNtpClient": wwpLeosNtpClient,
       "wwpLeosNtpClientState": wwpLeosNtpClientState,
       "wwpLeosNtpClientMode": wwpLeosNtpClientMode,
       "wwpLeosNtpClientPollFreq": wwpLeosNtpClientPollFreq,
       "wwpLeosNtpClientTable": wwpLeosNtpClientTable,
       "wwpLeosNtpClientEntry": wwpLeosNtpClientEntry,
       "wwpLeosNtpServerIndex": wwpLeosNtpServerIndex,
       "wwpLeosNtpServerAddrType": wwpLeosNtpServerAddrType,
       "wwpLeosNtpServerAddr": wwpLeosNtpServerAddr,
       "wwpLeosNtpServerResolvedAddr": wwpLeosNtpServerResolvedAddr,
       "wwpLeosNtpServerUserPri": wwpLeosNtpServerUserPri,
       "wwpLeosNtpServerDhcpPri": wwpLeosNtpServerDhcpPri,
       "wwpLeosNtpServerUserAdminState": wwpLeosNtpServerUserAdminState,
       "wwpLeosNtpServerScope": wwpLeosNtpServerScope,
       "wwpLeosNtpServerOperState": wwpLeosNtpServerOperState,
       "wwpLeosNtpServerStatus": wwpLeosNtpServerStatus,
       "wwpLeosNtpServerKeyId": wwpLeosNtpServerKeyId,
       "wwpLeosNtpServerState": wwpLeosNtpServerState,
       "wwpLeosNtpServerResolvedInetAddrType": wwpLeosNtpServerResolvedInetAddrType,
       "wwpLeosNtpServerResolvedInetAddr": wwpLeosNtpServerResolvedInetAddr,
       "wwpLeosNtpAuthTable": wwpLeosNtpAuthTable,
       "wwpLeosNtpAuthEntry": wwpLeosNtpAuthEntry,
       "wwpLeosNtpAuthKeyId": wwpLeosNtpAuthKeyId,
       "wwpLeosNtpAuthMd5Key": wwpLeosNtpAuthMd5Key,
       "wwpLeosNtpAuthRowStatus": wwpLeosNtpAuthRowStatus,
       "wwpLeosNtpAuthMD5KeyEnc": wwpLeosNtpAuthMD5KeyEnc,
       "wwpLeosNtpClientMD5State": wwpLeosNtpClientMD5State,
       "wwpLeosNtpClientDrift": wwpLeosNtpClientDrift,
       "wwpLeosNtpClientFastOffset": wwpLeosNtpClientFastOffset,
       "wwpLeosNtpClientSlowOffset": wwpLeosNtpClientSlowOffset,
       "wwpLeosNtpClientMinPollFreq": wwpLeosNtpClientMinPollFreq,
       "wwpLeosNtpClientMaxPollFreq": wwpLeosNtpClientMaxPollFreq,
       "wwpLeosNtpClientOffset": wwpLeosNtpClientOffset,
       "wwpLeosNtpClientDelay": wwpLeosNtpClientDelay,
       "wwpLeosNtpClientJitter": wwpLeosNtpClientJitter,
       "wwpLeosNtpClientNtpOffset": wwpLeosNtpClientNtpOffset,
       "wwpLeosNtpClientNtpFastStartMode": wwpLeosNtpClientNtpFastStartMode,
       "wwpLeosNtpMulticastTable": wwpLeosNtpMulticastTable,
       "wwpLeosNtpMulticastEntry": wwpLeosNtpMulticastEntry,
       "wwpLeosNtpMulticastIndex": wwpLeosNtpMulticastIndex,
       "wwpLeosNtpMulticastInetAddrType": wwpLeosNtpMulticastInetAddrType,
       "wwpLeosNtpMulticastInetAddr": wwpLeosNtpMulticastInetAddr,
       "wwpLeosNtpMulticastRowStatus": wwpLeosNtpMulticastRowStatus,
       "wwpLeosNtpClientSyncChangeNotifAdminState": wwpLeosNtpClientSyncChangeNotifAdminState,
       "wwpLeosNtpClientNotifAttrs": wwpLeosNtpClientNotifAttrs,
       "wwpLeosNtpClientSyncState": wwpLeosNtpClientSyncState,
       "wwpLeosNtpClientMIBNotificationPrefix": wwpLeosNtpClientMIBNotificationPrefix,
       "wwpLeosNtpClientMIBNotifications": wwpLeosNtpClientMIBNotifications,
       "wwpLeosNtpClientSyncStatusChangeNotification": wwpLeosNtpClientSyncStatusChangeNotification,
       "wwpLeosNtpClientMIBConformance": wwpLeosNtpClientMIBConformance,
       "wwpLeosNtpClientMIBCompliances": wwpLeosNtpClientMIBCompliances,
       "wwpLeosNtpClientMIBGroups": wwpLeosNtpClientMIBGroups}
)
