# SNMP MIB module (TPLINK-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-AAA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:45 2024
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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY

tplinkAaaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82)
)
tplinkAaaMIB.setRevisions(
        ("2015-06-11 14:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AaaGlobalConfig_ObjectIdentity = ObjectIdentity
aaaGlobalConfig = _AaaGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 1)
)


class _SwAaaGlobalEnable_Type(Integer32):
    """Custom type swAaaGlobalEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwAaaGlobalEnable_Type.__name__ = "Integer32"
_SwAaaGlobalEnable_Object = MibScalar
swAaaGlobalEnable = _SwAaaGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 1, 1),
    _SwAaaGlobalEnable_Type()
)
swAaaGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAaaGlobalEnable.setStatus("current")
_AaaApplicationList_ObjectIdentity = ObjectIdentity
aaaApplicationList = _AaaApplicationList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 1, 2)
)
_AaaApplicationListTable_Object = MibTable
aaaApplicationListTable = _AaaApplicationListTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 1, 2, 1)
)
if mibBuilder.loadTexts:
    aaaApplicationListTable.setStatus("current")
_AaaApplicationListEntry_Object = MibTableRow
aaaApplicationListEntry = _AaaApplicationListEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 1, 2, 1, 1)
)
aaaApplicationListEntry.setIndexNames(
    (0, "TPLINK-AAA-MIB", "moduleId"),
)
if mibBuilder.loadTexts:
    aaaApplicationListEntry.setStatus("current")
_ModuleId_Type = Integer32
_ModuleId_Object = MibTableColumn
moduleId = _ModuleId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 1, 2, 1, 1, 1),
    _ModuleId_Type()
)
moduleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleId.setStatus("current")


class _ModuleName_Type(OctetString):
    """Custom type moduleName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ModuleName_Type.__name__ = "OctetString"
_ModuleName_Object = MibTableColumn
moduleName = _ModuleName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 1, 2, 1, 1, 2),
    _ModuleName_Type()
)
moduleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleName.setStatus("current")


class _LoginList_Type(OctetString):
    """Custom type loginList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_LoginList_Type.__name__ = "OctetString"
_LoginList_Object = MibTableColumn
loginList = _LoginList_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 1, 2, 1, 1, 3),
    _LoginList_Type()
)
loginList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginList.setStatus("current")


class _EnableList_Type(OctetString):
    """Custom type enableList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_EnableList_Type.__name__ = "OctetString"
_EnableList_Object = MibTableColumn
enableList = _EnableList_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 1, 2, 1, 1, 4),
    _EnableList_Type()
)
enableList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableList.setStatus("current")
_AaaAuthenticationListConfig_ObjectIdentity = ObjectIdentity
aaaAuthenticationListConfig = _AaaAuthenticationListConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 2)
)
_AuthenticationLoginMethodListTable_Object = MibTable
authenticationLoginMethodListTable = _AuthenticationLoginMethodListTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 2, 1)
)
if mibBuilder.loadTexts:
    authenticationLoginMethodListTable.setStatus("current")
_AuthenticationLoginMethodListEntry_Object = MibTableRow
authenticationLoginMethodListEntry = _AuthenticationLoginMethodListEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 2, 1, 1)
)
authenticationLoginMethodListEntry.setIndexNames(
    (0, "TPLINK-AAA-MIB", "authenLoginListName"),
)
if mibBuilder.loadTexts:
    authenticationLoginMethodListEntry.setStatus("current")


class _AuthenLoginListName_Type(OctetString):
    """Custom type authenLoginListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AuthenLoginListName_Type.__name__ = "OctetString"
_AuthenLoginListName_Object = MibTableColumn
authenLoginListName = _AuthenLoginListName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 2, 1, 1, 1),
    _AuthenLoginListName_Type()
)
authenLoginListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authenLoginListName.setStatus("current")


class _AuthenLoginPri1_Type(OctetString):
    """Custom type authenLoginPri1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AuthenLoginPri1_Type.__name__ = "OctetString"
_AuthenLoginPri1_Object = MibTableColumn
authenLoginPri1 = _AuthenLoginPri1_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 2, 1, 1, 2),
    _AuthenLoginPri1_Type()
)
authenLoginPri1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authenLoginPri1.setStatus("current")


