# SNMP MIB module (HIRSCHMANN-MMP4-BASICL2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HIRSCHMANN-MMP4-BASICL2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:35 2024
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

(HmAgentLogSeverity,
 hirschmann) = mibBuilder.importSymbols(
    "HMPRIV-MGMT-SNMP-MIB",
    "HmAgentLogSeverity",
    "hirschmann")

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(dot1xPaePortNumber,) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "dot1xPaePortNumber")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

(VlanIndex,
 dot1qFdbId,
 dot1qVlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex",
    "dot1qFdbId",
    "dot1qVlanIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hmPlatform4BasicL2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 1)
)
hmPlatform4BasicL2.setRevisions(
        ("2005-11-22 12:00",
         "2005-08-18 12:00",
         "2004-07-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HmAgentPortMask(OctetString, TextualConvention):
    status = "current"


class BridgeId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class HmAgentDot1xPortControlMode(Integer32, TextualConvention):
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
        *(("auto", 2),
          ("forceAuthorized", 3),
          ("forceUnauthorized", 1),
          ("macBased", 4))
    )



class HmAgentDot1xSessionTerminationAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("reauthenticate", 2))
    )



# MIB Managed Objects in the order of their OIDs

_HmPlatform4_ObjectIdentity = ObjectIdentity
hmPlatform4 = _HmPlatform4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15)
)
_HmAgentInfoGroup_ObjectIdentity = ObjectIdentity
hmAgentInfoGroup = _HmAgentInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 1)
)
_HmAgentTrapLogGroup_ObjectIdentity = ObjectIdentity
hmAgentTrapLogGroup = _HmAgentTrapLogGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 1, 2)
)
_HmAgentTrapLogTotal_Type = Integer32
_HmAgentTrapLogTotal_Object = MibScalar
hmAgentTrapLogTotal = _HmAgentTrapLogTotal_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 1, 2, 1),
    _HmAgentTrapLogTotal_Type()
)
hmAgentTrapLogTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentTrapLogTotal.setStatus("current")
_HmAgentTrapLogTotalSinceLastViewed_Type = Integer32
_HmAgentTrapLogTotalSinceLastViewed_Object = MibScalar
hmAgentTrapLogTotalSinceLastViewed = _HmAgentTrapLogTotalSinceLastViewed_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 1, 2, 3),
    _HmAgentTrapLogTotalSinceLastViewed_Type()
)
hmAgentTrapLogTotalSinceLastViewed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentTrapLogTotalSinceLastViewed.setStatus("deprecated")
_HmAgentTrapLogTable_Object = MibTable
hmAgentTrapLogTable = _HmAgentTrapLogTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hmAgentTrapLogTable.setStatus("current")
_HmAgentTrapLogEntry_Object = MibTableRow
hmAgentTrapLogEntry = _HmAgentTrapLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 1, 2, 4, 1)
)
hmAgentTrapLogEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-BASICL2-MIB", "hmAgentTrapLogIndex"),
)
if mibBuilder.loadTexts:
    hmAgentTrapLogEntry.setStatus("current")
_HmAgentTrapLogIndex_Type = Integer32
_HmAgentTrapLogIndex_Object = MibTableColumn
hmAgentTrapLogIndex = _HmAgentTrapLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 1, 2, 4, 1, 1),
    _HmAgentTrapLogIndex_Type()
)
hmAgentTrapLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentTrapLogIndex.setStatus("current")
_HmAgentTrapLogSystemTime_Type = DisplayString
_HmAgentTrapLogSystemTime_Object = MibTableColumn
hmAgentTrapLogSystemTime = _HmAgentTrapLogSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 1, 2, 4, 1, 2),
    _HmAgentTrapLogSystemTime_Type()
)
hmAgentTrapLogSystemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentTrapLogSystemTime.setStatus("current")


class _HmAgentTrapLogTrap_Type(DisplayString):
    """Custom type hmAgentTrapLogTrap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_HmAgentTrapLogTrap_Type.__name__ = "DisplayString"
_HmAgentTrapLogTrap_Object = MibTableColumn
hmAgentTrapLogTrap = _HmAgentTrapLogTrap_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 1, 2, 4, 1, 3),
    _HmAgentTrapLogTrap_Type()
)
hmAgentTrapLogTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentTrapLogTrap.setStatus("current")
_HmAgentConfigGroup_ObjectIdentity = ObjectIdentity
hmAgentConfigGroup = _HmAgentConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2)
)
_HmAgentCLIConfigGroup_ObjectIdentity = ObjectIdentity
hmAgentCLIConfigGroup = _HmAgentCLIConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 1)
)
_HmAgentLoginSessionTable_Object = MibTable
hmAgentLoginSessionTable = _HmAgentLoginSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hmAgentLoginSessionTable.setStatus("current")
_HmAgentLoginSessionEntry_Object = MibTableRow
hmAgentLoginSessionEntry = _HmAgentLoginSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 1, 1, 1)
)
hmAgentLoginSessionEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-BASICL2-MIB", "hmAgentLoginSessionIndex"),
)
if mibBuilder.loadTexts:
    hmAgentLoginSessionEntry.setStatus("current")
_HmAgentLoginSessionIndex_Type = Integer32
_HmAgentLoginSessionIndex_Object = MibTableColumn
hmAgentLoginSessionIndex = _HmAgentLoginSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 1, 1, 1, 1),
    _HmAgentLoginSessionIndex_Type()
)
hmAgentLoginSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentLoginSessionIndex.setStatus("current")
_HmAgentLoginSessionUserName_Type = DisplayString
_HmAgentLoginSessionUserName_Object = MibTableColumn
hmAgentLoginSessionUserName = _HmAgentLoginSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 1, 1, 1, 2),
    _HmAgentLoginSessionUserName_Type()
)
hmAgentLoginSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentLoginSessionUserName.setStatus("current")
_HmAgentLoginSessionIPAddress_Type = IpAddress
_HmAgentLoginSessionIPAddress_Object = MibTableColumn
hmAgentLoginSessionIPAddress = _HmAgentLoginSessionIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 1, 1, 1, 3),
    _HmAgentLoginSessionIPAddress_Type()
)
hmAgentLoginSessionIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentLoginSessionIPAddress.setStatus("current")


class _HmAgentLoginSessionConnectionType_Type(Integer32):
    """Custom type hmAgentLoginSessionConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("serial", 1),
          ("telnet", 2))
    )


_HmAgentLoginSessionConnectionType_Type.__name__ = "Integer32"
_HmAgentLoginSessionConnectionType_Object = MibTableColumn
hmAgentLoginSessionConnectionType = _HmAgentLoginSessionConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 1, 1, 1, 4),
    _HmAgentLoginSessionConnectionType_Type()
)
hmAgentLoginSessionConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentLoginSessionConnectionType.setStatus("current")
_HmAgentLoginSessionIdleTime_Type = TimeTicks
_HmAgentLoginSessionIdleTime_Object = MibTableColumn
hmAgentLoginSessionIdleTime = _HmAgentLoginSessionIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 1, 1, 1, 5),
    _HmAgentLoginSessionIdleTime_Type()
)
hmAgentLoginSessionIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentLoginSessionIdleTime.setStatus("current")
_HmAgentLoginSessionSessionTime_Type = TimeTicks
_HmAgentLoginSessionSessionTime_Object = MibTableColumn
hmAgentLoginSessionSessionTime = _HmAgentLoginSessionSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 1, 1, 1, 6),
    _HmAgentLoginSessionSessionTime_Type()
)
hmAgentLoginSessionSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentLoginSessionSessionTime.setStatus("current")
_HmAgentLoginSessionStatus_Type = RowStatus
_HmAgentLoginSessionStatus_Object = MibTableColumn
hmAgentLoginSessionStatus = _HmAgentLoginSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 1, 1, 1, 7),
    _HmAgentLoginSessionStatus_Type()
)
hmAgentLoginSessionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentLoginSessionStatus.setStatus("current")
_HmAgentTelnetConfigGroup_ObjectIdentity = ObjectIdentity
hmAgentTelnetConfigGroup = _HmAgentTelnetConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 1, 2)
)


class _HmAgentTelnetLoginTimeout_Type(Integer32):
    """Custom type hmAgentTelnetLoginTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 160),
    )


_HmAgentTelnetLoginTimeout_Type.__name__ = "Integer32"
_HmAgentTelnetLoginTimeout_Object = MibScalar
hmAgentTelnetLoginTimeout = _HmAgentTelnetLoginTimeout_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 1, 2, 1),
    _HmAgentTelnetLoginTimeout_Type()
)
hmAgentTelnetLoginTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentTelnetLoginTimeout.setStatus("current")


class _HmAgentTelnetMaxSessions_Type(Integer32):
    """Custom type hmAgentTelnetMaxSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_HmAgentTelnetMaxSessions_Type.__name__ = "Integer32"
_HmAgentTelnetMaxSessions_Object = MibScalar
hmAgentTelnetMaxSessions = _HmAgentTelnetMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 1, 2, 2),
    _HmAgentTelnetMaxSessions_Type()
)
hmAgentTelnetMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentTelnetMaxSessions.setStatus("current")


class _HmAgentTelnetAllowNewMode_Type(Integer32):
    """Custom type hmAgentTelnetAllowNewMode based on Integer32"""
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


_HmAgentTelnetAllowNewMode_Type.__name__ = "Integer32"
_HmAgentTelnetAllowNewMode_Object = MibScalar
hmAgentTelnetAllowNewMode = _HmAgentTelnetAllowNewMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 1, 2, 3),
    _HmAgentTelnetAllowNewMode_Type()
)
hmAgentTelnetAllowNewMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentTelnetAllowNewMode.setStatus("current")
_HmAgentUserConfigGroup_ObjectIdentity = ObjectIdentity
hmAgentUserConfigGroup = _HmAgentUserConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 1, 3)
)


class _HmAgentUserConfigCreate_Type(DisplayString):
    """Custom type hmAgentUserConfigCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HmAgentUserConfigCreate_Type.__name__ = "DisplayString"
_HmAgentUserConfigCreate_Object = MibScalar
hmAgentUserConfigCreate = _HmAgentUserConfigCreate_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 1, 3, 1),
    _HmAgentUserConfigCreate_Type()
)
hmAgentUserConfigCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentUserConfigCreate.setStatus("current")
_HmAgentUserConfigTable_Object = MibTable
hmAgentUserConfigTable = _HmAgentUserConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hmAgentUserConfigTable.setStatus("current")
_HmAgentUserConfigEntry_Object = MibTableRow
hmAgentUserConfigEntry = _HmAgentUserConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 1, 3, 2, 1)
)
hmAgentUserConfigEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-BASICL2-MIB", "hmAgentUserIndex"),
)
if mibBuilder.loadTexts:
    hmAgentUserConfigEntry.setStatus("current")
_HmAgentUserIndex_Type = Integer32
_HmAgentUserIndex_Object = MibTableColumn
hmAgentUserIndex = _HmAgentUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 1, 3, 2, 1, 1),
    _HmAgentUserIndex_Type()
)
hmAgentUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmAgentUserIndex.setStatus("current")


class _HmAgentUserName_Type(DisplayString):
    """Custom type hmAgentUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HmAgentUserName_Type.__name__ = "DisplayString"
_HmAgentUserName_Object = MibTableColumn
hmAgentUserName = _HmAgentUserName_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 1, 3, 2, 1, 2),
    _HmAgentUserName_Type()
)
hmAgentUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentUserName.setStatus("current")


class _HmAgentUserPassword_Type(DisplayString):
    """Custom type hmAgentUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HmAgentUserPassword_Type.__name__ = "DisplayString"
_HmAgentUserPassword_Object = MibTableColumn
hmAgentUserPassword = _HmAgentUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 1, 3, 2, 1, 3),
    _HmAgentUserPassword_Type()
)
hmAgentUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentUserPassword.setStatus("current")


class _HmAgentUserAccessMode_Type(Integer32):
    """Custom type hmAgentUserAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read", 1),
          ("write", 2))
    )


_HmAgentUserAccessMode_Type.__name__ = "Integer32"
_HmAgentUserAccessMode_Object = MibTableColumn
hmAgentUserAccessMode = _HmAgentUserAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 1, 3, 2, 1, 4),
    _HmAgentUserAccessMode_Type()
)
hmAgentUserAccessMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentUserAccessMode.setStatus("current")
_HmAgentUserStatus_Type = RowStatus
_HmAgentUserStatus_Object = MibTableColumn
hmAgentUserStatus = _HmAgentUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 1, 3, 2, 1, 5),
    _HmAgentUserStatus_Type()
)
hmAgentUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentUserStatus.setStatus("current")


class _HmAgentUserAuthenticationType_Type(Integer32):
    """Custom type hmAgentUserAuthenticationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hmacmd5", 2),
          ("hmacsha", 3),
          ("none", 1))
    )


_HmAgentUserAuthenticationType_Type.__name__ = "Integer32"
_HmAgentUserAuthenticationType_Object = MibTableColumn
hmAgentUserAuthenticationType = _HmAgentUserAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 1, 3, 2, 1, 6),
    _HmAgentUserAuthenticationType_Type()
)
hmAgentUserAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentUserAuthenticationType.setStatus("current")


class _HmAgentUserEncryptionType_Type(Integer32):
    """Custom type hmAgentUserEncryptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("des", 2),
          ("none", 1))
    )


_HmAgentUserEncryptionType_Type.__name__ = "Integer32"
_HmAgentUserEncryptionType_Object = MibTableColumn
hmAgentUserEncryptionType = _HmAgentUserEncryptionType_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 1, 3, 2, 1, 7),
    _HmAgentUserEncryptionType_Type()
)
hmAgentUserEncryptionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentUserEncryptionType.setStatus("current")


class _HmAgentUserEncryptionPassword_Type(DisplayString):
    """Custom type hmAgentUserEncryptionPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 64),
    )


_HmAgentUserEncryptionPassword_Type.__name__ = "DisplayString"
_HmAgentUserEncryptionPassword_Object = MibTableColumn
hmAgentUserEncryptionPassword = _HmAgentUserEncryptionPassword_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 1, 3, 2, 1, 8),
    _HmAgentUserEncryptionPassword_Type()
)
hmAgentUserEncryptionPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentUserEncryptionPassword.setStatus("current")
_HmAgentUserDefaultPwdActive_Type = TruthValue
_HmAgentUserDefaultPwdActive_Object = MibScalar
hmAgentUserDefaultPwdActive = _HmAgentUserDefaultPwdActive_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 1, 3, 248),
    _HmAgentUserDefaultPwdActive_Type()
)
hmAgentUserDefaultPwdActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentUserDefaultPwdActive.setStatus("current")
_HmAgentLagConfigGroup_ObjectIdentity = ObjectIdentity
hmAgentLagConfigGroup = _HmAgentLagConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 2)
)


class _HmAgentLagConfigCreate_Type(DisplayString):
    """Custom type hmAgentLagConfigCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 15),
    )


_HmAgentLagConfigCreate_Type.__name__ = "DisplayString"
_HmAgentLagConfigCreate_Object = MibScalar
hmAgentLagConfigCreate = _HmAgentLagConfigCreate_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 2, 1),
    _HmAgentLagConfigCreate_Type()
)
hmAgentLagConfigCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentLagConfigCreate.setStatus("current")
_HmAgentLagSummaryConfigTable_Object = MibTable
hmAgentLagSummaryConfigTable = _HmAgentLagSummaryConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hmAgentLagSummaryConfigTable.setStatus("current")
_HmAgentLagSummaryConfigEntry_Object = MibTableRow
hmAgentLagSummaryConfigEntry = _HmAgentLagSummaryConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 2, 2, 1)
)
hmAgentLagSummaryConfigEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-BASICL2-MIB", "hmAgentLagSummaryLagIndex"),
)
if mibBuilder.loadTexts:
    hmAgentLagSummaryConfigEntry.setStatus("current")
_HmAgentLagSummaryLagIndex_Type = Integer32
_HmAgentLagSummaryLagIndex_Object = MibTableColumn
hmAgentLagSummaryLagIndex = _HmAgentLagSummaryLagIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 2, 2, 1, 1),
    _HmAgentLagSummaryLagIndex_Type()
)
hmAgentLagSummaryLagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentLagSummaryLagIndex.setStatus("current")


class _HmAgentLagSummaryName_Type(DisplayString):
    """Custom type hmAgentLagSummaryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_HmAgentLagSummaryName_Type.__name__ = "DisplayString"
_HmAgentLagSummaryName_Object = MibTableColumn
hmAgentLagSummaryName = _HmAgentLagSummaryName_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 2, 2, 1, 2),
    _HmAgentLagSummaryName_Type()
)
hmAgentLagSummaryName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentLagSummaryName.setStatus("current")
_HmAgentLagSummaryFlushTimer_Type = Integer32
_HmAgentLagSummaryFlushTimer_Object = MibTableColumn
hmAgentLagSummaryFlushTimer = _HmAgentLagSummaryFlushTimer_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 2, 2, 1, 3),
    _HmAgentLagSummaryFlushTimer_Type()
)
hmAgentLagSummaryFlushTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentLagSummaryFlushTimer.setStatus("obsolete")


class _HmAgentLagSummaryLinkTrap_Type(Integer32):
    """Custom type hmAgentLagSummaryLinkTrap based on Integer32"""
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


_HmAgentLagSummaryLinkTrap_Type.__name__ = "Integer32"
_HmAgentLagSummaryLinkTrap_Object = MibTableColumn
hmAgentLagSummaryLinkTrap = _HmAgentLagSummaryLinkTrap_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 2, 2, 1, 4),
    _HmAgentLagSummaryLinkTrap_Type()
)
hmAgentLagSummaryLinkTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentLagSummaryLinkTrap.setStatus("current")


class _HmAgentLagSummaryAdminMode_Type(Integer32):
    """Custom type hmAgentLagSummaryAdminMode based on Integer32"""
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


_HmAgentLagSummaryAdminMode_Type.__name__ = "Integer32"
_HmAgentLagSummaryAdminMode_Object = MibTableColumn
hmAgentLagSummaryAdminMode = _HmAgentLagSummaryAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 2, 2, 1, 5),
    _HmAgentLagSummaryAdminMode_Type()
)
hmAgentLagSummaryAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentLagSummaryAdminMode.setStatus("current")


class _HmAgentLagSummaryStpMode_Type(Integer32):
    """Custom type hmAgentLagSummaryStpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 4))
    )


_HmAgentLagSummaryStpMode_Type.__name__ = "Integer32"
_HmAgentLagSummaryStpMode_Object = MibTableColumn
hmAgentLagSummaryStpMode = _HmAgentLagSummaryStpMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 2, 2, 1, 6),
    _HmAgentLagSummaryStpMode_Type()
)
hmAgentLagSummaryStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentLagSummaryStpMode.setStatus("current")
_HmAgentLagSummaryAddPort_Type = Integer32
_HmAgentLagSummaryAddPort_Object = MibTableColumn
hmAgentLagSummaryAddPort = _HmAgentLagSummaryAddPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 2, 2, 1, 7),
    _HmAgentLagSummaryAddPort_Type()
)
hmAgentLagSummaryAddPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentLagSummaryAddPort.setStatus("current")
_HmAgentLagSummaryDeletePort_Type = Integer32
_HmAgentLagSummaryDeletePort_Object = MibTableColumn
hmAgentLagSummaryDeletePort = _HmAgentLagSummaryDeletePort_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 2, 2, 1, 8),
    _HmAgentLagSummaryDeletePort_Type()
)
hmAgentLagSummaryDeletePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentLagSummaryDeletePort.setStatus("current")
_HmAgentLagSummaryStatus_Type = RowStatus
_HmAgentLagSummaryStatus_Object = MibTableColumn
hmAgentLagSummaryStatus = _HmAgentLagSummaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 2, 2, 1, 9),
    _HmAgentLagSummaryStatus_Type()
)
hmAgentLagSummaryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentLagSummaryStatus.setStatus("current")


class _HmAgentLagSummaryType_Type(Integer32):
    """Custom type hmAgentLagSummaryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_HmAgentLagSummaryType_Type.__name__ = "Integer32"
_HmAgentLagSummaryType_Object = MibTableColumn
hmAgentLagSummaryType = _HmAgentLagSummaryType_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 2, 2, 1, 10),
    _HmAgentLagSummaryType_Type()
)
hmAgentLagSummaryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentLagSummaryType.setStatus("current")
_HmAgentLagDetailedConfigTable_Object = MibTable
hmAgentLagDetailedConfigTable = _HmAgentLagDetailedConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hmAgentLagDetailedConfigTable.setStatus("current")
_HmAgentLagDetailedConfigEntry_Object = MibTableRow
hmAgentLagDetailedConfigEntry = _HmAgentLagDetailedConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 2, 3, 1)
)
hmAgentLagDetailedConfigEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-BASICL2-MIB", "hmAgentLagDetailedLagIndex"),
    (0, "HIRSCHMANN-MMP4-BASICL2-MIB", "hmAgentLagDetailedIfIndex"),
)
if mibBuilder.loadTexts:
    hmAgentLagDetailedConfigEntry.setStatus("current")
_HmAgentLagDetailedLagIndex_Type = Integer32
_HmAgentLagDetailedLagIndex_Object = MibTableColumn
hmAgentLagDetailedLagIndex = _HmAgentLagDetailedLagIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 2, 3, 1, 1),
    _HmAgentLagDetailedLagIndex_Type()
)
hmAgentLagDetailedLagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentLagDetailedLagIndex.setStatus("current")
_HmAgentLagDetailedIfIndex_Type = Integer32
_HmAgentLagDetailedIfIndex_Object = MibTableColumn
hmAgentLagDetailedIfIndex = _HmAgentLagDetailedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 2, 3, 1, 2),
    _HmAgentLagDetailedIfIndex_Type()
)
hmAgentLagDetailedIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentLagDetailedIfIndex.setStatus("current")
_HmAgentLagDetailedPortSpeed_Type = ObjectIdentifier
_HmAgentLagDetailedPortSpeed_Object = MibTableColumn
hmAgentLagDetailedPortSpeed = _HmAgentLagDetailedPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 2, 3, 1, 3),
    _HmAgentLagDetailedPortSpeed_Type()
)
hmAgentLagDetailedPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentLagDetailedPortSpeed.setStatus("current")


class _HmAgentLagDetailedPortStatus_Type(Integer32):
    """Custom type hmAgentLagDetailedPortStatus based on Integer32"""
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


_HmAgentLagDetailedPortStatus_Type.__name__ = "Integer32"
_HmAgentLagDetailedPortStatus_Object = MibTableColumn
hmAgentLagDetailedPortStatus = _HmAgentLagDetailedPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 2, 3, 1, 4),
    _HmAgentLagDetailedPortStatus_Type()
)
hmAgentLagDetailedPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentLagDetailedPortStatus.setStatus("current")


class _HmAgentLagConfigStaticCapability_Type(Integer32):
    """Custom type hmAgentLagConfigStaticCapability based on Integer32"""
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


_HmAgentLagConfigStaticCapability_Type.__name__ = "Integer32"
_HmAgentLagConfigStaticCapability_Object = MibScalar
hmAgentLagConfigStaticCapability = _HmAgentLagConfigStaticCapability_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 2, 4),
    _HmAgentLagConfigStaticCapability_Type()
)
hmAgentLagConfigStaticCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentLagConfigStaticCapability.setStatus("current")
_HmAgentSpanningTreeConfigGroup_ObjectIdentity = ObjectIdentity
hmAgentSpanningTreeConfigGroup = _HmAgentSpanningTreeConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 7)
)


class _HmAgentSpanningTreeMode_Type(Integer32):
    """Custom type hmAgentSpanningTreeMode based on Integer32"""
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


_HmAgentSpanningTreeMode_Type.__name__ = "Integer32"
_HmAgentSpanningTreeMode_Object = MibScalar
hmAgentSpanningTreeMode = _HmAgentSpanningTreeMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 7, 1),
    _HmAgentSpanningTreeMode_Type()
)
hmAgentSpanningTreeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSpanningTreeMode.setStatus("current")
_HmAgentSwitchConfigGroup_ObjectIdentity = ObjectIdentity
hmAgentSwitchConfigGroup = _HmAgentSwitchConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8)
)


class _HmAgentSwitchBroadcastControlMode_Type(Integer32):
    """Custom type hmAgentSwitchBroadcastControlMode based on Integer32"""
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


_HmAgentSwitchBroadcastControlMode_Type.__name__ = "Integer32"
_HmAgentSwitchBroadcastControlMode_Object = MibScalar
hmAgentSwitchBroadcastControlMode = _HmAgentSwitchBroadcastControlMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 2),
    _HmAgentSwitchBroadcastControlMode_Type()
)
hmAgentSwitchBroadcastControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchBroadcastControlMode.setStatus("current")


class _HmAgentSwitchDot3FlowControlMode_Type(Integer32):
    """Custom type hmAgentSwitchDot3FlowControlMode based on Integer32"""
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


_HmAgentSwitchDot3FlowControlMode_Type.__name__ = "Integer32"
_HmAgentSwitchDot3FlowControlMode_Object = MibScalar
hmAgentSwitchDot3FlowControlMode = _HmAgentSwitchDot3FlowControlMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 3),
    _HmAgentSwitchDot3FlowControlMode_Type()
)
hmAgentSwitchDot3FlowControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchDot3FlowControlMode.setStatus("current")
_HmAgentSwitchAddressAgingTimeoutTable_Object = MibTable
hmAgentSwitchAddressAgingTimeoutTable = _HmAgentSwitchAddressAgingTimeoutTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 4)
)
if mibBuilder.loadTexts:
    hmAgentSwitchAddressAgingTimeoutTable.setStatus("current")
_HmAgentSwitchAddressAgingTimeoutEntry_Object = MibTableRow
hmAgentSwitchAddressAgingTimeoutEntry = _HmAgentSwitchAddressAgingTimeoutEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 4, 1)
)
hmAgentSwitchAddressAgingTimeoutEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qFdbId"),
)
if mibBuilder.loadTexts:
    hmAgentSwitchAddressAgingTimeoutEntry.setStatus("current")


class _HmAgentSwitchAddressAgingTimeout_Type(Integer32):
    """Custom type hmAgentSwitchAddressAgingTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_HmAgentSwitchAddressAgingTimeout_Type.__name__ = "Integer32"
