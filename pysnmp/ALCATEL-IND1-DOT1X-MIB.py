# SNMP MIB module (ALCATEL-IND1-DOT1X-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-DOT1X-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:54 2024
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

(softentIND1Dot1X,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Dot1X")

(dot1xPaePortNumber,) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "dot1xPaePortNumber")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

alcatelIND1Dot1XMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1)
)
alcatelIND1Dot1XMIB.setRevisions(
        ("2010-02-10 00:00",
         "2007-04-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ALADot1xClassificationPolicyType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("aaaAuthSvrDownBlock", 22),
          ("aaaAuthSvrDownUNP", 21),
          ("aaaRuleUNP", 20),
          ("authServerUNP", 18),
          ("block", 5),
          ("captivePortalAuthentication", 9),
          ("captivePortalBlock", 13),
          ("captivePortalDefaultVlan", 11),
          ("captivePortalGroupMobility", 10),
          ("captivePortalUnknown", 14),
          ("captivePortalUnpAAArule", 17),
          ("captivePortalUnpAuthSrv", 15),
          ("captivePortalUnpUsrCfg", 16),
          ("captivePortalVlanId", 12),
          ("defaultVlan", 4),
          ("dotXAuthentication", 0),
          ("groupMobilityRules", 2),
          ("internalUseOnlyA", 6),
          ("internalUseOnlyB", 7),
          ("internalUseOnlyC", 8),
          ("macAuthentication", 1),
          ("userConfigUNP", 19),
          ("vlanId", 3))
    )



class ALADot1xAuthenticationType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("captivePortal", 3),
          ("dotXAuthentication", 1),
          ("macAuthentication", 2),
          ("noAuthentication", 0))
    )



class ALADot1xAuthenticationResult(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 3),
          ("inProgress", 1),
          ("notApplicable", 0),
          ("success", 2))
    )



class ALADot1xMacLearntState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bridging", 0),
          ("filtering", 1),
          ("hicInProgress", 2),
          ("qmrInProgress", 3))
    )



class ALADot1xMacQueryType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("captivePortal", 3),
          ("nonSupplicant", 2),
          ("supplicant", 1))
    )



class ALADot1xDeviceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonSupplicant", 2),
          ("supplicant", 1))
    )



class AlaPassThroughStatus(Integer32, TextualConvention):
    status = "obsolete"
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



# MIB Managed Objects in the order of their OIDs

_AlaIND1Dot1XMIBObjects_ObjectIdentity = ObjectIdentity
alaIND1Dot1XMIBObjects = _AlaIND1Dot1XMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1)
)
if mibBuilder.loadTexts:
    alaIND1Dot1XMIBObjects.setStatus("current")
_AlaDot1xPortTable_Object = MibTable
alaDot1xPortTable = _AlaDot1xPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaDot1xPortTable.setStatus("deprecated")
_AlaDot1xPortEntry_Object = MibTableRow
alaDot1xPortEntry = _AlaDot1xPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 1, 1)
)
alaDot1xPortEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    alaDot1xPortEntry.setStatus("deprecated")


class _AlaDot1xPortSlotNumber_Type(Integer32):
    """Custom type alaDot1xPortSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AlaDot1xPortSlotNumber_Type.__name__ = "Integer32"
_AlaDot1xPortSlotNumber_Object = MibTableColumn
alaDot1xPortSlotNumber = _AlaDot1xPortSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 1, 1, 1),
    _AlaDot1xPortSlotNumber_Type()
)
alaDot1xPortSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xPortSlotNumber.setStatus("deprecated")


class _AlaDot1xPortPortNumber_Type(Integer32):
    """Custom type alaDot1xPortPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_AlaDot1xPortPortNumber_Type.__name__ = "Integer32"
_AlaDot1xPortPortNumber_Object = MibTableColumn
alaDot1xPortPortNumber = _AlaDot1xPortPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 1, 1, 2),
    _AlaDot1xPortPortNumber_Type()
)
alaDot1xPortPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xPortPortNumber.setStatus("deprecated")
_AlaDot1xPortMACAddress_Type = MacAddress
_AlaDot1xPortMACAddress_Object = MibTableColumn
alaDot1xPortMACAddress = _AlaDot1xPortMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 1, 1, 3),
    _AlaDot1xPortMACAddress_Type()
)
alaDot1xPortMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xPortMACAddress.setStatus("deprecated")


class _AlaDot1xPortVlan_Type(Integer32):
    """Custom type alaDot1xPortVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AlaDot1xPortVlan_Type.__name__ = "Integer32"
_AlaDot1xPortVlan_Object = MibTableColumn
alaDot1xPortVlan = _AlaDot1xPortVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 1, 1, 4),
    _AlaDot1xPortVlan_Type()
)
alaDot1xPortVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xPortVlan.setStatus("deprecated")


class _AlaDot1xPortProtocol_Type(Integer32):
    """Custom type alaDot1xPortProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AlaDot1xPortProtocol_Type.__name__ = "Integer32"
_AlaDot1xPortProtocol_Object = MibTableColumn
alaDot1xPortProtocol = _AlaDot1xPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 1, 1, 5),
    _AlaDot1xPortProtocol_Type()
)
alaDot1xPortProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xPortProtocol.setStatus("deprecated")
_AlaDot1xPortUserName_Type = DisplayString
_AlaDot1xPortUserName_Object = MibTableColumn
alaDot1xPortUserName = _AlaDot1xPortUserName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 1, 1, 6),
    _AlaDot1xPortUserName_Type()
)
alaDot1xPortUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xPortUserName.setStatus("deprecated")


class _AlaDot1xPortState_Type(Integer32):
    """Custom type alaDot1xPortState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("aborting", 6),
          ("authenticated", 5),
          ("authenticatedLocally", 10),
          ("authenticating", 4),
          ("connecting", 3),
          ("disconnected", 2),
          ("forceAuthenticated", 8),
          ("forceUnauthenticated", 9),
          ("held", 7),
          ("initialize", 1))
    )


_AlaDot1xPortState_Type.__name__ = "Integer32"
_AlaDot1xPortState_Object = MibTableColumn
alaDot1xPortState = _AlaDot1xPortState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 1, 1, 7),
    _AlaDot1xPortState_Type()
)
alaDot1xPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xPortState.setStatus("deprecated")
_AlaDot1xSupplicantPolicyUsed_Type = ALADot1xClassificationPolicyType
_AlaDot1xSupplicantPolicyUsed_Object = MibTableColumn
alaDot1xSupplicantPolicyUsed = _AlaDot1xSupplicantPolicyUsed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 1, 1, 8),
    _AlaDot1xSupplicantPolicyUsed_Type()
)
alaDot1xSupplicantPolicyUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xSupplicantPolicyUsed.setStatus("deprecated")
_AlaDot1xPortLookupTable_Object = MibTable
alaDot1xPortLookupTable = _AlaDot1xPortLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaDot1xPortLookupTable.setStatus("current")
_AlaDot1xPortLookupEntry_Object = MibTableRow
alaDot1xPortLookupEntry = _AlaDot1xPortLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 2, 1)
)
alaDot1xPortLookupEntry.setIndexNames(
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaDot1xPortLookupSlotNumber"),
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaDot1xPortLookupPortNumber"),
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaDot1xPortLookupMACAddress"),
)
if mibBuilder.loadTexts:
    alaDot1xPortLookupEntry.setStatus("current")


class _AlaDot1xPortLookupSlotNumber_Type(Integer32):
    """Custom type alaDot1xPortLookupSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AlaDot1xPortLookupSlotNumber_Type.__name__ = "Integer32"