class _AuthenLoginPri2_Type(OctetString):
    """Custom type authenLoginPri2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AuthenLoginPri2_Type.__name__ = "OctetString"
_AuthenLoginPri2_Object = MibTableColumn
authenLoginPri2 = _AuthenLoginPri2_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 2, 1, 1, 3),
    _AuthenLoginPri2_Type()
)
authenLoginPri2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authenLoginPri2.setStatus("current")


class _AuthenLoginPri3_Type(OctetString):
    """Custom type authenLoginPri3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AuthenLoginPri3_Type.__name__ = "OctetString"
_AuthenLoginPri3_Object = MibTableColumn
authenLoginPri3 = _AuthenLoginPri3_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 2, 1, 1, 4),
    _AuthenLoginPri3_Type()
)
authenLoginPri3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authenLoginPri3.setStatus("current")


class _AuthenLoginPri4_Type(OctetString):
    """Custom type authenLoginPri4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AuthenLoginPri4_Type.__name__ = "OctetString"
_AuthenLoginPri4_Object = MibTableColumn
authenLoginPri4 = _AuthenLoginPri4_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 2, 1, 1, 5),
    _AuthenLoginPri4_Type()
)
authenLoginPri4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authenLoginPri4.setStatus("current")
_AuthenLoginStatus_Type = TPRowStatus
_AuthenLoginStatus_Object = MibTableColumn
authenLoginStatus = _AuthenLoginStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 2, 1, 1, 6),
    _AuthenLoginStatus_Type()
)
authenLoginStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authenLoginStatus.setStatus("current")
_AuthenticationEnableMethodListTable_Object = MibTable
authenticationEnableMethodListTable = _AuthenticationEnableMethodListTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 2, 2)
)
if mibBuilder.loadTexts:
    authenticationEnableMethodListTable.setStatus("current")
_AuthenticationEnableMethodListEntry_Object = MibTableRow
authenticationEnableMethodListEntry = _AuthenticationEnableMethodListEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 2, 2, 1)
)
authenticationEnableMethodListEntry.setIndexNames(
    (0, "TPLINK-AAA-MIB", "authenEnableListName"),
)
if mibBuilder.loadTexts:
    authenticationEnableMethodListEntry.setStatus("current")


class _AuthenEnableListName_Type(OctetString):
    """Custom type authenEnableListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AuthenEnableListName_Type.__name__ = "OctetString"
_AuthenEnableListName_Object = MibTableColumn
authenEnableListName = _AuthenEnableListName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 2, 2, 1, 1),
    _AuthenEnableListName_Type()
)
authenEnableListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authenEnableListName.setStatus("current")


class _AuthenEnablePri1_Type(OctetString):
    """Custom type authenEnablePri1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AuthenEnablePri1_Type.__name__ = "OctetString"
_AuthenEnablePri1_Object = MibTableColumn
authenEnablePri1 = _AuthenEnablePri1_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 2, 2, 1, 2),
    _AuthenEnablePri1_Type()
)
authenEnablePri1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authenEnablePri1.setStatus("current")


class _AuthenEnablePri2_Type(OctetString):
    """Custom type authenEnablePri2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AuthenEnablePri2_Type.__name__ = "OctetString"
_AuthenEnablePri2_Object = MibTableColumn
authenEnablePri2 = _AuthenEnablePri2_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 2, 2, 1, 3),
    _AuthenEnablePri2_Type()
)
authenEnablePri2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authenEnablePri2.setStatus("current")


class _AuthenEnablePri3_Type(OctetString):
    """Custom type authenEnablePri3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AuthenEnablePri3_Type.__name__ = "OctetString"
_AuthenEnablePri3_Object = MibTableColumn
authenEnablePri3 = _AuthenEnablePri3_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 2, 2, 1, 4),
    _AuthenEnablePri3_Type()
)
authenEnablePri3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authenEnablePri3.setStatus("current")


class _AuthenEnablePri4_Type(OctetString):
    """Custom type authenEnablePri4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AuthenEnablePri4_Type.__name__ = "OctetString"
_AuthenEnablePri4_Object = MibTableColumn
authenEnablePri4 = _AuthenEnablePri4_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 2, 2, 1, 5),
    _AuthenEnablePri4_Type()
)
authenEnablePri4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authenEnablePri4.setStatus("current")
_AuthenEnableStatus_Type = TPRowStatus
_AuthenEnableStatus_Object = MibTableColumn
authenEnableStatus = _AuthenEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 2, 2, 1, 6),
    _AuthenEnableStatus_Type()
)
authenEnableStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authenEnableStatus.setStatus("current")
_AaaDot1xListConfig_ObjectIdentity = ObjectIdentity
aaaDot1xListConfig = _AaaDot1xListConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 3)
)
_AuthenticationDot1xMethodListTable_Object = MibTable
authenticationDot1xMethodListTable = _AuthenticationDot1xMethodListTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 3, 1)
)
if mibBuilder.loadTexts:
    authenticationDot1xMethodListTable.setStatus("current")
