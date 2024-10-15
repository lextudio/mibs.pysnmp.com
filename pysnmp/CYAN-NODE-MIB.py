# SNMP MIB module (CYAN-NODE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYAN-NODE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:11 2024
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

(CyanTypeTc,
 cyanEntityModules) = mibBuilder.importSymbols(
    "CYAN-MIB",
    "CyanTypeTc",
    "cyanEntityModules")

(CyanAdminStateTc,
 CyanEnDisabledTc,
 CyanNationalizationTc,
 CyanOpStateQualTc,
 CyanOpStateTc,
 CyanSecServiceStateTc,
 CyanTimezoneTc) = mibBuilder.importSymbols(
    "CYAN-TC-MIB",
    "CyanAdminStateTc",
    "CyanEnDisabledTc",
    "CyanNationalizationTc",
    "CyanOpStateQualTc",
    "CyanOpStateTc",
    "CyanSecServiceStateTc",
    "CyanTimezoneTc")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

cyanNodeModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10)
)
cyanNodeModule.setRevisions(
        ("2014-12-07 05:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CyanNodeMibObjects_ObjectIdentity = ObjectIdentity
cyanNodeMibObjects = _CyanNodeMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1)
)
_CyanNodeAdminState_Type = CyanAdminStateTc
_CyanNodeAdminState_Object = MibScalar
cyanNodeAdminState = _CyanNodeAdminState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 1),
    _CyanNodeAdminState_Type()
)
cyanNodeAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeAdminState.setStatus("current")


class _CyanNodeAssetTag_Type(DisplayString):
    """Custom type cyanNodeAssetTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 124),
    )


_CyanNodeAssetTag_Type.__name__ = "DisplayString"
_CyanNodeAssetTag_Object = MibScalar
cyanNodeAssetTag = _CyanNodeAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 2),
    _CyanNodeAssetTag_Type()
)
cyanNodeAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeAssetTag.setStatus("current")
_CyanNodeBaseMacAddress_Type = DisplayString
_CyanNodeBaseMacAddress_Object = MibScalar
cyanNodeBaseMacAddress = _CyanNodeBaseMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 3),
    _CyanNodeBaseMacAddress_Type()
)
cyanNodeBaseMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeBaseMacAddress.setStatus("current")


class _CyanNodeBay_Type(DisplayString):
    """Custom type cyanNodeBay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CyanNodeBay_Type.__name__ = "DisplayString"
_CyanNodeBay_Object = MibScalar
cyanNodeBay = _CyanNodeBay_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 4),
    _CyanNodeBay_Type()
)
cyanNodeBay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeBay.setStatus("current")


class _CyanNodeCity_Type(DisplayString):
    """Custom type cyanNodeCity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CyanNodeCity_Type.__name__ = "DisplayString"
_CyanNodeCity_Object = MibScalar
cyanNodeCity = _CyanNodeCity_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 5),
    _CyanNodeCity_Type()
)
cyanNodeCity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeCity.setStatus("current")


class _CyanNodeCountry_Type(DisplayString):
    """Custom type cyanNodeCountry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CyanNodeCountry_Type.__name__ = "DisplayString"
_CyanNodeCountry_Object = MibScalar
cyanNodeCountry = _CyanNodeCountry_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 6),
    _CyanNodeCountry_Type()
)
cyanNodeCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeCountry.setStatus("current")
_CyanNodeCurrentTimeZone_Type = CyanTimezoneTc
_CyanNodeCurrentTimeZone_Object = MibScalar
cyanNodeCurrentTimeZone = _CyanNodeCurrentTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 7),
    _CyanNodeCurrentTimeZone_Type()
)
cyanNodeCurrentTimeZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeCurrentTimeZone.setStatus("current")