_AlaDot1xPortLookupSlotNumber_Object = MibTableColumn
alaDot1xPortLookupSlotNumber = _AlaDot1xPortLookupSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 2, 1, 1),
    _AlaDot1xPortLookupSlotNumber_Type()
)
alaDot1xPortLookupSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xPortLookupSlotNumber.setStatus("current")


class _AlaDot1xPortLookupPortNumber_Type(Integer32):
    """Custom type alaDot1xPortLookupPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_AlaDot1xPortLookupPortNumber_Type.__name__ = "Integer32"
_AlaDot1xPortLookupPortNumber_Object = MibTableColumn
alaDot1xPortLookupPortNumber = _AlaDot1xPortLookupPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 2, 1, 2),
    _AlaDot1xPortLookupPortNumber_Type()
)
alaDot1xPortLookupPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xPortLookupPortNumber.setStatus("current")
_AlaDot1xPortLookupMACAddress_Type = MacAddress
_AlaDot1xPortLookupMACAddress_Object = MibTableColumn
alaDot1xPortLookupMACAddress = _AlaDot1xPortLookupMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 2, 1, 3),
    _AlaDot1xPortLookupMACAddress_Type()
)
alaDot1xPortLookupMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xPortLookupMACAddress.setStatus("current")
_AlaDot1xPortLookupInterfaceNumber_Type = InterfaceIndex
_AlaDot1xPortLookupInterfaceNumber_Object = MibTableColumn
alaDot1xPortLookupInterfaceNumber = _AlaDot1xPortLookupInterfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 2, 1, 4),
    _AlaDot1xPortLookupInterfaceNumber_Type()
)
alaDot1xPortLookupInterfaceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xPortLookupInterfaceNumber.setStatus("current")
_AlaDot1xMacTable_Object = MibTable
alaDot1xMacTable = _AlaDot1xMacTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alaDot1xMacTable.setStatus("current")
_AlaDot1xMacEntry_Object = MibTableRow
alaDot1xMacEntry = _AlaDot1xMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 4, 1)
)
alaDot1xMacEntry.setIndexNames(
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaDot1xMACAddress"),
)
if mibBuilder.loadTexts:
    alaDot1xMacEntry.setStatus("current")
_AlaDot1xMACAddress_Type = MacAddress
_AlaDot1xMACAddress_Object = MibTableColumn
alaDot1xMACAddress = _AlaDot1xMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 4, 1, 1),
    _AlaDot1xMACAddress_Type()
)
alaDot1xMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDot1xMACAddress.setStatus("current")
_AlaDot1xMacIfIndex_Type = InterfaceIndex
_AlaDot1xMacIfIndex_Object = MibTableColumn
alaDot1xMacIfIndex = _AlaDot1xMacIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 4, 1, 2),
    _AlaDot1xMacIfIndex_Type()
)
alaDot1xMacIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xMacIfIndex.setStatus("current")


class _AlaDot1xMacSlotNumber_Type(Integer32):
    """Custom type alaDot1xMacSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AlaDot1xMacSlotNumber_Type.__name__ = "Integer32"
_AlaDot1xMacSlotNumber_Object = MibTableColumn
alaDot1xMacSlotNumber = _AlaDot1xMacSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 4, 1, 3),
    _AlaDot1xMacSlotNumber_Type()
)
alaDot1xMacSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xMacSlotNumber.setStatus("current")


class _AlaDot1xMacPortNumber_Type(Integer32):
    """Custom type alaDot1xMacPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_AlaDot1xMacPortNumber_Type.__name__ = "Integer32"
_AlaDot1xMacPortNumber_Object = MibTableColumn
alaDot1xMacPortNumber = _AlaDot1xMacPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 4, 1, 4),
    _AlaDot1xMacPortNumber_Type()
)
alaDot1xMacPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xMacPortNumber.setStatus("current")


class _AlaDot1xMacVlan_Type(Integer32):
    """Custom type alaDot1xMacVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AlaDot1xMacVlan_Type.__name__ = "Integer32"
_AlaDot1xMacVlan_Object = MibTableColumn
alaDot1xMacVlan = _AlaDot1xMacVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 4, 1, 5),
    _AlaDot1xMacVlan_Type()
)
alaDot1xMacVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xMacVlan.setStatus("current")


class _AlaDot1xMacProtocol_Type(Integer32):
    """Custom type alaDot1xMacProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AlaDot1xMacProtocol_Type.__name__ = "Integer32"
_AlaDot1xMacProtocol_Object = MibTableColumn
alaDot1xMacProtocol = _AlaDot1xMacProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 4, 1, 6),
    _AlaDot1xMacProtocol_Type()
)
alaDot1xMacProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xMacProtocol.setStatus("current")


class _AlaDot1xMacUserName_Type(DisplayString):
    """Custom type alaDot1xMacUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AlaDot1xMacUserName_Type.__name__ = "DisplayString"
_AlaDot1xMacUserName_Object = MibTableColumn
alaDot1xMacUserName = _AlaDot1xMacUserName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 4, 1, 7),
    _AlaDot1xMacUserName_Type()
)
alaDot1xMacUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xMacUserName.setStatus("current")