_HmAgentSwitchAddressAgingTimeout_Object = MibTableColumn
hmAgentSwitchAddressAgingTimeout = _HmAgentSwitchAddressAgingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 4, 1, 1),
    _HmAgentSwitchAddressAgingTimeout_Type()
)
hmAgentSwitchAddressAgingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchAddressAgingTimeout.setStatus("current")
_HmAgentSwitchStaticMacFilteringTable_Object = MibTable
hmAgentSwitchStaticMacFilteringTable = _HmAgentSwitchStaticMacFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 5)
)
if mibBuilder.loadTexts:
    hmAgentSwitchStaticMacFilteringTable.setStatus("current")
_HmAgentSwitchStaticMacFilteringEntry_Object = MibTableRow
hmAgentSwitchStaticMacFilteringEntry = _HmAgentSwitchStaticMacFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 5, 1)
)
hmAgentSwitchStaticMacFilteringEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-BASICL2-MIB", "hmAgentSwitchStaticMacFilteringVlanId"),
    (0, "HIRSCHMANN-MMP4-BASICL2-MIB", "hmAgentSwitchStaticMacFilteringAddress"),
)
if mibBuilder.loadTexts:
    hmAgentSwitchStaticMacFilteringEntry.setStatus("current")
_HmAgentSwitchStaticMacFilteringVlanId_Type = Integer32
_HmAgentSwitchStaticMacFilteringVlanId_Object = MibTableColumn
hmAgentSwitchStaticMacFilteringVlanId = _HmAgentSwitchStaticMacFilteringVlanId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 5, 1, 1),
    _HmAgentSwitchStaticMacFilteringVlanId_Type()
)
hmAgentSwitchStaticMacFilteringVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchStaticMacFilteringVlanId.setStatus("current")
_HmAgentSwitchStaticMacFilteringAddress_Type = MacAddress
_HmAgentSwitchStaticMacFilteringAddress_Object = MibTableColumn
hmAgentSwitchStaticMacFilteringAddress = _HmAgentSwitchStaticMacFilteringAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 5, 1, 2),
    _HmAgentSwitchStaticMacFilteringAddress_Type()
)
hmAgentSwitchStaticMacFilteringAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchStaticMacFilteringAddress.setStatus("current")
_HmAgentSwitchStaticMacFilteringSourcePortMask_Type = HmAgentPortMask
_HmAgentSwitchStaticMacFilteringSourcePortMask_Object = MibTableColumn
hmAgentSwitchStaticMacFilteringSourcePortMask = _HmAgentSwitchStaticMacFilteringSourcePortMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 5, 1, 3),
    _HmAgentSwitchStaticMacFilteringSourcePortMask_Type()
)
hmAgentSwitchStaticMacFilteringSourcePortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchStaticMacFilteringSourcePortMask.setStatus("current")
_HmAgentSwitchStaticMacFilteringDestPortMask_Type = HmAgentPortMask
_HmAgentSwitchStaticMacFilteringDestPortMask_Object = MibTableColumn
hmAgentSwitchStaticMacFilteringDestPortMask = _HmAgentSwitchStaticMacFilteringDestPortMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 5, 1, 4),
    _HmAgentSwitchStaticMacFilteringDestPortMask_Type()
)
hmAgentSwitchStaticMacFilteringDestPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchStaticMacFilteringDestPortMask.setStatus("current")
_HmAgentSwitchStaticMacFilteringStatus_Type = RowStatus
_HmAgentSwitchStaticMacFilteringStatus_Object = MibTableColumn
hmAgentSwitchStaticMacFilteringStatus = _HmAgentSwitchStaticMacFilteringStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 5, 1, 5),
    _HmAgentSwitchStaticMacFilteringStatus_Type()
)
hmAgentSwitchStaticMacFilteringStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmAgentSwitchStaticMacFilteringStatus.setStatus("current")
_HmAgentSwitchIGMPSnoopingGroup_ObjectIdentity = ObjectIdentity
hmAgentSwitchIGMPSnoopingGroup = _HmAgentSwitchIGMPSnoopingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 6)
)


class _HmAgentSwitchIGMPSnoopingAdminMode_Type(Integer32):
    """Custom type hmAgentSwitchIGMPSnoopingAdminMode based on Integer32"""
    defaultValue = 2

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


_HmAgentSwitchIGMPSnoopingAdminMode_Type.__name__ = "Integer32"
_HmAgentSwitchIGMPSnoopingAdminMode_Object = MibScalar
hmAgentSwitchIGMPSnoopingAdminMode = _HmAgentSwitchIGMPSnoopingAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 6, 1),
    _HmAgentSwitchIGMPSnoopingAdminMode_Type()
)
hmAgentSwitchIGMPSnoopingAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchIGMPSnoopingAdminMode.setStatus("current")


class _HmAgentSwitchIGMPSnoopingGroupMembershipInterval_Type(Integer32):
    """Custom type hmAgentSwitchIGMPSnoopingGroupMembershipInterval based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3600),
    )


_HmAgentSwitchIGMPSnoopingGroupMembershipInterval_Type.__name__ = "Integer32"
_HmAgentSwitchIGMPSnoopingGroupMembershipInterval_Object = MibScalar
hmAgentSwitchIGMPSnoopingGroupMembershipInterval = _HmAgentSwitchIGMPSnoopingGroupMembershipInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 6, 2),
    _HmAgentSwitchIGMPSnoopingGroupMembershipInterval_Type()
)
hmAgentSwitchIGMPSnoopingGroupMembershipInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchIGMPSnoopingGroupMembershipInterval.setStatus("current")


class _HmAgentSwitchIGMPSnoopingMaxResponseTime_Type(Integer32):
    """Custom type hmAgentSwitchIGMPSnoopingMaxResponseTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3598),
    )


_HmAgentSwitchIGMPSnoopingMaxResponseTime_Type.__name__ = "Integer32"
_HmAgentSwitchIGMPSnoopingMaxResponseTime_Object = MibScalar
hmAgentSwitchIGMPSnoopingMaxResponseTime = _HmAgentSwitchIGMPSnoopingMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 6, 3),
    _HmAgentSwitchIGMPSnoopingMaxResponseTime_Type()
)
hmAgentSwitchIGMPSnoopingMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchIGMPSnoopingMaxResponseTime.setStatus("current")


class _HmAgentSwitchIGMPSnoopingMRPExpirationTime_Type(Integer32):
    """Custom type hmAgentSwitchIGMPSnoopingMRPExpirationTime based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_HmAgentSwitchIGMPSnoopingMRPExpirationTime_Type.__name__ = "Integer32"
_HmAgentSwitchIGMPSnoopingMRPExpirationTime_Object = MibScalar
hmAgentSwitchIGMPSnoopingMRPExpirationTime = _HmAgentSwitchIGMPSnoopingMRPExpirationTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 6, 4),
    _HmAgentSwitchIGMPSnoopingMRPExpirationTime_Type()
)
hmAgentSwitchIGMPSnoopingMRPExpirationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchIGMPSnoopingMRPExpirationTime.setStatus("current")


class _HmAgentSwitchIGMPSnoopingPortMask_Type(HmAgentPortMask):
    """Custom type hmAgentSwitchIGMPSnoopingPortMask based on HmAgentPortMask"""
    defaultHexValue = "000000000000"


_HmAgentSwitchIGMPSnoopingPortMask_Object = MibScalar
hmAgentSwitchIGMPSnoopingPortMask = _HmAgentSwitchIGMPSnoopingPortMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 6, 5),
    _HmAgentSwitchIGMPSnoopingPortMask_Type()
)
hmAgentSwitchIGMPSnoopingPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchIGMPSnoopingPortMask.setStatus("current")
_HmAgentSwitchIGMPSnoopingMulticastControlFramesProcessed_Type = Counter32
_HmAgentSwitchIGMPSnoopingMulticastControlFramesProcessed_Object = MibScalar
hmAgentSwitchIGMPSnoopingMulticastControlFramesProcessed = _HmAgentSwitchIGMPSnoopingMulticastControlFramesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 6, 6),
    _HmAgentSwitchIGMPSnoopingMulticastControlFramesProcessed_Type()
)
hmAgentSwitchIGMPSnoopingMulticastControlFramesProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchIGMPSnoopingMulticastControlFramesProcessed.setStatus("current")
_HmAgentSwitchMFDBGroup_ObjectIdentity = ObjectIdentity
hmAgentSwitchMFDBGroup = _HmAgentSwitchMFDBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 7)
)
_HmAgentSwitchMFDBTable_Object = MibTable
hmAgentSwitchMFDBTable = _HmAgentSwitchMFDBTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 7, 1)
)
if mibBuilder.loadTexts:
    hmAgentSwitchMFDBTable.setStatus("current")
_HmAgentSwitchMFDBEntry_Object = MibTableRow
hmAgentSwitchMFDBEntry = _HmAgentSwitchMFDBEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 7, 1, 1)
)
hmAgentSwitchMFDBEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-BASICL2-MIB", "hmAgentSwitchMFDBVlanId"),
    (0, "HIRSCHMANN-MMP4-BASICL2-MIB", "hmAgentSwitchMFDBMacAddress"),
    (0, "HIRSCHMANN-MMP4-BASICL2-MIB", "hmAgentSwitchMFDBProtocolType"),
)
if mibBuilder.loadTexts:
    hmAgentSwitchMFDBEntry.setStatus("current")
_HmAgentSwitchMFDBVlanId_Type = VlanIndex
_HmAgentSwitchMFDBVlanId_Object = MibTableColumn
hmAgentSwitchMFDBVlanId = _HmAgentSwitchMFDBVlanId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 7, 1, 1, 1),
    _HmAgentSwitchMFDBVlanId_Type()
)
hmAgentSwitchMFDBVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchMFDBVlanId.setStatus("current")
_HmAgentSwitchMFDBMacAddress_Type = MacAddress
_HmAgentSwitchMFDBMacAddress_Object = MibTableColumn
hmAgentSwitchMFDBMacAddress = _HmAgentSwitchMFDBMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 7, 1, 1, 2),
    _HmAgentSwitchMFDBMacAddress_Type()
)
hmAgentSwitchMFDBMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchMFDBMacAddress.setStatus("current")


class _HmAgentSwitchMFDBProtocolType_Type(Integer32):
    """Custom type hmAgentSwitchMFDBProtocolType based on Integer32"""
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
        *(("gmrp", 2),
          ("igmp", 3),
          ("msd", 4),
          ("static", 1))
    )


_HmAgentSwitchMFDBProtocolType_Type.__name__ = "Integer32"
_HmAgentSwitchMFDBProtocolType_Object = MibTableColumn
hmAgentSwitchMFDBProtocolType = _HmAgentSwitchMFDBProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 7, 1, 1, 3),
    _HmAgentSwitchMFDBProtocolType_Type()
)
hmAgentSwitchMFDBProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchMFDBProtocolType.setStatus("current")


class _HmAgentSwitchMFDBType_Type(Integer32):
    """Custom type hmAgentSwitchMFDBType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_HmAgentSwitchMFDBType_Type.__name__ = "Integer32"
_HmAgentSwitchMFDBType_Object = MibTableColumn
hmAgentSwitchMFDBType = _HmAgentSwitchMFDBType_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 7, 1, 1, 4),
    _HmAgentSwitchMFDBType_Type()
)
hmAgentSwitchMFDBType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchMFDBType.setStatus("current")
_HmAgentSwitchMFDBDescription_Type = DisplayString
_HmAgentSwitchMFDBDescription_Object = MibTableColumn
hmAgentSwitchMFDBDescription = _HmAgentSwitchMFDBDescription_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 7, 1, 1, 5),
    _HmAgentSwitchMFDBDescription_Type()
)
hmAgentSwitchMFDBDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchMFDBDescription.setStatus("current")
_HmAgentSwitchMFDBForwardingPortMask_Type = HmAgentPortMask
_HmAgentSwitchMFDBForwardingPortMask_Object = MibTableColumn
hmAgentSwitchMFDBForwardingPortMask = _HmAgentSwitchMFDBForwardingPortMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 7, 1, 1, 6),
    _HmAgentSwitchMFDBForwardingPortMask_Type()
)
hmAgentSwitchMFDBForwardingPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchMFDBForwardingPortMask.setStatus("current")
_HmAgentSwitchMFDBFilteringPortMask_Type = HmAgentPortMask
_HmAgentSwitchMFDBFilteringPortMask_Object = MibTableColumn
hmAgentSwitchMFDBFilteringPortMask = _HmAgentSwitchMFDBFilteringPortMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 7, 1, 1, 7),
    _HmAgentSwitchMFDBFilteringPortMask_Type()
)
hmAgentSwitchMFDBFilteringPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchMFDBFilteringPortMask.setStatus("current")
_HmAgentSwitchMFDBSummaryTable_Object = MibTable
hmAgentSwitchMFDBSummaryTable = _HmAgentSwitchMFDBSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 7, 2)
)
if mibBuilder.loadTexts:
    hmAgentSwitchMFDBSummaryTable.setStatus("current")
_HmAgentSwitchMFDBSummaryEntry_Object = MibTableRow
hmAgentSwitchMFDBSummaryEntry = _HmAgentSwitchMFDBSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 7, 2, 1)
)
hmAgentSwitchMFDBSummaryEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-BASICL2-MIB", "hmAgentSwitchMFDBSummaryVlanId"),
    (0, "HIRSCHMANN-MMP4-BASICL2-MIB", "hmAgentSwitchMFDBSummaryMacAddress"),
)
if mibBuilder.loadTexts:
    hmAgentSwitchMFDBSummaryEntry.setStatus("current")
_HmAgentSwitchMFDBSummaryVlanId_Type = VlanIndex
_HmAgentSwitchMFDBSummaryVlanId_Object = MibTableColumn
hmAgentSwitchMFDBSummaryVlanId = _HmAgentSwitchMFDBSummaryVlanId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 7, 2, 1, 1),
    _HmAgentSwitchMFDBSummaryVlanId_Type()
)
hmAgentSwitchMFDBSummaryVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchMFDBSummaryVlanId.setStatus("current")
_HmAgentSwitchMFDBSummaryMacAddress_Type = MacAddress
_HmAgentSwitchMFDBSummaryMacAddress_Object = MibTableColumn
hmAgentSwitchMFDBSummaryMacAddress = _HmAgentSwitchMFDBSummaryMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 7, 2, 1, 2),
    _HmAgentSwitchMFDBSummaryMacAddress_Type()
)
hmAgentSwitchMFDBSummaryMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchMFDBSummaryMacAddress.setStatus("current")
_HmAgentSwitchMFDBSummaryForwardingPortMask_Type = HmAgentPortMask
_HmAgentSwitchMFDBSummaryForwardingPortMask_Object = MibTableColumn
hmAgentSwitchMFDBSummaryForwardingPortMask = _HmAgentSwitchMFDBSummaryForwardingPortMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 7, 2, 1, 3),
    _HmAgentSwitchMFDBSummaryForwardingPortMask_Type()
)
hmAgentSwitchMFDBSummaryForwardingPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchMFDBSummaryForwardingPortMask.setStatus("current")
_HmAgentSwitchMFDBMaxTableEntries_Type = Gauge32
_HmAgentSwitchMFDBMaxTableEntries_Object = MibScalar
hmAgentSwitchMFDBMaxTableEntries = _HmAgentSwitchMFDBMaxTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 7, 3),
    _HmAgentSwitchMFDBMaxTableEntries_Type()
)
hmAgentSwitchMFDBMaxTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchMFDBMaxTableEntries.setStatus("current")
_HmAgentSwitchMFDBMostEntriesUsed_Type = Gauge32
_HmAgentSwitchMFDBMostEntriesUsed_Object = MibScalar
hmAgentSwitchMFDBMostEntriesUsed = _HmAgentSwitchMFDBMostEntriesUsed_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 7, 4),
    _HmAgentSwitchMFDBMostEntriesUsed_Type()
)
hmAgentSwitchMFDBMostEntriesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchMFDBMostEntriesUsed.setStatus("current")
_HmAgentSwitchMFDBCurrentEntries_Type = Gauge32
_HmAgentSwitchMFDBCurrentEntries_Object = MibScalar
hmAgentSwitchMFDBCurrentEntries = _HmAgentSwitchMFDBCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 7, 5),
    _HmAgentSwitchMFDBCurrentEntries_Type()
)
hmAgentSwitchMFDBCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchMFDBCurrentEntries.setStatus("current")
_HmAgentSwitchDVlanTagGroup_ObjectIdentity = ObjectIdentity
hmAgentSwitchDVlanTagGroup = _HmAgentSwitchDVlanTagGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 8)
)


class _HmAgentSwitchDVlanTagEthertype_Type(Integer32):
    """Custom type hmAgentSwitchDVlanTagEthertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HmAgentSwitchDVlanTagEthertype_Type.__name__ = "Integer32"
_HmAgentSwitchDVlanTagEthertype_Object = MibScalar
hmAgentSwitchDVlanTagEthertype = _HmAgentSwitchDVlanTagEthertype_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 8, 1),
    _HmAgentSwitchDVlanTagEthertype_Type()
)
hmAgentSwitchDVlanTagEthertype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchDVlanTagEthertype.setStatus("current")
_HmAgentSwitchVoiceVLANGroup_ObjectIdentity = ObjectIdentity
hmAgentSwitchVoiceVLANGroup = _HmAgentSwitchVoiceVLANGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 25)
)


class _HmAgentSwitchVoiceVLANAdminMode_Type(Integer32):
    """Custom type hmAgentSwitchVoiceVLANAdminMode based on Integer32"""
    defaultValue = 2

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


_HmAgentSwitchVoiceVLANAdminMode_Type.__name__ = "Integer32"
_HmAgentSwitchVoiceVLANAdminMode_Object = MibScalar
hmAgentSwitchVoiceVLANAdminMode = _HmAgentSwitchVoiceVLANAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 25, 1),
    _HmAgentSwitchVoiceVLANAdminMode_Type()
)
hmAgentSwitchVoiceVLANAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchVoiceVLANAdminMode.setStatus("current")
_HmAgentSwitchVoiceVlanDeviceTable_Object = MibTable
hmAgentSwitchVoiceVlanDeviceTable = _HmAgentSwitchVoiceVlanDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 25, 2)
)
if mibBuilder.loadTexts:
    hmAgentSwitchVoiceVlanDeviceTable.setStatus("current")
_HmAgentSwitchVoiceVlanDeviceEntry_Object = MibTableRow
hmAgentSwitchVoiceVlanDeviceEntry = _HmAgentSwitchVoiceVlanDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 25, 2, 1)
)
hmAgentSwitchVoiceVlanDeviceEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-BASICL2-MIB", "hmAgentSwitchVoiceVlanInterfaceNum"),
    (0, "HIRSCHMANN-MMP4-BASICL2-MIB", "hmAgentSwitchVoiceVlanDeviceMacAddress"),
)
if mibBuilder.loadTexts:
    hmAgentSwitchVoiceVlanDeviceEntry.setStatus("current")


class _HmAgentSwitchVoiceVlanInterfaceNum_Type(Integer32):
    """Custom type hmAgentSwitchVoiceVlanInterfaceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HmAgentSwitchVoiceVlanInterfaceNum_Type.__name__ = "Integer32"
_HmAgentSwitchVoiceVlanInterfaceNum_Object = MibTableColumn
hmAgentSwitchVoiceVlanInterfaceNum = _HmAgentSwitchVoiceVlanInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 25, 2, 1, 1),
    _HmAgentSwitchVoiceVlanInterfaceNum_Type()
)
hmAgentSwitchVoiceVlanInterfaceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchVoiceVlanInterfaceNum.setStatus("current")
_HmAgentSwitchVoiceVlanDeviceMacAddress_Type = MacAddress
_HmAgentSwitchVoiceVlanDeviceMacAddress_Object = MibTableColumn
hmAgentSwitchVoiceVlanDeviceMacAddress = _HmAgentSwitchVoiceVlanDeviceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 8, 25, 2, 1, 2),
    _HmAgentSwitchVoiceVlanDeviceMacAddress_Type()
)
hmAgentSwitchVoiceVlanDeviceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchVoiceVlanDeviceMacAddress.setStatus("current")
_HmAgentTransferConfigGroup_ObjectIdentity = ObjectIdentity
hmAgentTransferConfigGroup = _HmAgentTransferConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 9)
)
_HmAgentTransferUploadGroup_ObjectIdentity = ObjectIdentity
hmAgentTransferUploadGroup = _HmAgentTransferUploadGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 9, 1)
)


class _HmAgentTransferUploadMode_Type(Integer32):
    """Custom type hmAgentTransferUploadMode based on Integer32"""
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
        *(("tftp", 1),
          ("xmodem", 2),
          ("ymodem", 3),
          ("zmodem", 4))
    )


_HmAgentTransferUploadMode_Type.__name__ = "Integer32"
_HmAgentTransferUploadMode_Object = MibScalar
hmAgentTransferUploadMode = _HmAgentTransferUploadMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 9, 1, 1),
    _HmAgentTransferUploadMode_Type()
)
hmAgentTransferUploadMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentTransferUploadMode.setStatus("current")
_HmAgentTransferUploadServerIP_Type = IpAddress
_HmAgentTransferUploadServerIP_Object = MibScalar
hmAgentTransferUploadServerIP = _HmAgentTransferUploadServerIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 9, 1, 2),
    _HmAgentTransferUploadServerIP_Type()
)
hmAgentTransferUploadServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentTransferUploadServerIP.setStatus("current")


class _HmAgentTransferUploadPath_Type(DisplayString):
    """Custom type hmAgentTransferUploadPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HmAgentTransferUploadPath_Type.__name__ = "DisplayString"
_HmAgentTransferUploadPath_Object = MibScalar
hmAgentTransferUploadPath = _HmAgentTransferUploadPath_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 9, 1, 3),
    _HmAgentTransferUploadPath_Type()
)
hmAgentTransferUploadPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentTransferUploadPath.setStatus("current")


class _HmAgentTransferUploadFilename_Type(DisplayString):
    """Custom type hmAgentTransferUploadFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HmAgentTransferUploadFilename_Type.__name__ = "DisplayString"
_HmAgentTransferUploadFilename_Object = MibScalar
hmAgentTransferUploadFilename = _HmAgentTransferUploadFilename_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 9, 1, 4),
    _HmAgentTransferUploadFilename_Type()
)
hmAgentTransferUploadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentTransferUploadFilename.setStatus("current")


class _HmAgentTransferUploadDataType_Type(Integer32):
    """Custom type hmAgentTransferUploadDataType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("clibanner", 6),
          ("config", 2),
          ("errorlog", 3),
          ("messagelog", 4),
          ("traplog", 5))
    )


_HmAgentTransferUploadDataType_Type.__name__ = "Integer32"
_HmAgentTransferUploadDataType_Object = MibScalar
hmAgentTransferUploadDataType = _HmAgentTransferUploadDataType_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 9, 1, 5),
    _HmAgentTransferUploadDataType_Type()
)
hmAgentTransferUploadDataType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentTransferUploadDataType.setStatus("current")


class _HmAgentTransferUploadStart_Type(Integer32):
    """Custom type hmAgentTransferUploadStart based on Integer32"""
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


_HmAgentTransferUploadStart_Type.__name__ = "Integer32"
_HmAgentTransferUploadStart_Object = MibScalar
hmAgentTransferUploadStart = _HmAgentTransferUploadStart_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 9, 1, 6),
    _HmAgentTransferUploadStart_Type()
)
hmAgentTransferUploadStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentTransferUploadStart.setStatus("current")


class _HmAgentTransferUploadStatus_Type(Integer32):
    """Custom type hmAgentTransferUploadStatus based on Integer32"""
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
        *(("checkingCRC", 9),
          ("errorStarting", 3),
          ("failedCRC", 10),
          ("failureWritingToFlash", 8),
          ("invalidConfigFile", 6),
          ("notInitiated", 1),
          ("transferFailed", 13),
          ("transferStarting", 2),
          ("transferSuccessful", 12),
          ("unknownDirection", 11),
          ("updatingConfig", 5),
          ("writingToFlash", 7),
          ("wrongFileType", 4))
    )


_HmAgentTransferUploadStatus_Type.__name__ = "Integer32"
_HmAgentTransferUploadStatus_Object = MibScalar
hmAgentTransferUploadStatus = _HmAgentTransferUploadStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 9, 1, 7),
    _HmAgentTransferUploadStatus_Type()
)
hmAgentTransferUploadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentTransferUploadStatus.setStatus("current")
_HmAgentTransferDownloadGroup_ObjectIdentity = ObjectIdentity
hmAgentTransferDownloadGroup = _HmAgentTransferDownloadGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 9, 2)
)


class _HmAgentTransferDownloadMode_Type(Integer32):
    """Custom type hmAgentTransferDownloadMode based on Integer32"""
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
        *(("tftp", 1),
          ("xmodem", 2),
          ("ymodem", 3),
          ("zmodem", 4))
    )


_HmAgentTransferDownloadMode_Type.__name__ = "Integer32"
_HmAgentTransferDownloadMode_Object = MibScalar
hmAgentTransferDownloadMode = _HmAgentTransferDownloadMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 9, 2, 1),
    _HmAgentTransferDownloadMode_Type()
)
hmAgentTransferDownloadMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentTransferDownloadMode.setStatus("current")
_HmAgentTransferDownloadServerIP_Type = IpAddress
_HmAgentTransferDownloadServerIP_Object = MibScalar
hmAgentTransferDownloadServerIP = _HmAgentTransferDownloadServerIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 9, 2, 2),
    _HmAgentTransferDownloadServerIP_Type()
)
hmAgentTransferDownloadServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentTransferDownloadServerIP.setStatus("current")


class _HmAgentTransferDownloadPath_Type(DisplayString):
    """Custom type hmAgentTransferDownloadPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HmAgentTransferDownloadPath_Type.__name__ = "DisplayString"
_HmAgentTransferDownloadPath_Object = MibScalar
hmAgentTransferDownloadPath = _HmAgentTransferDownloadPath_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 9, 2, 3),
    _HmAgentTransferDownloadPath_Type()
)
hmAgentTransferDownloadPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentTransferDownloadPath.setStatus("current")


class _HmAgentTransferDownloadFilename_Type(DisplayString):
    """Custom type hmAgentTransferDownloadFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HmAgentTransferDownloadFilename_Type.__name__ = "DisplayString"
_HmAgentTransferDownloadFilename_Object = MibScalar
hmAgentTransferDownloadFilename = _HmAgentTransferDownloadFilename_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 9, 2, 4),
    _HmAgentTransferDownloadFilename_Type()
)
hmAgentTransferDownloadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentTransferDownloadFilename.setStatus("current")


class _HmAgentTransferDownloadDataType_Type(Integer32):
    """Custom type hmAgentTransferDownloadDataType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("clibanner", 11),
          ("code", 2),
          ("config", 3),
          ("sshkey-dsa", 6),
          ("sshkey-rsa1", 4),
          ("sshkey-rsa2", 5),
          ("sslpem-dhstrong", 10),
          ("sslpem-dhweak", 9),
          ("sslpem-root", 7),
          ("sslpem-server", 8))
    )