class _CyanNodeDescription_Type(DisplayString):
    """Custom type cyanNodeDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CyanNodeDescription_Type.__name__ = "DisplayString"
_CyanNodeDescription_Object = MibScalar
cyanNodeDescription = _CyanNodeDescription_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 8),
    _CyanNodeDescription_Type()
)
cyanNodeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeDescription.setStatus("current")
_CyanNodeDhcpOnConsolePort_Type = CyanEnDisabledTc
_CyanNodeDhcpOnConsolePort_Object = MibScalar
cyanNodeDhcpOnConsolePort = _CyanNodeDhcpOnConsolePort_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 9),
    _CyanNodeDhcpOnConsolePort_Type()
)
cyanNodeDhcpOnConsolePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeDhcpOnConsolePort.setStatus("current")
_CyanNodeIdentifier_Type = DisplayString
_CyanNodeIdentifier_Object = MibScalar
cyanNodeIdentifier = _CyanNodeIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 10),
    _CyanNodeIdentifier_Type()
)
cyanNodeIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeIdentifier.setStatus("current")
_CyanNodeLatitude_Type = Integer32
_CyanNodeLatitude_Object = MibScalar
cyanNodeLatitude = _CyanNodeLatitude_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 11),
    _CyanNodeLatitude_Type()
)
cyanNodeLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeLatitude.setStatus("current")
_CyanNodeLongitude_Type = Integer32
_CyanNodeLongitude_Object = MibScalar
cyanNodeLongitude = _CyanNodeLongitude_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 12),
    _CyanNodeLongitude_Type()
)
cyanNodeLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeLongitude.setStatus("current")


class _CyanNodeMacBlockSize_Type(Unsigned32):
    """Custom type cyanNodeMacBlockSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanNodeMacBlockSize_Type.__name__ = "Unsigned32"
_CyanNodeMacBlockSize_Object = MibScalar
cyanNodeMacBlockSize = _CyanNodeMacBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 13),
    _CyanNodeMacBlockSize_Type()
)
cyanNodeMacBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeMacBlockSize.setStatus("current")


class _CyanNodeMfgCleiCode_Type(DisplayString):
    """Custom type cyanNodeMfgCleiCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CyanNodeMfgCleiCode_Type.__name__ = "DisplayString"
_CyanNodeMfgCleiCode_Object = MibScalar
cyanNodeMfgCleiCode = _CyanNodeMfgCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 14),
    _CyanNodeMfgCleiCode_Type()
)
cyanNodeMfgCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeMfgCleiCode.setStatus("current")


class _CyanNodeMfgEciCode_Type(DisplayString):
    """Custom type cyanNodeMfgEciCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_CyanNodeMfgEciCode_Type.__name__ = "DisplayString"
_CyanNodeMfgEciCode_Object = MibScalar
cyanNodeMfgEciCode = _CyanNodeMfgEciCode_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 15),
    _CyanNodeMfgEciCode_Type()
)
cyanNodeMfgEciCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeMfgEciCode.setStatus("current")
_CyanNodeMfgModuleId_Type = Unsigned32
_CyanNodeMfgModuleId_Object = MibScalar
cyanNodeMfgModuleId = _CyanNodeMfgModuleId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 16),
    _CyanNodeMfgModuleId_Type()
)
cyanNodeMfgModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeMfgModuleId.setStatus("current")


class _CyanNodeMfgPartNumber_Type(DisplayString):
    """Custom type cyanNodeMfgPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CyanNodeMfgPartNumber_Type.__name__ = "DisplayString"
_CyanNodeMfgPartNumber_Object = MibScalar
cyanNodeMfgPartNumber = _CyanNodeMfgPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 17),
    _CyanNodeMfgPartNumber_Type()
)
cyanNodeMfgPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeMfgPartNumber.setStatus("current")


class _CyanNodeMfgRevision_Type(DisplayString):
    """Custom type cyanNodeMfgRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CyanNodeMfgRevision_Type.__name__ = "DisplayString"