class _AlaDot1xMacState_Type(Integer32):
    """Custom type alaDot1xMacState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("aborting", 6),
          ("authenticated", 5),
          ("authenticatedLocally", 10),
          ("authenticating", 4),
          ("connecting", 3),
          ("disconnected", 2),
          ("forceAuthenticated", 8),
          ("forceUnauthenticated", 9),
          ("held", 7),
          ("initialize", 1))
    )


_AlaDot1xMacState_Type.__name__ = "Integer32"
_AlaDot1xMacState_Object = MibTableColumn
alaDot1xMacState = _AlaDot1xMacState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 4, 1, 8),
    _AlaDot1xMacState_Type()
)
alaDot1xMacState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xMacState.setStatus("current")
_AlaDot1xMacSupplicantPolicyUsed_Type = ALADot1xClassificationPolicyType
_AlaDot1xMacSupplicantPolicyUsed_Object = MibTableColumn
alaDot1xMacSupplicantPolicyUsed = _AlaDot1xMacSupplicantPolicyUsed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 4, 1, 9),
    _AlaDot1xMacSupplicantPolicyUsed_Type()
)
alaDot1xMacSupplicantPolicyUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xMacSupplicantPolicyUsed.setStatus("current")
_AlaDot1xNonSupplicantTable_Object = MibTable
alaDot1xNonSupplicantTable = _AlaDot1xNonSupplicantTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 5)
)
if mibBuilder.loadTexts:
    alaDot1xNonSupplicantTable.setStatus("current")
_AlaDot1xNonSupplicantEntry_Object = MibTableRow
alaDot1xNonSupplicantEntry = _AlaDot1xNonSupplicantEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 5, 1)
)
alaDot1xNonSupplicantEntry.setIndexNames(
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaDot1xNonSupplicantIntfNum"),
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaDot1xNonSupplicantMACAddress"),
)
if mibBuilder.loadTexts:
    alaDot1xNonSupplicantEntry.setStatus("current")
_AlaDot1xNonSupplicantIntfNum_Type = InterfaceIndex
_AlaDot1xNonSupplicantIntfNum_Object = MibTableColumn
alaDot1xNonSupplicantIntfNum = _AlaDot1xNonSupplicantIntfNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 5, 1, 1),
    _AlaDot1xNonSupplicantIntfNum_Type()
)
alaDot1xNonSupplicantIntfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xNonSupplicantIntfNum.setStatus("current")
_AlaDot1xNonSupplicantMACAddress_Type = MacAddress
_AlaDot1xNonSupplicantMACAddress_Object = MibTableColumn
alaDot1xNonSupplicantMACAddress = _AlaDot1xNonSupplicantMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 5, 1, 2),
    _AlaDot1xNonSupplicantMACAddress_Type()
)
alaDot1xNonSupplicantMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xNonSupplicantMACAddress.setStatus("current")


class _AlaDot1xNonSupplicantVlanID_Type(Integer32):
    """Custom type alaDot1xNonSupplicantVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AlaDot1xNonSupplicantVlanID_Type.__name__ = "Integer32"
_AlaDot1xNonSupplicantVlanID_Object = MibTableColumn
alaDot1xNonSupplicantVlanID = _AlaDot1xNonSupplicantVlanID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 5, 1, 3),
    _AlaDot1xNonSupplicantVlanID_Type()
)
alaDot1xNonSupplicantVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xNonSupplicantVlanID.setStatus("current")
_AlaDot1xNonSupplicantPolicyUsed_Type = ALADot1xClassificationPolicyType
_AlaDot1xNonSupplicantPolicyUsed_Object = MibTableColumn
alaDot1xNonSupplicantPolicyUsed = _AlaDot1xNonSupplicantPolicyUsed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 5, 1, 4),
    _AlaDot1xNonSupplicantPolicyUsed_Type()
)
alaDot1xNonSupplicantPolicyUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xNonSupplicantPolicyUsed.setStatus("current")


class _AlaDot1xAuthenticationStatus_Type(Integer32):
    """Custom type alaDot1xAuthenticationStatus based on Integer32"""
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
        *(("authenticated", 3),
          ("failed", 4),
          ("failedNoResources", 7),
          ("failedNoServer", 6),
          ("failedTimeout", 5),
          ("idle", 1),
          ("inProgress", 2))
    )


_AlaDot1xAuthenticationStatus_Type.__name__ = "Integer32"
_AlaDot1xAuthenticationStatus_Object = MibTableColumn
alaDot1xAuthenticationStatus = _AlaDot1xAuthenticationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 5, 1, 5),
    _AlaDot1xAuthenticationStatus_Type()
)
alaDot1xAuthenticationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xAuthenticationStatus.setStatus("current")
_AlaDot1xAuthPolicyTable_Object = MibTable
alaDot1xAuthPolicyTable = _AlaDot1xAuthPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 6)
)
if mibBuilder.loadTexts:
    alaDot1xAuthPolicyTable.setStatus("current")
_AlaDot1xAuthPolicyEntry_Object = MibTableRow
alaDot1xAuthPolicyEntry = _AlaDot1xAuthPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 6, 1)
)
alaDot1xAuthPolicyEntry.setIndexNames(
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaDot1xAuthPolicyIntfNumber"),
)
if mibBuilder.loadTexts:
    alaDot1xAuthPolicyEntry.setStatus("current")
_AlaDot1xAuthPolicyIntfNumber_Type = InterfaceIndex
_AlaDot1xAuthPolicyIntfNumber_Object = MibTableColumn
alaDot1xAuthPolicyIntfNumber = _AlaDot1xAuthPolicyIntfNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 6, 1, 1),
    _AlaDot1xAuthPolicyIntfNumber_Type()
)
alaDot1xAuthPolicyIntfNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDot1xAuthPolicyIntfNumber.setStatus("current")


class _AlaDot1xNonSuppPolicy_Type(DisplayString):
    """Custom type alaDot1xNonSuppPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AlaDot1xNonSuppPolicy_Type.__name__ = "DisplayString"
_AlaDot1xNonSuppPolicy_Object = MibTableColumn
alaDot1xNonSuppPolicy = _AlaDot1xNonSuppPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 6, 1, 2),
    _AlaDot1xNonSuppPolicy_Type()
)
alaDot1xNonSuppPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xNonSuppPolicy.setStatus("current")


class _AlaDot1xSuppPolicy_Type(DisplayString):
    """Custom type alaDot1xSuppPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AlaDot1xSuppPolicy_Type.__name__ = "DisplayString"
_AlaDot1xSuppPolicy_Object = MibTableColumn
alaDot1xSuppPolicy = _AlaDot1xSuppPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 6, 1, 3),
    _AlaDot1xSuppPolicy_Type()
)
alaDot1xSuppPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xSuppPolicy.setStatus("current")


class _AlaDot1xPollingCnt_Type(Integer32):
    """Custom type alaDot1xPollingCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AlaDot1xPollingCnt_Type.__name__ = "Integer32"
_AlaDot1xPollingCnt_Object = MibTableColumn
alaDot1xPollingCnt = _AlaDot1xPollingCnt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 6, 1, 4),
    _AlaDot1xPollingCnt_Type()
)
alaDot1xPollingCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xPollingCnt.setStatus("current")


class _AlaDot1xCaptivePortalPolicy_Type(DisplayString):
    """Custom type alaDot1xCaptivePortalPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AlaDot1xCaptivePortalPolicy_Type.__name__ = "DisplayString"
