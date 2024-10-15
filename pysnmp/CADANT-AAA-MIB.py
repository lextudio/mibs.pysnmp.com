# SNMP MIB module (CADANT-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-AAA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:21 2024
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

(cadAuthentication,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadAuthentication")

(AAAmethod,
 AccountingType,
 InetAddressIPv4or6,
 LineType,
 SshAuthMethod,
 SshCipher,
 SshCipherType,
 SshKeyExchangeMethod,
 SshKeyType,
 SshMacAlg,
 SshProtocol,
 SshService) = mibBuilder.importSymbols(
    "CADANT-TC",
    "AAAmethod",
    "AccountingType",
    "InetAddressIPv4or6",
    "LineType",
    "SshAuthMethod",
    "SshCipher",
    "SshCipherType",
    "SshKeyExchangeMethod",
    "SshKeyType",
    "SshMacAlg",
    "SshProtocol",
    "SshService")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cadAAA = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1)
)
cadAAA.setRevisions(
        ("2015-09-30 00:00",
         "2015-08-20 00:00",
         "2015-07-16 00:00",
         "2013-10-22 00:00",
         "2009-10-09 00:00",
         "2005-09-23 00:00",
         "2005-06-09 00:00",
         "2004-11-30 00:00",
         "2004-08-27 00:00",
         "2004-08-19 00:00",
         "2004-07-20 00:00",
         "2004-02-24 00:00",
         "2004-02-18 00:00",
         "2003-08-22 00:00",
         "2003-08-20 00:00",
         "2003-08-15 00:00",
         "2003-08-01 00:00",
         "2003-07-16 00:00",
         "2003-06-13 00:00",
         "2003-05-15 00:00",
         "2003-05-08 00:00",
         "2003-05-07 00:00",
         "2003-04-01 00:00",
         "2003-03-14 00:00",
         "2002-10-16 00:00",
         "2002-08-30 00:00",
         "2002-08-21 00:00",
         "2002-07-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PemKey(OctetString, TextualConvention):
    status = "current"
    displayHint = "2800a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2800),
    )



class CmdNode(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



# MIB Managed Objects in the order of their OIDs

_CadLineTable_Object = MibTable
cadLineTable = _CadLineTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 2)
)
if mibBuilder.loadTexts:
    cadLineTable.setStatus("current")
_CadLineEntry_Object = MibTableRow
cadLineEntry = _CadLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 2, 1)
)
cadLineEntry.setIndexNames(
    (0, "CADANT-AAA-MIB", "cadLineIndex"),
)
if mibBuilder.loadTexts:
    cadLineEntry.setStatus("current")


class _CadLineIndex_Type(Integer32):
    """Custom type cadLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_CadLineIndex_Type.__name__ = "Integer32"
_CadLineIndex_Object = MibTableColumn
cadLineIndex = _CadLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 2, 1, 1),
    _CadLineIndex_Type()
)
cadLineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadLineIndex.setStatus("current")


class _CadLineType_Type(LineType):
    """Custom type cadLineType based on LineType"""


_CadLineType_Object = MibTableColumn
cadLineType = _CadLineType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 2, 1, 2),
    _CadLineType_Type()
)
cadLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLineType.setStatus("current")


class _CadLineEnabled_Type(TruthValue):
    """Custom type cadLineEnabled based on TruthValue"""


_CadLineEnabled_Object = MibTableColumn
cadLineEnabled = _CadLineEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 2, 1, 3),
    _CadLineEnabled_Type()
)
cadLineEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLineEnabled.setStatus("current")


class _CadLineSessionTimeout_Type(Integer32):
    """Custom type cadLineSessionTimeout based on Integer32"""
    defaultValue = 0


_CadLineSessionTimeout_Object = MibTableColumn
cadLineSessionTimeout = _CadLineSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 2, 1, 4),
    _CadLineSessionTimeout_Type()
)
cadLineSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLineSessionTimeout.setStatus("current")


class _CadLineIdleTimeout_Type(Integer32):
    """Custom type cadLineIdleTimeout based on Integer32"""
    defaultValue = 0


_CadLineIdleTimeout_Object = MibTableColumn
cadLineIdleTimeout = _CadLineIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 2, 1, 5),
    _CadLineIdleTimeout_Type()
)
cadLineIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLineIdleTimeout.setStatus("current")


class _CadLinePagination_Type(Integer32):
    """Custom type cadLinePagination based on Integer32"""
    defaultValue = 0


_CadLinePagination_Object = MibTableColumn
cadLinePagination = _CadLinePagination_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 2, 1, 6),
    _CadLinePagination_Type()
)
cadLinePagination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLinePagination.setStatus("current")


class _CadLineBaud_Type(Integer32):
    """Custom type cadLineBaud based on Integer32"""
    defaultValue = 9600


_CadLineBaud_Object = MibTableColumn
cadLineBaud = _CadLineBaud_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 2, 1, 7),
    _CadLineBaud_Type()
)
cadLineBaud.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLineBaud.setStatus("current")


class _CadLinePassword_Type(OctetString):
    """Custom type cadLinePassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CadLinePassword_Type.__name__ = "OctetString"
_CadLinePassword_Object = MibTableColumn
cadLinePassword = _CadLinePassword_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 2, 1, 8),
    _CadLinePassword_Type()
)
cadLinePassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLinePassword.setStatus("current")


class _CadLineLoginAuthMethodList_Type(SnmpAdminString):
    """Custom type cadLineLoginAuthMethodList based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CadLineLoginAuthMethodList_Type.__name__ = "SnmpAdminString"
_CadLineLoginAuthMethodList_Object = MibTableColumn
cadLineLoginAuthMethodList = _CadLineLoginAuthMethodList_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 2, 1, 9),
    _CadLineLoginAuthMethodList_Type()
)
cadLineLoginAuthMethodList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLineLoginAuthMethodList.setStatus("current")


class _CadLineEnableAuthMethodList_Type(SnmpAdminString):
    """Custom type cadLineEnableAuthMethodList based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CadLineEnableAuthMethodList_Type.__name__ = "SnmpAdminString"
_CadLineEnableAuthMethodList_Object = MibTableColumn
cadLineEnableAuthMethodList = _CadLineEnableAuthMethodList_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 2, 1, 10),
    _CadLineEnableAuthMethodList_Type()
)
cadLineEnableAuthMethodList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLineEnableAuthMethodList.setStatus("current")


class _CadLineAuthorMethodList_Type(SnmpAdminString):
    """Custom type cadLineAuthorMethodList based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CadLineAuthorMethodList_Type.__name__ = "SnmpAdminString"
_CadLineAuthorMethodList_Object = MibTableColumn
cadLineAuthorMethodList = _CadLineAuthorMethodList_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 2, 1, 11),
    _CadLineAuthorMethodList_Type()
)
cadLineAuthorMethodList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLineAuthorMethodList.setStatus("current")


class _CadLineShellAccountingMethodList_Type(SnmpAdminString):
    """Custom type cadLineShellAccountingMethodList based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CadLineShellAccountingMethodList_Type.__name__ = "SnmpAdminString"
_CadLineShellAccountingMethodList_Object = MibTableColumn
cadLineShellAccountingMethodList = _CadLineShellAccountingMethodList_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 2, 1, 12),
    _CadLineShellAccountingMethodList_Type()
)
cadLineShellAccountingMethodList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLineShellAccountingMethodList.setStatus("current")