_AuthenticationDot1xMethodListEntry_Object = MibTableRow
authenticationDot1xMethodListEntry = _AuthenticationDot1xMethodListEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 3, 1, 1)
)
authenticationDot1xMethodListEntry.setIndexNames(
    (0, "TPLINK-AAA-MIB", "authenDot1xListName"),
)
if mibBuilder.loadTexts:
    authenticationDot1xMethodListEntry.setStatus("current")


class _AuthenDot1xListName_Type(OctetString):
    """Custom type authenDot1xListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AuthenDot1xListName_Type.__name__ = "OctetString"
_AuthenDot1xListName_Object = MibTableColumn
authenDot1xListName = _AuthenDot1xListName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 3, 1, 1, 1),
    _AuthenDot1xListName_Type()
)
authenDot1xListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authenDot1xListName.setStatus("current")


class _AuthenDot1xPri1_Type(OctetString):
    """Custom type authenDot1xPri1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AuthenDot1xPri1_Type.__name__ = "OctetString"
_AuthenDot1xPri1_Object = MibTableColumn
authenDot1xPri1 = _AuthenDot1xPri1_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 3, 1, 1, 2),
    _AuthenDot1xPri1_Type()
)
authenDot1xPri1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authenDot1xPri1.setStatus("current")
_AuthenDot1xStatus_Type = TPRowStatus
_AuthenDot1xStatus_Object = MibTableColumn
authenDot1xStatus = _AuthenDot1xStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 3, 1, 1, 3),
    _AuthenDot1xStatus_Type()
)
authenDot1xStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authenDot1xStatus.setStatus("current")
_AccountingDot1xMethodListTable_Object = MibTable
accountingDot1xMethodListTable = _AccountingDot1xMethodListTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 3, 2)
)
if mibBuilder.loadTexts:
    accountingDot1xMethodListTable.setStatus("current")
_AccountingDot1xMethodListEntry_Object = MibTableRow
accountingDot1xMethodListEntry = _AccountingDot1xMethodListEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 3, 2, 1)
)
accountingDot1xMethodListEntry.setIndexNames(
    (0, "TPLINK-AAA-MIB", "acctDot1xListName"),
)
if mibBuilder.loadTexts:
    accountingDot1xMethodListEntry.setStatus("current")


class _AcctDot1xListName_Type(OctetString):
    """Custom type acctDot1xListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AcctDot1xListName_Type.__name__ = "OctetString"
_AcctDot1xListName_Object = MibTableColumn
acctDot1xListName = _AcctDot1xListName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 3, 2, 1, 1),
    _AcctDot1xListName_Type()
)
acctDot1xListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acctDot1xListName.setStatus("current")


class _AcctDot1xPri1_Type(OctetString):
    """Custom type acctDot1xPri1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AcctDot1xPri1_Type.__name__ = "OctetString"
_AcctDot1xPri1_Object = MibTableColumn
acctDot1xPri1 = _AcctDot1xPri1_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 3, 2, 1, 2),
    _AcctDot1xPri1_Type()
)
acctDot1xPri1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acctDot1xPri1.setStatus("current")
_AcctDot1xStatus_Type = TPRowStatus
_AcctDot1xStatus_Object = MibTableColumn
acctDot1xStatus = _AcctDot1xStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 3, 2, 1, 3),
    _AcctDot1xStatus_Type()
)
acctDot1xStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acctDot1xStatus.setStatus("current")
_RadiusDeamonTable_Object = MibTable
radiusDeamonTable = _RadiusDeamonTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 4)
)
if mibBuilder.loadTexts:
    radiusDeamonTable.setStatus("current")
_RadiusDeamonEntry_Object = MibTableRow
radiusDeamonEntry = _RadiusDeamonEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 4, 1)
)
radiusDeamonEntry.setIndexNames(
    (0, "TPLINK-AAA-MIB", "radiusDeamonServerIp"),
)
if mibBuilder.loadTexts:
    radiusDeamonEntry.setStatus("current")