_HmAgentTransferDownloadDataType_Type.__name__ = "Integer32"
_HmAgentTransferDownloadDataType_Object = MibScalar
hmAgentTransferDownloadDataType = _HmAgentTransferDownloadDataType_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 9, 2, 5),
    _HmAgentTransferDownloadDataType_Type()
)
hmAgentTransferDownloadDataType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentTransferDownloadDataType.setStatus("current")


class _HmAgentTransferDownloadStart_Type(Integer32):
    """Custom type hmAgentTransferDownloadStart based on Integer32"""
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


_HmAgentTransferDownloadStart_Type.__name__ = "Integer32"
_HmAgentTransferDownloadStart_Object = MibScalar
hmAgentTransferDownloadStart = _HmAgentTransferDownloadStart_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 9, 2, 6),
    _HmAgentTransferDownloadStart_Type()
)
hmAgentTransferDownloadStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentTransferDownloadStart.setStatus("current")


class _HmAgentTransferDownloadStatus_Type(Integer32):
    """Custom type hmAgentTransferDownloadStatus based on Integer32"""
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
        *(("checkingCRC", 9),
          ("errorStarting", 3),
          ("failedCRC", 10),
          ("failureWritingToFlash", 8),
          ("invalidConfigFile", 6),
          ("notInitiated", 1),
          ("transferFailed", 13),
          ("transferStarting", 2),
          ("transferSuccessful", 12),
          ("unknownDirection", 11),
          ("updatingConfig", 5),
          ("writingToFlash", 7),
          ("wrongFileType", 4))
    )


_HmAgentTransferDownloadStatus_Type.__name__ = "Integer32"
_HmAgentTransferDownloadStatus_Object = MibScalar
hmAgentTransferDownloadStatus = _HmAgentTransferDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 9, 2, 7),
    _HmAgentTransferDownloadStatus_Type()
)
hmAgentTransferDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentTransferDownloadStatus.setStatus("current")
_HmAgentPortMirroringGroup_ObjectIdentity = ObjectIdentity
hmAgentPortMirroringGroup = _HmAgentPortMirroringGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 10)
)


class _HmAgentMirroredPortIfIndex_Type(Integer32):
    """Custom type hmAgentMirroredPortIfIndex based on Integer32"""
    defaultValue = 0


_HmAgentMirroredPortIfIndex_Object = MibScalar
hmAgentMirroredPortIfIndex = _HmAgentMirroredPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 10, 1),
    _HmAgentMirroredPortIfIndex_Type()
)
hmAgentMirroredPortIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentMirroredPortIfIndex.setStatus("obsolete")


class _HmAgentProbePortIfIndex_Type(Integer32):
    """Custom type hmAgentProbePortIfIndex based on Integer32"""
    defaultValue = 0


_HmAgentProbePortIfIndex_Object = MibScalar
hmAgentProbePortIfIndex = _HmAgentProbePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 10, 2),
    _HmAgentProbePortIfIndex_Type()
)
hmAgentProbePortIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentProbePortIfIndex.setStatus("obsolete")


class _HmAgentPortMirroringMode_Type(Integer32):
    """Custom type hmAgentPortMirroringMode based on Integer32"""
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
        *(("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_HmAgentPortMirroringMode_Type.__name__ = "Integer32"
_HmAgentPortMirroringMode_Object = MibScalar
hmAgentPortMirroringMode = _HmAgentPortMirroringMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 10, 3),
    _HmAgentPortMirroringMode_Type()
)
hmAgentPortMirroringMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentPortMirroringMode.setStatus("obsolete")
_HmAgentPortMirrorTable_Object = MibTable
hmAgentPortMirrorTable = _HmAgentPortMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 10, 4)
)
if mibBuilder.loadTexts:
    hmAgentPortMirrorTable.setStatus("current")
_HmAgentPortMirrorEntry_Object = MibTableRow
hmAgentPortMirrorEntry = _HmAgentPortMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 10, 4, 1)
)
hmAgentPortMirrorEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-BASICL2-MIB", "hmAgentPortMirrorSessionNum"),
)
if mibBuilder.loadTexts:
    hmAgentPortMirrorEntry.setStatus("current")
_HmAgentPortMirrorSessionNum_Type = Unsigned32
_HmAgentPortMirrorSessionNum_Object = MibTableColumn
hmAgentPortMirrorSessionNum = _HmAgentPortMirrorSessionNum_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 10, 4, 1, 1),
    _HmAgentPortMirrorSessionNum_Type()
)
hmAgentPortMirrorSessionNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmAgentPortMirrorSessionNum.setStatus("current")


class _HmAgentPortMirrorDestinationPort_Type(Unsigned32):
    """Custom type hmAgentPortMirrorDestinationPort based on Unsigned32"""
    defaultValue = 0


_HmAgentPortMirrorDestinationPort_Object = MibTableColumn
hmAgentPortMirrorDestinationPort = _HmAgentPortMirrorDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 10, 4, 1, 2),
    _HmAgentPortMirrorDestinationPort_Type()
)
hmAgentPortMirrorDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentPortMirrorDestinationPort.setStatus("current")
_HmAgentPortMirrorSourcePortMask_Type = HmAgentPortMask
_HmAgentPortMirrorSourcePortMask_Object = MibTableColumn
hmAgentPortMirrorSourcePortMask = _HmAgentPortMirrorSourcePortMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 10, 4, 1, 3),
    _HmAgentPortMirrorSourcePortMask_Type()
)
hmAgentPortMirrorSourcePortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentPortMirrorSourcePortMask.setStatus("current")


class _HmAgentPortMirrorAdminMode_Type(Integer32):
    """Custom type hmAgentPortMirrorAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_HmAgentPortMirrorAdminMode_Type.__name__ = "Integer32"
_HmAgentPortMirrorAdminMode_Object = MibTableColumn
hmAgentPortMirrorAdminMode = _HmAgentPortMirrorAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 10, 4, 1, 4),
    _HmAgentPortMirrorAdminMode_Type()
)
hmAgentPortMirrorAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentPortMirrorAdminMode.setStatus("current")
_HmAgentPortMirrorIngressMask_Type = HmAgentPortMask
_HmAgentPortMirrorIngressMask_Object = MibTableColumn
hmAgentPortMirrorIngressMask = _HmAgentPortMirrorIngressMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 10, 4, 1, 248),
    _HmAgentPortMirrorIngressMask_Type()
)
hmAgentPortMirrorIngressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentPortMirrorIngressMask.setStatus("current")
_HmAgentPortMirrorEgressMask_Type = HmAgentPortMask
_HmAgentPortMirrorEgressMask_Object = MibTableColumn
hmAgentPortMirrorEgressMask = _HmAgentPortMirrorEgressMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 10, 4, 1, 249),
    _HmAgentPortMirrorEgressMask_Type()
)
hmAgentPortMirrorEgressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentPortMirrorEgressMask.setStatus("current")
_HmAgentDot3adAggPortTable_Object = MibTable
hmAgentDot3adAggPortTable = _HmAgentDot3adAggPortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 12)
)
if mibBuilder.loadTexts:
    hmAgentDot3adAggPortTable.setStatus("current")
_HmAgentDot3adAggPortEntry_Object = MibTableRow
hmAgentDot3adAggPortEntry = _HmAgentDot3adAggPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 12, 1)
)
hmAgentDot3adAggPortEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-BASICL2-MIB", "hmAgentDot3adAggPort"),
)
if mibBuilder.loadTexts:
    hmAgentDot3adAggPortEntry.setStatus("current")
_HmAgentDot3adAggPort_Type = Integer32
_HmAgentDot3adAggPort_Object = MibTableColumn
hmAgentDot3adAggPort = _HmAgentDot3adAggPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 12, 1, 1),
    _HmAgentDot3adAggPort_Type()
)
hmAgentDot3adAggPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentDot3adAggPort.setStatus("current")


class _HmAgentDot3adAggPortLACPMode_Type(Integer32):
    """Custom type hmAgentDot3adAggPortLACPMode based on Integer32"""
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


_HmAgentDot3adAggPortLACPMode_Type.__name__ = "Integer32"
_HmAgentDot3adAggPortLACPMode_Object = MibTableColumn
hmAgentDot3adAggPortLACPMode = _HmAgentDot3adAggPortLACPMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 12, 1, 2),
    _HmAgentDot3adAggPortLACPMode_Type()
)
hmAgentDot3adAggPortLACPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentDot3adAggPortLACPMode.setStatus("current")
_HmAgentPortConfigTable_Object = MibTable
hmAgentPortConfigTable = _HmAgentPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 13)
)
if mibBuilder.loadTexts:
    hmAgentPortConfigTable.setStatus("current")
_HmAgentPortConfigEntry_Object = MibTableRow
hmAgentPortConfigEntry = _HmAgentPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 13, 1)
)
hmAgentPortConfigEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-BASICL2-MIB", "hmAgentPortDot1dBasePort"),
)
if mibBuilder.loadTexts:
    hmAgentPortConfigEntry.setStatus("current")


class _HmAgentPortDot1dBasePort_Type(Integer32):
    """Custom type hmAgentPortDot1dBasePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HmAgentPortDot1dBasePort_Type.__name__ = "Integer32"
_HmAgentPortDot1dBasePort_Object = MibTableColumn
hmAgentPortDot1dBasePort = _HmAgentPortDot1dBasePort_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 13, 1, 1),
    _HmAgentPortDot1dBasePort_Type()
)
hmAgentPortDot1dBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentPortDot1dBasePort.setStatus("current")
_HmAgentPortIfIndex_Type = Integer32
_HmAgentPortIfIndex_Object = MibTableColumn
hmAgentPortIfIndex = _HmAgentPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 13, 1, 2),
    _HmAgentPortIfIndex_Type()
)
hmAgentPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentPortIfIndex.setStatus("current")
_HmAgentPortIanaType_Type = IANAifType
_HmAgentPortIanaType_Object = MibTableColumn
hmAgentPortIanaType = _HmAgentPortIanaType_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 13, 1, 3),
    _HmAgentPortIanaType_Type()
)
hmAgentPortIanaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentPortIanaType.setStatus("current")


class _HmAgentPortSTPMode_Type(Integer32):
    """Custom type hmAgentPortSTPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot1d", 1),
          ("fast", 2),
          ("off", 3))
    )


_HmAgentPortSTPMode_Type.__name__ = "Integer32"
_HmAgentPortSTPMode_Object = MibTableColumn
hmAgentPortSTPMode = _HmAgentPortSTPMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 13, 1, 4),
    _HmAgentPortSTPMode_Type()
)
hmAgentPortSTPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentPortSTPMode.setStatus("current")


class _HmAgentPortSTPState_Type(Integer32):
    """Custom type hmAgentPortSTPState based on Integer32"""
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
        *(("blocking", 1),
          ("disabled", 5),
          ("forwarding", 4),
          ("learning", 3),
          ("listening", 2))
    )


_HmAgentPortSTPState_Type.__name__ = "Integer32"
_HmAgentPortSTPState_Object = MibTableColumn
hmAgentPortSTPState = _HmAgentPortSTPState_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 13, 1, 5),
    _HmAgentPortSTPState_Type()
)
hmAgentPortSTPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentPortSTPState.setStatus("current")


class _HmAgentPortAdminMode_Type(Integer32):
    """Custom type hmAgentPortAdminMode based on Integer32"""
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


_HmAgentPortAdminMode_Type.__name__ = "Integer32"
_HmAgentPortAdminMode_Object = MibTableColumn
hmAgentPortAdminMode = _HmAgentPortAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 13, 1, 6),
    _HmAgentPortAdminMode_Type()
)
hmAgentPortAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentPortAdminMode.setStatus("current")


class _HmAgentPortPhysicalMode_Type(Integer32):
    """Custom type hmAgentPortPhysicalMode based on Integer32"""
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
        *(("auto-negotiate", 1),
          ("full-10", 3),
          ("full-100", 5),
          ("full-1000sx", 8),
          ("full-100fx", 7),
          ("half-10", 2),
          ("half-100", 4),
          ("half-100fx", 6))
    )


_HmAgentPortPhysicalMode_Type.__name__ = "Integer32"
_HmAgentPortPhysicalMode_Object = MibTableColumn
hmAgentPortPhysicalMode = _HmAgentPortPhysicalMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 13, 1, 7),
    _HmAgentPortPhysicalMode_Type()
)
hmAgentPortPhysicalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentPortPhysicalMode.setStatus("obsolete")


class _HmAgentPortPhysicalStatus_Type(Integer32):
    """Custom type hmAgentPortPhysicalStatus based on Integer32"""
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
        *(("auto-negotiate", 1),
          ("full-10", 3),
          ("full-100", 5),
          ("full-1000sx", 8),
          ("full-100fx", 7),
          ("half-10", 2),
          ("half-100", 4),
          ("half-100fx", 6))
    )


_HmAgentPortPhysicalStatus_Type.__name__ = "Integer32"
_HmAgentPortPhysicalStatus_Object = MibTableColumn
hmAgentPortPhysicalStatus = _HmAgentPortPhysicalStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 13, 1, 8),
    _HmAgentPortPhysicalStatus_Type()
)
hmAgentPortPhysicalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentPortPhysicalStatus.setStatus("obsolete")


class _HmAgentPortLinkTrapMode_Type(Integer32):
    """Custom type hmAgentPortLinkTrapMode based on Integer32"""
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


_HmAgentPortLinkTrapMode_Type.__name__ = "Integer32"
_HmAgentPortLinkTrapMode_Object = MibTableColumn
hmAgentPortLinkTrapMode = _HmAgentPortLinkTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 13, 1, 9),
    _HmAgentPortLinkTrapMode_Type()
)
hmAgentPortLinkTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentPortLinkTrapMode.setStatus("current")


class _HmAgentPortClearStats_Type(Integer32):
    """Custom type hmAgentPortClearStats based on Integer32"""
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


_HmAgentPortClearStats_Type.__name__ = "Integer32"
_HmAgentPortClearStats_Object = MibTableColumn
hmAgentPortClearStats = _HmAgentPortClearStats_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 13, 1, 10),
    _HmAgentPortClearStats_Type()
)
hmAgentPortClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentPortClearStats.setStatus("current")
_HmAgentPortDefaultType_Type = ObjectIdentifier
_HmAgentPortDefaultType_Object = MibTableColumn
hmAgentPortDefaultType = _HmAgentPortDefaultType_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 13, 1, 11),
    _HmAgentPortDefaultType_Type()
)
hmAgentPortDefaultType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentPortDefaultType.setStatus("current")
_HmAgentPortType_Type = ObjectIdentifier
_HmAgentPortType_Object = MibTableColumn
hmAgentPortType = _HmAgentPortType_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 13, 1, 12),
    _HmAgentPortType_Type()
)
hmAgentPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentPortType.setStatus("current")


class _HmAgentPortAutoNegAdminStatus_Type(Integer32):
    """Custom type hmAgentPortAutoNegAdminStatus based on Integer32"""
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


_HmAgentPortAutoNegAdminStatus_Type.__name__ = "Integer32"
_HmAgentPortAutoNegAdminStatus_Object = MibTableColumn
hmAgentPortAutoNegAdminStatus = _HmAgentPortAutoNegAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 13, 1, 13),
    _HmAgentPortAutoNegAdminStatus_Type()
)
hmAgentPortAutoNegAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentPortAutoNegAdminStatus.setStatus("current")


class _HmAgentPortDot3FlowControlMode_Type(Integer32):
    """Custom type hmAgentPortDot3FlowControlMode based on Integer32"""
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


_HmAgentPortDot3FlowControlMode_Type.__name__ = "Integer32"
_HmAgentPortDot3FlowControlMode_Object = MibTableColumn
hmAgentPortDot3FlowControlMode = _HmAgentPortDot3FlowControlMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 13, 1, 14),
    _HmAgentPortDot3FlowControlMode_Type()
)
hmAgentPortDot3FlowControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentPortDot3FlowControlMode.setStatus("current")


class _HmAgentPortDVlanTagMode_Type(Integer32):
    """Custom type hmAgentPortDVlanTagMode based on Integer32"""
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
        *(("access", 3),
          ("core", 1),
          ("normal", 2))
    )


_HmAgentPortDVlanTagMode_Type.__name__ = "Integer32"
_HmAgentPortDVlanTagMode_Object = MibTableColumn
hmAgentPortDVlanTagMode = _HmAgentPortDVlanTagMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 13, 1, 15),
    _HmAgentPortDVlanTagMode_Type()
)
hmAgentPortDVlanTagMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentPortDVlanTagMode.setStatus("current")


class _HmAgentPortDVlanTagEthertype_Type(Integer32):
    """Custom type hmAgentPortDVlanTagEthertype based on Integer32"""
    defaultValue = 33024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HmAgentPortDVlanTagEthertype_Type.__name__ = "Integer32"
_HmAgentPortDVlanTagEthertype_Object = MibTableColumn
hmAgentPortDVlanTagEthertype = _HmAgentPortDVlanTagEthertype_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 13, 1, 16),
    _HmAgentPortDVlanTagEthertype_Type()
)
hmAgentPortDVlanTagEthertype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentPortDVlanTagEthertype.setStatus("current")
_HmAgentPortDVlanTagCustomerId_Type = Integer32
_HmAgentPortDVlanTagCustomerId_Object = MibTableColumn
hmAgentPortDVlanTagCustomerId = _HmAgentPortDVlanTagCustomerId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 13, 1, 17),
    _HmAgentPortDVlanTagCustomerId_Type()
)
hmAgentPortDVlanTagCustomerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentPortDVlanTagCustomerId.setStatus("current")
_HmAgentPortMaxFrameSizeLimit_Type = Integer32
_HmAgentPortMaxFrameSizeLimit_Object = MibTableColumn
hmAgentPortMaxFrameSizeLimit = _HmAgentPortMaxFrameSizeLimit_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 13, 1, 18),
    _HmAgentPortMaxFrameSizeLimit_Type()
)
hmAgentPortMaxFrameSizeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentPortMaxFrameSizeLimit.setStatus("current")
_HmAgentPortMaxFrameSize_Type = Integer32
_HmAgentPortMaxFrameSize_Object = MibTableColumn
hmAgentPortMaxFrameSize = _HmAgentPortMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 13, 1, 19),
    _HmAgentPortMaxFrameSize_Type()
)
hmAgentPortMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentPortMaxFrameSize.setStatus("current")


class _HmAgentPortVoiceVlanMode_Type(Integer32):
    """Custom type hmAgentPortVoiceVlanMode based on Integer32"""
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
        *(("disable", 6),
          ("dot1p", 3),
          ("none", 1),
          ("untagged", 5),
          ("vlanid", 2),
          ("vlanidanddot1p", 4))
    )


_HmAgentPortVoiceVlanMode_Type.__name__ = "Integer32"
_HmAgentPortVoiceVlanMode_Object = MibTableColumn
hmAgentPortVoiceVlanMode = _HmAgentPortVoiceVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 13, 1, 20),
    _HmAgentPortVoiceVlanMode_Type()
)
hmAgentPortVoiceVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentPortVoiceVlanMode.setStatus("current")


class _HmAgentPortVoiceVlanID_Type(Integer32):
    """Custom type hmAgentPortVoiceVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4093),
    )


_HmAgentPortVoiceVlanID_Type.__name__ = "Integer32"
_HmAgentPortVoiceVlanID_Object = MibTableColumn
hmAgentPortVoiceVlanID = _HmAgentPortVoiceVlanID_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 13, 1, 21),
    _HmAgentPortVoiceVlanID_Type()
)
hmAgentPortVoiceVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentPortVoiceVlanID.setStatus("current")


class _HmAgentPortVoiceVlanPriority_Type(Integer32):
    """Custom type hmAgentPortVoiceVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HmAgentPortVoiceVlanPriority_Type.__name__ = "Integer32"
_HmAgentPortVoiceVlanPriority_Object = MibTableColumn
hmAgentPortVoiceVlanPriority = _HmAgentPortVoiceVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 13, 1, 22),
    _HmAgentPortVoiceVlanPriority_Type()
)
hmAgentPortVoiceVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentPortVoiceVlanPriority.setStatus("current")


class _HmAgentPortVoiceVlanDataPriorityMode_Type(Integer32):
    """Custom type hmAgentPortVoiceVlanDataPriorityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trust", 1),
          ("untrust", 2))
    )


_HmAgentPortVoiceVlanDataPriorityMode_Type.__name__ = "Integer32"
_HmAgentPortVoiceVlanDataPriorityMode_Object = MibTableColumn
hmAgentPortVoiceVlanDataPriorityMode = _HmAgentPortVoiceVlanDataPriorityMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 13, 1, 23),
    _HmAgentPortVoiceVlanDataPriorityMode_Type()
)
hmAgentPortVoiceVlanDataPriorityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentPortVoiceVlanDataPriorityMode.setStatus("current")


class _HmAgentPortVoiceVlanOperationalStatus_Type(Integer32):
    """Custom type hmAgentPortVoiceVlanOperationalStatus based on Integer32"""
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


_HmAgentPortVoiceVlanOperationalStatus_Type.__name__ = "Integer32"
_HmAgentPortVoiceVlanOperationalStatus_Object = MibTableColumn
hmAgentPortVoiceVlanOperationalStatus = _HmAgentPortVoiceVlanOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 13, 1, 24),
    _HmAgentPortVoiceVlanOperationalStatus_Type()
)
hmAgentPortVoiceVlanOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentPortVoiceVlanOperationalStatus.setStatus("current")
_HmAgentPortVoiceVlanDSCP_Type = Integer32
_HmAgentPortVoiceVlanDSCP_Object = MibTableColumn
hmAgentPortVoiceVlanDSCP = _HmAgentPortVoiceVlanDSCP_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 13, 1, 25),
    _HmAgentPortVoiceVlanDSCP_Type()
)
hmAgentPortVoiceVlanDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentPortVoiceVlanDSCP.setStatus("current")


class _HmAgentPortVoiceVlanAuthMode_Type(Integer32):
    """Custom type hmAgentPortVoiceVlanAuthMode based on Integer32"""
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


_HmAgentPortVoiceVlanAuthMode_Type.__name__ = "Integer32"
_HmAgentPortVoiceVlanAuthMode_Object = MibTableColumn
hmAgentPortVoiceVlanAuthMode = _HmAgentPortVoiceVlanAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 13, 1, 26),
    _HmAgentPortVoiceVlanAuthMode_Type()
)
hmAgentPortVoiceVlanAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentPortVoiceVlanAuthMode.setStatus("current")
_HmAgentProtocolConfigGroup_ObjectIdentity = ObjectIdentity
hmAgentProtocolConfigGroup = _HmAgentProtocolConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 14)
)


class _HmAgentProtocolGroupCreate_Type(DisplayString):
    """Custom type hmAgentProtocolGroupCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_HmAgentProtocolGroupCreate_Type.__name__ = "DisplayString"
_HmAgentProtocolGroupCreate_Object = MibScalar
hmAgentProtocolGroupCreate = _HmAgentProtocolGroupCreate_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 14, 1),
    _HmAgentProtocolGroupCreate_Type()
)
hmAgentProtocolGroupCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentProtocolGroupCreate.setStatus("current")
_HmAgentProtocolGroupTable_Object = MibTable
hmAgentProtocolGroupTable = _HmAgentProtocolGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 14, 2)
)
if mibBuilder.loadTexts:
    hmAgentProtocolGroupTable.setStatus("current")
_HmAgentProtocolGroupEntry_Object = MibTableRow
hmAgentProtocolGroupEntry = _HmAgentProtocolGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 14, 2, 1)
)
hmAgentProtocolGroupEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-BASICL2-MIB", "hmAgentProtocolGroupId"),
)
if mibBuilder.loadTexts:
    hmAgentProtocolGroupEntry.setStatus("current")
_HmAgentProtocolGroupId_Type = Integer32
_HmAgentProtocolGroupId_Object = MibTableColumn
hmAgentProtocolGroupId = _HmAgentProtocolGroupId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 14, 2, 1, 1),
    _HmAgentProtocolGroupId_Type()
)
hmAgentProtocolGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentProtocolGroupId.setStatus("current")
_HmAgentProtocolGroupName_Type = DisplayString
_HmAgentProtocolGroupName_Object = MibTableColumn
hmAgentProtocolGroupName = _HmAgentProtocolGroupName_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 14, 2, 1, 2),
    _HmAgentProtocolGroupName_Type()
)
hmAgentProtocolGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentProtocolGroupName.setStatus("current")
_HmAgentProtocolGroupVlanId_Type = Integer32
_HmAgentProtocolGroupVlanId_Object = MibTableColumn
hmAgentProtocolGroupVlanId = _HmAgentProtocolGroupVlanId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 14, 2, 1, 3),
    _HmAgentProtocolGroupVlanId_Type()
)
hmAgentProtocolGroupVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentProtocolGroupVlanId.setStatus("current")


class _HmAgentProtocolGroupProtocolIP_Type(Integer32):
    """Custom type hmAgentProtocolGroupProtocolIP based on Integer32"""
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


_HmAgentProtocolGroupProtocolIP_Type.__name__ = "Integer32"
_HmAgentProtocolGroupProtocolIP_Object = MibTableColumn
hmAgentProtocolGroupProtocolIP = _HmAgentProtocolGroupProtocolIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 14, 2, 1, 4),
    _HmAgentProtocolGroupProtocolIP_Type()
)
hmAgentProtocolGroupProtocolIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentProtocolGroupProtocolIP.setStatus("current")


class _HmAgentProtocolGroupProtocolARP_Type(Integer32):
    """Custom type hmAgentProtocolGroupProtocolARP based on Integer32"""
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


_HmAgentProtocolGroupProtocolARP_Type.__name__ = "Integer32"
_HmAgentProtocolGroupProtocolARP_Object = MibTableColumn
hmAgentProtocolGroupProtocolARP = _HmAgentProtocolGroupProtocolARP_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 14, 2, 1, 5),
    _HmAgentProtocolGroupProtocolARP_Type()
)
hmAgentProtocolGroupProtocolARP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentProtocolGroupProtocolARP.setStatus("current")


class _HmAgentProtocolGroupProtocolIPX_Type(Integer32):
    """Custom type hmAgentProtocolGroupProtocolIPX based on Integer32"""
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


_HmAgentProtocolGroupProtocolIPX_Type.__name__ = "Integer32"
_HmAgentProtocolGroupProtocolIPX_Object = MibTableColumn
hmAgentProtocolGroupProtocolIPX = _HmAgentProtocolGroupProtocolIPX_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 14, 2, 1, 6),
    _HmAgentProtocolGroupProtocolIPX_Type()
)
hmAgentProtocolGroupProtocolIPX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentProtocolGroupProtocolIPX.setStatus("current")
_HmAgentProtocolGroupStatus_Type = RowStatus
_HmAgentProtocolGroupStatus_Object = MibTableColumn
hmAgentProtocolGroupStatus = _HmAgentProtocolGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 14, 2, 1, 7),
    _HmAgentProtocolGroupStatus_Type()
)
hmAgentProtocolGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentProtocolGroupStatus.setStatus("current")
_HmAgentProtocolGroupPortTable_Object = MibTable
hmAgentProtocolGroupPortTable = _HmAgentProtocolGroupPortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 14, 3)
)
if mibBuilder.loadTexts:
    hmAgentProtocolGroupPortTable.setStatus("current")
_HmAgentProtocolGroupPortEntry_Object = MibTableRow
hmAgentProtocolGroupPortEntry = _HmAgentProtocolGroupPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 14, 3, 1)
)
hmAgentProtocolGroupPortEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-BASICL2-MIB", "hmAgentProtocolGroupId"),
    (0, "HIRSCHMANN-MMP4-BASICL2-MIB", "hmAgentProtocolGroupPortIfIndex"),
)
if mibBuilder.loadTexts:
    hmAgentProtocolGroupPortEntry.setStatus("current")
_HmAgentProtocolGroupPortIfIndex_Type = Integer32
_HmAgentProtocolGroupPortIfIndex_Object = MibTableColumn
hmAgentProtocolGroupPortIfIndex = _HmAgentProtocolGroupPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 14, 3, 1, 1),
    _HmAgentProtocolGroupPortIfIndex_Type()
)
hmAgentProtocolGroupPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentProtocolGroupPortIfIndex.setStatus("current")
_HmAgentProtocolGroupPortStatus_Type = RowStatus
_HmAgentProtocolGroupPortStatus_Object = MibTableColumn
hmAgentProtocolGroupPortStatus = _HmAgentProtocolGroupPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 14, 3, 1, 2),
    _HmAgentProtocolGroupPortStatus_Type()
)
hmAgentProtocolGroupPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmAgentProtocolGroupPortStatus.setStatus("current")
_HmAgentStpSwitchConfigGroup_ObjectIdentity = ObjectIdentity
hmAgentStpSwitchConfigGroup = _HmAgentStpSwitchConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15)
)


class _HmAgentStpConfigDigestKey_Type(OctetString):
    """Custom type hmAgentStpConfigDigestKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HmAgentStpConfigDigestKey_Type.__name__ = "OctetString"