class _CadLineCommandAccountingMethodList_Type(SnmpAdminString):
    """Custom type cadLineCommandAccountingMethodList based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CadLineCommandAccountingMethodList_Type.__name__ = "SnmpAdminString"
_CadLineCommandAccountingMethodList_Object = MibTableColumn
cadLineCommandAccountingMethodList = _CadLineCommandAccountingMethodList_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 2, 1, 13),
    _CadLineCommandAccountingMethodList_Type()
)
cadLineCommandAccountingMethodList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLineCommandAccountingMethodList.setStatus("current")


class _CadLineShellAccountingType_Type(AccountingType):
    """Custom type cadLineShellAccountingType based on AccountingType"""


_CadLineShellAccountingType_Object = MibTableColumn
cadLineShellAccountingType = _CadLineShellAccountingType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 2, 1, 14),
    _CadLineShellAccountingType_Type()
)
cadLineShellAccountingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLineShellAccountingType.setStatus("current")


class _CadLineCommandAccountingType_Type(AccountingType):
    """Custom type cadLineCommandAccountingType based on AccountingType"""


_CadLineCommandAccountingType_Object = MibTableColumn
cadLineCommandAccountingType = _CadLineCommandAccountingType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 2, 1, 15),
    _CadLineCommandAccountingType_Type()
)
cadLineCommandAccountingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLineCommandAccountingType.setStatus("current")


class _CadLineCommandAccountingPrivilegeLevel_Type(Integer32):
    """Custom type cadLineCommandAccountingPrivilegeLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CadLineCommandAccountingPrivilegeLevel_Type.__name__ = "Integer32"
_CadLineCommandAccountingPrivilegeLevel_Object = MibTableColumn
cadLineCommandAccountingPrivilegeLevel = _CadLineCommandAccountingPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 2, 1, 16),
    _CadLineCommandAccountingPrivilegeLevel_Type()
)
cadLineCommandAccountingPrivilegeLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLineCommandAccountingPrivilegeLevel.setStatus("current")
_CadAuthorizationMethodTable_Object = MibTable
cadAuthorizationMethodTable = _CadAuthorizationMethodTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 3)
)
if mibBuilder.loadTexts:
    cadAuthorizationMethodTable.setStatus("current")
_CadAuthorizationMethodEntry_Object = MibTableRow
cadAuthorizationMethodEntry = _CadAuthorizationMethodEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 3, 1)
)
cadAuthorizationMethodEntry.setIndexNames(
    (0, "CADANT-AAA-MIB", "cadAuthorizationListName"),
    (0, "CADANT-AAA-MIB", "cadAuthorizationListIndex"),
)
if mibBuilder.loadTexts:
    cadAuthorizationMethodEntry.setStatus("current")


class _CadAuthorizationListName_Type(SnmpAdminString):
    """Custom type cadAuthorizationListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CadAuthorizationListName_Type.__name__ = "SnmpAdminString"
_CadAuthorizationListName_Object = MibTableColumn
cadAuthorizationListName = _CadAuthorizationListName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 3, 1, 1),
    _CadAuthorizationListName_Type()
)
cadAuthorizationListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadAuthorizationListName.setStatus("current")


class _CadAuthorizationListIndex_Type(Integer32):
    """Custom type cadAuthorizationListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32),
    )


_CadAuthorizationListIndex_Type.__name__ = "Integer32"
_CadAuthorizationListIndex_Object = MibTableColumn
cadAuthorizationListIndex = _CadAuthorizationListIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 3, 1, 2),
    _CadAuthorizationListIndex_Type()
)
cadAuthorizationListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadAuthorizationListIndex.setStatus("current")
_CadAuthorizationType_Type = AAAmethod
_CadAuthorizationType_Object = MibTableColumn
cadAuthorizationType = _CadAuthorizationType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 3, 1, 3),
    _CadAuthorizationType_Type()
)
cadAuthorizationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadAuthorizationType.setStatus("current")


class _CadAuthorizationGroup_Type(SnmpAdminString):
    """Custom type cadAuthorizationGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CadAuthorizationGroup_Type.__name__ = "SnmpAdminString"
_CadAuthorizationGroup_Object = MibTableColumn
cadAuthorizationGroup = _CadAuthorizationGroup_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 3, 1, 4),
    _CadAuthorizationGroup_Type()
)
cadAuthorizationGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadAuthorizationGroup.setStatus("current")
_CadAuthorizationRowStatus_Type = RowStatus
_CadAuthorizationRowStatus_Object = MibTableColumn
cadAuthorizationRowStatus = _CadAuthorizationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 3, 1, 5),
    _CadAuthorizationRowStatus_Type()
)
cadAuthorizationRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadAuthorizationRowStatus.setStatus("current")
_CadAuthMethodTable_Object = MibTable
cadAuthMethodTable = _CadAuthMethodTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 4)
)
if mibBuilder.loadTexts:
    cadAuthMethodTable.setStatus("current")
_CadAuthMethodEntry_Object = MibTableRow
cadAuthMethodEntry = _CadAuthMethodEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 4, 1)
)
cadAuthMethodEntry.setIndexNames(
    (0, "CADANT-AAA-MIB", "cadAuthListName"),
    (0, "CADANT-AAA-MIB", "cadAuthListIndex"),
)
if mibBuilder.loadTexts:
    cadAuthMethodEntry.setStatus("current")


class _CadAuthListName_Type(SnmpAdminString):
    """Custom type cadAuthListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CadAuthListName_Type.__name__ = "SnmpAdminString"
_CadAuthListName_Object = MibTableColumn
cadAuthListName = _CadAuthListName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 4, 1, 1),
    _CadAuthListName_Type()
)
cadAuthListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadAuthListName.setStatus("current")


class _CadAuthListIndex_Type(Integer32):
    """Custom type cadAuthListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32),
    )


_CadAuthListIndex_Type.__name__ = "Integer32"
_CadAuthListIndex_Object = MibTableColumn
cadAuthListIndex = _CadAuthListIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 4, 1, 2),
    _CadAuthListIndex_Type()
)
cadAuthListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadAuthListIndex.setStatus("current")
_CadAuthType_Type = AAAmethod
_CadAuthType_Object = MibTableColumn
cadAuthType = _CadAuthType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 4, 1, 3),
    _CadAuthType_Type()
)
cadAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadAuthType.setStatus("current")


class _CadAuthGroup_Type(SnmpAdminString):
    """Custom type cadAuthGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CadAuthGroup_Type.__name__ = "SnmpAdminString"
_CadAuthGroup_Object = MibTableColumn
cadAuthGroup = _CadAuthGroup_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 4, 1, 4),
    _CadAuthGroup_Type()
)
cadAuthGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadAuthGroup.setStatus("current")
_CadAuthRowStatus_Type = RowStatus
_CadAuthRowStatus_Object = MibTableColumn
cadAuthRowStatus = _CadAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 4, 1, 5),
    _CadAuthRowStatus_Type()
)
cadAuthRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadAuthRowStatus.setStatus("current")
_CadAccountingMethodTable_Object = MibTable
cadAccountingMethodTable = _CadAccountingMethodTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 5)
)
if mibBuilder.loadTexts:
    cadAccountingMethodTable.setStatus("current")
_CadAccountingMethodEntry_Object = MibTableRow
cadAccountingMethodEntry = _CadAccountingMethodEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 5, 1)
)
cadAccountingMethodEntry.setIndexNames(
    (0, "CADANT-AAA-MIB", "cadAccountingListName"),
    (0, "CADANT-AAA-MIB", "cadAccountingListIndex"),
)
if mibBuilder.loadTexts:
    cadAccountingMethodEntry.setStatus("current")