_RadiusDeamonServerIp_Type = IpAddress
_RadiusDeamonServerIp_Object = MibTableColumn
radiusDeamonServerIp = _RadiusDeamonServerIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 4, 1, 1),
    _RadiusDeamonServerIp_Type()
)
radiusDeamonServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusDeamonServerIp.setStatus("current")


class _RadiusDeamonTimeout_Type(Integer32):
    """Custom type radiusDeamonTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_RadiusDeamonTimeout_Type.__name__ = "Integer32"
_RadiusDeamonTimeout_Object = MibTableColumn
radiusDeamonTimeout = _RadiusDeamonTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 4, 1, 2),
    _RadiusDeamonTimeout_Type()
)
radiusDeamonTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusDeamonTimeout.setStatus("current")


class _RadiusDeamonRetransimit_Type(Integer32):
    """Custom type radiusDeamonRetransimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_RadiusDeamonRetransimit_Type.__name__ = "Integer32"
_RadiusDeamonRetransimit_Object = MibTableColumn
radiusDeamonRetransimit = _RadiusDeamonRetransimit_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 4, 1, 3),
    _RadiusDeamonRetransimit_Type()
)
radiusDeamonRetransimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusDeamonRetransimit.setStatus("current")


class _RadiusDeamonKey_Type(OctetString):
    """Custom type radiusDeamonKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_RadiusDeamonKey_Type.__name__ = "OctetString"
_RadiusDeamonKey_Object = MibTableColumn
radiusDeamonKey = _RadiusDeamonKey_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 4, 1, 4),
    _RadiusDeamonKey_Type()
)
radiusDeamonKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusDeamonKey.setStatus("current")


class _RadiusDeamonAuthPort_Type(Integer32):
    """Custom type radiusDeamonAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusDeamonAuthPort_Type.__name__ = "Integer32"
_RadiusDeamonAuthPort_Object = MibTableColumn
radiusDeamonAuthPort = _RadiusDeamonAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 4, 1, 5),
    _RadiusDeamonAuthPort_Type()
)
radiusDeamonAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusDeamonAuthPort.setStatus("current")


class _RadiusDeamonAcctPort_Type(Integer32):
    """Custom type radiusDeamonAcctPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusDeamonAcctPort_Type.__name__ = "Integer32"
_RadiusDeamonAcctPort_Object = MibTableColumn
radiusDeamonAcctPort = _RadiusDeamonAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 4, 1, 6),
    _RadiusDeamonAcctPort_Type()
)
radiusDeamonAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusDeamonAcctPort.setStatus("current")
_RadiusDeamonStatus_Type = TPRowStatus
_RadiusDeamonStatus_Object = MibTableColumn
radiusDeamonStatus = _RadiusDeamonStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 4, 1, 7),
    _RadiusDeamonStatus_Type()
)
radiusDeamonStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusDeamonStatus.setStatus("current")
_TacacsDeamonTable_Object = MibTable
tacacsDeamonTable = _TacacsDeamonTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 5)
)
if mibBuilder.loadTexts:
    tacacsDeamonTable.setStatus("current")
_TacacsDeamonEntry_Object = MibTableRow
tacacsDeamonEntry = _TacacsDeamonEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 5, 1)
)
tacacsDeamonEntry.setIndexNames(
    (0, "TPLINK-AAA-MIB", "tacacsDeamonServerIp"),
)
if mibBuilder.loadTexts:
    tacacsDeamonEntry.setStatus("current")
_TacacsDeamonServerIp_Type = IpAddress
_TacacsDeamonServerIp_Object = MibTableColumn
tacacsDeamonServerIp = _TacacsDeamonServerIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 5, 1, 1),
    _TacacsDeamonServerIp_Type()
)
tacacsDeamonServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacacsDeamonServerIp.setStatus("current")


class _TacacsDeamonTimeout_Type(Integer32):
    """Custom type tacacsDeamonTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TacacsDeamonTimeout_Type.__name__ = "Integer32"
_TacacsDeamonTimeout_Object = MibTableColumn
tacacsDeamonTimeout = _TacacsDeamonTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 5, 1, 2),
    _TacacsDeamonTimeout_Type()
)
tacacsDeamonTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacacsDeamonTimeout.setStatus("current")