_HmAgentStpConfigDigestKey_Object = MibScalar
hmAgentStpConfigDigestKey = _HmAgentStpConfigDigestKey_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 1),
    _HmAgentStpConfigDigestKey_Type()
)
hmAgentStpConfigDigestKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpConfigDigestKey.setStatus("current")


class _HmAgentStpConfigFormatSelector_Type(Unsigned32):
    """Custom type hmAgentStpConfigFormatSelector based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HmAgentStpConfigFormatSelector_Type.__name__ = "Unsigned32"
_HmAgentStpConfigFormatSelector_Object = MibScalar
hmAgentStpConfigFormatSelector = _HmAgentStpConfigFormatSelector_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 2),
    _HmAgentStpConfigFormatSelector_Type()
)
hmAgentStpConfigFormatSelector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpConfigFormatSelector.setStatus("current")


class _HmAgentStpConfigName_Type(DisplayString):
    """Custom type hmAgentStpConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HmAgentStpConfigName_Type.__name__ = "DisplayString"
_HmAgentStpConfigName_Object = MibScalar
hmAgentStpConfigName = _HmAgentStpConfigName_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 3),
    _HmAgentStpConfigName_Type()
)
hmAgentStpConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentStpConfigName.setStatus("current")


class _HmAgentStpConfigRevision_Type(Unsigned32):
    """Custom type hmAgentStpConfigRevision based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HmAgentStpConfigRevision_Type.__name__ = "Unsigned32"
_HmAgentStpConfigRevision_Object = MibScalar
hmAgentStpConfigRevision = _HmAgentStpConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 4),
    _HmAgentStpConfigRevision_Type()
)
hmAgentStpConfigRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentStpConfigRevision.setStatus("current")


class _HmAgentStpForceVersion_Type(Integer32):
    """Custom type hmAgentStpForceVersion based on Integer32"""
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
        *(("dot1d", 1),
          ("dot1s", 3),
          ("dot1w", 2))
    )


_HmAgentStpForceVersion_Type.__name__ = "Integer32"
_HmAgentStpForceVersion_Object = MibScalar
hmAgentStpForceVersion = _HmAgentStpForceVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 5),
    _HmAgentStpForceVersion_Type()
)
hmAgentStpForceVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentStpForceVersion.setStatus("current")


class _HmAgentStpAdminMode_Type(Integer32):
    """Custom type hmAgentStpAdminMode based on Integer32"""
    defaultValue = 1

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


_HmAgentStpAdminMode_Type.__name__ = "Integer32"
_HmAgentStpAdminMode_Object = MibScalar
hmAgentStpAdminMode = _HmAgentStpAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 6),
    _HmAgentStpAdminMode_Type()
)
hmAgentStpAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentStpAdminMode.setStatus("current")
_HmAgentStpPortTable_Object = MibTable
hmAgentStpPortTable = _HmAgentStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 7)
)
if mibBuilder.loadTexts:
    hmAgentStpPortTable.setStatus("current")
_HmAgentStpPortEntry_Object = MibTableRow
hmAgentStpPortEntry = _HmAgentStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 7, 1)
)
hmAgentStpPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hmAgentStpPortEntry.setStatus("current")


class _HmAgentStpPortState_Type(Integer32):
    """Custom type hmAgentStpPortState based on Integer32"""
    defaultValue = 1

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


_HmAgentStpPortState_Type.__name__ = "Integer32"
_HmAgentStpPortState_Object = MibTableColumn
hmAgentStpPortState = _HmAgentStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 7, 1, 1),
    _HmAgentStpPortState_Type()
)
hmAgentStpPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentStpPortState.setStatus("current")
_HmAgentStpPortStatsMstpBpduRx_Type = Counter32
_HmAgentStpPortStatsMstpBpduRx_Object = MibTableColumn
hmAgentStpPortStatsMstpBpduRx = _HmAgentStpPortStatsMstpBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 7, 1, 2),
    _HmAgentStpPortStatsMstpBpduRx_Type()
)
hmAgentStpPortStatsMstpBpduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpPortStatsMstpBpduRx.setStatus("current")
_HmAgentStpPortStatsMstpBpduTx_Type = Counter32
_HmAgentStpPortStatsMstpBpduTx_Object = MibTableColumn
hmAgentStpPortStatsMstpBpduTx = _HmAgentStpPortStatsMstpBpduTx_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 7, 1, 3),
    _HmAgentStpPortStatsMstpBpduTx_Type()
)
hmAgentStpPortStatsMstpBpduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpPortStatsMstpBpduTx.setStatus("current")
_HmAgentStpPortStatsRstpBpduRx_Type = Counter32
_HmAgentStpPortStatsRstpBpduRx_Object = MibTableColumn
hmAgentStpPortStatsRstpBpduRx = _HmAgentStpPortStatsRstpBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 7, 1, 4),
    _HmAgentStpPortStatsRstpBpduRx_Type()
)
hmAgentStpPortStatsRstpBpduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpPortStatsRstpBpduRx.setStatus("current")
_HmAgentStpPortStatsRstpBpduTx_Type = Counter32
_HmAgentStpPortStatsRstpBpduTx_Object = MibTableColumn
hmAgentStpPortStatsRstpBpduTx = _HmAgentStpPortStatsRstpBpduTx_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 7, 1, 5),
    _HmAgentStpPortStatsRstpBpduTx_Type()
)
hmAgentStpPortStatsRstpBpduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpPortStatsRstpBpduTx.setStatus("current")
_HmAgentStpPortStatsStpBpduRx_Type = Counter32
_HmAgentStpPortStatsStpBpduRx_Object = MibTableColumn
hmAgentStpPortStatsStpBpduRx = _HmAgentStpPortStatsStpBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 7, 1, 6),
    _HmAgentStpPortStatsStpBpduRx_Type()
)
hmAgentStpPortStatsStpBpduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpPortStatsStpBpduRx.setStatus("current")
_HmAgentStpPortStatsStpBpduTx_Type = Counter32
_HmAgentStpPortStatsStpBpduTx_Object = MibTableColumn
hmAgentStpPortStatsStpBpduTx = _HmAgentStpPortStatsStpBpduTx_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 7, 1, 7),
    _HmAgentStpPortStatsStpBpduTx_Type()
)
hmAgentStpPortStatsStpBpduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpPortStatsStpBpduTx.setStatus("current")
_HmAgentStpPortUpTime_Type = TimeTicks
_HmAgentStpPortUpTime_Object = MibTableColumn
hmAgentStpPortUpTime = _HmAgentStpPortUpTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 7, 1, 8),
    _HmAgentStpPortUpTime_Type()
)
hmAgentStpPortUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpPortUpTime.setStatus("current")


class _HmAgentStpPortMigrationCheck_Type(Integer32):
    """Custom type hmAgentStpPortMigrationCheck based on Integer32"""
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


_HmAgentStpPortMigrationCheck_Type.__name__ = "Integer32"
_HmAgentStpPortMigrationCheck_Object = MibTableColumn
hmAgentStpPortMigrationCheck = _HmAgentStpPortMigrationCheck_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 7, 1, 9),
    _HmAgentStpPortMigrationCheck_Type()
)
hmAgentStpPortMigrationCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentStpPortMigrationCheck.setStatus("current")


class _HmAgentStpPortHelloTime_Type(Unsigned32):
    """Custom type hmAgentStpPortHelloTime based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HmAgentStpPortHelloTime_Type.__name__ = "Unsigned32"
_HmAgentStpPortHelloTime_Object = MibTableColumn
hmAgentStpPortHelloTime = _HmAgentStpPortHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 7, 1, 10),
    _HmAgentStpPortHelloTime_Type()
)
hmAgentStpPortHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentStpPortHelloTime.setStatus("current")
_HmAgentStpCstConfigGroup_ObjectIdentity = ObjectIdentity
hmAgentStpCstConfigGroup = _HmAgentStpCstConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 8)
)
_HmAgentStpCstHelloTime_Type = Unsigned32
_HmAgentStpCstHelloTime_Object = MibScalar
hmAgentStpCstHelloTime = _HmAgentStpCstHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 8, 1),
    _HmAgentStpCstHelloTime_Type()
)
hmAgentStpCstHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpCstHelloTime.setStatus("current")
_HmAgentStpCstMaxAge_Type = Unsigned32
_HmAgentStpCstMaxAge_Object = MibScalar
hmAgentStpCstMaxAge = _HmAgentStpCstMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 8, 2),
    _HmAgentStpCstMaxAge_Type()
)
hmAgentStpCstMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpCstMaxAge.setStatus("current")


class _HmAgentStpCstRegionalRootId_Type(OctetString):
    """Custom type hmAgentStpCstRegionalRootId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HmAgentStpCstRegionalRootId_Type.__name__ = "OctetString"
_HmAgentStpCstRegionalRootId_Object = MibScalar
hmAgentStpCstRegionalRootId = _HmAgentStpCstRegionalRootId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 8, 3),
    _HmAgentStpCstRegionalRootId_Type()
)
hmAgentStpCstRegionalRootId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpCstRegionalRootId.setStatus("current")
_HmAgentStpCstRegionalRootPathCost_Type = Unsigned32
_HmAgentStpCstRegionalRootPathCost_Object = MibScalar
hmAgentStpCstRegionalRootPathCost = _HmAgentStpCstRegionalRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 8, 4),
    _HmAgentStpCstRegionalRootPathCost_Type()
)
hmAgentStpCstRegionalRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpCstRegionalRootPathCost.setStatus("current")
_HmAgentStpCstRootFwdDelay_Type = Unsigned32
_HmAgentStpCstRootFwdDelay_Object = MibScalar
hmAgentStpCstRootFwdDelay = _HmAgentStpCstRootFwdDelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 8, 5),
    _HmAgentStpCstRootFwdDelay_Type()
)
hmAgentStpCstRootFwdDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpCstRootFwdDelay.setStatus("current")


class _HmAgentStpCstBridgeFwdDelay_Type(Unsigned32):
    """Custom type hmAgentStpCstBridgeFwdDelay based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_HmAgentStpCstBridgeFwdDelay_Type.__name__ = "Unsigned32"
_HmAgentStpCstBridgeFwdDelay_Object = MibScalar
hmAgentStpCstBridgeFwdDelay = _HmAgentStpCstBridgeFwdDelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 8, 6),
    _HmAgentStpCstBridgeFwdDelay_Type()
)
hmAgentStpCstBridgeFwdDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentStpCstBridgeFwdDelay.setStatus("current")


class _HmAgentStpCstBridgeHelloTime_Type(Unsigned32):
    """Custom type hmAgentStpCstBridgeHelloTime based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HmAgentStpCstBridgeHelloTime_Type.__name__ = "Unsigned32"
_HmAgentStpCstBridgeHelloTime_Object = MibScalar
hmAgentStpCstBridgeHelloTime = _HmAgentStpCstBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 8, 7),
    _HmAgentStpCstBridgeHelloTime_Type()
)
hmAgentStpCstBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentStpCstBridgeHelloTime.setStatus("current")
_HmAgentStpCstBridgeHoldTime_Type = Unsigned32
_HmAgentStpCstBridgeHoldTime_Object = MibScalar
hmAgentStpCstBridgeHoldTime = _HmAgentStpCstBridgeHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 8, 8),
    _HmAgentStpCstBridgeHoldTime_Type()
)
hmAgentStpCstBridgeHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpCstBridgeHoldTime.setStatus("current")


class _HmAgentStpCstBridgeMaxAge_Type(Unsigned32):
    """Custom type hmAgentStpCstBridgeMaxAge based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_HmAgentStpCstBridgeMaxAge_Type.__name__ = "Unsigned32"
_HmAgentStpCstBridgeMaxAge_Object = MibScalar
hmAgentStpCstBridgeMaxAge = _HmAgentStpCstBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 8, 9),
    _HmAgentStpCstBridgeMaxAge_Type()
)
hmAgentStpCstBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentStpCstBridgeMaxAge.setStatus("current")
_HmAgentStpCstBridgeDesignatedRoot_Type = BridgeId
_HmAgentStpCstBridgeDesignatedRoot_Object = MibScalar
hmAgentStpCstBridgeDesignatedRoot = _HmAgentStpCstBridgeDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 8, 10),
    _HmAgentStpCstBridgeDesignatedRoot_Type()
)
hmAgentStpCstBridgeDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpCstBridgeDesignatedRoot.setStatus("current")


class _HmAgentStpCstBridgePriority_Type(Unsigned32):
    """Custom type hmAgentStpCstBridgePriority based on Unsigned32"""
    defaultValue = 32768

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_HmAgentStpCstBridgePriority_Type.__name__ = "Unsigned32"
_HmAgentStpCstBridgePriority_Object = MibScalar
hmAgentStpCstBridgePriority = _HmAgentStpCstBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 8, 11),
    _HmAgentStpCstBridgePriority_Type()
)
hmAgentStpCstBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentStpCstBridgePriority.setStatus("current")
_HmAgentStpCstBridgeTimeSinceTopologyChange_Type = TimeTicks
_HmAgentStpCstBridgeTimeSinceTopologyChange_Object = MibScalar
hmAgentStpCstBridgeTimeSinceTopologyChange = _HmAgentStpCstBridgeTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 8, 12),
    _HmAgentStpCstBridgeTimeSinceTopologyChange_Type()
)
hmAgentStpCstBridgeTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpCstBridgeTimeSinceTopologyChange.setStatus("current")
_HmAgentStpCstBridgeTopChanges_Type = Counter32
_HmAgentStpCstBridgeTopChanges_Object = MibScalar
hmAgentStpCstBridgeTopChanges = _HmAgentStpCstBridgeTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 8, 13),
    _HmAgentStpCstBridgeTopChanges_Type()
)
hmAgentStpCstBridgeTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpCstBridgeTopChanges.setStatus("current")
_HmAgentStpCstBridgeRootCost_Type = Unsigned32
_HmAgentStpCstBridgeRootCost_Object = MibScalar
hmAgentStpCstBridgeRootCost = _HmAgentStpCstBridgeRootCost_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 8, 14),
    _HmAgentStpCstBridgeRootCost_Type()
)
hmAgentStpCstBridgeRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpCstBridgeRootCost.setStatus("current")
_HmAgentStpCstBridgeRootPort_Type = Unsigned32
_HmAgentStpCstBridgeRootPort_Object = MibScalar
hmAgentStpCstBridgeRootPort = _HmAgentStpCstBridgeRootPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 8, 15),
    _HmAgentStpCstBridgeRootPort_Type()
)
hmAgentStpCstBridgeRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpCstBridgeRootPort.setStatus("current")


class _HmAgentStpCstBridgeMaxHops_Type(Unsigned32):
    """Custom type hmAgentStpCstBridgeMaxHops based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_HmAgentStpCstBridgeMaxHops_Type.__name__ = "Unsigned32"
_HmAgentStpCstBridgeMaxHops_Object = MibScalar
hmAgentStpCstBridgeMaxHops = _HmAgentStpCstBridgeMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 8, 16),
    _HmAgentStpCstBridgeMaxHops_Type()
)
hmAgentStpCstBridgeMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentStpCstBridgeMaxHops.setStatus("current")


class _HmAgentStpCstBridgeHoldCount_Type(Unsigned32):
    """Custom type hmAgentStpCstBridgeHoldCount based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_HmAgentStpCstBridgeHoldCount_Type.__name__ = "Unsigned32"
_HmAgentStpCstBridgeHoldCount_Object = MibScalar
hmAgentStpCstBridgeHoldCount = _HmAgentStpCstBridgeHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 8, 17),
    _HmAgentStpCstBridgeHoldCount_Type()
)
hmAgentStpCstBridgeHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentStpCstBridgeHoldCount.setStatus("current")
_HmAgentStpCstPortTable_Object = MibTable
hmAgentStpCstPortTable = _HmAgentStpCstPortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 9)
)
if mibBuilder.loadTexts:
    hmAgentStpCstPortTable.setStatus("current")
_HmAgentStpCstPortEntry_Object = MibTableRow
hmAgentStpCstPortEntry = _HmAgentStpCstPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 9, 1)
)
hmAgentStpCstPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hmAgentStpCstPortEntry.setStatus("current")


class _HmAgentStpCstPortOperEdge_Type(Integer32):
    """Custom type hmAgentStpCstPortOperEdge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HmAgentStpCstPortOperEdge_Type.__name__ = "Integer32"
_HmAgentStpCstPortOperEdge_Object = MibTableColumn
hmAgentStpCstPortOperEdge = _HmAgentStpCstPortOperEdge_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 9, 1, 1),
    _HmAgentStpCstPortOperEdge_Type()
)
hmAgentStpCstPortOperEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpCstPortOperEdge.setStatus("current")


class _HmAgentStpCstPortOperPointToPoint_Type(Integer32):
    """Custom type hmAgentStpCstPortOperPointToPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HmAgentStpCstPortOperPointToPoint_Type.__name__ = "Integer32"
_HmAgentStpCstPortOperPointToPoint_Object = MibTableColumn
hmAgentStpCstPortOperPointToPoint = _HmAgentStpCstPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 9, 1, 2),
    _HmAgentStpCstPortOperPointToPoint_Type()
)
hmAgentStpCstPortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpCstPortOperPointToPoint.setStatus("current")


class _HmAgentStpCstPortTopologyChangeAck_Type(Integer32):
    """Custom type hmAgentStpCstPortTopologyChangeAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HmAgentStpCstPortTopologyChangeAck_Type.__name__ = "Integer32"
_HmAgentStpCstPortTopologyChangeAck_Object = MibTableColumn
hmAgentStpCstPortTopologyChangeAck = _HmAgentStpCstPortTopologyChangeAck_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 9, 1, 3),
    _HmAgentStpCstPortTopologyChangeAck_Type()
)
hmAgentStpCstPortTopologyChangeAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpCstPortTopologyChangeAck.setStatus("current")


class _HmAgentStpCstPortEdge_Type(Integer32):
    """Custom type hmAgentStpCstPortEdge based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HmAgentStpCstPortEdge_Type.__name__ = "Integer32"
_HmAgentStpCstPortEdge_Object = MibTableColumn
hmAgentStpCstPortEdge = _HmAgentStpCstPortEdge_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 9, 1, 4),
    _HmAgentStpCstPortEdge_Type()
)
hmAgentStpCstPortEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentStpCstPortEdge.setStatus("current")


class _HmAgentStpCstPortForwardingState_Type(Integer32):
    """Custom type hmAgentStpCstPortForwardingState based on Integer32"""
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
        *(("disabled", 4),
          ("discarding", 1),
          ("forwarding", 3),
          ("learning", 2),
          ("manualFwd", 5),
          ("notParticipate", 6))
    )


_HmAgentStpCstPortForwardingState_Type.__name__ = "Integer32"
_HmAgentStpCstPortForwardingState_Object = MibTableColumn
hmAgentStpCstPortForwardingState = _HmAgentStpCstPortForwardingState_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 9, 1, 5),
    _HmAgentStpCstPortForwardingState_Type()
)
hmAgentStpCstPortForwardingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpCstPortForwardingState.setStatus("current")
_HmAgentStpCstPortId_Type = OctetString
_HmAgentStpCstPortId_Object = MibTableColumn
hmAgentStpCstPortId = _HmAgentStpCstPortId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 9, 1, 6),
    _HmAgentStpCstPortId_Type()
)
hmAgentStpCstPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpCstPortId.setStatus("current")


class _HmAgentStpCstPortPathCost_Type(Unsigned32):
    """Custom type hmAgentStpCstPortPathCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_HmAgentStpCstPortPathCost_Type.__name__ = "Unsigned32"
_HmAgentStpCstPortPathCost_Object = MibTableColumn
hmAgentStpCstPortPathCost = _HmAgentStpCstPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 9, 1, 7),
    _HmAgentStpCstPortPathCost_Type()
)
hmAgentStpCstPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentStpCstPortPathCost.setStatus("current")


class _HmAgentStpCstPortPriority_Type(Unsigned32):
    """Custom type hmAgentStpCstPortPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_HmAgentStpCstPortPriority_Type.__name__ = "Unsigned32"
_HmAgentStpCstPortPriority_Object = MibTableColumn
hmAgentStpCstPortPriority = _HmAgentStpCstPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 9, 1, 8),
    _HmAgentStpCstPortPriority_Type()
)
hmAgentStpCstPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentStpCstPortPriority.setStatus("current")


class _HmAgentStpCstDesignatedBridgeId_Type(OctetString):
    """Custom type hmAgentStpCstDesignatedBridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HmAgentStpCstDesignatedBridgeId_Type.__name__ = "OctetString"
_HmAgentStpCstDesignatedBridgeId_Object = MibTableColumn
hmAgentStpCstDesignatedBridgeId = _HmAgentStpCstDesignatedBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 9, 1, 9),
    _HmAgentStpCstDesignatedBridgeId_Type()
)
hmAgentStpCstDesignatedBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpCstDesignatedBridgeId.setStatus("current")
_HmAgentStpCstDesignatedCost_Type = Unsigned32
_HmAgentStpCstDesignatedCost_Object = MibTableColumn
hmAgentStpCstDesignatedCost = _HmAgentStpCstDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 9, 1, 10),
    _HmAgentStpCstDesignatedCost_Type()
)
hmAgentStpCstDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpCstDesignatedCost.setStatus("current")


class _HmAgentStpCstDesignatedPortId_Type(OctetString):
    """Custom type hmAgentStpCstDesignatedPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_HmAgentStpCstDesignatedPortId_Type.__name__ = "OctetString"
_HmAgentStpCstDesignatedPortId_Object = MibTableColumn
hmAgentStpCstDesignatedPortId = _HmAgentStpCstDesignatedPortId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 9, 1, 11),
    _HmAgentStpCstDesignatedPortId_Type()
)
hmAgentStpCstDesignatedPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpCstDesignatedPortId.setStatus("current")


class _HmAgentStpCstExtPortPathCost_Type(Unsigned32):
    """Custom type hmAgentStpCstExtPortPathCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_HmAgentStpCstExtPortPathCost_Type.__name__ = "Unsigned32"
_HmAgentStpCstExtPortPathCost_Object = MibTableColumn
hmAgentStpCstExtPortPathCost = _HmAgentStpCstExtPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 9, 1, 12),
    _HmAgentStpCstExtPortPathCost_Type()
)
hmAgentStpCstExtPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentStpCstExtPortPathCost.setStatus("current")


class _HmAgentStpCstPortAutoEdge_Type(Integer32):
    """Custom type hmAgentStpCstPortAutoEdge based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HmAgentStpCstPortAutoEdge_Type.__name__ = "Integer32"
_HmAgentStpCstPortAutoEdge_Object = MibTableColumn
hmAgentStpCstPortAutoEdge = _HmAgentStpCstPortAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 9, 1, 13),
    _HmAgentStpCstPortAutoEdge_Type()
)
hmAgentStpCstPortAutoEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentStpCstPortAutoEdge.setStatus("current")


class _HmAgentStpCstPortRole_Type(Integer32):
    """Custom type hmAgentStpCstPortRole based on Integer32"""
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
        *(("alternate", 2),
          ("backup", 4),
          ("designated", 3),
          ("disabled", 6),
          ("master", 5),
          ("root", 1))
    )


_HmAgentStpCstPortRole_Type.__name__ = "Integer32"
_HmAgentStpCstPortRole_Object = MibTableColumn
hmAgentStpCstPortRole = _HmAgentStpCstPortRole_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 9, 1, 14),
    _HmAgentStpCstPortRole_Type()
)
hmAgentStpCstPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpCstPortRole.setStatus("current")