class _CadAccountingListName_Type(SnmpAdminString):
    """Custom type cadAccountingListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CadAccountingListName_Type.__name__ = "SnmpAdminString"
_CadAccountingListName_Object = MibTableColumn
cadAccountingListName = _CadAccountingListName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 5, 1, 1),
    _CadAccountingListName_Type()
)
cadAccountingListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadAccountingListName.setStatus("current")


class _CadAccountingListIndex_Type(Integer32):
    """Custom type cadAccountingListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32),
    )


_CadAccountingListIndex_Type.__name__ = "Integer32"
_CadAccountingListIndex_Object = MibTableColumn
cadAccountingListIndex = _CadAccountingListIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 5, 1, 2),
    _CadAccountingListIndex_Type()
)
cadAccountingListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadAccountingListIndex.setStatus("current")
_CadAccountingType_Type = AAAmethod
_CadAccountingType_Object = MibTableColumn
cadAccountingType = _CadAccountingType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 5, 1, 3),
    _CadAccountingType_Type()
)
cadAccountingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadAccountingType.setStatus("current")


class _CadAccountingGroup_Type(SnmpAdminString):
    """Custom type cadAccountingGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CadAccountingGroup_Type.__name__ = "SnmpAdminString"
_CadAccountingGroup_Object = MibTableColumn
cadAccountingGroup = _CadAccountingGroup_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 5, 1, 4),
    _CadAccountingGroup_Type()
)
cadAccountingGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadAccountingGroup.setStatus("current")
_CadAccountingRowStatus_Type = RowStatus
_CadAccountingRowStatus_Object = MibTableColumn
cadAccountingRowStatus = _CadAccountingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 5, 1, 5),
    _CadAccountingRowStatus_Type()
)
cadAccountingRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadAccountingRowStatus.setStatus("current")
_CadServerGroupTable_Object = MibTable
cadServerGroupTable = _CadServerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 6)
)
if mibBuilder.loadTexts:
    cadServerGroupTable.setStatus("current")
_CadServerGroupEntry_Object = MibTableRow
cadServerGroupEntry = _CadServerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 6, 1)
)
cadServerGroupEntry.setIndexNames(
    (0, "CADANT-AAA-MIB", "cadGroupName"),
    (0, "CADANT-AAA-MIB", "cadGroupIndex"),
)
if mibBuilder.loadTexts:
    cadServerGroupEntry.setStatus("current")


class _CadGroupName_Type(SnmpAdminString):
    """Custom type cadGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CadGroupName_Type.__name__ = "SnmpAdminString"
_CadGroupName_Object = MibTableColumn
cadGroupName = _CadGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 6, 1, 1),
    _CadGroupName_Type()
)
cadGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadGroupName.setStatus("current")


class _CadGroupIndex_Type(Integer32):
    """Custom type cadGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32),
    )


_CadGroupIndex_Type.__name__ = "Integer32"
_CadGroupIndex_Object = MibTableColumn
cadGroupIndex = _CadGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 6, 1, 2),
    _CadGroupIndex_Type()
)
cadGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadGroupIndex.setStatus("current")


class _CadGroupType_Type(Integer32):
    """Custom type cadGroupType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("radius", 1),
          ("tacacs", 2))
    )


_CadGroupType_Type.__name__ = "Integer32"
_CadGroupType_Object = MibTableColumn
cadGroupType = _CadGroupType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 6, 1, 3),
    _CadGroupType_Type()
)
cadGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadGroupType.setStatus("current")
_CadGroupIpAddress_Type = InetAddressIPv4or6
_CadGroupIpAddress_Object = MibTableColumn
cadGroupIpAddress = _CadGroupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 6, 1, 4),
    _CadGroupIpAddress_Type()
)
cadGroupIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadGroupIpAddress.setStatus("current")
_CadGroupPort_Type = Integer32
_CadGroupPort_Object = MibTableColumn
cadGroupPort = _CadGroupPort_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 6, 1, 5),
    _CadGroupPort_Type()
)
cadGroupPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadGroupPort.setStatus("current")
_CadGroupRowStatus_Type = RowStatus
_CadGroupRowStatus_Object = MibTableColumn
cadGroupRowStatus = _CadGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 6, 1, 6),
    _CadGroupRowStatus_Type()
)
cadGroupRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadGroupRowStatus.setStatus("current")
_CadRadiusTable_Object = MibTable
cadRadiusTable = _CadRadiusTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 7)
)
if mibBuilder.loadTexts:
    cadRadiusTable.setStatus("current")
_CadRadiusEntry_Object = MibTableRow
cadRadiusEntry = _CadRadiusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 7, 1)
)
cadRadiusEntry.setIndexNames(
    (0, "CADANT-AAA-MIB", "cadRadiusIpAddress"),
)
if mibBuilder.loadTexts:
    cadRadiusEntry.setStatus("current")
_CadRadiusIpAddress_Type = InetAddressIPv4or6
_CadRadiusIpAddress_Object = MibTableColumn
cadRadiusIpAddress = _CadRadiusIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 7, 1, 1),
    _CadRadiusIpAddress_Type()
)
cadRadiusIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadRadiusIpAddress.setStatus("current")


class _CadRadiusAuthPort_Type(Integer32):
    """Custom type cadRadiusAuthPort based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadRadiusAuthPort_Type.__name__ = "Integer32"
_CadRadiusAuthPort_Object = MibTableColumn
cadRadiusAuthPort = _CadRadiusAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 7, 1, 2),
    _CadRadiusAuthPort_Type()
)
cadRadiusAuthPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadRadiusAuthPort.setStatus("current")


class _CadRadiusAcctPort_Type(Integer32):
    """Custom type cadRadiusAcctPort based on Integer32"""
    defaultValue = 1813

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadRadiusAcctPort_Type.__name__ = "Integer32"
_CadRadiusAcctPort_Object = MibTableColumn
cadRadiusAcctPort = _CadRadiusAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 7, 1, 3),
    _CadRadiusAcctPort_Type()
)
cadRadiusAcctPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadRadiusAcctPort.setStatus("current")


class _CadRadiusTimeout_Type(Integer32):
    """Custom type cadRadiusTimeout based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_CadRadiusTimeout_Type.__name__ = "Integer32"
_CadRadiusTimeout_Object = MibTableColumn
cadRadiusTimeout = _CadRadiusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 7, 1, 4),
    _CadRadiusTimeout_Type()
)
cadRadiusTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadRadiusTimeout.setStatus("current")


class _CadRadiusRetrans_Type(Integer32):
    """Custom type cadRadiusRetrans based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CadRadiusRetrans_Type.__name__ = "Integer32"
_CadRadiusRetrans_Object = MibTableColumn
cadRadiusRetrans = _CadRadiusRetrans_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 7, 1, 5),
    _CadRadiusRetrans_Type()
)
cadRadiusRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadRadiusRetrans.setStatus("current")


class _CadRadiusKey_Type(OctetString):
    """Custom type cadRadiusKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CadRadiusKey_Type.__name__ = "OctetString"
_CadRadiusKey_Object = MibTableColumn
cadRadiusKey = _CadRadiusKey_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 7, 1, 7),
    _CadRadiusKey_Type()
)
cadRadiusKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadRadiusKey.setStatus("current")


