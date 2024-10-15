# SNMP MIB module (AP-MANAGEMENT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AP-MANAGEMENT
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:03 2024
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

ap_management_mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Pepwave_ObjectIdentity = ObjectIdentity
pepwave = _Pepwave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662)
)
_ProductID_ObjectIdentity = ObjectIdentity
productID = _ProductID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200)
)
_ApMib_ObjectIdentity = ObjectIdentity
apMib = _ApMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1)
)
_ApGeneralMib_ObjectIdentity = ObjectIdentity
apGeneralMib = _ApGeneralMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1)
)
_ApWeb_ObjectIdentity = ObjectIdentity
apWeb = _ApWeb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 1)
)
_ApWebAdmin_ObjectIdentity = ObjectIdentity
apWebAdmin = _ApWebAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 1, 1)
)


class _ApWebAccessProtocol_Type(Integer32):
    """Custom type apWebAccessProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("http", 0),
          ("https", 1))
    )


_ApWebAccessProtocol_Type.__name__ = "Integer32"
_ApWebAccessProtocol_Object = MibScalar
apWebAccessProtocol = _ApWebAccessProtocol_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 1, 1, 1),
    _ApWebAccessProtocol_Type()
)
apWebAccessProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWebAccessProtocol.setStatus("current")


class _ApWebManagementPort_Type(Integer32):
    """Custom type apWebManagementPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApWebManagementPort_Type.__name__ = "Integer32"
_ApWebManagementPort_Object = MibScalar
apWebManagementPort = _ApWebManagementPort_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 1, 1, 2),
    _ApWebManagementPort_Type()
)
apWebManagementPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWebManagementPort.setStatus("current")


class _ApWebHttpRedirection_Type(Integer32):
    """Custom type apWebHttpRedirection based on Integer32"""
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


_ApWebHttpRedirection_Type.__name__ = "Integer32"
_ApWebHttpRedirection_Object = MibScalar
apWebHttpRedirection = _ApWebHttpRedirection_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 1, 1, 3),
    _ApWebHttpRedirection_Type()
)
apWebHttpRedirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWebHttpRedirection.setStatus("current")


class _ApWebUsername_Type(OctetString):
    """Custom type apWebUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApWebUsername_Type.__name__ = "OctetString"
_ApWebUsername_Object = MibScalar
apWebUsername = _ApWebUsername_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 1, 1, 4),
    _ApWebUsername_Type()
)
apWebUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWebUsername.setStatus("current")


class _ApWebPassword_Type(OctetString):
    """Custom type apWebPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApWebPassword_Type.__name__ = "OctetString"
_ApWebPassword_Object = MibScalar
apWebPassword = _ApWebPassword_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 1, 1, 5),
    _ApWebPassword_Type()
)
apWebPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWebPassword.setStatus("current")


class _ApWebAdministration_Type(Integer32):
    """Custom type apWebAdministration based on Integer32"""
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


_ApWebAdministration_Type.__name__ = "Integer32"
_ApWebAdministration_Object = MibScalar
apWebAdministration = _ApWebAdministration_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 1, 1, 6),
    _ApWebAdministration_Type()
)
apWebAdministration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWebAdministration.setStatus("current")
_ApSnmp_ObjectIdentity = ObjectIdentity
apSnmp = _ApSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2)
)
_ApSnmpBasic_ObjectIdentity = ObjectIdentity
apSnmpBasic = _ApSnmpBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 1)
)