class _HmAgentStpCstPortDisputed_Type(Integer32):
    """Custom type hmAgentStpCstPortDisputed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HmAgentStpCstPortDisputed_Type.__name__ = "Integer32"
_HmAgentStpCstPortDisputed_Object = MibTableColumn
hmAgentStpCstPortDisputed = _HmAgentStpCstPortDisputed_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 9, 1, 15),
    _HmAgentStpCstPortDisputed_Type()
)
hmAgentStpCstPortDisputed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpCstPortDisputed.setStatus("current")


class _HmAgentStpCstPortBpduGuardEffect_Type(Integer32):
    """Custom type hmAgentStpCstPortBpduGuardEffect based on Integer32"""
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


_HmAgentStpCstPortBpduGuardEffect_Type.__name__ = "Integer32"
_HmAgentStpCstPortBpduGuardEffect_Object = MibTableColumn
hmAgentStpCstPortBpduGuardEffect = _HmAgentStpCstPortBpduGuardEffect_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 9, 1, 16),
    _HmAgentStpCstPortBpduGuardEffect_Type()
)
hmAgentStpCstPortBpduGuardEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpCstPortBpduGuardEffect.setStatus("current")


class _HmAgentStpCstPortBpduFilter_Type(Integer32):
    """Custom type hmAgentStpCstPortBpduFilter based on Integer32"""
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


_HmAgentStpCstPortBpduFilter_Type.__name__ = "Integer32"
_HmAgentStpCstPortBpduFilter_Object = MibTableColumn
hmAgentStpCstPortBpduFilter = _HmAgentStpCstPortBpduFilter_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 9, 1, 17),
    _HmAgentStpCstPortBpduFilter_Type()
)
hmAgentStpCstPortBpduFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentStpCstPortBpduFilter.setStatus("current")


class _HmAgentStpCstPortBpduFlood_Type(Integer32):
    """Custom type hmAgentStpCstPortBpduFlood based on Integer32"""
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


_HmAgentStpCstPortBpduFlood_Type.__name__ = "Integer32"
_HmAgentStpCstPortBpduFlood_Object = MibTableColumn
hmAgentStpCstPortBpduFlood = _HmAgentStpCstPortBpduFlood_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 9, 1, 18),
    _HmAgentStpCstPortBpduFlood_Type()
)
hmAgentStpCstPortBpduFlood.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentStpCstPortBpduFlood.setStatus("current")


class _HmAgentStpCstPortRootGuard_Type(Integer32):
    """Custom type hmAgentStpCstPortRootGuard based on Integer32"""
    defaultValue = 2

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


_HmAgentStpCstPortRootGuard_Type.__name__ = "Integer32"
_HmAgentStpCstPortRootGuard_Object = MibTableColumn
hmAgentStpCstPortRootGuard = _HmAgentStpCstPortRootGuard_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 9, 1, 19),
    _HmAgentStpCstPortRootGuard_Type()
)
hmAgentStpCstPortRootGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentStpCstPortRootGuard.setStatus("current")


class _HmAgentStpCstPortTCNGuard_Type(Integer32):
    """Custom type hmAgentStpCstPortTCNGuard based on Integer32"""
    defaultValue = 2

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


_HmAgentStpCstPortTCNGuard_Type.__name__ = "Integer32"
_HmAgentStpCstPortTCNGuard_Object = MibTableColumn
hmAgentStpCstPortTCNGuard = _HmAgentStpCstPortTCNGuard_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 9, 1, 20),
    _HmAgentStpCstPortTCNGuard_Type()
)
hmAgentStpCstPortTCNGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentStpCstPortTCNGuard.setStatus("current")


class _HmAgentStpCstPortLoopGuard_Type(Integer32):
    """Custom type hmAgentStpCstPortLoopGuard based on Integer32"""
    defaultValue = 2

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


_HmAgentStpCstPortLoopGuard_Type.__name__ = "Integer32"
_HmAgentStpCstPortLoopGuard_Object = MibTableColumn
hmAgentStpCstPortLoopGuard = _HmAgentStpCstPortLoopGuard_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 9, 1, 21),
    _HmAgentStpCstPortLoopGuard_Type()
)
hmAgentStpCstPortLoopGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentStpCstPortLoopGuard.setStatus("current")
_HmAgentStpMstTable_Object = MibTable
hmAgentStpMstTable = _HmAgentStpMstTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 10)
)
if mibBuilder.loadTexts:
    hmAgentStpMstTable.setStatus("current")
_HmAgentStpMstEntry_Object = MibTableRow
hmAgentStpMstEntry = _HmAgentStpMstEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 10, 1)
)
hmAgentStpMstEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-BASICL2-MIB", "hmAgentStpMstId"),
)
if mibBuilder.loadTexts:
    hmAgentStpMstEntry.setStatus("current")
_HmAgentStpMstId_Type = Unsigned32
_HmAgentStpMstId_Object = MibTableColumn
hmAgentStpMstId = _HmAgentStpMstId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 10, 1, 1),
    _HmAgentStpMstId_Type()
)
hmAgentStpMstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpMstId.setStatus("current")


class _HmAgentStpMstBridgePriority_Type(Unsigned32):
    """Custom type hmAgentStpMstBridgePriority based on Unsigned32"""
    defaultValue = 32768

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_HmAgentStpMstBridgePriority_Type.__name__ = "Unsigned32"
_HmAgentStpMstBridgePriority_Object = MibTableColumn
hmAgentStpMstBridgePriority = _HmAgentStpMstBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 10, 1, 2),
    _HmAgentStpMstBridgePriority_Type()
)
hmAgentStpMstBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentStpMstBridgePriority.setStatus("current")


class _HmAgentStpMstBridgeIdentifier_Type(OctetString):
    """Custom type hmAgentStpMstBridgeIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HmAgentStpMstBridgeIdentifier_Type.__name__ = "OctetString"
_HmAgentStpMstBridgeIdentifier_Object = MibTableColumn
hmAgentStpMstBridgeIdentifier = _HmAgentStpMstBridgeIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 10, 1, 3),
    _HmAgentStpMstBridgeIdentifier_Type()
)
hmAgentStpMstBridgeIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpMstBridgeIdentifier.setStatus("current")


class _HmAgentStpMstDesignatedRootId_Type(OctetString):
    """Custom type hmAgentStpMstDesignatedRootId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HmAgentStpMstDesignatedRootId_Type.__name__ = "OctetString"
_HmAgentStpMstDesignatedRootId_Object = MibTableColumn
hmAgentStpMstDesignatedRootId = _HmAgentStpMstDesignatedRootId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 10, 1, 4),
    _HmAgentStpMstDesignatedRootId_Type()
)
hmAgentStpMstDesignatedRootId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpMstDesignatedRootId.setStatus("current")
_HmAgentStpMstRootPathCost_Type = Unsigned32
_HmAgentStpMstRootPathCost_Object = MibTableColumn
hmAgentStpMstRootPathCost = _HmAgentStpMstRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 10, 1, 5),
    _HmAgentStpMstRootPathCost_Type()
)
hmAgentStpMstRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpMstRootPathCost.setStatus("current")
_HmAgentStpMstRootPortId_Type = OctetString
_HmAgentStpMstRootPortId_Object = MibTableColumn
hmAgentStpMstRootPortId = _HmAgentStpMstRootPortId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 10, 1, 6),
    _HmAgentStpMstRootPortId_Type()
)
hmAgentStpMstRootPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpMstRootPortId.setStatus("current")
_HmAgentStpMstTimeSinceTopologyChange_Type = TimeTicks
_HmAgentStpMstTimeSinceTopologyChange_Object = MibTableColumn
hmAgentStpMstTimeSinceTopologyChange = _HmAgentStpMstTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 10, 1, 7),
    _HmAgentStpMstTimeSinceTopologyChange_Type()
)
hmAgentStpMstTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpMstTimeSinceTopologyChange.setStatus("current")
_HmAgentStpMstTopologyChangeCount_Type = Counter32
_HmAgentStpMstTopologyChangeCount_Object = MibTableColumn
hmAgentStpMstTopologyChangeCount = _HmAgentStpMstTopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 10, 1, 8),
    _HmAgentStpMstTopologyChangeCount_Type()
)
hmAgentStpMstTopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpMstTopologyChangeCount.setStatus("current")


class _HmAgentStpMstTopologyChangeParm_Type(Integer32):
    """Custom type hmAgentStpMstTopologyChangeParm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HmAgentStpMstTopologyChangeParm_Type.__name__ = "Integer32"
_HmAgentStpMstTopologyChangeParm_Object = MibTableColumn
hmAgentStpMstTopologyChangeParm = _HmAgentStpMstTopologyChangeParm_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 10, 1, 9),
    _HmAgentStpMstTopologyChangeParm_Type()
)
hmAgentStpMstTopologyChangeParm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpMstTopologyChangeParm.setStatus("current")
_HmAgentStpMstRowStatus_Type = RowStatus
_HmAgentStpMstRowStatus_Object = MibTableColumn
hmAgentStpMstRowStatus = _HmAgentStpMstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 10, 1, 10),
    _HmAgentStpMstRowStatus_Type()
)
hmAgentStpMstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmAgentStpMstRowStatus.setStatus("current")
_HmAgentStpMstPortTable_Object = MibTable
hmAgentStpMstPortTable = _HmAgentStpMstPortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 11)
)
if mibBuilder.loadTexts:
    hmAgentStpMstPortTable.setStatus("current")
_HmAgentStpMstPortEntry_Object = MibTableRow
hmAgentStpMstPortEntry = _HmAgentStpMstPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 11, 1)
)
hmAgentStpMstPortEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-BASICL2-MIB", "hmAgentStpMstId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hmAgentStpMstPortEntry.setStatus("current")


class _HmAgentStpMstPortForwardingState_Type(Integer32):
    """Custom type hmAgentStpMstPortForwardingState based on Integer32"""
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
        *(("disabled", 4),
          ("discarding", 1),
          ("forwarding", 3),
          ("learning", 2),
          ("manualFwd", 5),
          ("notParticipate", 6))
    )


_HmAgentStpMstPortForwardingState_Type.__name__ = "Integer32"
_HmAgentStpMstPortForwardingState_Object = MibTableColumn
hmAgentStpMstPortForwardingState = _HmAgentStpMstPortForwardingState_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 11, 1, 1),
    _HmAgentStpMstPortForwardingState_Type()
)
hmAgentStpMstPortForwardingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpMstPortForwardingState.setStatus("current")
_HmAgentStpMstPortId_Type = OctetString
_HmAgentStpMstPortId_Object = MibTableColumn
hmAgentStpMstPortId = _HmAgentStpMstPortId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 11, 1, 2),
    _HmAgentStpMstPortId_Type()
)
hmAgentStpMstPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpMstPortId.setStatus("current")


class _HmAgentStpMstPortPathCost_Type(Unsigned32):
    """Custom type hmAgentStpMstPortPathCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_HmAgentStpMstPortPathCost_Type.__name__ = "Unsigned32"
_HmAgentStpMstPortPathCost_Object = MibTableColumn
hmAgentStpMstPortPathCost = _HmAgentStpMstPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 11, 1, 3),
    _HmAgentStpMstPortPathCost_Type()
)
hmAgentStpMstPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentStpMstPortPathCost.setStatus("current")


class _HmAgentStpMstPortPriority_Type(Unsigned32):
    """Custom type hmAgentStpMstPortPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_HmAgentStpMstPortPriority_Type.__name__ = "Unsigned32"
_HmAgentStpMstPortPriority_Object = MibTableColumn
hmAgentStpMstPortPriority = _HmAgentStpMstPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 11, 1, 4),
    _HmAgentStpMstPortPriority_Type()
)
hmAgentStpMstPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentStpMstPortPriority.setStatus("current")


class _HmAgentStpMstDesignatedBridgeId_Type(OctetString):
    """Custom type hmAgentStpMstDesignatedBridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HmAgentStpMstDesignatedBridgeId_Type.__name__ = "OctetString"
_HmAgentStpMstDesignatedBridgeId_Object = MibTableColumn
hmAgentStpMstDesignatedBridgeId = _HmAgentStpMstDesignatedBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 11, 1, 5),
    _HmAgentStpMstDesignatedBridgeId_Type()
)
hmAgentStpMstDesignatedBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpMstDesignatedBridgeId.setStatus("current")
_HmAgentStpMstDesignatedCost_Type = Unsigned32
_HmAgentStpMstDesignatedCost_Object = MibTableColumn
hmAgentStpMstDesignatedCost = _HmAgentStpMstDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 11, 1, 6),
    _HmAgentStpMstDesignatedCost_Type()
)
hmAgentStpMstDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpMstDesignatedCost.setStatus("current")


class _HmAgentStpMstDesignatedPortId_Type(OctetString):
    """Custom type hmAgentStpMstDesignatedPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_HmAgentStpMstDesignatedPortId_Type.__name__ = "OctetString"
_HmAgentStpMstDesignatedPortId_Object = MibTableColumn
hmAgentStpMstDesignatedPortId = _HmAgentStpMstDesignatedPortId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 11, 1, 7),
    _HmAgentStpMstDesignatedPortId_Type()
)
hmAgentStpMstDesignatedPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpMstDesignatedPortId.setStatus("current")


class _HmAgentStpMstPortRole_Type(Integer32):
    """Custom type hmAgentStpMstPortRole based on Integer32"""
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
        *(("alternate", 2),
          ("backup", 4),
          ("designated", 3),
          ("disabled", 6),
          ("master", 5),
          ("root", 1))
    )


_HmAgentStpMstPortRole_Type.__name__ = "Integer32"
_HmAgentStpMstPortRole_Object = MibTableColumn
hmAgentStpMstPortRole = _HmAgentStpMstPortRole_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 11, 1, 8),
    _HmAgentStpMstPortRole_Type()
)
hmAgentStpMstPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpMstPortRole.setStatus("current")


class _HmAgentStpMstPortDisputed_Type(Integer32):
    """Custom type hmAgentStpMstPortDisputed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HmAgentStpMstPortDisputed_Type.__name__ = "Integer32"
_HmAgentStpMstPortDisputed_Object = MibTableColumn
hmAgentStpMstPortDisputed = _HmAgentStpMstPortDisputed_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 11, 1, 9),
    _HmAgentStpMstPortDisputed_Type()
)
hmAgentStpMstPortDisputed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpMstPortDisputed.setStatus("current")


class _HmAgentStpMstPortLoopInconsistentState_Type(Integer32):
    """Custom type hmAgentStpMstPortLoopInconsistentState based on Integer32"""
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


_HmAgentStpMstPortLoopInconsistentState_Type.__name__ = "Integer32"
_HmAgentStpMstPortLoopInconsistentState_Object = MibTableColumn
hmAgentStpMstPortLoopInconsistentState = _HmAgentStpMstPortLoopInconsistentState_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 11, 1, 10),
    _HmAgentStpMstPortLoopInconsistentState_Type()
)
hmAgentStpMstPortLoopInconsistentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpMstPortLoopInconsistentState.setStatus("current")
_HmAgentStpMstPortTransitionsIntoLoopInconsistentState_Type = Counter32
_HmAgentStpMstPortTransitionsIntoLoopInconsistentState_Object = MibTableColumn
hmAgentStpMstPortTransitionsIntoLoopInconsistentState = _HmAgentStpMstPortTransitionsIntoLoopInconsistentState_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 11, 1, 11),
    _HmAgentStpMstPortTransitionsIntoLoopInconsistentState_Type()
)
hmAgentStpMstPortTransitionsIntoLoopInconsistentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpMstPortTransitionsIntoLoopInconsistentState.setStatus("current")
_HmAgentStpMstPortTransitionsOutOfLoopInconsistentState_Type = Counter32
_HmAgentStpMstPortTransitionsOutOfLoopInconsistentState_Object = MibTableColumn
hmAgentStpMstPortTransitionsOutOfLoopInconsistentState = _HmAgentStpMstPortTransitionsOutOfLoopInconsistentState_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 11, 1, 12),
    _HmAgentStpMstPortTransitionsOutOfLoopInconsistentState_Type()
)
hmAgentStpMstPortTransitionsOutOfLoopInconsistentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpMstPortTransitionsOutOfLoopInconsistentState.setStatus("current")


class _HmAgentStpMstReceivedBridgeId_Type(OctetString):
    """Custom type hmAgentStpMstReceivedBridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HmAgentStpMstReceivedBridgeId_Type.__name__ = "OctetString"
_HmAgentStpMstReceivedBridgeId_Object = MibTableColumn
hmAgentStpMstReceivedBridgeId = _HmAgentStpMstReceivedBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 11, 1, 13),
    _HmAgentStpMstReceivedBridgeId_Type()
)
hmAgentStpMstReceivedBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpMstReceivedBridgeId.setStatus("current")
_HmAgentStpMstReceivedRPC_Type = Unsigned32
_HmAgentStpMstReceivedRPC_Object = MibTableColumn
hmAgentStpMstReceivedRPC = _HmAgentStpMstReceivedRPC_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 11, 1, 14),
    _HmAgentStpMstReceivedRPC_Type()
)
hmAgentStpMstReceivedRPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpMstReceivedRPC.setStatus("current")


class _HmAgentStpMstReceivedPortId_Type(OctetString):
    """Custom type hmAgentStpMstReceivedPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_HmAgentStpMstReceivedPortId_Type.__name__ = "OctetString"
_HmAgentStpMstReceivedPortId_Object = MibTableColumn
hmAgentStpMstReceivedPortId = _HmAgentStpMstReceivedPortId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 11, 1, 15),
    _HmAgentStpMstReceivedPortId_Type()
)
hmAgentStpMstReceivedPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentStpMstReceivedPortId.setStatus("current")
_HmAgentStpMstVlanTable_Object = MibTable
hmAgentStpMstVlanTable = _HmAgentStpMstVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 12)
)
if mibBuilder.loadTexts:
    hmAgentStpMstVlanTable.setStatus("current")
_HmAgentStpMstVlanEntry_Object = MibTableRow
hmAgentStpMstVlanEntry = _HmAgentStpMstVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 12, 1)
)
hmAgentStpMstVlanEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-BASICL2-MIB", "hmAgentStpMstId"),
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    hmAgentStpMstVlanEntry.setStatus("current")
_HmAgentStpMstVlanRowStatus_Type = RowStatus
_HmAgentStpMstVlanRowStatus_Object = MibTableColumn
hmAgentStpMstVlanRowStatus = _HmAgentStpMstVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 12, 1, 1),
    _HmAgentStpMstVlanRowStatus_Type()
)
hmAgentStpMstVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmAgentStpMstVlanRowStatus.setStatus("current")


class _HmAgentStpBpduGuardMode_Type(Integer32):
    """Custom type hmAgentStpBpduGuardMode based on Integer32"""
    defaultValue = 2

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


_HmAgentStpBpduGuardMode_Type.__name__ = "Integer32"
_HmAgentStpBpduGuardMode_Object = MibScalar
hmAgentStpBpduGuardMode = _HmAgentStpBpduGuardMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 13),
    _HmAgentStpBpduGuardMode_Type()
)
hmAgentStpBpduGuardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentStpBpduGuardMode.setStatus("current")


class _HmAgentStpBpduFilterDefault_Type(Integer32):
    """Custom type hmAgentStpBpduFilterDefault based on Integer32"""
    defaultValue = 2

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


_HmAgentStpBpduFilterDefault_Type.__name__ = "Integer32"
_HmAgentStpBpduFilterDefault_Object = MibScalar
hmAgentStpBpduFilterDefault = _HmAgentStpBpduFilterDefault_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 15, 14),
    _HmAgentStpBpduFilterDefault_Type()
)
hmAgentStpBpduFilterDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentStpBpduFilterDefault.setStatus("current")
_HmAgentClassOfServiceGroup_ObjectIdentity = ObjectIdentity
hmAgentClassOfServiceGroup = _HmAgentClassOfServiceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 17)
)
_HmAgentClassOfServicePortTable_Object = MibTable
hmAgentClassOfServicePortTable = _HmAgentClassOfServicePortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 17, 1)
)
if mibBuilder.loadTexts:
    hmAgentClassOfServicePortTable.setStatus("current")
_HmAgentClassOfServicePortEntry_Object = MibTableRow
hmAgentClassOfServicePortEntry = _HmAgentClassOfServicePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 17, 1, 1)
)
hmAgentClassOfServicePortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HIRSCHMANN-MMP4-BASICL2-MIB", "hmAgentClassOfServicePortPriority"),
)
if mibBuilder.loadTexts:
    hmAgentClassOfServicePortEntry.setStatus("current")


class _HmAgentClassOfServicePortPriority_Type(Integer32):
    """Custom type hmAgentClassOfServicePortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HmAgentClassOfServicePortPriority_Type.__name__ = "Integer32"
_HmAgentClassOfServicePortPriority_Object = MibTableColumn
hmAgentClassOfServicePortPriority = _HmAgentClassOfServicePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 17, 1, 1, 1),
    _HmAgentClassOfServicePortPriority_Type()
)
hmAgentClassOfServicePortPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmAgentClassOfServicePortPriority.setStatus("current")


class _HmAgentClassOfServicePortClass_Type(Integer32):
    """Custom type hmAgentClassOfServicePortClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HmAgentClassOfServicePortClass_Type.__name__ = "Integer32"
_HmAgentClassOfServicePortClass_Object = MibTableColumn
hmAgentClassOfServicePortClass = _HmAgentClassOfServicePortClass_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 2, 17, 1, 1, 2),
    _HmAgentClassOfServicePortClass_Type()
)
hmAgentClassOfServicePortClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentClassOfServicePortClass.setStatus("current")
_HmAgentSystemGroup_ObjectIdentity = ObjectIdentity
hmAgentSystemGroup = _HmAgentSystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 3)
)


class _HmAgentSaveConfig_Type(Integer32):
    """Custom type hmAgentSaveConfig based on Integer32"""
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


_HmAgentSaveConfig_Type.__name__ = "Integer32"
_HmAgentSaveConfig_Object = MibScalar
hmAgentSaveConfig = _HmAgentSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 3, 1),
    _HmAgentSaveConfig_Type()
)
hmAgentSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSaveConfig.setStatus("current")


class _HmAgentClearConfig_Type(Integer32):
    """Custom type hmAgentClearConfig based on Integer32"""
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


_HmAgentClearConfig_Type.__name__ = "Integer32"
_HmAgentClearConfig_Object = MibScalar
hmAgentClearConfig = _HmAgentClearConfig_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 3, 2),
    _HmAgentClearConfig_Type()
)
hmAgentClearConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentClearConfig.setStatus("current")


class _HmAgentClearLags_Type(Integer32):
    """Custom type hmAgentClearLags based on Integer32"""
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


_HmAgentClearLags_Type.__name__ = "Integer32"
_HmAgentClearLags_Object = MibScalar
hmAgentClearLags = _HmAgentClearLags_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 3, 3),
    _HmAgentClearLags_Type()
)
hmAgentClearLags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentClearLags.setStatus("current")


class _HmAgentClearLoginSessions_Type(Integer32):
    """Custom type hmAgentClearLoginSessions based on Integer32"""
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


_HmAgentClearLoginSessions_Type.__name__ = "Integer32"
_HmAgentClearLoginSessions_Object = MibScalar
hmAgentClearLoginSessions = _HmAgentClearLoginSessions_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 3, 4),
    _HmAgentClearLoginSessions_Type()
)
hmAgentClearLoginSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentClearLoginSessions.setStatus("current")


class _HmAgentClearPasswords_Type(Integer32):
    """Custom type hmAgentClearPasswords based on Integer32"""
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


_HmAgentClearPasswords_Type.__name__ = "Integer32"
_HmAgentClearPasswords_Object = MibScalar
hmAgentClearPasswords = _HmAgentClearPasswords_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 3, 5),
    _HmAgentClearPasswords_Type()
)
hmAgentClearPasswords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentClearPasswords.setStatus("current")


class _HmAgentClearPortStats_Type(Integer32):
    """Custom type hmAgentClearPortStats based on Integer32"""
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


_HmAgentClearPortStats_Type.__name__ = "Integer32"
_HmAgentClearPortStats_Object = MibScalar
hmAgentClearPortStats = _HmAgentClearPortStats_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 3, 6),
    _HmAgentClearPortStats_Type()
)
hmAgentClearPortStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentClearPortStats.setStatus("current")


class _HmAgentClearSwitchStats_Type(Integer32):
    """Custom type hmAgentClearSwitchStats based on Integer32"""
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


_HmAgentClearSwitchStats_Type.__name__ = "Integer32"
_HmAgentClearSwitchStats_Object = MibScalar
hmAgentClearSwitchStats = _HmAgentClearSwitchStats_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 3, 7),
    _HmAgentClearSwitchStats_Type()
)
hmAgentClearSwitchStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentClearSwitchStats.setStatus("current")


class _HmAgentClearTrapLog_Type(Integer32):
    """Custom type hmAgentClearTrapLog based on Integer32"""
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


_HmAgentClearTrapLog_Type.__name__ = "Integer32"
_HmAgentClearTrapLog_Object = MibScalar
hmAgentClearTrapLog = _HmAgentClearTrapLog_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 3, 8),
    _HmAgentClearTrapLog_Type()
)
hmAgentClearTrapLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentClearTrapLog.setStatus("current")


class _HmAgentClearVlan_Type(Integer32):
    """Custom type hmAgentClearVlan based on Integer32"""
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


_HmAgentClearVlan_Type.__name__ = "Integer32"
_HmAgentClearVlan_Object = MibScalar
hmAgentClearVlan = _HmAgentClearVlan_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 3, 9),
    _HmAgentClearVlan_Type()
)
hmAgentClearVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentClearVlan.setStatus("current")


class _HmAgentResetSystem_Type(Integer32):
    """Custom type hmAgentResetSystem based on Integer32"""
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


_HmAgentResetSystem_Type.__name__ = "Integer32"
_HmAgentResetSystem_Object = MibScalar
hmAgentResetSystem = _HmAgentResetSystem_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 3, 10),
    _HmAgentResetSystem_Type()
)
hmAgentResetSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentResetSystem.setStatus("current")


class _HmAgentSaveConfigStatus_Type(Integer32):
    """Custom type hmAgentSaveConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notInitiated", 1),
          ("savingComplete", 3),
          ("savingInProcess", 2))
    )


_HmAgentSaveConfigStatus_Type.__name__ = "Integer32"
_HmAgentSaveConfigStatus_Object = MibScalar
hmAgentSaveConfigStatus = _HmAgentSaveConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 3, 11),
    _HmAgentSaveConfigStatus_Type()
)
hmAgentSaveConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSaveConfigStatus.setStatus("current")
_HmAgentCableTesterGroup_ObjectIdentity = ObjectIdentity
hmAgentCableTesterGroup = _HmAgentCableTesterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 4)
)


class _HmAgentCableTesterStatus_Type(Integer32):
    """Custom type hmAgentCableTesterStatus based on Integer32"""
    defaultValue = 4

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
        *(("active", 1),
          ("failure", 3),
          ("success", 2),
          ("uninitialized", 4))
    )