_CyanNodeMfgRevision_Object = MibScalar
cyanNodeMfgRevision = _CyanNodeMfgRevision_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 18),
    _CyanNodeMfgRevision_Type()
)
cyanNodeMfgRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeMfgRevision.setStatus("current")


class _CyanNodeMfgSerialNumber_Type(DisplayString):
    """Custom type cyanNodeMfgSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CyanNodeMfgSerialNumber_Type.__name__ = "DisplayString"
_CyanNodeMfgSerialNumber_Object = MibScalar
cyanNodeMfgSerialNumber = _CyanNodeMfgSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 19),
    _CyanNodeMfgSerialNumber_Type()
)
cyanNodeMfgSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeMfgSerialNumber.setStatus("current")
_CyanNodeName_Type = DisplayString
_CyanNodeName_Object = MibScalar
cyanNodeName = _CyanNodeName_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 20),
    _CyanNodeName_Type()
)
cyanNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeName.setStatus("current")
_CyanNodeNationalization_Type = CyanNationalizationTc
_CyanNodeNationalization_Object = MibScalar
cyanNodeNationalization = _CyanNodeNationalization_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 21),
    _CyanNodeNationalization_Type()
)
cyanNodeNationalization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeNationalization.setStatus("current")
_CyanNodeNodeId_Type = Unsigned32
_CyanNodeNodeId_Object = MibScalar
cyanNodeNodeId = _CyanNodeNodeId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 22),
    _CyanNodeNodeId_Type()
)
cyanNodeNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeNodeId.setStatus("current")
_CyanNodeOidClass_Type = DisplayString
_CyanNodeOidClass_Object = MibScalar
cyanNodeOidClass = _CyanNodeOidClass_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 23),
    _CyanNodeOidClass_Type()
)
cyanNodeOidClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeOidClass.setStatus("current")
_CyanNodeOperState_Type = CyanOpStateTc
_CyanNodeOperState_Object = MibScalar
cyanNodeOperState = _CyanNodeOperState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 24),
    _CyanNodeOperState_Type()
)
cyanNodeOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeOperState.setStatus("current")
_CyanNodeOperStateQual_Type = CyanOpStateQualTc
_CyanNodeOperStateQual_Object = MibScalar
cyanNodeOperStateQual = _CyanNodeOperStateQual_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 25),
    _CyanNodeOperStateQual_Type()
)
cyanNodeOperStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeOperStateQual.setStatus("current")


class _CyanNodeOssLabel_Type(DisplayString):
    """Custom type cyanNodeOssLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CyanNodeOssLabel_Type.__name__ = "DisplayString"
_CyanNodeOssLabel_Object = MibScalar
cyanNodeOssLabel = _CyanNodeOssLabel_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 26),
    _CyanNodeOssLabel_Type()
)
cyanNodeOssLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeOssLabel.setStatus("current")


class _CyanNodeOwner_Type(DisplayString):
    """Custom type cyanNodeOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CyanNodeOwner_Type.__name__ = "DisplayString"
_CyanNodeOwner_Object = MibScalar
cyanNodeOwner = _CyanNodeOwner_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 27),
    _CyanNodeOwner_Type()
)
cyanNodeOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeOwner.setStatus("current")


class _CyanNodePartNumber_Type(DisplayString):
    """Custom type cyanNodePartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_CyanNodePartNumber_Type.__name__ = "DisplayString"
_CyanNodePartNumber_Object = MibScalar
cyanNodePartNumber = _CyanNodePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 28),
    _CyanNodePartNumber_Type()
)
cyanNodePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodePartNumber.setStatus("current")


class _CyanNodePostalCode_Type(DisplayString):
    """Custom type cyanNodePostalCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CyanNodePostalCode_Type.__name__ = "DisplayString"
_CyanNodePostalCode_Object = MibScalar
cyanNodePostalCode = _CyanNodePostalCode_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 29),
    _CyanNodePostalCode_Type()
)
cyanNodePostalCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodePostalCode.setStatus("current")


class _CyanNodeRackUnits_Type(DisplayString):
    """Custom type cyanNodeRackUnits based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CyanNodeRackUnits_Type.__name__ = "DisplayString"