class _ApSnmpName_Type(OctetString):
    """Custom type apSnmpName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ApSnmpName_Type.__name__ = "OctetString"
_ApSnmpName_Object = MibScalar
apSnmpName = _ApSnmpName_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 1, 1),
    _ApSnmpName_Type()
)
apSnmpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpName.setStatus("current")


class _ApSnmpV1Enable_Type(Integer32):
    """Custom type apSnmpV1Enable based on Integer32"""
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


_ApSnmpV1Enable_Type.__name__ = "Integer32"
_ApSnmpV1Enable_Object = MibScalar
apSnmpV1Enable = _ApSnmpV1Enable_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 1, 2),
    _ApSnmpV1Enable_Type()
)
apSnmpV1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpV1Enable.setStatus("current")


class _ApSnmpV2Enable_Type(Integer32):
    """Custom type apSnmpV2Enable based on Integer32"""
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


_ApSnmpV2Enable_Type.__name__ = "Integer32"
_ApSnmpV2Enable_Object = MibScalar
apSnmpV2Enable = _ApSnmpV2Enable_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 1, 3),
    _ApSnmpV2Enable_Type()
)
apSnmpV2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpV2Enable.setStatus("current")


class _ApSnmpV3Enable_Type(Integer32):
    """Custom type apSnmpV3Enable based on Integer32"""
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


_ApSnmpV3Enable_Type.__name__ = "Integer32"
_ApSnmpV3Enable_Object = MibScalar
apSnmpV3Enable = _ApSnmpV3Enable_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 1, 4),
    _ApSnmpV3Enable_Type()
)
apSnmpV3Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpV3Enable.setStatus("current")
_ApSnmpTrap_ObjectIdentity = ObjectIdentity
apSnmpTrap = _ApSnmpTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 2)
)


class _ApSnmpTrapEnable_Type(Integer32):
    """Custom type apSnmpTrapEnable based on Integer32"""
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


_ApSnmpTrapEnable_Type.__name__ = "Integer32"
_ApSnmpTrapEnable_Object = MibScalar
apSnmpTrapEnable = _ApSnmpTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 2, 1),
    _ApSnmpTrapEnable_Type()
)
apSnmpTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpTrapEnable.setStatus("current")


class _ApSnmpTrapName_Type(OctetString):
    """Custom type apSnmpTrapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ApSnmpTrapName_Type.__name__ = "OctetString"
_ApSnmpTrapName_Object = MibScalar
apSnmpTrapName = _ApSnmpTrapName_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 2, 2),
    _ApSnmpTrapName_Type()
)
apSnmpTrapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpTrapName.setStatus("current")
_ApSnmpTrapIpAddress_Type = IpAddress
_ApSnmpTrapIpAddress_Object = MibScalar
apSnmpTrapIpAddress = _ApSnmpTrapIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 2, 3),
    _ApSnmpTrapIpAddress_Type()
)
apSnmpTrapIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpTrapIpAddress.setStatus("current")
_ApSnmpCommunityTable_Object = MibTable
apSnmpCommunityTable = _ApSnmpCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 3)
)
if mibBuilder.loadTexts:
    apSnmpCommunityTable.setStatus("current")
_ApSnmpCommunityEntry_Object = MibTableRow
apSnmpCommunityEntry = _ApSnmpCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 3, 1)
)
apSnmpCommunityEntry.setIndexNames(
    (0, "AP-MANAGEMENT", "apSnmpCommunityIndex"),
)
if mibBuilder.loadTexts:
    apSnmpCommunityEntry.setStatus("current")
_ApSnmpCommunityIndex_Type = Integer32
_ApSnmpCommunityIndex_Object = MibTableColumn
apSnmpCommunityIndex = _ApSnmpCommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 3, 1, 1),
    _ApSnmpCommunityIndex_Type()
)
apSnmpCommunityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSnmpCommunityIndex.setStatus("current")
_ApSnmpCommunityRowControl_Type = RowStatus
_ApSnmpCommunityRowControl_Object = MibTableColumn
apSnmpCommunityRowControl = _ApSnmpCommunityRowControl_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 3, 1, 2),
    _ApSnmpCommunityRowControl_Type()
)
apSnmpCommunityRowControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSnmpCommunityRowControl.setStatus("current")


class _ApSnmpCommunityStatus_Type(Integer32):
    """Custom type apSnmpCommunityStatus based on Integer32"""
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


_ApSnmpCommunityStatus_Type.__name__ = "Integer32"
_ApSnmpCommunityStatus_Object = MibTableColumn
apSnmpCommunityStatus = _ApSnmpCommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 3, 1, 3),
    _ApSnmpCommunityStatus_Type()
)
apSnmpCommunityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpCommunityStatus.setStatus("current")