_HmAgentCableTesterStatus_Type.__name__ = "Integer32"
_HmAgentCableTesterStatus_Object = MibScalar
hmAgentCableTesterStatus = _HmAgentCableTesterStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 4, 1),
    _HmAgentCableTesterStatus_Type()
)
hmAgentCableTesterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentCableTesterStatus.setStatus("current")


class _HmAgentCableTesterIfIndex_Type(Unsigned32):
    """Custom type hmAgentCableTesterIfIndex based on Unsigned32"""
    defaultValue = 0


_HmAgentCableTesterIfIndex_Object = MibScalar
hmAgentCableTesterIfIndex = _HmAgentCableTesterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 4, 2),
    _HmAgentCableTesterIfIndex_Type()
)
hmAgentCableTesterIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentCableTesterIfIndex.setStatus("current")


class _HmAgentCableTesterCableStatus_Type(Integer32):
    """Custom type hmAgentCableTesterCableStatus based on Integer32"""
    defaultValue = 4

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
        *(("normal", 1),
          ("open", 2),
          ("short", 3),
          ("unknown", 4))
    )


_HmAgentCableTesterCableStatus_Type.__name__ = "Integer32"
_HmAgentCableTesterCableStatus_Object = MibScalar
hmAgentCableTesterCableStatus = _HmAgentCableTesterCableStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 4, 3),
    _HmAgentCableTesterCableStatus_Type()
)
hmAgentCableTesterCableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentCableTesterCableStatus.setStatus("current")


class _HmAgentCableTesterMinimumCableLength_Type(Unsigned32):
    """Custom type hmAgentCableTesterMinimumCableLength based on Unsigned32"""
    defaultValue = 0


_HmAgentCableTesterMinimumCableLength_Object = MibScalar
hmAgentCableTesterMinimumCableLength = _HmAgentCableTesterMinimumCableLength_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 4, 4),
    _HmAgentCableTesterMinimumCableLength_Type()
)
hmAgentCableTesterMinimumCableLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentCableTesterMinimumCableLength.setStatus("current")


class _HmAgentCableTesterMaximumCableLength_Type(Unsigned32):
    """Custom type hmAgentCableTesterMaximumCableLength based on Unsigned32"""
    defaultValue = 0


_HmAgentCableTesterMaximumCableLength_Object = MibScalar
hmAgentCableTesterMaximumCableLength = _HmAgentCableTesterMaximumCableLength_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 4, 5),
    _HmAgentCableTesterMaximumCableLength_Type()
)
hmAgentCableTesterMaximumCableLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentCableTesterMaximumCableLength.setStatus("current")


class _HmAgentCableTesterCableFailureLocation_Type(Unsigned32):
    """Custom type hmAgentCableTesterCableFailureLocation based on Unsigned32"""
    defaultValue = 0


_HmAgentCableTesterCableFailureLocation_Object = MibScalar
hmAgentCableTesterCableFailureLocation = _HmAgentCableTesterCableFailureLocation_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 4, 6),
    _HmAgentCableTesterCableFailureLocation_Type()
)
hmAgentCableTesterCableFailureLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentCableTesterCableFailureLocation.setStatus("current")
_HmPlatform4SwitchingTraps_ObjectIdentity = ObjectIdentity
hmPlatform4SwitchingTraps = _HmPlatform4SwitchingTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 50)
)
_HmRadius_ObjectIdentity = ObjectIdentity
hmRadius = _HmRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 8)
)
_HmAgentRadiusConfigGroup_ObjectIdentity = ObjectIdentity
hmAgentRadiusConfigGroup = _HmAgentRadiusConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 8, 1)
)


class _HmAgentRadiusMaxTransmit_Type(Unsigned32):
    """Custom type hmAgentRadiusMaxTransmit based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HmAgentRadiusMaxTransmit_Type.__name__ = "Unsigned32"
_HmAgentRadiusMaxTransmit_Object = MibScalar
hmAgentRadiusMaxTransmit = _HmAgentRadiusMaxTransmit_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 8, 1, 1),
    _HmAgentRadiusMaxTransmit_Type()
)
hmAgentRadiusMaxTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRadiusMaxTransmit.setStatus("current")


class _HmAgentRadiusTimeout_Type(Unsigned32):
    """Custom type hmAgentRadiusTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_HmAgentRadiusTimeout_Type.__name__ = "Unsigned32"
_HmAgentRadiusTimeout_Object = MibScalar
hmAgentRadiusTimeout = _HmAgentRadiusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 8, 1, 2),
    _HmAgentRadiusTimeout_Type()
)
hmAgentRadiusTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRadiusTimeout.setStatus("current")


class _HmAgentRadiusAccountingMode_Type(Integer32):
    """Custom type hmAgentRadiusAccountingMode based on Integer32"""
    defaultValue = 2

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


_HmAgentRadiusAccountingMode_Type.__name__ = "Integer32"
_HmAgentRadiusAccountingMode_Object = MibScalar
hmAgentRadiusAccountingMode = _HmAgentRadiusAccountingMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 8, 1, 3),
    _HmAgentRadiusAccountingMode_Type()
)
hmAgentRadiusAccountingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRadiusAccountingMode.setStatus("current")


class _HmAgentRadiusStatsClear_Type(Integer32):
    """Custom type hmAgentRadiusStatsClear based on Integer32"""
    defaultValue = 2

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


_HmAgentRadiusStatsClear_Type.__name__ = "Integer32"
_HmAgentRadiusStatsClear_Object = MibScalar
hmAgentRadiusStatsClear = _HmAgentRadiusStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 8, 1, 4),
    _HmAgentRadiusStatsClear_Type()
)
hmAgentRadiusStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRadiusStatsClear.setStatus("current")


class _HmAgentRadiusAccountingIndexNextValid_Type(Integer32):
    """Custom type hmAgentRadiusAccountingIndexNextValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_HmAgentRadiusAccountingIndexNextValid_Type.__name__ = "Integer32"
_HmAgentRadiusAccountingIndexNextValid_Object = MibScalar
hmAgentRadiusAccountingIndexNextValid = _HmAgentRadiusAccountingIndexNextValid_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 8, 1, 5),
    _HmAgentRadiusAccountingIndexNextValid_Type()
)
hmAgentRadiusAccountingIndexNextValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentRadiusAccountingIndexNextValid.setStatus("current")
_HmAgentRadiusAccountingConfigTable_Object = MibTable
hmAgentRadiusAccountingConfigTable = _HmAgentRadiusAccountingConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 8, 1, 6)
)
if mibBuilder.loadTexts:
    hmAgentRadiusAccountingConfigTable.setStatus("current")
_HmAgentRadiusAccountingConfigEntry_Object = MibTableRow
hmAgentRadiusAccountingConfigEntry = _HmAgentRadiusAccountingConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 8, 1, 6, 1)
)
hmAgentRadiusAccountingConfigEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-BASICL2-MIB", "hmAgentRadiusAccountingServerIndex"),
)
if mibBuilder.loadTexts:
    hmAgentRadiusAccountingConfigEntry.setStatus("current")


class _HmAgentRadiusAccountingServerIndex_Type(Integer32):
    """Custom type hmAgentRadiusAccountingServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HmAgentRadiusAccountingServerIndex_Type.__name__ = "Integer32"
_HmAgentRadiusAccountingServerIndex_Object = MibTableColumn
hmAgentRadiusAccountingServerIndex = _HmAgentRadiusAccountingServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 8, 1, 6, 1, 1),
    _HmAgentRadiusAccountingServerIndex_Type()
)
hmAgentRadiusAccountingServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmAgentRadiusAccountingServerIndex.setStatus("current")
_HmAgentRadiusAccountingServerAddress_Type = IpAddress
_HmAgentRadiusAccountingServerAddress_Object = MibTableColumn
hmAgentRadiusAccountingServerAddress = _HmAgentRadiusAccountingServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 8, 1, 6, 1, 2),
    _HmAgentRadiusAccountingServerAddress_Type()
)
hmAgentRadiusAccountingServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmAgentRadiusAccountingServerAddress.setStatus("current")


class _HmAgentRadiusAccountingPort_Type(Unsigned32):
    """Custom type hmAgentRadiusAccountingPort based on Unsigned32"""
    defaultValue = 1813

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HmAgentRadiusAccountingPort_Type.__name__ = "Unsigned32"
_HmAgentRadiusAccountingPort_Object = MibTableColumn
hmAgentRadiusAccountingPort = _HmAgentRadiusAccountingPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 8, 1, 6, 1, 3),
    _HmAgentRadiusAccountingPort_Type()
)
hmAgentRadiusAccountingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRadiusAccountingPort.setStatus("current")


class _HmAgentRadiusAccountingSecret_Type(DisplayString):
    """Custom type hmAgentRadiusAccountingSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_HmAgentRadiusAccountingSecret_Type.__name__ = "DisplayString"
_HmAgentRadiusAccountingSecret_Object = MibTableColumn
hmAgentRadiusAccountingSecret = _HmAgentRadiusAccountingSecret_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 8, 1, 6, 1, 4),
    _HmAgentRadiusAccountingSecret_Type()
)
hmAgentRadiusAccountingSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRadiusAccountingSecret.setStatus("current")
_HmAgentRadiusAccountingStatus_Type = RowStatus
_HmAgentRadiusAccountingStatus_Object = MibTableColumn
hmAgentRadiusAccountingStatus = _HmAgentRadiusAccountingStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 8, 1, 6, 1, 5),
    _HmAgentRadiusAccountingStatus_Type()
)
hmAgentRadiusAccountingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmAgentRadiusAccountingStatus.setStatus("current")


class _HmAgentRadiusServerIndexNextValid_Type(Integer32):
    """Custom type hmAgentRadiusServerIndexNextValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_HmAgentRadiusServerIndexNextValid_Type.__name__ = "Integer32"
_HmAgentRadiusServerIndexNextValid_Object = MibScalar
hmAgentRadiusServerIndexNextValid = _HmAgentRadiusServerIndexNextValid_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 8, 1, 7),
    _HmAgentRadiusServerIndexNextValid_Type()
)
hmAgentRadiusServerIndexNextValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentRadiusServerIndexNextValid.setStatus("current")
_HmAgentRadiusServerConfigTable_Object = MibTable
hmAgentRadiusServerConfigTable = _HmAgentRadiusServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 8, 1, 8)
)
if mibBuilder.loadTexts:
    hmAgentRadiusServerConfigTable.setStatus("current")
_HmAgentRadiusServerConfigEntry_Object = MibTableRow
hmAgentRadiusServerConfigEntry = _HmAgentRadiusServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 8, 1, 8, 1)
)
hmAgentRadiusServerConfigEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-BASICL2-MIB", "hmAgentRadiusServerIndex"),
)
if mibBuilder.loadTexts:
    hmAgentRadiusServerConfigEntry.setStatus("current")


class _HmAgentRadiusServerIndex_Type(Integer32):
    """Custom type hmAgentRadiusServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HmAgentRadiusServerIndex_Type.__name__ = "Integer32"
_HmAgentRadiusServerIndex_Object = MibTableColumn
hmAgentRadiusServerIndex = _HmAgentRadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 8, 1, 8, 1, 1),
    _HmAgentRadiusServerIndex_Type()
)
hmAgentRadiusServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmAgentRadiusServerIndex.setStatus("current")
_HmAgentRadiusServerAddress_Type = IpAddress
_HmAgentRadiusServerAddress_Object = MibTableColumn
hmAgentRadiusServerAddress = _HmAgentRadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 8, 1, 8, 1, 2),
    _HmAgentRadiusServerAddress_Type()
)
hmAgentRadiusServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmAgentRadiusServerAddress.setStatus("current")


class _HmAgentRadiusServerPort_Type(Unsigned32):
    """Custom type hmAgentRadiusServerPort based on Unsigned32"""
    defaultValue = 1812

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HmAgentRadiusServerPort_Type.__name__ = "Unsigned32"
_HmAgentRadiusServerPort_Object = MibTableColumn
hmAgentRadiusServerPort = _HmAgentRadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 8, 1, 8, 1, 3),
    _HmAgentRadiusServerPort_Type()
)
hmAgentRadiusServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRadiusServerPort.setStatus("current")


class _HmAgentRadiusServerSecret_Type(DisplayString):
    """Custom type hmAgentRadiusServerSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_HmAgentRadiusServerSecret_Type.__name__ = "DisplayString"
_HmAgentRadiusServerSecret_Object = MibTableColumn
hmAgentRadiusServerSecret = _HmAgentRadiusServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 8, 1, 8, 1, 4),
    _HmAgentRadiusServerSecret_Type()
)
hmAgentRadiusServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRadiusServerSecret.setStatus("current")


class _HmAgentRadiusServerPrimaryMode_Type(Integer32):
    """Custom type hmAgentRadiusServerPrimaryMode based on Integer32"""
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


_HmAgentRadiusServerPrimaryMode_Type.__name__ = "Integer32"
_HmAgentRadiusServerPrimaryMode_Object = MibTableColumn
hmAgentRadiusServerPrimaryMode = _HmAgentRadiusServerPrimaryMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 8, 1, 8, 1, 5),
    _HmAgentRadiusServerPrimaryMode_Type()
)
hmAgentRadiusServerPrimaryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRadiusServerPrimaryMode.setStatus("current")


class _HmAgentRadiusServerCurrentMode_Type(Integer32):
    """Custom type hmAgentRadiusServerCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_HmAgentRadiusServerCurrentMode_Type.__name__ = "Integer32"
_HmAgentRadiusServerCurrentMode_Object = MibTableColumn
hmAgentRadiusServerCurrentMode = _HmAgentRadiusServerCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 8, 1, 8, 1, 6),
    _HmAgentRadiusServerCurrentMode_Type()
)
hmAgentRadiusServerCurrentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentRadiusServerCurrentMode.setStatus("current")


class _HmAgentRadiusServerMsgAuth_Type(Integer32):
    """Custom type hmAgentRadiusServerMsgAuth based on Integer32"""
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


_HmAgentRadiusServerMsgAuth_Type.__name__ = "Integer32"
_HmAgentRadiusServerMsgAuth_Object = MibTableColumn
hmAgentRadiusServerMsgAuth = _HmAgentRadiusServerMsgAuth_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 8, 1, 8, 1, 7),
    _HmAgentRadiusServerMsgAuth_Type()
)
hmAgentRadiusServerMsgAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRadiusServerMsgAuth.setStatus("current")
_HmAgentRadiusServerStatus_Type = RowStatus
_HmAgentRadiusServerStatus_Object = MibTableColumn
hmAgentRadiusServerStatus = _HmAgentRadiusServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 8, 1, 8, 1, 8),
    _HmAgentRadiusServerStatus_Type()
)
hmAgentRadiusServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmAgentRadiusServerStatus.setStatus("current")
_HmAgentMgmtSecurity_ObjectIdentity = ObjectIdentity
hmAgentMgmtSecurity = _HmAgentMgmtSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 11)
)
_HmAgentSSHConfigGroup_ObjectIdentity = ObjectIdentity
hmAgentSSHConfigGroup = _HmAgentSSHConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 11, 2)
)


class _HmAgentSSHAdminMode_Type(Integer32):
    """Custom type hmAgentSSHAdminMode based on Integer32"""
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


_HmAgentSSHAdminMode_Type.__name__ = "Integer32"
_HmAgentSSHAdminMode_Object = MibScalar
hmAgentSSHAdminMode = _HmAgentSSHAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 11, 2, 1),
    _HmAgentSSHAdminMode_Type()
)
hmAgentSSHAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSSHAdminMode.setStatus("current")


class _HmAgentSSHProtocolLevel_Type(Integer32):
    """Custom type hmAgentSSHProtocolLevel based on Integer32"""
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
          ("ssh10", 1),
          ("ssh20", 2))
    )


_HmAgentSSHProtocolLevel_Type.__name__ = "Integer32"
_HmAgentSSHProtocolLevel_Object = MibScalar
hmAgentSSHProtocolLevel = _HmAgentSSHProtocolLevel_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 11, 2, 2),
    _HmAgentSSHProtocolLevel_Type()
)
hmAgentSSHProtocolLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSSHProtocolLevel.setStatus("current")
_HmAgentSSHSessionsCount_Type = Integer32
_HmAgentSSHSessionsCount_Object = MibScalar
hmAgentSSHSessionsCount = _HmAgentSSHSessionsCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 11, 2, 3),
    _HmAgentSSHSessionsCount_Type()
)
hmAgentSSHSessionsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSSHSessionsCount.setStatus("current")


class _HmAgentSSHMaxSessionsCount_Type(Integer32):
    """Custom type hmAgentSSHMaxSessionsCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_HmAgentSSHMaxSessionsCount_Type.__name__ = "Integer32"
_HmAgentSSHMaxSessionsCount_Object = MibScalar
hmAgentSSHMaxSessionsCount = _HmAgentSSHMaxSessionsCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 11, 2, 4),
    _HmAgentSSHMaxSessionsCount_Type()
)
hmAgentSSHMaxSessionsCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSSHMaxSessionsCount.setStatus("current")


class _HmAgentSSHSessionTimeout_Type(Integer32):
    """Custom type hmAgentSSHSessionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 160),
    )


_HmAgentSSHSessionTimeout_Type.__name__ = "Integer32"
_HmAgentSSHSessionTimeout_Object = MibScalar
hmAgentSSHSessionTimeout = _HmAgentSSHSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 11, 2, 5),
    _HmAgentSSHSessionTimeout_Type()
)
hmAgentSSHSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSSHSessionTimeout.setStatus("current")
_HmAgentLogging_ObjectIdentity = ObjectIdentity
hmAgentLogging = _HmAgentLogging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 14)
)
_HmAgentLogConfigGroup_ObjectIdentity = ObjectIdentity
hmAgentLogConfigGroup = _HmAgentLogConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 14, 1)
)
_HmAgentLogSysLogConfigGroup_ObjectIdentity = ObjectIdentity
hmAgentLogSysLogConfigGroup = _HmAgentLogSysLogConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 14, 1, 4)
)


class _HmAgentLogSyslogAdminStatus_Type(Integer32):
    """Custom type hmAgentLogSyslogAdminStatus based on Integer32"""
    defaultValue = 2

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


_HmAgentLogSyslogAdminStatus_Type.__name__ = "Integer32"
_HmAgentLogSyslogAdminStatus_Object = MibScalar
hmAgentLogSyslogAdminStatus = _HmAgentLogSyslogAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 14, 1, 4, 1),
    _HmAgentLogSyslogAdminStatus_Type()
)
hmAgentLogSyslogAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentLogSyslogAdminStatus.setStatus("current")
_HmAgentLogSyslogHostTable_Object = MibTable
hmAgentLogSyslogHostTable = _HmAgentLogSyslogHostTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 14, 1, 4, 5)
)
if mibBuilder.loadTexts:
    hmAgentLogSyslogHostTable.setStatus("current")
_HmAgentLogSyslogHostEntry_Object = MibTableRow
hmAgentLogSyslogHostEntry = _HmAgentLogSyslogHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 14, 1, 4, 5, 1)
)
hmAgentLogSyslogHostEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-BASICL2-MIB", "hmAgentLogHostTableIndex"),
)
if mibBuilder.loadTexts:
    hmAgentLogSyslogHostEntry.setStatus("current")
_HmAgentLogHostTableIndex_Type = Unsigned32
_HmAgentLogHostTableIndex_Object = MibTableColumn
hmAgentLogHostTableIndex = _HmAgentLogHostTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 14, 1, 4, 5, 1, 1),
    _HmAgentLogHostTableIndex_Type()
)
hmAgentLogHostTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmAgentLogHostTableIndex.setStatus("current")


class _HmAgentLogHostTableIpAddress_Type(IpAddress):
    """Custom type hmAgentLogHostTableIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_HmAgentLogHostTableIpAddress_Object = MibTableColumn
hmAgentLogHostTableIpAddress = _HmAgentLogHostTableIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 14, 1, 4, 5, 1, 3),
    _HmAgentLogHostTableIpAddress_Type()
)
hmAgentLogHostTableIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmAgentLogHostTableIpAddress.setStatus("current")


class _HmAgentLogHostTablePort_Type(Unsigned32):
    """Custom type hmAgentLogHostTablePort based on Unsigned32"""
    defaultValue = 514

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HmAgentLogHostTablePort_Type.__name__ = "Unsigned32"
_HmAgentLogHostTablePort_Object = MibTableColumn
hmAgentLogHostTablePort = _HmAgentLogHostTablePort_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 14, 1, 4, 5, 1, 4),
    _HmAgentLogHostTablePort_Type()
)
hmAgentLogHostTablePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmAgentLogHostTablePort.setStatus("current")


class _HmAgentLogHostTableSeverityFilter_Type(HmAgentLogSeverity):
    """Custom type hmAgentLogHostTableSeverityFilter based on HmAgentLogSeverity"""


_HmAgentLogHostTableSeverityFilter_Object = MibTableColumn
hmAgentLogHostTableSeverityFilter = _HmAgentLogHostTableSeverityFilter_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 14, 1, 4, 5, 1, 5),
    _HmAgentLogHostTableSeverityFilter_Type()
)
hmAgentLogHostTableSeverityFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmAgentLogHostTableSeverityFilter.setStatus("current")
_HmAgentLogHostTableRowStatus_Type = RowStatus
_HmAgentLogHostTableRowStatus_Object = MibTableColumn
hmAgentLogHostTableRowStatus = _HmAgentLogHostTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 14, 1, 4, 5, 1, 7),
    _HmAgentLogHostTableRowStatus_Type()
)
hmAgentLogHostTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmAgentLogHostTableRowStatus.setStatus("current")
_HmPlatform4OutboundTelnetPrivate_ObjectIdentity = ObjectIdentity
hmPlatform4OutboundTelnetPrivate = _HmPlatform4OutboundTelnetPrivate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 19)
)
_HmAgentOutboundTelnetGroup_ObjectIdentity = ObjectIdentity
hmAgentOutboundTelnetGroup = _HmAgentOutboundTelnetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 19, 1)
)


class _HmAgentOutboundTelnetAdminMode_Type(Integer32):
    """Custom type hmAgentOutboundTelnetAdminMode based on Integer32"""
    defaultValue = 1

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


_HmAgentOutboundTelnetAdminMode_Type.__name__ = "Integer32"
_HmAgentOutboundTelnetAdminMode_Object = MibScalar
hmAgentOutboundTelnetAdminMode = _HmAgentOutboundTelnetAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 19, 1, 1),
    _HmAgentOutboundTelnetAdminMode_Type()
)
hmAgentOutboundTelnetAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentOutboundTelnetAdminMode.setStatus("current")


class _HmAgentOutboundTelnetMaxNoOfSessions_Type(Integer32):
    """Custom type hmAgentOutboundTelnetMaxNoOfSessions based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_HmAgentOutboundTelnetMaxNoOfSessions_Type.__name__ = "Integer32"
_HmAgentOutboundTelnetMaxNoOfSessions_Object = MibScalar
hmAgentOutboundTelnetMaxNoOfSessions = _HmAgentOutboundTelnetMaxNoOfSessions_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 19, 1, 2),
    _HmAgentOutboundTelnetMaxNoOfSessions_Type()
)
hmAgentOutboundTelnetMaxNoOfSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentOutboundTelnetMaxNoOfSessions.setStatus("current")


class _HmAgentOutboundTelnetTimeout_Type(Integer32):
    """Custom type hmAgentOutboundTelnetTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 160),
    )


_HmAgentOutboundTelnetTimeout_Type.__name__ = "Integer32"
_HmAgentOutboundTelnetTimeout_Object = MibScalar
hmAgentOutboundTelnetTimeout = _HmAgentOutboundTelnetTimeout_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 19, 1, 3),
    _HmAgentOutboundTelnetTimeout_Type()
)
hmAgentOutboundTelnetTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentOutboundTelnetTimeout.setStatus("current")
_HmAgentDot1xAdvanced_ObjectIdentity = ObjectIdentity
hmAgentDot1xAdvanced = _HmAgentDot1xAdvanced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 36)
)
_HmAgentDot1xEnhancementConfigGroup_ObjectIdentity = ObjectIdentity
hmAgentDot1xEnhancementConfigGroup = _HmAgentDot1xEnhancementConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 1)
)


class _HmAgentDot1xRadiusVlanAssignment_Type(Integer32):
    """Custom type hmAgentDot1xRadiusVlanAssignment based on Integer32"""
    defaultValue = 2

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


_HmAgentDot1xRadiusVlanAssignment_Type.__name__ = "Integer32"
_HmAgentDot1xRadiusVlanAssignment_Object = MibScalar
hmAgentDot1xRadiusVlanAssignment = _HmAgentDot1xRadiusVlanAssignment_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 1, 1),
    _HmAgentDot1xRadiusVlanAssignment_Type()
)
hmAgentDot1xRadiusVlanAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentDot1xRadiusVlanAssignment.setStatus("current")


class _HmAgentDot1xDynamicVlanCreationMode_Type(Integer32):
    """Custom type hmAgentDot1xDynamicVlanCreationMode based on Integer32"""
    defaultValue = 2

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


_HmAgentDot1xDynamicVlanCreationMode_Type.__name__ = "Integer32"
_HmAgentDot1xDynamicVlanCreationMode_Object = MibScalar
hmAgentDot1xDynamicVlanCreationMode = _HmAgentDot1xDynamicVlanCreationMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 1, 2),
    _HmAgentDot1xDynamicVlanCreationMode_Type()
)
hmAgentDot1xDynamicVlanCreationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentDot1xDynamicVlanCreationMode.setStatus("current")


class _HmAgentDot1xSafeVlanMode_Type(Integer32):
    """Custom type hmAgentDot1xSafeVlanMode based on Integer32"""
    defaultValue = 2

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


_HmAgentDot1xSafeVlanMode_Type.__name__ = "Integer32"
_HmAgentDot1xSafeVlanMode_Object = MibScalar
hmAgentDot1xSafeVlanMode = _HmAgentDot1xSafeVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 1, 3),
    _HmAgentDot1xSafeVlanMode_Type()
)
hmAgentDot1xSafeVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentDot1xSafeVlanMode.setStatus("current")
_HmAgentDot1xPortConfigGroup_ObjectIdentity = ObjectIdentity
hmAgentDot1xPortConfigGroup = _HmAgentDot1xPortConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 2)
)
_HmAgentDot1xPortConfigTable_Object = MibTable
hmAgentDot1xPortConfigTable = _HmAgentDot1xPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 2, 1)
)
if mibBuilder.loadTexts:
    hmAgentDot1xPortConfigTable.setStatus("current")