_CyanNodeRackUnits_Object = MibScalar
cyanNodeRackUnits = _CyanNodeRackUnits_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 30),
    _CyanNodeRackUnits_Type()
)
cyanNodeRackUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeRackUnits.setStatus("current")


class _CyanNodeRegion_Type(DisplayString):
    """Custom type cyanNodeRegion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CyanNodeRegion_Type.__name__ = "DisplayString"
_CyanNodeRegion_Object = MibScalar
cyanNodeRegion = _CyanNodeRegion_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 31),
    _CyanNodeRegion_Type()
)
cyanNodeRegion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeRegion.setStatus("current")


class _CyanNodeRelayRack_Type(DisplayString):
    """Custom type cyanNodeRelayRack based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CyanNodeRelayRack_Type.__name__ = "DisplayString"
_CyanNodeRelayRack_Object = MibScalar
cyanNodeRelayRack = _CyanNodeRelayRack_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 32),
    _CyanNodeRelayRack_Type()
)
cyanNodeRelayRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeRelayRack.setStatus("current")
_CyanNodeSecServState_Type = CyanSecServiceStateTc
_CyanNodeSecServState_Object = MibScalar
cyanNodeSecServState = _CyanNodeSecServState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 33),
    _CyanNodeSecServState_Type()
)
cyanNodeSecServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeSecServState.setStatus("current")