class _ApSnmpCommunityName_Type(OctetString):
    """Custom type apSnmpCommunityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ApSnmpCommunityName_Type.__name__ = "OctetString"
_ApSnmpCommunityName_Object = MibTableColumn
apSnmpCommunityName = _ApSnmpCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 3, 1, 4),
    _ApSnmpCommunityName_Type()
)
apSnmpCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpCommunityName.setStatus("current")
_ApSnmpCommunityIpAddress_Type = IpAddress
_ApSnmpCommunityIpAddress_Object = MibTableColumn
apSnmpCommunityIpAddress = _ApSnmpCommunityIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 3, 1, 5),
    _ApSnmpCommunityIpAddress_Type()
)
apSnmpCommunityIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpCommunityIpAddress.setStatus("current")
_ApSnmpCommunityNetmask_Type = IpAddress
_ApSnmpCommunityNetmask_Object = MibTableColumn
apSnmpCommunityNetmask = _ApSnmpCommunityNetmask_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 3, 1, 6),
    _ApSnmpCommunityNetmask_Type()
)
apSnmpCommunityNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpCommunityNetmask.setStatus("current")


class _ApSnmpCommunityAccess_Type(Integer32):
    """Custom type apSnmpCommunityAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("readonly", 0),
          ("readwrite", 1))
    )


_ApSnmpCommunityAccess_Type.__name__ = "Integer32"
_ApSnmpCommunityAccess_Object = MibTableColumn
apSnmpCommunityAccess = _ApSnmpCommunityAccess_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 3, 1, 7),
    _ApSnmpCommunityAccess_Type()
)
apSnmpCommunityAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpCommunityAccess.setStatus("current")
_ApSnmpUserTable_Object = MibTable
apSnmpUserTable = _ApSnmpUserTable_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 4)
)
if mibBuilder.loadTexts:
    apSnmpUserTable.setStatus("current")
_ApSnmpUserEntry_Object = MibTableRow
apSnmpUserEntry = _ApSnmpUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 4, 1)
)
apSnmpUserEntry.setIndexNames(
    (0, "AP-MANAGEMENT", "apSnmpUserIndex"),
)
if mibBuilder.loadTexts:
    apSnmpUserEntry.setStatus("current")
_ApSnmpUserIndex_Type = Integer32
_ApSnmpUserIndex_Object = MibTableColumn
apSnmpUserIndex = _ApSnmpUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 4, 1, 1),
    _ApSnmpUserIndex_Type()
)
apSnmpUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSnmpUserIndex.setStatus("current")
_ApSnmpUserRowControl_Type = RowStatus
_ApSnmpUserRowControl_Object = MibTableColumn
apSnmpUserRowControl = _ApSnmpUserRowControl_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 4, 1, 2),
    _ApSnmpUserRowControl_Type()
)
apSnmpUserRowControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSnmpUserRowControl.setStatus("current")


class _ApSnmpUserStatus_Type(Integer32):
    """Custom type apSnmpUserStatus based on Integer32"""
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


_ApSnmpUserStatus_Type.__name__ = "Integer32"
_ApSnmpUserStatus_Object = MibTableColumn
apSnmpUserStatus = _ApSnmpUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 4, 1, 3),
    _ApSnmpUserStatus_Type()
)
apSnmpUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpUserStatus.setStatus("current")


class _ApSnmpUserName_Type(OctetString):
    """Custom type apSnmpUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ApSnmpUserName_Type.__name__ = "OctetString"
_ApSnmpUserName_Object = MibTableColumn
apSnmpUserName = _ApSnmpUserName_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 4, 1, 4),
    _ApSnmpUserName_Type()
)
apSnmpUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpUserName.setStatus("current")


class _ApSnmpUserAuthProtocol_Type(Integer32):
    """Custom type apSnmpUserAuthProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("md5", 0),
          ("sha", 1))
    )


_ApSnmpUserAuthProtocol_Type.__name__ = "Integer32"
_ApSnmpUserAuthProtocol_Object = MibTableColumn
apSnmpUserAuthProtocol = _ApSnmpUserAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 4, 1, 5),
    _ApSnmpUserAuthProtocol_Type()
)
apSnmpUserAuthProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpUserAuthProtocol.setStatus("current")