class _CadRadiusAuthServerIndex_Type(Integer32):
    """Custom type cadRadiusAuthServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CadRadiusAuthServerIndex_Type.__name__ = "Integer32"
_CadRadiusAuthServerIndex_Object = MibTableColumn
cadRadiusAuthServerIndex = _CadRadiusAuthServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 7, 1, 8),
    _CadRadiusAuthServerIndex_Type()
)
cadRadiusAuthServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadRadiusAuthServerIndex.setStatus("current")
_CadRadiusRowStatus_Type = RowStatus
_CadRadiusRowStatus_Object = MibTableColumn
cadRadiusRowStatus = _CadRadiusRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 7, 1, 9),
    _CadRadiusRowStatus_Type()
)
cadRadiusRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadRadiusRowStatus.setStatus("current")
_CadTacacsTable_Object = MibTable
cadTacacsTable = _CadTacacsTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 8)
)
if mibBuilder.loadTexts:
    cadTacacsTable.setStatus("current")
_CadTacacsEntry_Object = MibTableRow
cadTacacsEntry = _CadTacacsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 8, 1)
)
cadTacacsEntry.setIndexNames(
    (0, "CADANT-AAA-MIB", "cadTacacsIpAddress"),
)
if mibBuilder.loadTexts:
    cadTacacsEntry.setStatus("current")
_CadTacacsIpAddress_Type = InetAddressIPv4or6
_CadTacacsIpAddress_Object = MibTableColumn
cadTacacsIpAddress = _CadTacacsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 8, 1, 1),
    _CadTacacsIpAddress_Type()
)
cadTacacsIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadTacacsIpAddress.setStatus("current")


class _CadTacacsPort_Type(Integer32):
    """Custom type cadTacacsPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadTacacsPort_Type.__name__ = "Integer32"
_CadTacacsPort_Object = MibTableColumn
cadTacacsPort = _CadTacacsPort_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 8, 1, 2),
    _CadTacacsPort_Type()
)
cadTacacsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadTacacsPort.setStatus("current")


class _CadTacacsTimeout_Type(Integer32):
    """Custom type cadTacacsTimeout based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_CadTacacsTimeout_Type.__name__ = "Integer32"
_CadTacacsTimeout_Object = MibTableColumn
cadTacacsTimeout = _CadTacacsTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 8, 1, 3),
    _CadTacacsTimeout_Type()
)
cadTacacsTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadTacacsTimeout.setStatus("current")


class _CadTacacsKey_Type(OctetString):
    """Custom type cadTacacsKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CadTacacsKey_Type.__name__ = "OctetString"
_CadTacacsKey_Object = MibTableColumn
cadTacacsKey = _CadTacacsKey_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 8, 1, 4),
    _CadTacacsKey_Type()
)
cadTacacsKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadTacacsKey.setStatus("current")


class _CadTacacsSingleConnect_Type(TruthValue):
    """Custom type cadTacacsSingleConnect based on TruthValue"""


_CadTacacsSingleConnect_Object = MibTableColumn
cadTacacsSingleConnect = _CadTacacsSingleConnect_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 8, 1, 5),
    _CadTacacsSingleConnect_Type()
)
cadTacacsSingleConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadTacacsSingleConnect.setStatus("current")


class _CadTacacsServerIndex_Type(Integer32):
    """Custom type cadTacacsServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CadTacacsServerIndex_Type.__name__ = "Integer32"
_CadTacacsServerIndex_Object = MibTableColumn
cadTacacsServerIndex = _CadTacacsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 8, 1, 6),
    _CadTacacsServerIndex_Type()
)
cadTacacsServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadTacacsServerIndex.setStatus("current")
_CadTacacsRowStatus_Type = RowStatus
_CadTacacsRowStatus_Object = MibTableColumn
cadTacacsRowStatus = _CadTacacsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 8, 1, 7),
    _CadTacacsRowStatus_Type()
)
cadTacacsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadTacacsRowStatus.setStatus("current")
_CadSshConfig_ObjectIdentity = ObjectIdentity
cadSshConfig = _CadSshConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 9)
)


class _CadSshEnabled_Type(TruthValue):
    """Custom type cadSshEnabled based on TruthValue"""


_CadSshEnabled_Object = MibScalar
cadSshEnabled = _CadSshEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 9, 1),
    _CadSshEnabled_Type()
)
cadSshEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSshEnabled.setStatus("current")


class _CadSshPort_Type(Integer32):
    """Custom type cadSshPort based on Integer32"""
    defaultValue = 22

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CadSshPort_Type.__name__ = "Integer32"
_CadSshPort_Object = MibScalar
cadSshPort = _CadSshPort_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 9, 2),
    _CadSshPort_Type()
)
cadSshPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSshPort.setStatus("current")


class _CadSshSessionIdleTimeout_Type(Integer32):
    """Custom type cadSshSessionIdleTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12000),
    )


_CadSshSessionIdleTimeout_Type.__name__ = "Integer32"
_CadSshSessionIdleTimeout_Object = MibScalar
cadSshSessionIdleTimeout = _CadSshSessionIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 9, 3),
    _CadSshSessionIdleTimeout_Type()
)
cadSshSessionIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSshSessionIdleTimeout.setStatus("current")


class _CadSshMaxClients_Type(Integer32):
    """Custom type cadSshMaxClients based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_CadSshMaxClients_Type.__name__ = "Integer32"
_CadSshMaxClients_Object = MibScalar
cadSshMaxClients = _CadSshMaxClients_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 9, 4),
    _CadSshMaxClients_Type()
)
cadSshMaxClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSshMaxClients.setStatus("current")


class _CadSshPasswordAuthEnabled_Type(TruthValue):
    """Custom type cadSshPasswordAuthEnabled based on TruthValue"""


_CadSshPasswordAuthEnabled_Object = MibScalar
cadSshPasswordAuthEnabled = _CadSshPasswordAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 9, 5),
    _CadSshPasswordAuthEnabled_Type()
)
cadSshPasswordAuthEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSshPasswordAuthEnabled.setStatus("current")


class _CadSshPublicKeyAuthEnabled_Type(TruthValue):
    """Custom type cadSshPublicKeyAuthEnabled based on TruthValue"""


_CadSshPublicKeyAuthEnabled_Object = MibScalar
cadSshPublicKeyAuthEnabled = _CadSshPublicKeyAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 9, 6),
    _CadSshPublicKeyAuthEnabled_Type()
)
cadSshPublicKeyAuthEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSshPublicKeyAuthEnabled.setStatus("current")


class _CadSshCliLoginEnabled_Type(TruthValue):
    """Custom type cadSshCliLoginEnabled based on TruthValue"""


_CadSshCliLoginEnabled_Object = MibScalar
cadSshCliLoginEnabled = _CadSshCliLoginEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 9, 7),
    _CadSshCliLoginEnabled_Type()
)
cadSshCliLoginEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSshCliLoginEnabled.setStatus("current")


class _CadSshSecureFtpEnabled_Type(TruthValue):
    """Custom type cadSshSecureFtpEnabled based on TruthValue"""


_CadSshSecureFtpEnabled_Object = MibScalar
cadSshSecureFtpEnabled = _CadSshSecureFtpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 9, 8),
    _CadSshSecureFtpEnabled_Type()
)
cadSshSecureFtpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSshSecureFtpEnabled.setStatus("current")
_CadSshPublicKey_Type = PemKey
_CadSshPublicKey_Object = MibScalar
cadSshPublicKey = _CadSshPublicKey_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 9, 11),
    _CadSshPublicKey_Type()
)
cadSshPublicKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSshPublicKey.setStatus("current")
_CadSshPrivateKey_Type = PemKey
_CadSshPrivateKey_Object = MibScalar
cadSshPrivateKey = _CadSshPrivateKey_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 9, 12),
    _CadSshPrivateKey_Type()
)
cadSshPrivateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSshPrivateKey.setStatus("current")


class _CadSshCiphers_Type(SshCipher):
    """Custom type cadSshCiphers based on SshCipher"""
    defaultHexValue = "7C"


_CadSshCiphers_Object = MibScalar
cadSshCiphers = _CadSshCiphers_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 9, 13),
    _CadSshCiphers_Type()
)
cadSshCiphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSshCiphers.setStatus("current")


class _CadSshPortForwardingEnabled_Type(TruthValue):
    """Custom type cadSshPortForwardingEnabled based on TruthValue"""


_CadSshPortForwardingEnabled_Object = MibScalar
cadSshPortForwardingEnabled = _CadSshPortForwardingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 9, 14),
    _CadSshPortForwardingEnabled_Type()
)
cadSshPortForwardingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSshPortForwardingEnabled.setStatus("current")


class _CadSshPasswordAuthRequired_Type(TruthValue):
    """Custom type cadSshPasswordAuthRequired based on TruthValue"""


_CadSshPasswordAuthRequired_Object = MibScalar
cadSshPasswordAuthRequired = _CadSshPasswordAuthRequired_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 9, 15),
    _CadSshPasswordAuthRequired_Type()
)
cadSshPasswordAuthRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSshPasswordAuthRequired.setStatus("current")


class _CadSshPublicKeyAuthRequired_Type(TruthValue):
    """Custom type cadSshPublicKeyAuthRequired based on TruthValue"""


_CadSshPublicKeyAuthRequired_Object = MibScalar
cadSshPublicKeyAuthRequired = _CadSshPublicKeyAuthRequired_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 9, 16),
    _CadSshPublicKeyAuthRequired_Type()
)
cadSshPublicKeyAuthRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSshPublicKeyAuthRequired.setStatus("current")


class _CadSshPublicKeyAuthFirst_Type(TruthValue):
    """Custom type cadSshPublicKeyAuthFirst based on TruthValue"""


_CadSshPublicKeyAuthFirst_Object = MibScalar
cadSshPublicKeyAuthFirst = _CadSshPublicKeyAuthFirst_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 9, 17),
    _CadSshPublicKeyAuthFirst_Type()
)
cadSshPublicKeyAuthFirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSshPublicKeyAuthFirst.setStatus("current")


class _CadSshMaxAuthFailures_Type(Unsigned32):
    """Custom type cadSshMaxAuthFailures based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_CadSshMaxAuthFailures_Type.__name__ = "Unsigned32"