class _CyanNodeStreet_Type(DisplayString):
    """Custom type cyanNodeStreet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CyanNodeStreet_Type.__name__ = "DisplayString"
_CyanNodeStreet_Object = MibScalar
cyanNodeStreet = _CyanNodeStreet_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 34),
    _CyanNodeStreet_Type()
)
cyanNodeStreet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeStreet.setStatus("current")
_CyanNodeType_Type = CyanTypeTc
_CyanNodeType_Object = MibScalar
cyanNodeType = _CyanNodeType_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 1, 35),
    _CyanNodeType_Type()
)
cyanNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanNodeType.setStatus("current")

# Managed Objects groups

cyanNodeObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 20)
)
cyanNodeObjectGroup.setObjects(
      *(("CYAN-NODE-MIB", "cyanNodeAdminState"),
        ("CYAN-NODE-MIB", "cyanNodeAssetTag"),
        ("CYAN-NODE-MIB", "cyanNodeBaseMacAddress"),
        ("CYAN-NODE-MIB", "cyanNodeBay"),
        ("CYAN-NODE-MIB", "cyanNodeCity"),
        ("CYAN-NODE-MIB", "cyanNodeCountry"),
        ("CYAN-NODE-MIB", "cyanNodeCurrentTimeZone"),
        ("CYAN-NODE-MIB", "cyanNodeDescription"),
        ("CYAN-NODE-MIB", "cyanNodeDhcpOnConsolePort"),
        ("CYAN-NODE-MIB", "cyanNodeIdentifier"),
        ("CYAN-NODE-MIB", "cyanNodeLatitude"),
        ("CYAN-NODE-MIB", "cyanNodeLongitude"),
        ("CYAN-NODE-MIB", "cyanNodeMacBlockSize"),
        ("CYAN-NODE-MIB", "cyanNodeMfgCleiCode"),
        ("CYAN-NODE-MIB", "cyanNodeMfgEciCode"),
        ("CYAN-NODE-MIB", "cyanNodeMfgModuleId"),
        ("CYAN-NODE-MIB", "cyanNodeMfgPartNumber"),
        ("CYAN-NODE-MIB", "cyanNodeMfgRevision"),
        ("CYAN-NODE-MIB", "cyanNodeMfgSerialNumber"),
        ("CYAN-NODE-MIB", "cyanNodeName"),
        ("CYAN-NODE-MIB", "cyanNodeNationalization"),
        ("CYAN-NODE-MIB", "cyanNodeNodeId"),
        ("CYAN-NODE-MIB", "cyanNodeOidClass"),
        ("CYAN-NODE-MIB", "cyanNodeOperState"),
        ("CYAN-NODE-MIB", "cyanNodeOperStateQual"),
        ("CYAN-NODE-MIB", "cyanNodeOssLabel"),
        ("CYAN-NODE-MIB", "cyanNodeOwner"),
        ("CYAN-NODE-MIB", "cyanNodePartNumber"),
        ("CYAN-NODE-MIB", "cyanNodePostalCode"),
        ("CYAN-NODE-MIB", "cyanNodeRackUnits"),
        ("CYAN-NODE-MIB", "cyanNodeRegion"),
        ("CYAN-NODE-MIB", "cyanNodeRelayRack"),
        ("CYAN-NODE-MIB", "cyanNodeSecServState"),
        ("CYAN-NODE-MIB", "cyanNodeStreet"),
        ("CYAN-NODE-MIB", "cyanNodeType"))
)
if mibBuilder.loadTexts:
    cyanNodeObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cyanNodeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 10, 30)
)
if mibBuilder.loadTexts:
    cyanNodeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYAN-NODE-MIB",
    **{"cyanNodeModule": cyanNodeModule,
       "cyanNodeMibObjects": cyanNodeMibObjects,
       "cyanNodeAdminState": cyanNodeAdminState,
       "cyanNodeAssetTag": cyanNodeAssetTag,
       "cyanNodeBaseMacAddress": cyanNodeBaseMacAddress,
       "cyanNodeBay": cyanNodeBay,
       "cyanNodeCity": cyanNodeCity,
       "cyanNodeCountry": cyanNodeCountry,
       "cyanNodeCurrentTimeZone": cyanNodeCurrentTimeZone,
       "cyanNodeDescription": cyanNodeDescription,
       "cyanNodeDhcpOnConsolePort": cyanNodeDhcpOnConsolePort,
       "cyanNodeIdentifier": cyanNodeIdentifier,
       "cyanNodeLatitude": cyanNodeLatitude,
       "cyanNodeLongitude": cyanNodeLongitude,
       "cyanNodeMacBlockSize": cyanNodeMacBlockSize,
       "cyanNodeMfgCleiCode": cyanNodeMfgCleiCode,
       "cyanNodeMfgEciCode": cyanNodeMfgEciCode,
       "cyanNodeMfgModuleId": cyanNodeMfgModuleId,
       "cyanNodeMfgPartNumber": cyanNodeMfgPartNumber,
       "cyanNodeMfgRevision": cyanNodeMfgRevision,
       "cyanNodeMfgSerialNumber": cyanNodeMfgSerialNumber,
       "cyanNodeName": cyanNodeName,
       "cyanNodeNationalization": cyanNodeNationalization,
       "cyanNodeNodeId": cyanNodeNodeId,
       "cyanNodeOidClass": cyanNodeOidClass,
       "cyanNodeOperState": cyanNodeOperState,
       "cyanNodeOperStateQual": cyanNodeOperStateQual,
       "cyanNodeOssLabel": cyanNodeOssLabel,
       "cyanNodeOwner": cyanNodeOwner,
       "cyanNodePartNumber": cyanNodePartNumber,
       "cyanNodePostalCode": cyanNodePostalCode,
       "cyanNodeRackUnits": cyanNodeRackUnits,
       "cyanNodeRegion": cyanNodeRegion,
       "cyanNodeRelayRack": cyanNodeRelayRack,
       "cyanNodeSecServState": cyanNodeSecServState,
       "cyanNodeStreet": cyanNodeStreet,
       "cyanNodeType": cyanNodeType,
       "cyanNodeObjectGroup": cyanNodeObjectGroup,
       "cyanNodeCompliance": cyanNodeCompliance}
)