class _ApSnmpUserAuthPassword_Type(OctetString):
    """Custom type apSnmpUserAuthPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApSnmpUserAuthPassword_Type.__name__ = "OctetString"
_ApSnmpUserAuthPassword_Object = MibTableColumn
apSnmpUserAuthPassword = _ApSnmpUserAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 4, 1, 6),
    _ApSnmpUserAuthPassword_Type()
)
apSnmpUserAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpUserAuthPassword.setStatus("current")


class _ApSnmpUserPrivProtocol_Type(Integer32):
    """Custom type apSnmpUserPrivProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("des", 1),
          ("none", 0))
    )


_ApSnmpUserPrivProtocol_Type.__name__ = "Integer32"
_ApSnmpUserPrivProtocol_Object = MibTableColumn
apSnmpUserPrivProtocol = _ApSnmpUserPrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 4, 1, 7),
    _ApSnmpUserPrivProtocol_Type()
)
apSnmpUserPrivProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpUserPrivProtocol.setStatus("current")


class _ApSnmpUserPrivPassword_Type(OctetString):
    """Custom type apSnmpUserPrivPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApSnmpUserPrivPassword_Type.__name__ = "OctetString"
_ApSnmpUserPrivPassword_Object = MibTableColumn
apSnmpUserPrivPassword = _ApSnmpUserPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 4, 1, 8),
    _ApSnmpUserPrivPassword_Type()
)
apSnmpUserPrivPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpUserPrivPassword.setStatus("current")


class _ApSnmpUserAccess_Type(Integer32):
    """Custom type apSnmpUserAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("readonly", 0),
          ("readwrite", 1))
    )


_ApSnmpUserAccess_Type.__name__ = "Integer32"
_ApSnmpUserAccess_Object = MibTableColumn
apSnmpUserAccess = _ApSnmpUserAccess_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 4, 1, 9),
    _ApSnmpUserAccess_Type()
)
apSnmpUserAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpUserAccess.setStatus("current")
_ApRemoteAssistance_ObjectIdentity = ObjectIdentity
apRemoteAssistance = _ApRemoteAssistance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 3)
)
_ApRemoteAssistanceBasic_ObjectIdentity = ObjectIdentity
apRemoteAssistanceBasic = _ApRemoteAssistanceBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 3, 1)
)


class _ApRemoteAssistanceCurrentStatus_Type(Integer32):
    """Custom type apRemoteAssistanceCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("connecting", 1),
          ("disable", 0))
    )


_ApRemoteAssistanceCurrentStatus_Type.__name__ = "Integer32"
_ApRemoteAssistanceCurrentStatus_Object = MibScalar
apRemoteAssistanceCurrentStatus = _ApRemoteAssistanceCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 3, 1, 1),
    _ApRemoteAssistanceCurrentStatus_Type()
)
apRemoteAssistanceCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRemoteAssistanceCurrentStatus.setStatus("current")


class _ApRemoteAssistanceStatus_Type(Integer32):
    """Custom type apRemoteAssistanceStatus based on Integer32"""
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


_ApRemoteAssistanceStatus_Type.__name__ = "Integer32"
_ApRemoteAssistanceStatus_Object = MibScalar
apRemoteAssistanceStatus = _ApRemoteAssistanceStatus_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 3, 1, 2),
    _ApRemoteAssistanceStatus_Type()
)
apRemoteAssistanceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRemoteAssistanceStatus.setStatus("current")
_ApControl_ObjectIdentity = ObjectIdentity
apControl = _ApControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 4)
)
_ApCommands_ObjectIdentity = ObjectIdentity
apCommands = _ApCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 4, 1)
)


class _ApSaveAndActivate_Type(Integer32):
    """Custom type apSaveAndActivate based on Integer32"""
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


_ApSaveAndActivate_Type.__name__ = "Integer32"
_ApSaveAndActivate_Object = MibScalar
apSaveAndActivate = _ApSaveAndActivate_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 4, 1, 1),
    _ApSaveAndActivate_Type()
)
apSaveAndActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSaveAndActivate.setStatus("current")


class _ApReboot_Type(Integer32):
    """Custom type apReboot based on Integer32"""
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
        *(("disable", 0),
          ("rebootCurrentFlash", 3),
          ("rebootFlash1", 1),
          ("rebootFlash2", 2))
    )


_ApReboot_Type.__name__ = "Integer32"
_ApReboot_Object = MibScalar
apReboot = _ApReboot_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 4, 1, 2),
    _ApReboot_Type()
)
apReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apReboot.setStatus("current")


class _ApRestoreDefault_Type(Integer32):
    """Custom type apRestoreDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("restoreDefault", 1),
          ("restorePreserveNetwork", 2))
    )