_CadSshMaxAuthFailures_Object = MibScalar
cadSshMaxAuthFailures = _CadSshMaxAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 9, 18),
    _CadSshMaxAuthFailures_Type()
)
cadSshMaxAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSshMaxAuthFailures.setStatus("current")


class _CadSshServerKeyType_Type(SshKeyType):
    """Custom type cadSshServerKeyType based on SshKeyType"""


_CadSshServerKeyType_Object = MibScalar
cadSshServerKeyType = _CadSshServerKeyType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 9, 19),
    _CadSshServerKeyType_Type()
)
cadSshServerKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSshServerKeyType.setStatus("current")


class _CadSshKeyExchange_Type(SshKeyExchangeMethod):
    """Custom type cadSshKeyExchange based on SshKeyExchangeMethod"""
    defaultHexValue = "80"


_CadSshKeyExchange_Object = MibScalar
cadSshKeyExchange = _CadSshKeyExchange_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 9, 20),
    _CadSshKeyExchange_Type()
)
cadSshKeyExchange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSshKeyExchange.setStatus("current")
_CadPasswordTable_Object = MibTable
cadPasswordTable = _CadPasswordTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 10)
)
if mibBuilder.loadTexts:
    cadPasswordTable.setStatus("current")
_CadPasswordEntry_Object = MibTableRow
cadPasswordEntry = _CadPasswordEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 10, 1)
)
cadPasswordEntry.setIndexNames(
    (0, "CADANT-AAA-MIB", "cadPassUser"),
)
if mibBuilder.loadTexts:
    cadPasswordEntry.setStatus("current")


class _CadPassUser_Type(SnmpAdminString):
    """Custom type cadPassUser based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CadPassUser_Type.__name__ = "SnmpAdminString"
_CadPassUser_Object = MibTableColumn
cadPassUser = _CadPassUser_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 10, 1, 1),
    _CadPassUser_Type()
)
cadPassUser.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadPassUser.setStatus("current")


class _CadPassPassword_Type(OctetString):
    """Custom type cadPassPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CadPassPassword_Type.__name__ = "OctetString"
_CadPassPassword_Object = MibTableColumn
cadPassPassword = _CadPassPassword_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 10, 1, 2),
    _CadPassPassword_Type()
)
cadPassPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPassPassword.setStatus("current")


class _CadPassAuthLevel_Type(Integer32):
    """Custom type cadPassAuthLevel based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("priviledged", 1))
    )


_CadPassAuthLevel_Type.__name__ = "Integer32"
_CadPassAuthLevel_Object = MibTableColumn
cadPassAuthLevel = _CadPassAuthLevel_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 10, 1, 3),
    _CadPassAuthLevel_Type()
)
cadPassAuthLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPassAuthLevel.setStatus("current")
_CadPassPublicKey_Type = PemKey
_CadPassPublicKey_Object = MibTableColumn
cadPassPublicKey = _CadPassPublicKey_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 10, 1, 4),
    _CadPassPublicKey_Type()
)
cadPassPublicKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPassPublicKey.setStatus("current")
_CadPassRowStatus_Type = RowStatus
_CadPassRowStatus_Object = MibTableColumn
cadPassRowStatus = _CadPassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 10, 1, 5),
    _CadPassRowStatus_Type()
)
cadPassRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPassRowStatus.setStatus("current")
_CadEnablePasswordTable_Object = MibTable
cadEnablePasswordTable = _CadEnablePasswordTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 11)
)
if mibBuilder.loadTexts:
    cadEnablePasswordTable.setStatus("current")
_CadEnablePasswordEntry_Object = MibTableRow
cadEnablePasswordEntry = _CadEnablePasswordEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 11, 1)
)
cadEnablePasswordEntry.setIndexNames(
    (0, "CADANT-AAA-MIB", "cadPrivilegeLevel"),
)
if mibBuilder.loadTexts:
    cadEnablePasswordEntry.setStatus("current")


class _CadPrivilegeLevel_Type(Integer32):
    """Custom type cadPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CadPrivilegeLevel_Type.__name__ = "Integer32"
_CadPrivilegeLevel_Object = MibTableColumn
cadPrivilegeLevel = _CadPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 11, 1, 1),
    _CadPrivilegeLevel_Type()
)
cadPrivilegeLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadPrivilegeLevel.setStatus("current")