_AlaDot1xCaptivePortalPolicy_Object = MibTableColumn
alaDot1xCaptivePortalPolicy = _AlaDot1xCaptivePortalPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 6, 1, 5),
    _AlaDot1xCaptivePortalPolicy_Type()
)
alaDot1xCaptivePortalPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xCaptivePortalPolicy.setStatus("current")


class _AlaDot1xCPortalSessionLimit_Type(Integer32):
    """Custom type alaDot1xCPortalSessionLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AlaDot1xCPortalSessionLimit_Type.__name__ = "Integer32"
_AlaDot1xCPortalSessionLimit_Object = MibTableColumn
alaDot1xCPortalSessionLimit = _AlaDot1xCPortalSessionLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 6, 1, 6),
    _AlaDot1xCPortalSessionLimit_Type()
)
alaDot1xCPortalSessionLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xCPortalSessionLimit.setStatus("current")


class _AlaDot1xCPortalRetryCnt_Type(Integer32):
    """Custom type alaDot1xCPortalRetryCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AlaDot1xCPortalRetryCnt_Type.__name__ = "Integer32"
_AlaDot1xCPortalRetryCnt_Object = MibTableColumn
alaDot1xCPortalRetryCnt = _AlaDot1xCPortalRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 6, 1, 7),
    _AlaDot1xCPortalRetryCnt_Type()
)
alaDot1xCPortalRetryCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xCPortalRetryCnt.setStatus("current")
_AlaDot1xCportalConfig_ObjectIdentity = ObjectIdentity
alaDot1xCportalConfig = _AlaDot1xCportalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 7)
)
_AlaDot1xCPortalIpAddress_Type = IpAddress
_AlaDot1xCPortalIpAddress_Object = MibScalar
alaDot1xCPortalIpAddress = _AlaDot1xCPortalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 7, 1),
    _AlaDot1xCPortalIpAddress_Type()
)
alaDot1xCPortalIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xCPortalIpAddress.setStatus("current")


class _AlaDot1xCPortalProxyURL_Type(SnmpAdminString):
    """Custom type alaDot1xCPortalProxyURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AlaDot1xCPortalProxyURL_Type.__name__ = "SnmpAdminString"
_AlaDot1xCPortalProxyURL_Object = MibScalar
alaDot1xCPortalProxyURL = _AlaDot1xCPortalProxyURL_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 7, 2),
    _AlaDot1xCPortalProxyURL_Type()
)
alaDot1xCPortalProxyURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xCPortalProxyURL.setStatus("current")


class _AlaDot1xCPortalPostAuthSuccessRedirectURL_Type(SnmpAdminString):
    """Custom type alaDot1xCPortalPostAuthSuccessRedirectURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AlaDot1xCPortalPostAuthSuccessRedirectURL_Type.__name__ = "SnmpAdminString"
_AlaDot1xCPortalPostAuthSuccessRedirectURL_Object = MibScalar
alaDot1xCPortalPostAuthSuccessRedirectURL = _AlaDot1xCPortalPostAuthSuccessRedirectURL_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 7, 3),
    _AlaDot1xCPortalPostAuthSuccessRedirectURL_Type()
)
alaDot1xCPortalPostAuthSuccessRedirectURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xCPortalPostAuthSuccessRedirectURL.setStatus("current")


class _AlaDot1xCPortalPostAuthFailRedirectURL_Type(SnmpAdminString):
    """Custom type alaDot1xCPortalPostAuthFailRedirectURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AlaDot1xCPortalPostAuthFailRedirectURL_Type.__name__ = "SnmpAdminString"
_AlaDot1xCPortalPostAuthFailRedirectURL_Object = MibScalar
alaDot1xCPortalPostAuthFailRedirectURL = _AlaDot1xCPortalPostAuthFailRedirectURL_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 7, 4),
    _AlaDot1xCPortalPostAuthFailRedirectURL_Type()
)
alaDot1xCPortalPostAuthFailRedirectURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xCPortalPostAuthFailRedirectURL.setStatus("current")


class _AlaDot1xCPortalDNSKeyword1_Type(SnmpAdminString):
    """Custom type alaDot1xCPortalDNSKeyword1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AlaDot1xCPortalDNSKeyword1_Type.__name__ = "SnmpAdminString"
_AlaDot1xCPortalDNSKeyword1_Object = MibScalar
alaDot1xCPortalDNSKeyword1 = _AlaDot1xCPortalDNSKeyword1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 7, 5),
    _AlaDot1xCPortalDNSKeyword1_Type()
)
alaDot1xCPortalDNSKeyword1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xCPortalDNSKeyword1.setStatus("current")


class _AlaDot1xCPortalDNSKeyword2_Type(SnmpAdminString):
    """Custom type alaDot1xCPortalDNSKeyword2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AlaDot1xCPortalDNSKeyword2_Type.__name__ = "SnmpAdminString"
_AlaDot1xCPortalDNSKeyword2_Object = MibScalar
alaDot1xCPortalDNSKeyword2 = _AlaDot1xCPortalDNSKeyword2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 7, 6),
    _AlaDot1xCPortalDNSKeyword2_Type()
)
alaDot1xCPortalDNSKeyword2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xCPortalDNSKeyword2.setStatus("current")


class _AlaDot1xCPortalDNSKeyword3_Type(SnmpAdminString):
    """Custom type alaDot1xCPortalDNSKeyword3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AlaDot1xCPortalDNSKeyword3_Type.__name__ = "SnmpAdminString"
_AlaDot1xCPortalDNSKeyword3_Object = MibScalar
alaDot1xCPortalDNSKeyword3 = _AlaDot1xCPortalDNSKeyword3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 7, 7),
    _AlaDot1xCPortalDNSKeyword3_Type()
)
alaDot1xCPortalDNSKeyword3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xCPortalDNSKeyword3.setStatus("current")