_HmAgentDot1xPortConfigEntry_Object = MibTableRow
hmAgentDot1xPortConfigEntry = _HmAgentDot1xPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 2, 1, 1)
)
hmAgentDot1xPortConfigEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    hmAgentDot1xPortConfigEntry.setStatus("current")


class _HmAgentDot1xPortControlMode_Type(HmAgentDot1xPortControlMode):
    """Custom type hmAgentDot1xPortControlMode based on HmAgentDot1xPortControlMode"""


_HmAgentDot1xPortControlMode_Object = MibTableColumn
hmAgentDot1xPortControlMode = _HmAgentDot1xPortControlMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 2, 1, 1, 1),
    _HmAgentDot1xPortControlMode_Type()
)
hmAgentDot1xPortControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentDot1xPortControlMode.setStatus("current")


class _HmAgentDot1xGuestVlanId_Type(Unsigned32):
    """Custom type hmAgentDot1xGuestVlanId based on Unsigned32"""
    defaultValue = 0


_HmAgentDot1xGuestVlanId_Object = MibTableColumn
hmAgentDot1xGuestVlanId = _HmAgentDot1xGuestVlanId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 2, 1, 1, 2),
    _HmAgentDot1xGuestVlanId_Type()
)
hmAgentDot1xGuestVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentDot1xGuestVlanId.setStatus("current")


class _HmAgentDot1xGuestVlanPeriod_Type(Unsigned32):
    """Custom type hmAgentDot1xGuestVlanPeriod based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HmAgentDot1xGuestVlanPeriod_Type.__name__ = "Unsigned32"
_HmAgentDot1xGuestVlanPeriod_Object = MibTableColumn
hmAgentDot1xGuestVlanPeriod = _HmAgentDot1xGuestVlanPeriod_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 2, 1, 1, 3),
    _HmAgentDot1xGuestVlanPeriod_Type()
)
hmAgentDot1xGuestVlanPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentDot1xGuestVlanPeriod.setStatus("current")


class _HmAgentDot1xUnauthenticatedVlan_Type(Unsigned32):
    """Custom type hmAgentDot1xUnauthenticatedVlan based on Unsigned32"""
    defaultValue = 0


_HmAgentDot1xUnauthenticatedVlan_Object = MibTableColumn
hmAgentDot1xUnauthenticatedVlan = _HmAgentDot1xUnauthenticatedVlan_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 2, 1, 1, 4),
    _HmAgentDot1xUnauthenticatedVlan_Type()
)
hmAgentDot1xUnauthenticatedVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentDot1xUnauthenticatedVlan.setStatus("current")
_HmAgentDot1xMaxUsers_Type = Unsigned32
_HmAgentDot1xMaxUsers_Object = MibTableColumn
hmAgentDot1xMaxUsers = _HmAgentDot1xMaxUsers_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 2, 1, 1, 5),
    _HmAgentDot1xMaxUsers_Type()
)
hmAgentDot1xMaxUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentDot1xMaxUsers.setStatus("current")


class _HmAgentDot1xPortVlanAssigned_Type(Unsigned32):
    """Custom type hmAgentDot1xPortVlanAssigned based on Unsigned32"""
    defaultValue = 0


_HmAgentDot1xPortVlanAssigned_Object = MibTableColumn
hmAgentDot1xPortVlanAssigned = _HmAgentDot1xPortVlanAssigned_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 2, 1, 1, 6),
    _HmAgentDot1xPortVlanAssigned_Type()
)
hmAgentDot1xPortVlanAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentDot1xPortVlanAssigned.setStatus("current")


class _HmAgentDot1xPortVlanAssignedReason_Type(Integer32):
    """Custom type hmAgentDot1xPortVlanAssignedReason based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("guestVlan", 4),
          ("notAssigned", 7),
          ("radius", 2),
          ("unauthenticatedVlan", 3),
          ("voiceVlan", 5))
    )


_HmAgentDot1xPortVlanAssignedReason_Type.__name__ = "Integer32"
_HmAgentDot1xPortVlanAssignedReason_Object = MibTableColumn
hmAgentDot1xPortVlanAssignedReason = _HmAgentDot1xPortVlanAssignedReason_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 2, 1, 1, 7),
    _HmAgentDot1xPortVlanAssignedReason_Type()
)
hmAgentDot1xPortVlanAssignedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentDot1xPortVlanAssignedReason.setStatus("current")
_HmAgentDot1xPortSessionTimeout_Type = Unsigned32
_HmAgentDot1xPortSessionTimeout_Object = MibTableColumn
hmAgentDot1xPortSessionTimeout = _HmAgentDot1xPortSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 2, 1, 1, 8),
    _HmAgentDot1xPortSessionTimeout_Type()
)
hmAgentDot1xPortSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentDot1xPortSessionTimeout.setStatus("current")


class _HmAgentDot1xPortTerminationAction_Type(HmAgentDot1xSessionTerminationAction):
    """Custom type hmAgentDot1xPortTerminationAction based on HmAgentDot1xSessionTerminationAction"""
    defaultValue = 1


_HmAgentDot1xPortTerminationAction_Object = MibTableColumn
hmAgentDot1xPortTerminationAction = _HmAgentDot1xPortTerminationAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 2, 1, 1, 9),
    _HmAgentDot1xPortTerminationAction_Type()
)
hmAgentDot1xPortTerminationAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentDot1xPortTerminationAction.setStatus("current")


class _HmAgentDot1xPortMABenabled_Type(Integer32):
    """Custom type hmAgentDot1xPortMABenabled based on Integer32"""
    defaultValue = 2

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


_HmAgentDot1xPortMABenabled_Type.__name__ = "Integer32"
_HmAgentDot1xPortMABenabled_Object = MibTableColumn
hmAgentDot1xPortMABenabled = _HmAgentDot1xPortMABenabled_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 2, 1, 1, 10),
    _HmAgentDot1xPortMABenabled_Type()
)
hmAgentDot1xPortMABenabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentDot1xPortMABenabled.setStatus("current")


class _HmAgentDot1xPortMABenabledOperational_Type(Integer32):
    """Custom type hmAgentDot1xPortMABenabledOperational based on Integer32"""
    defaultValue = 2

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


_HmAgentDot1xPortMABenabledOperational_Type.__name__ = "Integer32"
_HmAgentDot1xPortMABenabledOperational_Object = MibTableColumn
hmAgentDot1xPortMABenabledOperational = _HmAgentDot1xPortMABenabledOperational_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 2, 1, 1, 11),
    _HmAgentDot1xPortMABenabledOperational_Type()
)
hmAgentDot1xPortMABenabledOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentDot1xPortMABenabledOperational.setStatus("current")
_HmAgentDot1xClientConfigGroup_ObjectIdentity = ObjectIdentity
hmAgentDot1xClientConfigGroup = _HmAgentDot1xClientConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 3)
)
_HmAgentDot1xClientConfigTable_Object = MibTable
hmAgentDot1xClientConfigTable = _HmAgentDot1xClientConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 3, 1)
)
if mibBuilder.loadTexts:
    hmAgentDot1xClientConfigTable.setStatus("current")
_HmAgentDot1xClientConfigEntry_Object = MibTableRow
hmAgentDot1xClientConfigEntry = _HmAgentDot1xClientConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 3, 1, 1)
)
hmAgentDot1xClientConfigEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-BASICL2-MIB", "hmAgentDot1xClientMacAddress"),
)
if mibBuilder.loadTexts:
    hmAgentDot1xClientConfigEntry.setStatus("current")
_HmAgentDot1xClientMacAddress_Type = MacAddress
_HmAgentDot1xClientMacAddress_Object = MibTableColumn
hmAgentDot1xClientMacAddress = _HmAgentDot1xClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 3, 1, 1, 1),
    _HmAgentDot1xClientMacAddress_Type()
)
hmAgentDot1xClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentDot1xClientMacAddress.setStatus("current")
_HmAgentDot1xLogicalPort_Type = Unsigned32
_HmAgentDot1xLogicalPort_Object = MibTableColumn
hmAgentDot1xLogicalPort = _HmAgentDot1xLogicalPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 3, 1, 1, 2),
    _HmAgentDot1xLogicalPort_Type()
)
hmAgentDot1xLogicalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentDot1xLogicalPort.setStatus("current")
_HmAgentDot1xInterface_Type = Unsigned32
_HmAgentDot1xInterface_Object = MibTableColumn
hmAgentDot1xInterface = _HmAgentDot1xInterface_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 3, 1, 1, 3),
    _HmAgentDot1xInterface_Type()
)
hmAgentDot1xInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentDot1xInterface.setStatus("current")


class _HmAgentDot1xClientAuthPAEstate_Type(Integer32):
    """Custom type hmAgentDot1xClientAuthPAEstate based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("aborting", 6),
          ("authenticated", 5),
          ("authenticating", 4),
          ("connecting", 3),
          ("disconnected", 2),
          ("forceAuth", 8),
          ("forceUnauth", 9),
          ("held", 7),
          ("initialize", 1))
    )


_HmAgentDot1xClientAuthPAEstate_Type.__name__ = "Integer32"
_HmAgentDot1xClientAuthPAEstate_Object = MibTableColumn
hmAgentDot1xClientAuthPAEstate = _HmAgentDot1xClientAuthPAEstate_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 3, 1, 1, 4),
    _HmAgentDot1xClientAuthPAEstate_Type()
)
hmAgentDot1xClientAuthPAEstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentDot1xClientAuthPAEstate.setStatus("current")


class _HmAgentDot1xClientBackendState_Type(Integer32):
    """Custom type hmAgentDot1xClientBackendState based on Integer32"""
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
        *(("fail", 4),
          ("idle", 6),
          ("initialize", 7),
          ("request", 1),
          ("response", 2),
          ("success", 3),
          ("timeout", 5))
    )


_HmAgentDot1xClientBackendState_Type.__name__ = "Integer32"
_HmAgentDot1xClientBackendState_Object = MibTableColumn
hmAgentDot1xClientBackendState = _HmAgentDot1xClientBackendState_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 3, 1, 1, 5),
    _HmAgentDot1xClientBackendState_Type()
)
hmAgentDot1xClientBackendState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentDot1xClientBackendState.setStatus("current")
_HmAgentDot1xClientUserName_Type = DisplayString
_HmAgentDot1xClientUserName_Object = MibTableColumn
hmAgentDot1xClientUserName = _HmAgentDot1xClientUserName_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 3, 1, 1, 6),
    _HmAgentDot1xClientUserName_Type()
)
hmAgentDot1xClientUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentDot1xClientUserName.setStatus("current")
_HmAgentDot1xClientSessionTime_Type = Unsigned32
_HmAgentDot1xClientSessionTime_Object = MibTableColumn
hmAgentDot1xClientSessionTime = _HmAgentDot1xClientSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 3, 1, 1, 7),
    _HmAgentDot1xClientSessionTime_Type()
)
hmAgentDot1xClientSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentDot1xClientSessionTime.setStatus("current")
_HmAgentDot1xClientFilterID_Type = DisplayString
_HmAgentDot1xClientFilterID_Object = MibTableColumn
hmAgentDot1xClientFilterID = _HmAgentDot1xClientFilterID_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 3, 1, 1, 8),
    _HmAgentDot1xClientFilterID_Type()
)
hmAgentDot1xClientFilterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentDot1xClientFilterID.setStatus("current")
_HmAgentDot1xClientVlanAssigned_Type = Unsigned32
_HmAgentDot1xClientVlanAssigned_Object = MibTableColumn
hmAgentDot1xClientVlanAssigned = _HmAgentDot1xClientVlanAssigned_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 3, 1, 1, 9),
    _HmAgentDot1xClientVlanAssigned_Type()
)
hmAgentDot1xClientVlanAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentDot1xClientVlanAssigned.setStatus("current")


class _HmAgentDot1xClientVlanAssignedReason_Type(Integer32):
    """Custom type hmAgentDot1xClientVlanAssignedReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("guestVlan", 4),
          ("invalid", 7),
          ("radius", 2),
          ("unauthenticatedVlan", 3),
          ("voiceVlan", 5))
    )


_HmAgentDot1xClientVlanAssignedReason_Type.__name__ = "Integer32"
_HmAgentDot1xClientVlanAssignedReason_Object = MibTableColumn
hmAgentDot1xClientVlanAssignedReason = _HmAgentDot1xClientVlanAssignedReason_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 3, 1, 1, 10),
    _HmAgentDot1xClientVlanAssignedReason_Type()
)
hmAgentDot1xClientVlanAssignedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentDot1xClientVlanAssignedReason.setStatus("current")
_HmAgentDot1xClientSessionTimeout_Type = Unsigned32
_HmAgentDot1xClientSessionTimeout_Object = MibTableColumn
hmAgentDot1xClientSessionTimeout = _HmAgentDot1xClientSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 3, 1, 1, 11),
    _HmAgentDot1xClientSessionTimeout_Type()
)
hmAgentDot1xClientSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentDot1xClientSessionTimeout.setStatus("current")
_HmAgentDot1xClientTerminationAction_Type = HmAgentDot1xSessionTerminationAction
_HmAgentDot1xClientTerminationAction_Object = MibTableColumn
hmAgentDot1xClientTerminationAction = _HmAgentDot1xClientTerminationAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 3, 1, 1, 12),
    _HmAgentDot1xClientTerminationAction_Type()
)
hmAgentDot1xClientTerminationAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentDot1xClientTerminationAction.setStatus("current")
_Dot1xTraps_ObjectIdentity = ObjectIdentity
dot1xTraps = _Dot1xTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 4)
)

# Managed Objects groups


# Notification objects

multipleUsersTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 50, 1)
)
if mibBuilder.loadTexts:
    multipleUsersTrap.setStatus(
        "current"
    )

broadcastStormStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 50, 2)
)
if mibBuilder.loadTexts:
    broadcastStormStartTrap.setStatus(
        "obsolete"
    )

broadcastStormEndTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 50, 3)
)
if mibBuilder.loadTexts:
    broadcastStormEndTrap.setStatus(
        "obsolete"
    )

linkFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 50, 4)
)
if mibBuilder.loadTexts:
    linkFailureTrap.setStatus(
        "obsolete"
    )

vlanRequestFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 50, 5)
)
vlanRequestFailureTrap.setObjects(
    ("Q-BRIDGE-MIB", "dot1qVlanIndex")
)
if mibBuilder.loadTexts:
    vlanRequestFailureTrap.setStatus(
        "obsolete"
    )

vlanDeleteLastTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 50, 6)
)
vlanDeleteLastTrap.setObjects(
    ("Q-BRIDGE-MIB", "dot1qVlanIndex")
)
if mibBuilder.loadTexts:
    vlanDeleteLastTrap.setStatus(
        "current"
    )

vlanDefaultCfgFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 50, 7)
)
vlanDefaultCfgFailureTrap.setObjects(
    ("Q-BRIDGE-MIB", "dot1qVlanIndex")
)
if mibBuilder.loadTexts:
    vlanDefaultCfgFailureTrap.setStatus(
        "current"
    )

vlanRestoreFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 50, 8)
)
vlanRestoreFailureTrap.setObjects(
    ("Q-BRIDGE-MIB", "dot1qVlanIndex")
)
if mibBuilder.loadTexts:
    vlanRestoreFailureTrap.setStatus(
        "obsolete"
    )

fanFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 50, 9)
)
if mibBuilder.loadTexts:
    fanFailureTrap.setStatus(
        "obsolete"
    )

stpInstanceNewRootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 50, 10)
)
stpInstanceNewRootTrap.setObjects(
    ("HIRSCHMANN-MMP4-BASICL2-MIB", "hmAgentStpMstId")
)
if mibBuilder.loadTexts:
    stpInstanceNewRootTrap.setStatus(
        "current"
    )

stpInstanceTopologyChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 50, 11)
)
stpInstanceTopologyChangeTrap.setObjects(
    ("HIRSCHMANN-MMP4-BASICL2-MIB", "hmAgentStpMstId")
)
if mibBuilder.loadTexts:
    stpInstanceTopologyChangeTrap.setStatus(
        "current"
    )

powerSupplyStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 50, 12)
)
if mibBuilder.loadTexts:
    powerSupplyStatusChangeTrap.setStatus(
        "obsolete"
    )

failedUserLoginTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 15, 1, 50, 13)
)
if mibBuilder.loadTexts:
    failedUserLoginTrap.setStatus(
        "current"
    )

dot1xPortStatusAuthorized = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 4, 1)
)
dot1xPortStatusAuthorized.setObjects(
    ("IEEE8021-PAE-MIB", "dot1xPaePortNumber")
)
if mibBuilder.loadTexts:
    dot1xPortStatusAuthorized.setStatus(
        "current"
    )