class _TacacsDeamonKey_Type(OctetString):
    """Custom type tacacsDeamonKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TacacsDeamonKey_Type.__name__ = "OctetString"
_TacacsDeamonKey_Object = MibTableColumn
tacacsDeamonKey = _TacacsDeamonKey_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 5, 1, 3),
    _TacacsDeamonKey_Type()
)
tacacsDeamonKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacacsDeamonKey.setStatus("current")


class _TacacsDeamonPort_Type(Integer32):
    """Custom type tacacsDeamonPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TacacsDeamonPort_Type.__name__ = "Integer32"
_TacacsDeamonPort_Object = MibTableColumn
tacacsDeamonPort = _TacacsDeamonPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 5, 1, 4),
    _TacacsDeamonPort_Type()
)
tacacsDeamonPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacacsDeamonPort.setStatus("current")
_TacacsDeamonStatus_Type = TPRowStatus
_TacacsDeamonStatus_Object = MibTableColumn
tacacsDeamonStatus = _TacacsDeamonStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 82, 5, 1, 5),
    _TacacsDeamonStatus_Type()
)
tacacsDeamonStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacacsDeamonStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-AAA-MIB",
    **{"tplinkAaaMIB": tplinkAaaMIB,
       "aaaGlobalConfig": aaaGlobalConfig,
       "swAaaGlobalEnable": swAaaGlobalEnable,
       "aaaApplicationList": aaaApplicationList,
       "aaaApplicationListTable": aaaApplicationListTable,
       "aaaApplicationListEntry": aaaApplicationListEntry,
       "moduleId": moduleId,
       "moduleName": moduleName,
       "loginList": loginList,
       "enableList": enableList,
       "aaaAuthenticationListConfig": aaaAuthenticationListConfig,
       "authenticationLoginMethodListTable": authenticationLoginMethodListTable,
       "authenticationLoginMethodListEntry": authenticationLoginMethodListEntry,
       "authenLoginListName": authenLoginListName,
       "authenLoginPri1": authenLoginPri1,
       "authenLoginPri2": authenLoginPri2,
       "authenLoginPri3": authenLoginPri3,
       "authenLoginPri4": authenLoginPri4,
       "authenLoginStatus": authenLoginStatus,
       "authenticationEnableMethodListTable": authenticationEnableMethodListTable,
       "authenticationEnableMethodListEntry": authenticationEnableMethodListEntry,
       "authenEnableListName": authenEnableListName,
       "authenEnablePri1": authenEnablePri1,
       "authenEnablePri2": authenEnablePri2,
       "authenEnablePri3": authenEnablePri3,
       "authenEnablePri4": authenEnablePri4,
       "authenEnableStatus": authenEnableStatus,
       "aaaDot1xListConfig": aaaDot1xListConfig,
       "authenticationDot1xMethodListTable": authenticationDot1xMethodListTable,
       "authenticationDot1xMethodListEntry": authenticationDot1xMethodListEntry,
       "authenDot1xListName": authenDot1xListName,
       "authenDot1xPri1": authenDot1xPri1,
       "authenDot1xStatus": authenDot1xStatus,
       "accountingDot1xMethodListTable": accountingDot1xMethodListTable,
       "accountingDot1xMethodListEntry": accountingDot1xMethodListEntry,
       "acctDot1xListName": acctDot1xListName,
       "acctDot1xPri1": acctDot1xPri1,
       "acctDot1xStatus": acctDot1xStatus,
       "radiusDeamonTable": radiusDeamonTable,
       "radiusDeamonEntry": radiusDeamonEntry,
       "radiusDeamonServerIp": radiusDeamonServerIp,
       "radiusDeamonTimeout": radiusDeamonTimeout,
       "radiusDeamonRetransimit": radiusDeamonRetransimit,
       "radiusDeamonKey": radiusDeamonKey,
       "radiusDeamonAuthPort": radiusDeamonAuthPort,
       "radiusDeamonAcctPort": radiusDeamonAcctPort,
       "radiusDeamonStatus": radiusDeamonStatus,
       "tacacsDeamonTable": tacacsDeamonTable,
       "tacacsDeamonEntry": tacacsDeamonEntry,
       "tacacsDeamonServerIp": tacacsDeamonServerIp,
       "tacacsDeamonTimeout": tacacsDeamonTimeout,
       "tacacsDeamonKey": tacacsDeamonKey,
       "tacacsDeamonPort": tacacsDeamonPort,
       "tacacsDeamonStatus": tacacsDeamonStatus}
)