class _CadEnablePassword_Type(OctetString):
    """Custom type cadEnablePassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CadEnablePassword_Type.__name__ = "OctetString"
_CadEnablePassword_Object = MibTableColumn
cadEnablePassword = _CadEnablePassword_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 11, 1, 2),
    _CadEnablePassword_Type()
)
cadEnablePassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadEnablePassword.setStatus("current")
_CadEnablePasswordRowStatus_Type = RowStatus
_CadEnablePasswordRowStatus_Object = MibTableColumn
cadEnablePasswordRowStatus = _CadEnablePasswordRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 11, 1, 3),
    _CadEnablePasswordRowStatus_Type()
)
cadEnablePasswordRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadEnablePasswordRowStatus.setStatus("current")
_CadCLIcommandPrivilegeLevelTable_ObjectIdentity = ObjectIdentity
cadCLIcommandPrivilegeLevelTable = _CadCLIcommandPrivilegeLevelTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 12)
)
_CadSshStatus_ObjectIdentity = ObjectIdentity
cadSshStatus = _CadSshStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 13)
)
_CadSshServerVersion_Type = SnmpAdminString
_CadSshServerVersion_Object = MibScalar
cadSshServerVersion = _CadSshServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 13, 1),
    _CadSshServerVersion_Type()
)
cadSshServerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSshServerVersion.setStatus("current")
_CadSshOfferedProtocols_Type = SshProtocol
_CadSshOfferedProtocols_Object = MibScalar
cadSshOfferedProtocols = _CadSshOfferedProtocols_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 13, 2),
    _CadSshOfferedProtocols_Type()
)
cadSshOfferedProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSshOfferedProtocols.setStatus("current")
_CadSshServerRunning_Type = TruthValue
_CadSshServerRunning_Object = MibScalar
cadSshServerRunning = _CadSshServerRunning_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 13, 3),
    _CadSshServerRunning_Type()
)
cadSshServerRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSshServerRunning.setStatus("current")
_CadSshSessionTable_Object = MibTable
cadSshSessionTable = _CadSshSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 13, 4)
)
if mibBuilder.loadTexts:
    cadSshSessionTable.setStatus("current")
_CadSshSessionEntry_Object = MibTableRow
cadSshSessionEntry = _CadSshSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 13, 4, 1)
)
cadSshSessionEntry.setIndexNames(
    (0, "CADANT-AAA-MIB", "cadSshSessionIndex"),
)
if mibBuilder.loadTexts:
    cadSshSessionEntry.setStatus("current")


class _CadSshSessionIndex_Type(Integer32):
    """Custom type cadSshSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CadSshSessionIndex_Type.__name__ = "Integer32"
_CadSshSessionIndex_Object = MibTableColumn
cadSshSessionIndex = _CadSshSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 13, 4, 1, 1),
    _CadSshSessionIndex_Type()
)
cadSshSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadSshSessionIndex.setStatus("current")
_CadSshConnectionId_Type = Integer32
_CadSshConnectionId_Object = MibTableColumn
cadSshConnectionId = _CadSshConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 13, 4, 1, 2),
    _CadSshConnectionId_Type()
)
cadSshConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSshConnectionId.setStatus("current")


class _CadSshUser_Type(SnmpAdminString):
    """Custom type cadSshUser based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CadSshUser_Type.__name__ = "SnmpAdminString"
_CadSshUser_Object = MibTableColumn
cadSshUser = _CadSshUser_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 13, 4, 1, 3),
    _CadSshUser_Type()
)
cadSshUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSshUser.setStatus("current")
_CadSshClientIpAddr_Type = InetAddressIPv4or6
_CadSshClientIpAddr_Object = MibTableColumn
cadSshClientIpAddr = _CadSshClientIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 13, 4, 1, 4),
    _CadSshClientIpAddr_Type()
)
cadSshClientIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSshClientIpAddr.setStatus("current")
_CadSshServiceType_Type = SshService
_CadSshServiceType_Object = MibTableColumn
cadSshServiceType = _CadSshServiceType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 13, 4, 1, 5),
    _CadSshServiceType_Type()
)
cadSshServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSshServiceType.setStatus("current")
_CadSshAuthMethod_Type = SshAuthMethod
_CadSshAuthMethod_Object = MibTableColumn
cadSshAuthMethod = _CadSshAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 13, 4, 1, 6),
    _CadSshAuthMethod_Type()
)
cadSshAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSshAuthMethod.setStatus("current")
_CadSshCipherType_Type = SshCipherType
_CadSshCipherType_Object = MibTableColumn
cadSshCipherType = _CadSshCipherType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 13, 4, 1, 7),
    _CadSshCipherType_Type()
)
cadSshCipherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSshCipherType.setStatus("current")
_CadSshMacAlg_Type = SshMacAlg
_CadSshMacAlg_Object = MibTableColumn
cadSshMacAlg = _CadSshMacAlg_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 13, 4, 1, 8),
    _CadSshMacAlg_Type()
)
cadSshMacAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSshMacAlg.setStatus("current")


class _CadSshClientSw_Type(SnmpAdminString):
    """Custom type cadSshClientSw based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CadSshClientSw_Type.__name__ = "SnmpAdminString"
_CadSshClientSw_Object = MibTableColumn
cadSshClientSw = _CadSshClientSw_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 13, 4, 1, 9),
    _CadSshClientSw_Type()
)
cadSshClientSw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSshClientSw.setStatus("current")
_CadSshSessionRowStatus_Type = RowStatus
_CadSshSessionRowStatus_Object = MibTableColumn
cadSshSessionRowStatus = _CadSshSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 13, 4, 1, 10),
    _CadSshSessionRowStatus_Type()
)
cadSshSessionRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSshSessionRowStatus.setStatus("current")
_CadCLIcommandPrivilegeTable_Object = MibTable
cadCLIcommandPrivilegeTable = _CadCLIcommandPrivilegeTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 14)
)
if mibBuilder.loadTexts:
    cadCLIcommandPrivilegeTable.setStatus("current")
_CadCLIcommandPrivilegeEntry_Object = MibTableRow
cadCLIcommandPrivilegeEntry = _CadCLIcommandPrivilegeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 14, 1)
)
cadCLIcommandPrivilegeEntry.setIndexNames(
    (0, "CADANT-AAA-MIB", "cadCLIcommandPrivilegeCommand"),
)
if mibBuilder.loadTexts:
    cadCLIcommandPrivilegeEntry.setStatus("current")
_CadCLIcommandPrivilegeNodeAddr_Type = CmdNode
_CadCLIcommandPrivilegeNodeAddr_Object = MibTableColumn
cadCLIcommandPrivilegeNodeAddr = _CadCLIcommandPrivilegeNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 14, 1, 1),
    _CadCLIcommandPrivilegeNodeAddr_Type()
)
cadCLIcommandPrivilegeNodeAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadCLIcommandPrivilegeNodeAddr.setStatus("obsolete")
_CadCLIcommandPrivilegeCommand_Type = DisplayString
_CadCLIcommandPrivilegeCommand_Object = MibTableColumn
cadCLIcommandPrivilegeCommand = _CadCLIcommandPrivilegeCommand_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 14, 1, 2),
    _CadCLIcommandPrivilegeCommand_Type()
)
cadCLIcommandPrivilegeCommand.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadCLIcommandPrivilegeCommand.setStatus("current")


class _CadCLIcommandPrivilegeOriginalLevel_Type(Integer32):
    """Custom type cadCLIcommandPrivilegeOriginalLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CadCLIcommandPrivilegeOriginalLevel_Type.__name__ = "Integer32"
_CadCLIcommandPrivilegeOriginalLevel_Object = MibTableColumn
cadCLIcommandPrivilegeOriginalLevel = _CadCLIcommandPrivilegeOriginalLevel_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 14, 1, 3),
    _CadCLIcommandPrivilegeOriginalLevel_Type()
)
cadCLIcommandPrivilegeOriginalLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadCLIcommandPrivilegeOriginalLevel.setStatus("current")


class _CadCLIcommandPrivilegeNewLevel_Type(Integer32):
    """Custom type cadCLIcommandPrivilegeNewLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CadCLIcommandPrivilegeNewLevel_Type.__name__ = "Integer32"