_ApRestoreDefault_Type.__name__ = "Integer32"
_ApRestoreDefault_Object = MibScalar
apRestoreDefault = _ApRestoreDefault_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 4, 1, 3),
    _ApRestoreDefault_Type()
)
apRestoreDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRestoreDefault.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AP-MANAGEMENT",
    **{"pepwave": pepwave,
       "productID": productID,
       "apMib": apMib,
       "apGeneralMib": apGeneralMib,
       "ap-management-mib": ap_management_mib,
       "apWeb": apWeb,
       "apWebAdmin": apWebAdmin,
       "apWebAccessProtocol": apWebAccessProtocol,
       "apWebManagementPort": apWebManagementPort,
       "apWebHttpRedirection": apWebHttpRedirection,
       "apWebUsername": apWebUsername,
       "apWebPassword": apWebPassword,
       "apWebAdministration": apWebAdministration,
       "apSnmp": apSnmp,
       "apSnmpBasic": apSnmpBasic,
       "apSnmpName": apSnmpName,
       "apSnmpV1Enable": apSnmpV1Enable,
       "apSnmpV2Enable": apSnmpV2Enable,
       "apSnmpV3Enable": apSnmpV3Enable,
       "apSnmpTrap": apSnmpTrap,
       "apSnmpTrapEnable": apSnmpTrapEnable,
       "apSnmpTrapName": apSnmpTrapName,
       "apSnmpTrapIpAddress": apSnmpTrapIpAddress,
       "apSnmpCommunityTable": apSnmpCommunityTable,
       "apSnmpCommunityEntry": apSnmpCommunityEntry,
       "apSnmpCommunityIndex": apSnmpCommunityIndex,
       "apSnmpCommunityRowControl": apSnmpCommunityRowControl,
       "apSnmpCommunityStatus": apSnmpCommunityStatus,
       "apSnmpCommunityName": apSnmpCommunityName,
       "apSnmpCommunityIpAddress": apSnmpCommunityIpAddress,
       "apSnmpCommunityNetmask": apSnmpCommunityNetmask,
       "apSnmpCommunityAccess": apSnmpCommunityAccess,
       "apSnmpUserTable": apSnmpUserTable,
       "apSnmpUserEntry": apSnmpUserEntry,
       "apSnmpUserIndex": apSnmpUserIndex,
       "apSnmpUserRowControl": apSnmpUserRowControl,
       "apSnmpUserStatus": apSnmpUserStatus,
       "apSnmpUserName": apSnmpUserName,
       "apSnmpUserAuthProtocol": apSnmpUserAuthProtocol,
       "apSnmpUserAuthPassword": apSnmpUserAuthPassword,
       "apSnmpUserPrivProtocol": apSnmpUserPrivProtocol,
       "apSnmpUserPrivPassword": apSnmpUserPrivPassword,
       "apSnmpUserAccess": apSnmpUserAccess,
       "apRemoteAssistance": apRemoteAssistance,
       "apRemoteAssistanceBasic": apRemoteAssistanceBasic,
       "apRemoteAssistanceCurrentStatus": apRemoteAssistanceCurrentStatus,
       "apRemoteAssistanceStatus": apRemoteAssistanceStatus,
       "apControl": apControl,
       "apCommands": apCommands,
       "apSaveAndActivate": apSaveAndActivate,
       "apReboot": apReboot,
       "apRestoreDefault": apRestoreDefault}
)