class _AlaDot1xCPortalDNSKeyword4_Type(SnmpAdminString):
    """Custom type alaDot1xCPortalDNSKeyword4 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AlaDot1xCPortalDNSKeyword4_Type.__name__ = "SnmpAdminString"
_AlaDot1xCPortalDNSKeyword4_Object = MibScalar
alaDot1xCPortalDNSKeyword4 = _AlaDot1xCPortalDNSKeyword4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 7, 8),
    _AlaDot1xCPortalDNSKeyword4_Type()
)
alaDot1xCPortalDNSKeyword4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xCPortalDNSKeyword4.setStatus("current")
_AlaDot1xDeviceStatusTable_Object = MibTable
alaDot1xDeviceStatusTable = _AlaDot1xDeviceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 8)
)
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusTable.setStatus("current")
_AlaDot1xDeviceStatusEntry_Object = MibTableRow
alaDot1xDeviceStatusEntry = _AlaDot1xDeviceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 8, 1)
)
alaDot1xDeviceStatusEntry.setIndexNames(
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaDot1xDeviceStatusMacQueryType"),
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaDot1xDeviceStatusSlotNumber"),
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaDot1xDeviceStatusPortNumber"),
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaDot1xDeviceStatusMACAddress"),
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaDot1xDeviceStatusDeviceType"),
)
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusEntry.setStatus("current")
_AlaDot1xDeviceStatusMacQueryType_Type = ALADot1xMacQueryType
_AlaDot1xDeviceStatusMacQueryType_Object = MibTableColumn
alaDot1xDeviceStatusMacQueryType = _AlaDot1xDeviceStatusMacQueryType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 8, 1, 1),
    _AlaDot1xDeviceStatusMacQueryType_Type()
)
alaDot1xDeviceStatusMacQueryType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusMacQueryType.setStatus("current")


class _AlaDot1xDeviceStatusSlotNumber_Type(Integer32):
    """Custom type alaDot1xDeviceStatusSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AlaDot1xDeviceStatusSlotNumber_Type.__name__ = "Integer32"
_AlaDot1xDeviceStatusSlotNumber_Object = MibTableColumn
alaDot1xDeviceStatusSlotNumber = _AlaDot1xDeviceStatusSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 8, 1, 2),
    _AlaDot1xDeviceStatusSlotNumber_Type()
)
alaDot1xDeviceStatusSlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusSlotNumber.setStatus("current")


class _AlaDot1xDeviceStatusPortNumber_Type(Integer32):
    """Custom type alaDot1xDeviceStatusPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_AlaDot1xDeviceStatusPortNumber_Type.__name__ = "Integer32"
_AlaDot1xDeviceStatusPortNumber_Object = MibTableColumn
alaDot1xDeviceStatusPortNumber = _AlaDot1xDeviceStatusPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 8, 1, 3),
    _AlaDot1xDeviceStatusPortNumber_Type()
)
alaDot1xDeviceStatusPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusPortNumber.setStatus("current")
_AlaDot1xDeviceStatusMACAddress_Type = MacAddress
_AlaDot1xDeviceStatusMACAddress_Object = MibTableColumn
alaDot1xDeviceStatusMACAddress = _AlaDot1xDeviceStatusMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 8, 1, 4),
    _AlaDot1xDeviceStatusMACAddress_Type()
)
alaDot1xDeviceStatusMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusMACAddress.setStatus("current")
_AlaDot1xDeviceStatusDeviceType_Type = ALADot1xDeviceType
_AlaDot1xDeviceStatusDeviceType_Object = MibTableColumn
alaDot1xDeviceStatusDeviceType = _AlaDot1xDeviceStatusDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 8, 1, 5),
    _AlaDot1xDeviceStatusDeviceType_Type()
)
alaDot1xDeviceStatusDeviceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusDeviceType.setStatus("current")


class _AlaDot1xDeviceStatusVlan_Type(Integer32):
    """Custom type alaDot1xDeviceStatusVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AlaDot1xDeviceStatusVlan_Type.__name__ = "Integer32"
_AlaDot1xDeviceStatusVlan_Object = MibTableColumn
alaDot1xDeviceStatusVlan = _AlaDot1xDeviceStatusVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 8, 1, 6),
    _AlaDot1xDeviceStatusVlan_Type()
)
alaDot1xDeviceStatusVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusVlan.setStatus("current")
_AlaDot1xDeviceStatusIPAddress_Type = IpAddress
_AlaDot1xDeviceStatusIPAddress_Object = MibTableColumn
alaDot1xDeviceStatusIPAddress = _AlaDot1xDeviceStatusIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 8, 1, 7),
    _AlaDot1xDeviceStatusIPAddress_Type()
)
alaDot1xDeviceStatusIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusIPAddress.setStatus("current")
_AlaDot1xDeviceStatusUserName_Type = SnmpAdminString
_AlaDot1xDeviceStatusUserName_Object = MibTableColumn
alaDot1xDeviceStatusUserName = _AlaDot1xDeviceStatusUserName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 8, 1, 8),
    _AlaDot1xDeviceStatusUserName_Type()
)
alaDot1xDeviceStatusUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusUserName.setStatus("current")
_AlaDot1xDeviceStatusProfileUsed_Type = SnmpAdminString
_AlaDot1xDeviceStatusProfileUsed_Object = MibTableColumn
alaDot1xDeviceStatusProfileUsed = _AlaDot1xDeviceStatusProfileUsed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 8, 1, 9),
    _AlaDot1xDeviceStatusProfileUsed_Type()
)
alaDot1xDeviceStatusProfileUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusProfileUsed.setStatus("current")
_AlaDot1xDeviceStatusAuthType_Type = ALADot1xAuthenticationType
_AlaDot1xDeviceStatusAuthType_Object = MibTableColumn
alaDot1xDeviceStatusAuthType = _AlaDot1xDeviceStatusAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 8, 1, 10),
    _AlaDot1xDeviceStatusAuthType_Type()
)
alaDot1xDeviceStatusAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusAuthType.setStatus("current")
_AlaDot1xDeviceStatusPolicyUsed_Type = ALADot1xClassificationPolicyType
_AlaDot1xDeviceStatusPolicyUsed_Object = MibTableColumn
alaDot1xDeviceStatusPolicyUsed = _AlaDot1xDeviceStatusPolicyUsed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 8, 1, 11),
    _AlaDot1xDeviceStatusPolicyUsed_Type()
)
alaDot1xDeviceStatusPolicyUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusPolicyUsed.setStatus("current")
_AlaDot1xDeviceStatusAuthResult_Type = ALADot1xAuthenticationResult
_AlaDot1xDeviceStatusAuthResult_Object = MibTableColumn
alaDot1xDeviceStatusAuthResult = _AlaDot1xDeviceStatusAuthResult_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 8, 1, 12),
    _AlaDot1xDeviceStatusAuthResult_Type()
)
alaDot1xDeviceStatusAuthResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusAuthResult.setStatus("current")
_AlaDot1xDeviceStatusMacLearntState_Type = ALADot1xMacLearntState
_AlaDot1xDeviceStatusMacLearntState_Object = MibTableColumn
alaDot1xDeviceStatusMacLearntState = _AlaDot1xDeviceStatusMacLearntState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 8, 1, 13),
    _AlaDot1xDeviceStatusMacLearntState_Type()
)
alaDot1xDeviceStatusMacLearntState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusMacLearntState.setStatus("current")
_AlaDot1xDeviceStatusTimeLearned_Type = TimeStamp
_AlaDot1xDeviceStatusTimeLearned_Object = MibTableColumn
alaDot1xDeviceStatusTimeLearned = _AlaDot1xDeviceStatusTimeLearned_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 8, 1, 14),
    _AlaDot1xDeviceStatusTimeLearned_Type()
)
alaDot1xDeviceStatusTimeLearned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusTimeLearned.setStatus("current")
_AlaDot1xDeviceStatusCaptivePortalUsed_Type = TruthValue
_AlaDot1xDeviceStatusCaptivePortalUsed_Object = MibTableColumn
alaDot1xDeviceStatusCaptivePortalUsed = _AlaDot1xDeviceStatusCaptivePortalUsed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 8, 1, 15),
    _AlaDot1xDeviceStatusCaptivePortalUsed_Type()
)
alaDot1xDeviceStatusCaptivePortalUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusCaptivePortalUsed.setStatus("current")
_AlaDot1xAdminLogoutParams_ObjectIdentity = ObjectIdentity
alaDot1xAdminLogoutParams = _AlaDot1xAdminLogoutParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 9)
)