_CadCLIcommandPrivilegeNewLevel_Object = MibTableColumn
cadCLIcommandPrivilegeNewLevel = _CadCLIcommandPrivilegeNewLevel_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 14, 1, 4),
    _CadCLIcommandPrivilegeNewLevel_Type()
)
cadCLIcommandPrivilegeNewLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadCLIcommandPrivilegeNewLevel.setStatus("current")


class _CadCLIcommandPrivilegeRowStatus_Type(RowStatus):
    """Custom type cadCLIcommandPrivilegeRowStatus based on RowStatus"""


_CadCLIcommandPrivilegeRowStatus_Object = MibTableColumn
cadCLIcommandPrivilegeRowStatus = _CadCLIcommandPrivilegeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 14, 1, 5),
    _CadCLIcommandPrivilegeRowStatus_Type()
)
cadCLIcommandPrivilegeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadCLIcommandPrivilegeRowStatus.setStatus("current")
_CadAAAConformance_ObjectIdentity = ObjectIdentity
cadAAAConformance = _CadAAAConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 20)
)
_CadAAAGroups_ObjectIdentity = ObjectIdentity
cadAAAGroups = _CadAAAGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 20, 1)
)
_CadAAACompliances_ObjectIdentity = ObjectIdentity
cadAAACompliances = _CadAAACompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 20, 2)
)

# Managed Objects groups

cadAAALineGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 20, 1, 1)
)
cadAAALineGroup.setObjects(
      *(("CADANT-AAA-MIB", "cadLineType"),
        ("CADANT-AAA-MIB", "cadLineEnabled"),
        ("CADANT-AAA-MIB", "cadLineSessionTimeout"),
        ("CADANT-AAA-MIB", "cadLineIdleTimeout"),
        ("CADANT-AAA-MIB", "cadLinePagination"),
        ("CADANT-AAA-MIB", "cadLineBaud"),
        ("CADANT-AAA-MIB", "cadLinePassword"),
        ("CADANT-AAA-MIB", "cadLineLoginAuthMethodList"),
        ("CADANT-AAA-MIB", "cadLineEnableAuthMethodList"),
        ("CADANT-AAA-MIB", "cadLineAuthorMethodList"),
        ("CADANT-AAA-MIB", "cadLineShellAccountingMethodList"),
        ("CADANT-AAA-MIB", "cadLineCommandAccountingMethodList"),
        ("CADANT-AAA-MIB", "cadLineShellAccountingType"),
        ("CADANT-AAA-MIB", "cadLineCommandAccountingType"),
        ("CADANT-AAA-MIB", "cadLineCommandAccountingPrivilegeLevel"))
)
if mibBuilder.loadTexts:
    cadAAALineGroup.setStatus("current")

cadAAAMethodGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 20, 1, 2)
)
cadAAAMethodGroup.setObjects(
      *(("CADANT-AAA-MIB", "cadAuthType"),
        ("CADANT-AAA-MIB", "cadAuthGroup"))
)
if mibBuilder.loadTexts:
    cadAAAMethodGroup.setStatus("current")

cadAAAServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 20, 1, 3)
)
cadAAAServerGroup.setObjects(
      *(("CADANT-AAA-MIB", "cadGroupIpAddress"),
        ("CADANT-AAA-MIB", "cadGroupType"))
)
if mibBuilder.loadTexts:
    cadAAAServerGroup.setStatus("current")

cadAAAProtocolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 20, 1, 4)
)
cadAAAProtocolGroup.setObjects(
      *(("CADANT-AAA-MIB", "cadTacacsPort"),
        ("CADANT-AAA-MIB", "cadTacacsTimeout"),
        ("CADANT-AAA-MIB", "cadTacacsKey"),
        ("CADANT-AAA-MIB", "cadTacacsSingleConnect"),
        ("CADANT-AAA-MIB", "cadTacacsServerIndex"))
)
if mibBuilder.loadTexts:
    cadAAAProtocolGroup.setStatus("current")

cadAAASshGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 20, 1, 5)
)
cadAAASshGroup.setObjects(
      *(("CADANT-AAA-MIB", "cadSshEnabled"),
        ("CADANT-AAA-MIB", "cadSshPort"),
        ("CADANT-AAA-MIB", "cadSshSessionIdleTimeout"),
        ("CADANT-AAA-MIB", "cadSshMaxClients"),
        ("CADANT-AAA-MIB", "cadSshPasswordAuthEnabled"),
        ("CADANT-AAA-MIB", "cadSshPublicKeyAuthEnabled"),
        ("CADANT-AAA-MIB", "cadSshCliLoginEnabled"),
        ("CADANT-AAA-MIB", "cadSshSecureFtpEnabled"),
        ("CADANT-AAA-MIB", "cadSshPublicKey"),
        ("CADANT-AAA-MIB", "cadSshPrivateKey"),
        ("CADANT-AAA-MIB", "cadSshCiphers"),
        ("CADANT-AAA-MIB", "cadSshPortForwardingEnabled"),
        ("CADANT-AAA-MIB", "cadSshPasswordAuthRequired"),
        ("CADANT-AAA-MIB", "cadSshPublicKeyAuthRequired"),
        ("CADANT-AAA-MIB", "cadSshPublicKeyAuthFirst"),
        ("CADANT-AAA-MIB", "cadSshMaxAuthFailures"),
        ("CADANT-AAA-MIB", "cadSshServerKeyType"),
        ("CADANT-AAA-MIB", "cadSshKeyExchange"))
)
if mibBuilder.loadTexts:
    cadAAASshGroup.setStatus("current")

cadAAAPasswordGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 20, 1, 6)
)
cadAAAPasswordGroup.setObjects(
      *(("CADANT-AAA-MIB", "cadPassPassword"),
        ("CADANT-AAA-MIB", "cadPassAuthLevel"),
        ("CADANT-AAA-MIB", "cadPassPublicKey"))
)
if mibBuilder.loadTexts:
    cadAAAPasswordGroup.setStatus("current")

cadAAAEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 20, 1, 7)
)
cadAAAEnableGroup.setObjects(
    ("CADANT-AAA-MIB", "cadEnablePassword")
)
if mibBuilder.loadTexts:
    cadAAAEnableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cadAAACompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40, 1, 20, 2, 1)
)
if mibBuilder.loadTexts:
    cadAAACompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-AAA-MIB",
    **{"PemKey": PemKey,
       "CmdNode": CmdNode,
       "cadAAA": cadAAA,
       "cadLineTable": cadLineTable,
       "cadLineEntry": cadLineEntry,
       "cadLineIndex": cadLineIndex,
       "cadLineType": cadLineType,
       "cadLineEnabled": cadLineEnabled,
       "cadLineSessionTimeout": cadLineSessionTimeout,
       "cadLineIdleTimeout": cadLineIdleTimeout,
       "cadLinePagination": cadLinePagination,
       "cadLineBaud": cadLineBaud,
       "cadLinePassword": cadLinePassword,
       "cadLineLoginAuthMethodList": cadLineLoginAuthMethodList,
       "cadLineEnableAuthMethodList": cadLineEnableAuthMethodList,
       "cadLineAuthorMethodList": cadLineAuthorMethodList,
       "cadLineShellAccountingMethodList": cadLineShellAccountingMethodList,
       "cadLineCommandAccountingMethodList": cadLineCommandAccountingMethodList,
       "cadLineShellAccountingType": cadLineShellAccountingType,
       "cadLineCommandAccountingType": cadLineCommandAccountingType,
       "cadLineCommandAccountingPrivilegeLevel": cadLineCommandAccountingPrivilegeLevel,
       "cadAuthorizationMethodTable": cadAuthorizationMethodTable,
       "cadAuthorizationMethodEntry": cadAuthorizationMethodEntry,
       "cadAuthorizationListName": cadAuthorizationListName,
       "cadAuthorizationListIndex": cadAuthorizationListIndex,
       "cadAuthorizationType": cadAuthorizationType,
       "cadAuthorizationGroup": cadAuthorizationGroup,
       "cadAuthorizationRowStatus": cadAuthorizationRowStatus,
       "cadAuthMethodTable": cadAuthMethodTable,
       "cadAuthMethodEntry": cadAuthMethodEntry,
       "cadAuthListName": cadAuthListName,
       "cadAuthListIndex": cadAuthListIndex,
       "cadAuthType": cadAuthType,
       "cadAuthGroup": cadAuthGroup,
       "cadAuthRowStatus": cadAuthRowStatus,
       "cadAccountingMethodTable": cadAccountingMethodTable,
       "cadAccountingMethodEntry": cadAccountingMethodEntry,
       "cadAccountingListName": cadAccountingListName,
       "cadAccountingListIndex": cadAccountingListIndex,
       "cadAccountingType": cadAccountingType,
       "cadAccountingGroup": cadAccountingGroup,
       "cadAccountingRowStatus": cadAccountingRowStatus,
       "cadServerGroupTable": cadServerGroupTable,
       "cadServerGroupEntry": cadServerGroupEntry,
       "cadGroupName": cadGroupName,
       "cadGroupIndex": cadGroupIndex,
       "cadGroupType": cadGroupType,
       "cadGroupIpAddress": cadGroupIpAddress,
       "cadGroupPort": cadGroupPort,
       "cadGroupRowStatus": cadGroupRowStatus,
       "cadRadiusTable": cadRadiusTable,
       "cadRadiusEntry": cadRadiusEntry,
       "cadRadiusIpAddress": cadRadiusIpAddress,
       "cadRadiusAuthPort": cadRadiusAuthPort,
       "cadRadiusAcctPort": cadRadiusAcctPort,
       "cadRadiusTimeout": cadRadiusTimeout,
       "cadRadiusRetrans": cadRadiusRetrans,
       "cadRadiusKey": cadRadiusKey,
       "cadRadiusAuthServerIndex": cadRadiusAuthServerIndex,
       "cadRadiusRowStatus": cadRadiusRowStatus,
       "cadTacacsTable": cadTacacsTable,
       "cadTacacsEntry": cadTacacsEntry,
       "cadTacacsIpAddress": cadTacacsIpAddress,
       "cadTacacsPort": cadTacacsPort,
       "cadTacacsTimeout": cadTacacsTimeout,
       "cadTacacsKey": cadTacacsKey,
       "cadTacacsSingleConnect": cadTacacsSingleConnect,
       "cadTacacsServerIndex": cadTacacsServerIndex,
       "cadTacacsRowStatus": cadTacacsRowStatus,
       "cadSshConfig": cadSshConfig,
       "cadSshEnabled": cadSshEnabled,
       "cadSshPort": cadSshPort,
       "cadSshSessionIdleTimeout": cadSshSessionIdleTimeout,
       "cadSshMaxClients": cadSshMaxClients,
       "cadSshPasswordAuthEnabled": cadSshPasswordAuthEnabled,
       "cadSshPublicKeyAuthEnabled": cadSshPublicKeyAuthEnabled,
       "cadSshCliLoginEnabled": cadSshCliLoginEnabled,
       "cadSshSecureFtpEnabled": cadSshSecureFtpEnabled,
       "cadSshPublicKey": cadSshPublicKey,
       "cadSshPrivateKey": cadSshPrivateKey,
       "cadSshCiphers": cadSshCiphers,
       "cadSshPortForwardingEnabled": cadSshPortForwardingEnabled,
       "cadSshPasswordAuthRequired": cadSshPasswordAuthRequired,
       "cadSshPublicKeyAuthRequired": cadSshPublicKeyAuthRequired,
       "cadSshPublicKeyAuthFirst": cadSshPublicKeyAuthFirst,
       "cadSshMaxAuthFailures": cadSshMaxAuthFailures,
       "cadSshServerKeyType": cadSshServerKeyType,
       "cadSshKeyExchange": cadSshKeyExchange,
       "cadPasswordTable": cadPasswordTable,
       "cadPasswordEntry": cadPasswordEntry,
       "cadPassUser": cadPassUser,
       "cadPassPassword": cadPassPassword,
       "cadPassAuthLevel": cadPassAuthLevel,
       "cadPassPublicKey": cadPassPublicKey,
       "cadPassRowStatus": cadPassRowStatus,
       "cadEnablePasswordTable": cadEnablePasswordTable,
       "cadEnablePasswordEntry": cadEnablePasswordEntry,
       "cadPrivilegeLevel": cadPrivilegeLevel,
       "cadEnablePassword": cadEnablePassword,
       "cadEnablePasswordRowStatus": cadEnablePasswordRowStatus,
       "cadCLIcommandPrivilegeLevelTable": cadCLIcommandPrivilegeLevelTable,
       "cadSshStatus": cadSshStatus,
       "cadSshServerVersion": cadSshServerVersion,
       "cadSshOfferedProtocols": cadSshOfferedProtocols,
       "cadSshServerRunning": cadSshServerRunning,
       "cadSshSessionTable": cadSshSessionTable,
       "cadSshSessionEntry": cadSshSessionEntry,
       "cadSshSessionIndex": cadSshSessionIndex,
       "cadSshConnectionId": cadSshConnectionId,
       "cadSshUser": cadSshUser,
       "cadSshClientIpAddr": cadSshClientIpAddr,
       "cadSshServiceType": cadSshServiceType,
       "cadSshAuthMethod": cadSshAuthMethod,
       "cadSshCipherType": cadSshCipherType,
       "cadSshMacAlg": cadSshMacAlg,
       "cadSshClientSw": cadSshClientSw,
       "cadSshSessionRowStatus": cadSshSessionRowStatus,
       "cadCLIcommandPrivilegeTable": cadCLIcommandPrivilegeTable,
       "cadCLIcommandPrivilegeEntry": cadCLIcommandPrivilegeEntry,
       "cadCLIcommandPrivilegeNodeAddr": cadCLIcommandPrivilegeNodeAddr,
       "cadCLIcommandPrivilegeCommand": cadCLIcommandPrivilegeCommand,
       "cadCLIcommandPrivilegeOriginalLevel": cadCLIcommandPrivilegeOriginalLevel,
       "cadCLIcommandPrivilegeNewLevel": cadCLIcommandPrivilegeNewLevel,
       "cadCLIcommandPrivilegeRowStatus": cadCLIcommandPrivilegeRowStatus,
       "cadAAAConformance": cadAAAConformance,
       "cadAAAGroups": cadAAAGroups,
       "cadAAALineGroup": cadAAALineGroup,
       "cadAAAMethodGroup": cadAAAMethodGroup,
       "cadAAAServerGroup": cadAAAServerGroup,
       "cadAAAProtocolGroup": cadAAAProtocolGroup,
       "cadAAASshGroup": cadAAASshGroup,
       "cadAAAPasswordGroup": cadAAAPasswordGroup,
       "cadAAAEnableGroup": cadAAAEnableGroup,
       "cadAAACompliances": cadAAACompliances,
       "cadAAACompliance": cadAAACompliance}
)