dot1xPortStatusUnauthorized = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 15, 36, 4, 2)
)
dot1xPortStatusUnauthorized.setObjects(
    ("IEEE8021-PAE-MIB", "dot1xPaePortNumber")
)
if mibBuilder.loadTexts:
    dot1xPortStatusUnauthorized.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HIRSCHMANN-MMP4-BASICL2-MIB",
    **{"HmAgentPortMask": HmAgentPortMask,
       "BridgeId": BridgeId,
       "HmAgentDot1xPortControlMode": HmAgentDot1xPortControlMode,
       "HmAgentDot1xSessionTerminationAction": HmAgentDot1xSessionTerminationAction,
       "hmPlatform4": hmPlatform4,
       "hmPlatform4BasicL2": hmPlatform4BasicL2,
       "hmAgentInfoGroup": hmAgentInfoGroup,
       "hmAgentTrapLogGroup": hmAgentTrapLogGroup,
       "hmAgentTrapLogTotal": hmAgentTrapLogTotal,
       "hmAgentTrapLogTotalSinceLastViewed": hmAgentTrapLogTotalSinceLastViewed,
       "hmAgentTrapLogTable": hmAgentTrapLogTable,
       "hmAgentTrapLogEntry": hmAgentTrapLogEntry,
       "hmAgentTrapLogIndex": hmAgentTrapLogIndex,
       "hmAgentTrapLogSystemTime": hmAgentTrapLogSystemTime,
       "hmAgentTrapLogTrap": hmAgentTrapLogTrap,
       "hmAgentConfigGroup": hmAgentConfigGroup,
       "hmAgentCLIConfigGroup": hmAgentCLIConfigGroup,
       "hmAgentLoginSessionTable": hmAgentLoginSessionTable,
       "hmAgentLoginSessionEntry": hmAgentLoginSessionEntry,
       "hmAgentLoginSessionIndex": hmAgentLoginSessionIndex,
       "hmAgentLoginSessionUserName": hmAgentLoginSessionUserName,
       "hmAgentLoginSessionIPAddress": hmAgentLoginSessionIPAddress,
       "hmAgentLoginSessionConnectionType": hmAgentLoginSessionConnectionType,
       "hmAgentLoginSessionIdleTime": hmAgentLoginSessionIdleTime,
       "hmAgentLoginSessionSessionTime": hmAgentLoginSessionSessionTime,
       "hmAgentLoginSessionStatus": hmAgentLoginSessionStatus,
       "hmAgentTelnetConfigGroup": hmAgentTelnetConfigGroup,
       "hmAgentTelnetLoginTimeout": hmAgentTelnetLoginTimeout,
       "hmAgentTelnetMaxSessions": hmAgentTelnetMaxSessions,
       "hmAgentTelnetAllowNewMode": hmAgentTelnetAllowNewMode,
       "hmAgentUserConfigGroup": hmAgentUserConfigGroup,
       "hmAgentUserConfigCreate": hmAgentUserConfigCreate,
       "hmAgentUserConfigTable": hmAgentUserConfigTable,
       "hmAgentUserConfigEntry": hmAgentUserConfigEntry,
       "hmAgentUserIndex": hmAgentUserIndex,
       "hmAgentUserName": hmAgentUserName,
       "hmAgentUserPassword": hmAgentUserPassword,
       "hmAgentUserAccessMode": hmAgentUserAccessMode,
       "hmAgentUserStatus": hmAgentUserStatus,
       "hmAgentUserAuthenticationType": hmAgentUserAuthenticationType,
       "hmAgentUserEncryptionType": hmAgentUserEncryptionType,
       "hmAgentUserEncryptionPassword": hmAgentUserEncryptionPassword,
       "hmAgentUserDefaultPwdActive": hmAgentUserDefaultPwdActive,
       "hmAgentLagConfigGroup": hmAgentLagConfigGroup,
       "hmAgentLagConfigCreate": hmAgentLagConfigCreate,
       "hmAgentLagSummaryConfigTable": hmAgentLagSummaryConfigTable,
       "hmAgentLagSummaryConfigEntry": hmAgentLagSummaryConfigEntry,
       "hmAgentLagSummaryLagIndex": hmAgentLagSummaryLagIndex,
       "hmAgentLagSummaryName": hmAgentLagSummaryName,
       "hmAgentLagSummaryFlushTimer": hmAgentLagSummaryFlushTimer,
       "hmAgentLagSummaryLinkTrap": hmAgentLagSummaryLinkTrap,
       "hmAgentLagSummaryAdminMode": hmAgentLagSummaryAdminMode,
       "hmAgentLagSummaryStpMode": hmAgentLagSummaryStpMode,
       "hmAgentLagSummaryAddPort": hmAgentLagSummaryAddPort,
       "hmAgentLagSummaryDeletePort": hmAgentLagSummaryDeletePort,
       "hmAgentLagSummaryStatus": hmAgentLagSummaryStatus,
       "hmAgentLagSummaryType": hmAgentLagSummaryType,
       "hmAgentLagDetailedConfigTable": hmAgentLagDetailedConfigTable,
       "hmAgentLagDetailedConfigEntry": hmAgentLagDetailedConfigEntry,
       "hmAgentLagDetailedLagIndex": hmAgentLagDetailedLagIndex,
       "hmAgentLagDetailedIfIndex": hmAgentLagDetailedIfIndex,
       "hmAgentLagDetailedPortSpeed": hmAgentLagDetailedPortSpeed,
       "hmAgentLagDetailedPortStatus": hmAgentLagDetailedPortStatus,
       "hmAgentLagConfigStaticCapability": hmAgentLagConfigStaticCapability,
       "hmAgentSpanningTreeConfigGroup": hmAgentSpanningTreeConfigGroup,
       "hmAgentSpanningTreeMode": hmAgentSpanningTreeMode,
       "hmAgentSwitchConfigGroup": hmAgentSwitchConfigGroup,
       "hmAgentSwitchBroadcastControlMode": hmAgentSwitchBroadcastControlMode,
       "hmAgentSwitchDot3FlowControlMode": hmAgentSwitchDot3FlowControlMode,
       "hmAgentSwitchAddressAgingTimeoutTable": hmAgentSwitchAddressAgingTimeoutTable,
       "hmAgentSwitchAddressAgingTimeoutEntry": hmAgentSwitchAddressAgingTimeoutEntry,
       "hmAgentSwitchAddressAgingTimeout": hmAgentSwitchAddressAgingTimeout,
       "hmAgentSwitchStaticMacFilteringTable": hmAgentSwitchStaticMacFilteringTable,
       "hmAgentSwitchStaticMacFilteringEntry": hmAgentSwitchStaticMacFilteringEntry,
       "hmAgentSwitchStaticMacFilteringVlanId": hmAgentSwitchStaticMacFilteringVlanId,
       "hmAgentSwitchStaticMacFilteringAddress": hmAgentSwitchStaticMacFilteringAddress,
       "hmAgentSwitchStaticMacFilteringSourcePortMask": hmAgentSwitchStaticMacFilteringSourcePortMask,
       "hmAgentSwitchStaticMacFilteringDestPortMask": hmAgentSwitchStaticMacFilteringDestPortMask,
       "hmAgentSwitchStaticMacFilteringStatus": hmAgentSwitchStaticMacFilteringStatus,
       "hmAgentSwitchIGMPSnoopingGroup": hmAgentSwitchIGMPSnoopingGroup,
       "hmAgentSwitchIGMPSnoopingAdminMode": hmAgentSwitchIGMPSnoopingAdminMode,
       "hmAgentSwitchIGMPSnoopingGroupMembershipInterval": hmAgentSwitchIGMPSnoopingGroupMembershipInterval,
       "hmAgentSwitchIGMPSnoopingMaxResponseTime": hmAgentSwitchIGMPSnoopingMaxResponseTime,
       "hmAgentSwitchIGMPSnoopingMRPExpirationTime": hmAgentSwitchIGMPSnoopingMRPExpirationTime,
       "hmAgentSwitchIGMPSnoopingPortMask": hmAgentSwitchIGMPSnoopingPortMask,
       "hmAgentSwitchIGMPSnoopingMulticastControlFramesProcessed": hmAgentSwitchIGMPSnoopingMulticastControlFramesProcessed,
       "hmAgentSwitchMFDBGroup": hmAgentSwitchMFDBGroup,
       "hmAgentSwitchMFDBTable": hmAgentSwitchMFDBTable,
       "hmAgentSwitchMFDBEntry": hmAgentSwitchMFDBEntry,
       "hmAgentSwitchMFDBVlanId": hmAgentSwitchMFDBVlanId,
       "hmAgentSwitchMFDBMacAddress": hmAgentSwitchMFDBMacAddress,
       "hmAgentSwitchMFDBProtocolType": hmAgentSwitchMFDBProtocolType,
       "hmAgentSwitchMFDBType": hmAgentSwitchMFDBType,
       "hmAgentSwitchMFDBDescription": hmAgentSwitchMFDBDescription,
       "hmAgentSwitchMFDBForwardingPortMask": hmAgentSwitchMFDBForwardingPortMask,
       "hmAgentSwitchMFDBFilteringPortMask": hmAgentSwitchMFDBFilteringPortMask,
       "hmAgentSwitchMFDBSummaryTable": hmAgentSwitchMFDBSummaryTable,
       "hmAgentSwitchMFDBSummaryEntry": hmAgentSwitchMFDBSummaryEntry,
       "hmAgentSwitchMFDBSummaryVlanId": hmAgentSwitchMFDBSummaryVlanId,
       "hmAgentSwitchMFDBSummaryMacAddress": hmAgentSwitchMFDBSummaryMacAddress,
       "hmAgentSwitchMFDBSummaryForwardingPortMask": hmAgentSwitchMFDBSummaryForwardingPortMask,
       "hmAgentSwitchMFDBMaxTableEntries": hmAgentSwitchMFDBMaxTableEntries,
       "hmAgentSwitchMFDBMostEntriesUsed": hmAgentSwitchMFDBMostEntriesUsed,
       "hmAgentSwitchMFDBCurrentEntries": hmAgentSwitchMFDBCurrentEntries,
       "hmAgentSwitchDVlanTagGroup": hmAgentSwitchDVlanTagGroup,
       "hmAgentSwitchDVlanTagEthertype": hmAgentSwitchDVlanTagEthertype,
       "hmAgentSwitchVoiceVLANGroup": hmAgentSwitchVoiceVLANGroup,
       "hmAgentSwitchVoiceVLANAdminMode": hmAgentSwitchVoiceVLANAdminMode,
       "hmAgentSwitchVoiceVlanDeviceTable": hmAgentSwitchVoiceVlanDeviceTable,
       "hmAgentSwitchVoiceVlanDeviceEntry": hmAgentSwitchVoiceVlanDeviceEntry,
       "hmAgentSwitchVoiceVlanInterfaceNum": hmAgentSwitchVoiceVlanInterfaceNum,
       "hmAgentSwitchVoiceVlanDeviceMacAddress": hmAgentSwitchVoiceVlanDeviceMacAddress,
       "hmAgentTransferConfigGroup": hmAgentTransferConfigGroup,
       "hmAgentTransferUploadGroup": hmAgentTransferUploadGroup,
       "hmAgentTransferUploadMode": hmAgentTransferUploadMode,
       "hmAgentTransferUploadServerIP": hmAgentTransferUploadServerIP,
       "hmAgentTransferUploadPath": hmAgentTransferUploadPath,
       "hmAgentTransferUploadFilename": hmAgentTransferUploadFilename,
       "hmAgentTransferUploadDataType": hmAgentTransferUploadDataType,
       "hmAgentTransferUploadStart": hmAgentTransferUploadStart,
       "hmAgentTransferUploadStatus": hmAgentTransferUploadStatus,
       "hmAgentTransferDownloadGroup": hmAgentTransferDownloadGroup,
       "hmAgentTransferDownloadMode": hmAgentTransferDownloadMode,
       "hmAgentTransferDownloadServerIP": hmAgentTransferDownloadServerIP,
       "hmAgentTransferDownloadPath": hmAgentTransferDownloadPath,
       "hmAgentTransferDownloadFilename": hmAgentTransferDownloadFilename,
       "hmAgentTransferDownloadDataType": hmAgentTransferDownloadDataType,
       "hmAgentTransferDownloadStart": hmAgentTransferDownloadStart,
       "hmAgentTransferDownloadStatus": hmAgentTransferDownloadStatus,
       "hmAgentPortMirroringGroup": hmAgentPortMirroringGroup,
       "hmAgentMirroredPortIfIndex": hmAgentMirroredPortIfIndex,
       "hmAgentProbePortIfIndex": hmAgentProbePortIfIndex,
       "hmAgentPortMirroringMode": hmAgentPortMirroringMode,
       "hmAgentPortMirrorTable": hmAgentPortMirrorTable,
       "hmAgentPortMirrorEntry": hmAgentPortMirrorEntry,
       "hmAgentPortMirrorSessionNum": hmAgentPortMirrorSessionNum,
       "hmAgentPortMirrorDestinationPort": hmAgentPortMirrorDestinationPort,
       "hmAgentPortMirrorSourcePortMask": hmAgentPortMirrorSourcePortMask,
       "hmAgentPortMirrorAdminMode": hmAgentPortMirrorAdminMode,
       "hmAgentPortMirrorIngressMask": hmAgentPortMirrorIngressMask,
       "hmAgentPortMirrorEgressMask": hmAgentPortMirrorEgressMask,
       "hmAgentDot3adAggPortTable": hmAgentDot3adAggPortTable,
       "hmAgentDot3adAggPortEntry": hmAgentDot3adAggPortEntry,
       "hmAgentDot3adAggPort": hmAgentDot3adAggPort,
       "hmAgentDot3adAggPortLACPMode": hmAgentDot3adAggPortLACPMode,
       "hmAgentPortConfigTable": hmAgentPortConfigTable,
       "hmAgentPortConfigEntry": hmAgentPortConfigEntry,
       "hmAgentPortDot1dBasePort": hmAgentPortDot1dBasePort,
       "hmAgentPortIfIndex": hmAgentPortIfIndex,
       "hmAgentPortIanaType": hmAgentPortIanaType,
       "hmAgentPortSTPMode": hmAgentPortSTPMode,
       "hmAgentPortSTPState": hmAgentPortSTPState,
       "hmAgentPortAdminMode": hmAgentPortAdminMode,
       "hmAgentPortPhysicalMode": hmAgentPortPhysicalMode,
       "hmAgentPortPhysicalStatus": hmAgentPortPhysicalStatus,
       "hmAgentPortLinkTrapMode": hmAgentPortLinkTrapMode,
       "hmAgentPortClearStats": hmAgentPortClearStats,
       "hmAgentPortDefaultType": hmAgentPortDefaultType,
       "hmAgentPortType": hmAgentPortType,
       "hmAgentPortAutoNegAdminStatus": hmAgentPortAutoNegAdminStatus,
       "hmAgentPortDot3FlowControlMode": hmAgentPortDot3FlowControlMode,
       "hmAgentPortDVlanTagMode": hmAgentPortDVlanTagMode,
       "hmAgentPortDVlanTagEthertype": hmAgentPortDVlanTagEthertype,
       "hmAgentPortDVlanTagCustomerId": hmAgentPortDVlanTagCustomerId,
       "hmAgentPortMaxFrameSizeLimit": hmAgentPortMaxFrameSizeLimit,
       "hmAgentPortMaxFrameSize": hmAgentPortMaxFrameSize,
       "hmAgentPortVoiceVlanMode": hmAgentPortVoiceVlanMode,
       "hmAgentPortVoiceVlanID": hmAgentPortVoiceVlanID,
       "hmAgentPortVoiceVlanPriority": hmAgentPortVoiceVlanPriority,
       "hmAgentPortVoiceVlanDataPriorityMode": hmAgentPortVoiceVlanDataPriorityMode,
       "hmAgentPortVoiceVlanOperationalStatus": hmAgentPortVoiceVlanOperationalStatus,
       "hmAgentPortVoiceVlanDSCP": hmAgentPortVoiceVlanDSCP,
       "hmAgentPortVoiceVlanAuthMode": hmAgentPortVoiceVlanAuthMode,
       "hmAgentProtocolConfigGroup": hmAgentProtocolConfigGroup,
       "hmAgentProtocolGroupCreate": hmAgentProtocolGroupCreate,
       "hmAgentProtocolGroupTable": hmAgentProtocolGroupTable,
       "hmAgentProtocolGroupEntry": hmAgentProtocolGroupEntry,
       "hmAgentProtocolGroupId": hmAgentProtocolGroupId,
       "hmAgentProtocolGroupName": hmAgentProtocolGroupName,
       "hmAgentProtocolGroupVlanId": hmAgentProtocolGroupVlanId,
       "hmAgentProtocolGroupProtocolIP": hmAgentProtocolGroupProtocolIP,
       "hmAgentProtocolGroupProtocolARP": hmAgentProtocolGroupProtocolARP,
       "hmAgentProtocolGroupProtocolIPX": hmAgentProtocolGroupProtocolIPX,
       "hmAgentProtocolGroupStatus": hmAgentProtocolGroupStatus,
       "hmAgentProtocolGroupPortTable": hmAgentProtocolGroupPortTable,
       "hmAgentProtocolGroupPortEntry": hmAgentProtocolGroupPortEntry,
       "hmAgentProtocolGroupPortIfIndex": hmAgentProtocolGroupPortIfIndex,
       "hmAgentProtocolGroupPortStatus": hmAgentProtocolGroupPortStatus,
       "hmAgentStpSwitchConfigGroup": hmAgentStpSwitchConfigGroup,
       "hmAgentStpConfigDigestKey": hmAgentStpConfigDigestKey,
       "hmAgentStpConfigFormatSelector": hmAgentStpConfigFormatSelector,
       "hmAgentStpConfigName": hmAgentStpConfigName,
       "hmAgentStpConfigRevision": hmAgentStpConfigRevision,
       "hmAgentStpForceVersion": hmAgentStpForceVersion,
       "hmAgentStpAdminMode": hmAgentStpAdminMode,
       "hmAgentStpPortTable": hmAgentStpPortTable,
       "hmAgentStpPortEntry": hmAgentStpPortEntry,
       "hmAgentStpPortState": hmAgentStpPortState,
       "hmAgentStpPortStatsMstpBpduRx": hmAgentStpPortStatsMstpBpduRx,
       "hmAgentStpPortStatsMstpBpduTx": hmAgentStpPortStatsMstpBpduTx,
       "hmAgentStpPortStatsRstpBpduRx": hmAgentStpPortStatsRstpBpduRx,
       "hmAgentStpPortStatsRstpBpduTx": hmAgentStpPortStatsRstpBpduTx,
       "hmAgentStpPortStatsStpBpduRx": hmAgentStpPortStatsStpBpduRx,
       "hmAgentStpPortStatsStpBpduTx": hmAgentStpPortStatsStpBpduTx,
       "hmAgentStpPortUpTime": hmAgentStpPortUpTime,
       "hmAgentStpPortMigrationCheck": hmAgentStpPortMigrationCheck,
       "hmAgentStpPortHelloTime": hmAgentStpPortHelloTime,
       "hmAgentStpCstConfigGroup": hmAgentStpCstConfigGroup,
       "hmAgentStpCstHelloTime": hmAgentStpCstHelloTime,
       "hmAgentStpCstMaxAge": hmAgentStpCstMaxAge,
       "hmAgentStpCstRegionalRootId": hmAgentStpCstRegionalRootId,
       "hmAgentStpCstRegionalRootPathCost": hmAgentStpCstRegionalRootPathCost,
       "hmAgentStpCstRootFwdDelay": hmAgentStpCstRootFwdDelay,
       "hmAgentStpCstBridgeFwdDelay": hmAgentStpCstBridgeFwdDelay,
       "hmAgentStpCstBridgeHelloTime": hmAgentStpCstBridgeHelloTime,
       "hmAgentStpCstBridgeHoldTime": hmAgentStpCstBridgeHoldTime,
       "hmAgentStpCstBridgeMaxAge": hmAgentStpCstBridgeMaxAge,
       "hmAgentStpCstBridgeDesignatedRoot": hmAgentStpCstBridgeDesignatedRoot,
       "hmAgentStpCstBridgePriority": hmAgentStpCstBridgePriority,
       "hmAgentStpCstBridgeTimeSinceTopologyChange": hmAgentStpCstBridgeTimeSinceTopologyChange,
       "hmAgentStpCstBridgeTopChanges": hmAgentStpCstBridgeTopChanges,
       "hmAgentStpCstBridgeRootCost": hmAgentStpCstBridgeRootCost,
       "hmAgentStpCstBridgeRootPort": hmAgentStpCstBridgeRootPort,
       "hmAgentStpCstBridgeMaxHops": hmAgentStpCstBridgeMaxHops,
       "hmAgentStpCstBridgeHoldCount": hmAgentStpCstBridgeHoldCount,
       "hmAgentStpCstPortTable": hmAgentStpCstPortTable,
       "hmAgentStpCstPortEntry": hmAgentStpCstPortEntry,
       "hmAgentStpCstPortOperEdge": hmAgentStpCstPortOperEdge,
       "hmAgentStpCstPortOperPointToPoint": hmAgentStpCstPortOperPointToPoint,
       "hmAgentStpCstPortTopologyChangeAck": hmAgentStpCstPortTopologyChangeAck,
       "hmAgentStpCstPortEdge": hmAgentStpCstPortEdge,
       "hmAgentStpCstPortForwardingState": hmAgentStpCstPortForwardingState,
       "hmAgentStpCstPortId": hmAgentStpCstPortId,
       "hmAgentStpCstPortPathCost": hmAgentStpCstPortPathCost,
       "hmAgentStpCstPortPriority": hmAgentStpCstPortPriority,
       "hmAgentStpCstDesignatedBridgeId": hmAgentStpCstDesignatedBridgeId,
       "hmAgentStpCstDesignatedCost": hmAgentStpCstDesignatedCost,
       "hmAgentStpCstDesignatedPortId": hmAgentStpCstDesignatedPortId,
       "hmAgentStpCstExtPortPathCost": hmAgentStpCstExtPortPathCost,
       "hmAgentStpCstPortAutoEdge": hmAgentStpCstPortAutoEdge,
       "hmAgentStpCstPortRole": hmAgentStpCstPortRole,
       "hmAgentStpCstPortDisputed": hmAgentStpCstPortDisputed,
       "hmAgentStpCstPortBpduGuardEffect": hmAgentStpCstPortBpduGuardEffect,
       "hmAgentStpCstPortBpduFilter": hmAgentStpCstPortBpduFilter,
       "hmAgentStpCstPortBpduFlood": hmAgentStpCstPortBpduFlood,
       "hmAgentStpCstPortRootGuard": hmAgentStpCstPortRootGuard,
       "hmAgentStpCstPortTCNGuard": hmAgentStpCstPortTCNGuard,
       "hmAgentStpCstPortLoopGuard": hmAgentStpCstPortLoopGuard,
       "hmAgentStpMstTable": hmAgentStpMstTable,
       "hmAgentStpMstEntry": hmAgentStpMstEntry,
       "hmAgentStpMstId": hmAgentStpMstId,
       "hmAgentStpMstBridgePriority": hmAgentStpMstBridgePriority,
       "hmAgentStpMstBridgeIdentifier": hmAgentStpMstBridgeIdentifier,
       "hmAgentStpMstDesignatedRootId": hmAgentStpMstDesignatedRootId,
       "hmAgentStpMstRootPathCost": hmAgentStpMstRootPathCost,
       "hmAgentStpMstRootPortId": hmAgentStpMstRootPortId,
       "hmAgentStpMstTimeSinceTopologyChange": hmAgentStpMstTimeSinceTopologyChange,
       "hmAgentStpMstTopologyChangeCount": hmAgentStpMstTopologyChangeCount,
       "hmAgentStpMstTopologyChangeParm": hmAgentStpMstTopologyChangeParm,
       "hmAgentStpMstRowStatus": hmAgentStpMstRowStatus,
       "hmAgentStpMstPortTable": hmAgentStpMstPortTable,
       "hmAgentStpMstPortEntry": hmAgentStpMstPortEntry,
       "hmAgentStpMstPortForwardingState": hmAgentStpMstPortForwardingState,
       "hmAgentStpMstPortId": hmAgentStpMstPortId,
       "hmAgentStpMstPortPathCost": hmAgentStpMstPortPathCost,
       "hmAgentStpMstPortPriority": hmAgentStpMstPortPriority,
       "hmAgentStpMstDesignatedBridgeId": hmAgentStpMstDesignatedBridgeId,
       "hmAgentStpMstDesignatedCost": hmAgentStpMstDesignatedCost,
       "hmAgentStpMstDesignatedPortId": hmAgentStpMstDesignatedPortId,
       "hmAgentStpMstPortRole": hmAgentStpMstPortRole,
       "hmAgentStpMstPortDisputed": hmAgentStpMstPortDisputed,
       "hmAgentStpMstPortLoopInconsistentState": hmAgentStpMstPortLoopInconsistentState,
       "hmAgentStpMstPortTransitionsIntoLoopInconsistentState": hmAgentStpMstPortTransitionsIntoLoopInconsistentState,
       "hmAgentStpMstPortTransitionsOutOfLoopInconsistentState": hmAgentStpMstPortTransitionsOutOfLoopInconsistentState,
       "hmAgentStpMstReceivedBridgeId": hmAgentStpMstReceivedBridgeId,
       "hmAgentStpMstReceivedRPC": hmAgentStpMstReceivedRPC,
       "hmAgentStpMstReceivedPortId": hmAgentStpMstReceivedPortId,
       "hmAgentStpMstVlanTable": hmAgentStpMstVlanTable,
       "hmAgentStpMstVlanEntry": hmAgentStpMstVlanEntry,
       "hmAgentStpMstVlanRowStatus": hmAgentStpMstVlanRowStatus,
       "hmAgentStpBpduGuardMode": hmAgentStpBpduGuardMode,
       "hmAgentStpBpduFilterDefault": hmAgentStpBpduFilterDefault,
       "hmAgentClassOfServiceGroup": hmAgentClassOfServiceGroup,
       "hmAgentClassOfServicePortTable": hmAgentClassOfServicePortTable,
       "hmAgentClassOfServicePortEntry": hmAgentClassOfServicePortEntry,
       "hmAgentClassOfServicePortPriority": hmAgentClassOfServicePortPriority,
       "hmAgentClassOfServicePortClass": hmAgentClassOfServicePortClass,
       "hmAgentSystemGroup": hmAgentSystemGroup,
       "hmAgentSaveConfig": hmAgentSaveConfig,
       "hmAgentClearConfig": hmAgentClearConfig,
       "hmAgentClearLags": hmAgentClearLags,
       "hmAgentClearLoginSessions": hmAgentClearLoginSessions,
       "hmAgentClearPasswords": hmAgentClearPasswords,
       "hmAgentClearPortStats": hmAgentClearPortStats,
       "hmAgentClearSwitchStats": hmAgentClearSwitchStats,
       "hmAgentClearTrapLog": hmAgentClearTrapLog,
       "hmAgentClearVlan": hmAgentClearVlan,
       "hmAgentResetSystem": hmAgentResetSystem,
       "hmAgentSaveConfigStatus": hmAgentSaveConfigStatus,
       "hmAgentCableTesterGroup": hmAgentCableTesterGroup,
       "hmAgentCableTesterStatus": hmAgentCableTesterStatus,
       "hmAgentCableTesterIfIndex": hmAgentCableTesterIfIndex,
       "hmAgentCableTesterCableStatus": hmAgentCableTesterCableStatus,
       "hmAgentCableTesterMinimumCableLength": hmAgentCableTesterMinimumCableLength,
       "hmAgentCableTesterMaximumCableLength": hmAgentCableTesterMaximumCableLength,
       "hmAgentCableTesterCableFailureLocation": hmAgentCableTesterCableFailureLocation,
       "hmPlatform4SwitchingTraps": hmPlatform4SwitchingTraps,
       "multipleUsersTrap": multipleUsersTrap,
       "broadcastStormStartTrap": broadcastStormStartTrap,
       "broadcastStormEndTrap": broadcastStormEndTrap,
       "linkFailureTrap": linkFailureTrap,
       "vlanRequestFailureTrap": vlanRequestFailureTrap,
       "vlanDeleteLastTrap": vlanDeleteLastTrap,
       "vlanDefaultCfgFailureTrap": vlanDefaultCfgFailureTrap,
       "vlanRestoreFailureTrap": vlanRestoreFailureTrap,
       "fanFailureTrap": fanFailureTrap,
       "stpInstanceNewRootTrap": stpInstanceNewRootTrap,
       "stpInstanceTopologyChangeTrap": stpInstanceTopologyChangeTrap,
       "powerSupplyStatusChangeTrap": powerSupplyStatusChangeTrap,
       "failedUserLoginTrap": failedUserLoginTrap,
       "hmRadius": hmRadius,
       "hmAgentRadiusConfigGroup": hmAgentRadiusConfigGroup,
       "hmAgentRadiusMaxTransmit": hmAgentRadiusMaxTransmit,
       "hmAgentRadiusTimeout": hmAgentRadiusTimeout,
       "hmAgentRadiusAccountingMode": hmAgentRadiusAccountingMode,
       "hmAgentRadiusStatsClear": hmAgentRadiusStatsClear,
       "hmAgentRadiusAccountingIndexNextValid": hmAgentRadiusAccountingIndexNextValid,
       "hmAgentRadiusAccountingConfigTable": hmAgentRadiusAccountingConfigTable,
       "hmAgentRadiusAccountingConfigEntry": hmAgentRadiusAccountingConfigEntry,
       "hmAgentRadiusAccountingServerIndex": hmAgentRadiusAccountingServerIndex,
       "hmAgentRadiusAccountingServerAddress": hmAgentRadiusAccountingServerAddress,
       "hmAgentRadiusAccountingPort": hmAgentRadiusAccountingPort,
       "hmAgentRadiusAccountingSecret": hmAgentRadiusAccountingSecret,
       "hmAgentRadiusAccountingStatus": hmAgentRadiusAccountingStatus,
       "hmAgentRadiusServerIndexNextValid": hmAgentRadiusServerIndexNextValid,
       "hmAgentRadiusServerConfigTable": hmAgentRadiusServerConfigTable,
       "hmAgentRadiusServerConfigEntry": hmAgentRadiusServerConfigEntry,
       "hmAgentRadiusServerIndex": hmAgentRadiusServerIndex,
       "hmAgentRadiusServerAddress": hmAgentRadiusServerAddress,
       "hmAgentRadiusServerPort": hmAgentRadiusServerPort,
       "hmAgentRadiusServerSecret": hmAgentRadiusServerSecret,
       "hmAgentRadiusServerPrimaryMode": hmAgentRadiusServerPrimaryMode,
       "hmAgentRadiusServerCurrentMode": hmAgentRadiusServerCurrentMode,
       "hmAgentRadiusServerMsgAuth": hmAgentRadiusServerMsgAuth,
       "hmAgentRadiusServerStatus": hmAgentRadiusServerStatus,
       "hmAgentMgmtSecurity": hmAgentMgmtSecurity,
       "hmAgentSSHConfigGroup": hmAgentSSHConfigGroup,
       "hmAgentSSHAdminMode": hmAgentSSHAdminMode,
       "hmAgentSSHProtocolLevel": hmAgentSSHProtocolLevel,
       "hmAgentSSHSessionsCount": hmAgentSSHSessionsCount,
       "hmAgentSSHMaxSessionsCount": hmAgentSSHMaxSessionsCount,
       "hmAgentSSHSessionTimeout": hmAgentSSHSessionTimeout,
       "hmAgentLogging": hmAgentLogging,
       "hmAgentLogConfigGroup": hmAgentLogConfigGroup,
       "hmAgentLogSysLogConfigGroup": hmAgentLogSysLogConfigGroup,
       "hmAgentLogSyslogAdminStatus": hmAgentLogSyslogAdminStatus,
       "hmAgentLogSyslogHostTable": hmAgentLogSyslogHostTable,
       "hmAgentLogSyslogHostEntry": hmAgentLogSyslogHostEntry,
       "hmAgentLogHostTableIndex": hmAgentLogHostTableIndex,
       "hmAgentLogHostTableIpAddress": hmAgentLogHostTableIpAddress,
       "hmAgentLogHostTablePort": hmAgentLogHostTablePort,
       "hmAgentLogHostTableSeverityFilter": hmAgentLogHostTableSeverityFilter,
       "hmAgentLogHostTableRowStatus": hmAgentLogHostTableRowStatus,
       "hmPlatform4OutboundTelnetPrivate": hmPlatform4OutboundTelnetPrivate,
       "hmAgentOutboundTelnetGroup": hmAgentOutboundTelnetGroup,
       "hmAgentOutboundTelnetAdminMode": hmAgentOutboundTelnetAdminMode,
       "hmAgentOutboundTelnetMaxNoOfSessions": hmAgentOutboundTelnetMaxNoOfSessions,
       "hmAgentOutboundTelnetTimeout": hmAgentOutboundTelnetTimeout,
       "hmAgentDot1xAdvanced": hmAgentDot1xAdvanced,
       "hmAgentDot1xEnhancementConfigGroup": hmAgentDot1xEnhancementConfigGroup,
       "hmAgentDot1xRadiusVlanAssignment": hmAgentDot1xRadiusVlanAssignment,
       "hmAgentDot1xDynamicVlanCreationMode": hmAgentDot1xDynamicVlanCreationMode,
       "hmAgentDot1xSafeVlanMode": hmAgentDot1xSafeVlanMode,
       "hmAgentDot1xPortConfigGroup": hmAgentDot1xPortConfigGroup,
       "hmAgentDot1xPortConfigTable": hmAgentDot1xPortConfigTable,
       "hmAgentDot1xPortConfigEntry": hmAgentDot1xPortConfigEntry,
       "hmAgentDot1xPortControlMode": hmAgentDot1xPortControlMode,
       "hmAgentDot1xGuestVlanId": hmAgentDot1xGuestVlanId,
       "hmAgentDot1xGuestVlanPeriod": hmAgentDot1xGuestVlanPeriod,
       "hmAgentDot1xUnauthenticatedVlan": hmAgentDot1xUnauthenticatedVlan,
       "hmAgentDot1xMaxUsers": hmAgentDot1xMaxUsers,
       "hmAgentDot1xPortVlanAssigned": hmAgentDot1xPortVlanAssigned,
       "hmAgentDot1xPortVlanAssignedReason": hmAgentDot1xPortVlanAssignedReason,
       "hmAgentDot1xPortSessionTimeout": hmAgentDot1xPortSessionTimeout,
       "hmAgentDot1xPortTerminationAction": hmAgentDot1xPortTerminationAction,
       "hmAgentDot1xPortMABenabled": hmAgentDot1xPortMABenabled,
       "hmAgentDot1xPortMABenabledOperational": hmAgentDot1xPortMABenabledOperational,
       "hmAgentDot1xClientConfigGroup": hmAgentDot1xClientConfigGroup,
       "hmAgentDot1xClientConfigTable": hmAgentDot1xClientConfigTable,
       "hmAgentDot1xClientConfigEntry": hmAgentDot1xClientConfigEntry,
       "hmAgentDot1xClientMacAddress": hmAgentDot1xClientMacAddress,
       "hmAgentDot1xLogicalPort": hmAgentDot1xLogicalPort,
       "hmAgentDot1xInterface": hmAgentDot1xInterface,
       "hmAgentDot1xClientAuthPAEstate": hmAgentDot1xClientAuthPAEstate,
       "hmAgentDot1xClientBackendState": hmAgentDot1xClientBackendState,
       "hmAgentDot1xClientUserName": hmAgentDot1xClientUserName,
       "hmAgentDot1xClientSessionTime": hmAgentDot1xClientSessionTime,
       "hmAgentDot1xClientFilterID": hmAgentDot1xClientFilterID,
       "hmAgentDot1xClientVlanAssigned": hmAgentDot1xClientVlanAssigned,
       "hmAgentDot1xClientVlanAssignedReason": hmAgentDot1xClientVlanAssignedReason,
       "hmAgentDot1xClientSessionTimeout": hmAgentDot1xClientSessionTimeout,
       "hmAgentDot1xClientTerminationAction": hmAgentDot1xClientTerminationAction,
       "dot1xTraps": dot1xTraps,
       "dot1xPortStatusAuthorized": dot1xPortStatusAuthorized,
       "dot1xPortStatusUnauthorized": dot1xPortStatusUnauthorized}
)