class _AlaDot1xAdminLogoutType_Type(Integer32):
    """Custom type alaDot1xAdminLogoutType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("interfaceId", 4),
          ("macAddress", 1),
          ("networkProfileName", 3),
          ("noOperation", 0),
          ("username", 2))
    )


_AlaDot1xAdminLogoutType_Type.__name__ = "Integer32"
_AlaDot1xAdminLogoutType_Object = MibScalar
alaDot1xAdminLogoutType = _AlaDot1xAdminLogoutType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 9, 1),
    _AlaDot1xAdminLogoutType_Type()
)
alaDot1xAdminLogoutType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xAdminLogoutType.setStatus("current")
_AlaDot1xAdminLogoutMacAddress_Type = MacAddress
_AlaDot1xAdminLogoutMacAddress_Object = MibScalar
alaDot1xAdminLogoutMacAddress = _AlaDot1xAdminLogoutMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 9, 2),
    _AlaDot1xAdminLogoutMacAddress_Type()
)
alaDot1xAdminLogoutMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xAdminLogoutMacAddress.setStatus("current")


class _AlaDot1xAdminLogoutUserName_Type(SnmpAdminString):
    """Custom type alaDot1xAdminLogoutUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDot1xAdminLogoutUserName_Type.__name__ = "SnmpAdminString"
_AlaDot1xAdminLogoutUserName_Object = MibScalar
alaDot1xAdminLogoutUserName = _AlaDot1xAdminLogoutUserName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 9, 3),
    _AlaDot1xAdminLogoutUserName_Type()
)
alaDot1xAdminLogoutUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xAdminLogoutUserName.setStatus("current")


class _AlaDot1xAdminLogoutNetworkProfileName_Type(SnmpAdminString):
    """Custom type alaDot1xAdminLogoutNetworkProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDot1xAdminLogoutNetworkProfileName_Type.__name__ = "SnmpAdminString"
_AlaDot1xAdminLogoutNetworkProfileName_Object = MibScalar
alaDot1xAdminLogoutNetworkProfileName = _AlaDot1xAdminLogoutNetworkProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 9, 4),
    _AlaDot1xAdminLogoutNetworkProfileName_Type()
)
alaDot1xAdminLogoutNetworkProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xAdminLogoutNetworkProfileName.setStatus("current")
_AlaDot1xAdminLogoutInterfaceId_Type = InterfaceIndexOrZero
_AlaDot1xAdminLogoutInterfaceId_Object = MibScalar
alaDot1xAdminLogoutInterfaceId = _AlaDot1xAdminLogoutInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 9, 5),
    _AlaDot1xAdminLogoutInterfaceId_Type()
)
alaDot1xAdminLogoutInterfaceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xAdminLogoutInterfaceId.setStatus("current")
_AlaDot1xAuthServerTimeout_ObjectIdentity = ObjectIdentity
alaDot1xAuthServerTimeout = _AlaDot1xAuthServerTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 10)
)


class _AlaDot1xAuthSvrTimeoutPolicy_Type(DisplayString):
    """Custom type alaDot1xAuthSvrTimeoutPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AlaDot1xAuthSvrTimeoutPolicy_Type.__name__ = "DisplayString"
_AlaDot1xAuthSvrTimeoutPolicy_Object = MibScalar
alaDot1xAuthSvrTimeoutPolicy = _AlaDot1xAuthSvrTimeoutPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 10, 1),
    _AlaDot1xAuthSvrTimeoutPolicy_Type()
)
alaDot1xAuthSvrTimeoutPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xAuthSvrTimeoutPolicy.setStatus("current")


class _AlaDot1xAuthSvrTimeoutReAuthPeriod_Type(Integer32):
    """Custom type alaDot1xAuthSvrTimeoutReAuthPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 9999),
    )


_AlaDot1xAuthSvrTimeoutReAuthPeriod_Type.__name__ = "Integer32"
_AlaDot1xAuthSvrTimeoutReAuthPeriod_Object = MibScalar
alaDot1xAuthSvrTimeoutReAuthPeriod = _AlaDot1xAuthSvrTimeoutReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 10, 2),
    _AlaDot1xAuthSvrTimeoutReAuthPeriod_Type()
)
alaDot1xAuthSvrTimeoutReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xAuthSvrTimeoutReAuthPeriod.setStatus("current")


class _AlaDot1xAuthSvrTimeoutStatus_Type(Integer32):
    """Custom type alaDot1xAuthSvrTimeoutStatus based on Integer32"""
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


_AlaDot1xAuthSvrTimeoutStatus_Type.__name__ = "Integer32"
_AlaDot1xAuthSvrTimeoutStatus_Object = MibScalar
alaDot1xAuthSvrTimeoutStatus = _AlaDot1xAuthSvrTimeoutStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 10, 3),
    _AlaDot1xAuthSvrTimeoutStatus_Type()
)
alaDot1xAuthSvrTimeoutStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xAuthSvrTimeoutStatus.setStatus("current")
_AlaPassthroughConfig_ObjectIdentity = ObjectIdentity
alaPassthroughConfig = _AlaPassthroughConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 11)
)
_AlaDot1xPassthroughStatus_Type = AlaPassThroughStatus
_AlaDot1xPassthroughStatus_Object = MibScalar
alaDot1xPassthroughStatus = _AlaDot1xPassthroughStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 11, 1),
    _AlaDot1xPassthroughStatus_Type()
)
alaDot1xPassthroughStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xPassthroughStatus.setStatus("obsolete")
_AlaAvlanPassthroughStatus_Type = AlaPassThroughStatus
_AlaAvlanPassthroughStatus_Object = MibScalar
alaAvlanPassthroughStatus = _AlaAvlanPassthroughStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 1, 11, 2),
    _AlaAvlanPassthroughStatus_Type()
)
alaAvlanPassthroughStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAvlanPassthroughStatus.setStatus("obsolete")
_AlaIND1Dot1XMIBConformance_ObjectIdentity = ObjectIdentity
alaIND1Dot1XMIBConformance = _AlaIND1Dot1XMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 2)
)
if mibBuilder.loadTexts:
    alaIND1Dot1XMIBConformance.setStatus("current")
_AlaIND1Dot1XMIBGroups_ObjectIdentity = ObjectIdentity
alaIND1Dot1XMIBGroups = _AlaIND1Dot1XMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alaIND1Dot1XMIBGroups.setStatus("current")

# Managed Objects groups

alaINDDot1XPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 2, 1, 1)
)
alaINDDot1XPortGroup.setObjects(
      *(("ALCATEL-IND1-DOT1X-MIB", "alaDot1xPortSlotNumber"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xPortPortNumber"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xPortMACAddress"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xPortVlan"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xPortProtocol"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xPortUserName"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xPortState"))
)
if mibBuilder.loadTexts:
    alaINDDot1XPortGroup.setStatus("current")

alaDot1xPortLookupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 2, 1, 2)
)
alaDot1xPortLookupGroup.setObjects(
      *(("ALCATEL-IND1-DOT1X-MIB", "alaDot1xPortLookupSlotNumber"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xPortLookupPortNumber"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xPortLookupMACAddress"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xPortLookupInterfaceNumber"))
)
if mibBuilder.loadTexts:
    alaDot1xPortLookupGroup.setStatus("current")

alaINDDot1XPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 2, 1, 3)
)
alaINDDot1XPolicyGroup.setObjects(
      *(("ALCATEL-IND1-DOT1X-MIB", "alaDot1xNonSuppPolicy"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xSuppPolicy"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xPollingCnt"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xCaptivePortalPolicy"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xCPortalSessionLimit"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xCPortalRetryCnt"))
)
if mibBuilder.loadTexts:
    alaINDDot1XPolicyGroup.setStatus("current")

alaINDDot1XDeviceStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 2, 1, 4)
)
alaINDDot1XDeviceStatusGroup.setObjects(
      *(("ALCATEL-IND1-DOT1X-MIB", "alaDot1xDeviceStatusVlan"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xDeviceStatusIPAddress"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xDeviceStatusUserName"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xDeviceStatusProfileUsed"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xDeviceStatusAuthType"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xDeviceStatusPolicyUsed"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xDeviceStatusAuthResult"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xDeviceStatusMacLearntState"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xDeviceStatusTimeLearned"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xDeviceStatusCaptivePortalUsed"))
)
if mibBuilder.loadTexts:
    alaINDDot1XDeviceStatusGroup.setStatus("current")

alaDot1xAuthSvrTimeoutGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 2, 1, 5)
)
alaDot1xAuthSvrTimeoutGroup.setObjects(
      *(("ALCATEL-IND1-DOT1X-MIB", "alaDot1xAuthSvrTimeoutPolicy"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xAuthSvrTimeoutReAuthPeriod"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xAuthSvrTimeoutStatus"))
)
if mibBuilder.loadTexts:
    alaDot1xAuthSvrTimeoutGroup.setStatus("current")

alaPassthroughConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 2, 1, 6)
)
alaPassthroughConfigGroup.setObjects(
      *(("ALCATEL-IND1-DOT1X-MIB", "alaDot1xPassthroughStatus"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaAvlanPassthroughStatus"))
)
if mibBuilder.loadTexts:
    alaPassthroughConfigGroup.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alaIND1Dot1XMIBCompliances = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alaIND1Dot1XMIBCompliances.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-DOT1X-MIB",
    **{"ALADot1xClassificationPolicyType": ALADot1xClassificationPolicyType,
       "ALADot1xAuthenticationType": ALADot1xAuthenticationType,
       "ALADot1xAuthenticationResult": ALADot1xAuthenticationResult,
       "ALADot1xMacLearntState": ALADot1xMacLearntState,
       "ALADot1xMacQueryType": ALADot1xMacQueryType,
       "ALADot1xDeviceType": ALADot1xDeviceType,
       "AlaPassThroughStatus": AlaPassThroughStatus,
       "alcatelIND1Dot1XMIB": alcatelIND1Dot1XMIB,
       "alaIND1Dot1XMIBObjects": alaIND1Dot1XMIBObjects,
       "alaDot1xPortTable": alaDot1xPortTable,
       "alaDot1xPortEntry": alaDot1xPortEntry,
       "alaDot1xPortSlotNumber": alaDot1xPortSlotNumber,
       "alaDot1xPortPortNumber": alaDot1xPortPortNumber,
       "alaDot1xPortMACAddress": alaDot1xPortMACAddress,
       "alaDot1xPortVlan": alaDot1xPortVlan,
       "alaDot1xPortProtocol": alaDot1xPortProtocol,
       "alaDot1xPortUserName": alaDot1xPortUserName,
       "alaDot1xPortState": alaDot1xPortState,
       "alaDot1xSupplicantPolicyUsed": alaDot1xSupplicantPolicyUsed,
       "alaDot1xPortLookupTable": alaDot1xPortLookupTable,
       "alaDot1xPortLookupEntry": alaDot1xPortLookupEntry,
       "alaDot1xPortLookupSlotNumber": alaDot1xPortLookupSlotNumber,
       "alaDot1xPortLookupPortNumber": alaDot1xPortLookupPortNumber,
       "alaDot1xPortLookupMACAddress": alaDot1xPortLookupMACAddress,
       "alaDot1xPortLookupInterfaceNumber": alaDot1xPortLookupInterfaceNumber,
       "alaDot1xMacTable": alaDot1xMacTable,
       "alaDot1xMacEntry": alaDot1xMacEntry,
       "alaDot1xMACAddress": alaDot1xMACAddress,
       "alaDot1xMacIfIndex": alaDot1xMacIfIndex,
       "alaDot1xMacSlotNumber": alaDot1xMacSlotNumber,
       "alaDot1xMacPortNumber": alaDot1xMacPortNumber,
       "alaDot1xMacVlan": alaDot1xMacVlan,
       "alaDot1xMacProtocol": alaDot1xMacProtocol,
       "alaDot1xMacUserName": alaDot1xMacUserName,
       "alaDot1xMacState": alaDot1xMacState,
       "alaDot1xMacSupplicantPolicyUsed": alaDot1xMacSupplicantPolicyUsed,
       "alaDot1xNonSupplicantTable": alaDot1xNonSupplicantTable,
       "alaDot1xNonSupplicantEntry": alaDot1xNonSupplicantEntry,
       "alaDot1xNonSupplicantIntfNum": alaDot1xNonSupplicantIntfNum,
       "alaDot1xNonSupplicantMACAddress": alaDot1xNonSupplicantMACAddress,
       "alaDot1xNonSupplicantVlanID": alaDot1xNonSupplicantVlanID,
       "alaDot1xNonSupplicantPolicyUsed": alaDot1xNonSupplicantPolicyUsed,
       "alaDot1xAuthenticationStatus": alaDot1xAuthenticationStatus,
       "alaDot1xAuthPolicyTable": alaDot1xAuthPolicyTable,
       "alaDot1xAuthPolicyEntry": alaDot1xAuthPolicyEntry,
       "alaDot1xAuthPolicyIntfNumber": alaDot1xAuthPolicyIntfNumber,
       "alaDot1xNonSuppPolicy": alaDot1xNonSuppPolicy,
       "alaDot1xSuppPolicy": alaDot1xSuppPolicy,
       "alaDot1xPollingCnt": alaDot1xPollingCnt,
       "alaDot1xCaptivePortalPolicy": alaDot1xCaptivePortalPolicy,
       "alaDot1xCPortalSessionLimit": alaDot1xCPortalSessionLimit,
       "alaDot1xCPortalRetryCnt": alaDot1xCPortalRetryCnt,
       "alaDot1xCportalConfig": alaDot1xCportalConfig,
       "alaDot1xCPortalIpAddress": alaDot1xCPortalIpAddress,
       "alaDot1xCPortalProxyURL": alaDot1xCPortalProxyURL,
       "alaDot1xCPortalPostAuthSuccessRedirectURL": alaDot1xCPortalPostAuthSuccessRedirectURL,
       "alaDot1xCPortalPostAuthFailRedirectURL": alaDot1xCPortalPostAuthFailRedirectURL,
       "alaDot1xCPortalDNSKeyword1": alaDot1xCPortalDNSKeyword1,
       "alaDot1xCPortalDNSKeyword2": alaDot1xCPortalDNSKeyword2,
       "alaDot1xCPortalDNSKeyword3": alaDot1xCPortalDNSKeyword3,
       "alaDot1xCPortalDNSKeyword4": alaDot1xCPortalDNSKeyword4,
       "alaDot1xDeviceStatusTable": alaDot1xDeviceStatusTable,
       "alaDot1xDeviceStatusEntry": alaDot1xDeviceStatusEntry,
       "alaDot1xDeviceStatusMacQueryType": alaDot1xDeviceStatusMacQueryType,
       "alaDot1xDeviceStatusSlotNumber": alaDot1xDeviceStatusSlotNumber,
       "alaDot1xDeviceStatusPortNumber": alaDot1xDeviceStatusPortNumber,
       "alaDot1xDeviceStatusMACAddress": alaDot1xDeviceStatusMACAddress,
       "alaDot1xDeviceStatusDeviceType": alaDot1xDeviceStatusDeviceType,
       "alaDot1xDeviceStatusVlan": alaDot1xDeviceStatusVlan,
       "alaDot1xDeviceStatusIPAddress": alaDot1xDeviceStatusIPAddress,
       "alaDot1xDeviceStatusUserName": alaDot1xDeviceStatusUserName,
       "alaDot1xDeviceStatusProfileUsed": alaDot1xDeviceStatusProfileUsed,
       "alaDot1xDeviceStatusAuthType": alaDot1xDeviceStatusAuthType,
       "alaDot1xDeviceStatusPolicyUsed": alaDot1xDeviceStatusPolicyUsed,
       "alaDot1xDeviceStatusAuthResult": alaDot1xDeviceStatusAuthResult,
       "alaDot1xDeviceStatusMacLearntState": alaDot1xDeviceStatusMacLearntState,
       "alaDot1xDeviceStatusTimeLearned": alaDot1xDeviceStatusTimeLearned,
       "alaDot1xDeviceStatusCaptivePortalUsed": alaDot1xDeviceStatusCaptivePortalUsed,
       "alaDot1xAdminLogoutParams": alaDot1xAdminLogoutParams,
       "alaDot1xAdminLogoutType": alaDot1xAdminLogoutType,
       "alaDot1xAdminLogoutMacAddress": alaDot1xAdminLogoutMacAddress,
       "alaDot1xAdminLogoutUserName": alaDot1xAdminLogoutUserName,
       "alaDot1xAdminLogoutNetworkProfileName": alaDot1xAdminLogoutNetworkProfileName,
       "alaDot1xAdminLogoutInterfaceId": alaDot1xAdminLogoutInterfaceId,
       "alaDot1xAuthServerTimeout": alaDot1xAuthServerTimeout,
       "alaDot1xAuthSvrTimeoutPolicy": alaDot1xAuthSvrTimeoutPolicy,
       "alaDot1xAuthSvrTimeoutReAuthPeriod": alaDot1xAuthSvrTimeoutReAuthPeriod,
       "alaDot1xAuthSvrTimeoutStatus": alaDot1xAuthSvrTimeoutStatus,
       "alaPassthroughConfig": alaPassthroughConfig,
       "alaDot1xPassthroughStatus": alaDot1xPassthroughStatus,
       "alaAvlanPassthroughStatus": alaAvlanPassthroughStatus,
       "alaIND1Dot1XMIBConformance": alaIND1Dot1XMIBConformance,
       "alaIND1Dot1XMIBGroups": alaIND1Dot1XMIBGroups,
       "alaINDDot1XPortGroup": alaINDDot1XPortGroup,
       "alaDot1xPortLookupGroup": alaDot1xPortLookupGroup,
       "alaINDDot1XPolicyGroup": alaINDDot1XPolicyGroup,
       "alaINDDot1XDeviceStatusGroup": alaINDDot1XDeviceStatusGroup,
       "alaDot1xAuthSvrTimeoutGroup": alaDot1xAuthSvrTimeoutGroup,
       "alaPassthroughConfigGroup": alaPassthroughConfigGroup,
       "alaIND1Dot1XMIBCompliances": alaIND1Dot1XMIBCompliances}
)
