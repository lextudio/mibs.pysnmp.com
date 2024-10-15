# SNMP MIB module (TRAPEZE-NETWORKS-BASIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRAPEZE-NETWORKS-BASIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:28 2024
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

(TrpzLicenseFeature,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-LICENSE-FEATURE-TC-MIB",
    "TrpzLicenseFeature")

(trpzMibs,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-ROOT-MIB",
    "trpzMibs")


# MODULE-IDENTITY

trpzBasic = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 2)
)
trpzBasic.setRevisions(
        ("2009-11-16 00:10",
         "2006-07-10 00:08",
         "2006-04-14 00:07",
         "2005-01-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TrpzBasicSystemInfo_ObjectIdentity = ObjectIdentity
trpzBasicSystemInfo = _TrpzBasicSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 2, 1)
)


class _TrpzSerialNumber_Type(DisplayString):
    """Custom type trpzSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TrpzSerialNumber_Type.__name__ = "DisplayString"
_TrpzSerialNumber_Object = MibScalar
trpzSerialNumber = _TrpzSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 2, 1, 1),
    _TrpzSerialNumber_Type()
)
trpzSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzSerialNumber.setStatus("current")


class _TrpzSwMajorVersionNumber_Type(Integer32):
    """Custom type trpzSwMajorVersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TrpzSwMajorVersionNumber_Type.__name__ = "Integer32"
_TrpzSwMajorVersionNumber_Object = MibScalar
trpzSwMajorVersionNumber = _TrpzSwMajorVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 2, 1, 2),
    _TrpzSwMajorVersionNumber_Type()
)
trpzSwMajorVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzSwMajorVersionNumber.setStatus("current")


class _TrpzSwMinorVersionNumber_Type(Integer32):
    """Custom type trpzSwMinorVersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TrpzSwMinorVersionNumber_Type.__name__ = "Integer32"
_TrpzSwMinorVersionNumber_Object = MibScalar
trpzSwMinorVersionNumber = _TrpzSwMinorVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 2, 1, 3),
    _TrpzSwMinorVersionNumber_Type()
)
trpzSwMinorVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzSwMinorVersionNumber.setStatus("current")


class _TrpzVersionString_Type(DisplayString):
    """Custom type trpzVersionString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TrpzVersionString_Type.__name__ = "DisplayString"
_TrpzVersionString_Object = MibScalar
trpzVersionString = _TrpzVersionString_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 2, 1, 4),
    _TrpzVersionString_Type()
)
trpzVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzVersionString.setStatus("current")
_TrpzMobilityDomainInfo_ObjectIdentity = ObjectIdentity
trpzMobilityDomainInfo = _TrpzMobilityDomainInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 2, 2)
)


class _TrpzMobilityDomainName_Type(DisplayString):
    """Custom type trpzMobilityDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TrpzMobilityDomainName_Type.__name__ = "DisplayString"
_TrpzMobilityDomainName_Object = MibScalar
trpzMobilityDomainName = _TrpzMobilityDomainName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 2, 2, 1),
    _TrpzMobilityDomainName_Type()
)
trpzMobilityDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzMobilityDomainName.setStatus("current")
_TrpzMobilitySeedIp_Type = IpAddress
_TrpzMobilitySeedIp_Object = MibScalar
trpzMobilitySeedIp = _TrpzMobilitySeedIp_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 2, 2, 2),
    _TrpzMobilitySeedIp_Type()
)
trpzMobilitySeedIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzMobilitySeedIp.setStatus("current")


class _TrpzMobilityMemberTableSize_Type(Integer32):
    """Custom type trpzMobilityMemberTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_TrpzMobilityMemberTableSize_Type.__name__ = "Integer32"
_TrpzMobilityMemberTableSize_Object = MibScalar
trpzMobilityMemberTableSize = _TrpzMobilityMemberTableSize_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 2, 2, 3),
    _TrpzMobilityMemberTableSize_Type()
)
trpzMobilityMemberTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzMobilityMemberTableSize.setStatus("current")
_TrpzMobilityMemberTable_Object = MibTable
trpzMobilityMemberTable = _TrpzMobilityMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 2, 2, 4)
)
if mibBuilder.loadTexts:
    trpzMobilityMemberTable.setStatus("current")
_TrpzMobilityMemberEntry_Object = MibTableRow
trpzMobilityMemberEntry = _TrpzMobilityMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 2, 2, 4, 1)
)
trpzMobilityMemberEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-BASIC-MIB", "trpzMobilityMemberEntryAddr"),
)
if mibBuilder.loadTexts:
    trpzMobilityMemberEntry.setStatus("current")
_TrpzMobilityMemberEntryAddr_Type = IpAddress
_TrpzMobilityMemberEntryAddr_Object = MibTableColumn
trpzMobilityMemberEntryAddr = _TrpzMobilityMemberEntryAddr_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 2, 2, 4, 1, 1),
    _TrpzMobilityMemberEntryAddr_Type()
)
trpzMobilityMemberEntryAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzMobilityMemberEntryAddr.setStatus("current")
_TrpzLicenseInfoGroup_ObjectIdentity = ObjectIdentity
trpzLicenseInfoGroup = _TrpzLicenseInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 2, 3)
)


class _TrpzLicenseInfoTableSize_Type(Integer32):
    """Custom type trpzLicenseInfoTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_TrpzLicenseInfoTableSize_Type.__name__ = "Integer32"
_TrpzLicenseInfoTableSize_Object = MibScalar
trpzLicenseInfoTableSize = _TrpzLicenseInfoTableSize_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 2, 3, 1),
    _TrpzLicenseInfoTableSize_Type()
)
trpzLicenseInfoTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzLicenseInfoTableSize.setStatus("current")
_TrpzLicenseInfoTable_Object = MibTable
trpzLicenseInfoTable = _TrpzLicenseInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 2, 3, 2)
)
if mibBuilder.loadTexts:
    trpzLicenseInfoTable.setStatus("current")
_TrpzLicenseInfoEntry_Object = MibTableRow
trpzLicenseInfoEntry = _TrpzLicenseInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 2, 3, 2, 1)
)
trpzLicenseInfoEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-BASIC-MIB", "trpzLicenseInfoEntryFeature"),
)
if mibBuilder.loadTexts:
    trpzLicenseInfoEntry.setStatus("current")
_TrpzLicenseInfoEntryFeature_Type = TrpzLicenseFeature
_TrpzLicenseInfoEntryFeature_Object = MibTableColumn
trpzLicenseInfoEntryFeature = _TrpzLicenseInfoEntryFeature_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 2, 3, 2, 1, 1),
    _TrpzLicenseInfoEntryFeature_Type()
)
trpzLicenseInfoEntryFeature.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzLicenseInfoEntryFeature.setStatus("current")


class _TrpzLicenseInfoEntryValue_Type(Integer32):
    """Custom type trpzLicenseInfoEntryValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TrpzLicenseInfoEntryValue_Type.__name__ = "Integer32"
_TrpzLicenseInfoEntryValue_Object = MibTableColumn
trpzLicenseInfoEntryValue = _TrpzLicenseInfoEntryValue_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 2, 3, 2, 1, 2),
    _TrpzLicenseInfoEntryValue_Type()
)
trpzLicenseInfoEntryValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzLicenseInfoEntryValue.setStatus("current")


class _TrpzLicenseInfoEntryDescr_Type(DisplayString):
    """Custom type trpzLicenseInfoEntryDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrpzLicenseInfoEntryDescr_Type.__name__ = "DisplayString"
_TrpzLicenseInfoEntryDescr_Object = MibTableColumn
trpzLicenseInfoEntryDescr = _TrpzLicenseInfoEntryDescr_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 2, 3, 2, 1, 3),
    _TrpzLicenseInfoEntryDescr_Type()
)
trpzLicenseInfoEntryDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzLicenseInfoEntryDescr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRAPEZE-NETWORKS-BASIC-MIB",
    **{"trpzBasic": trpzBasic,
       "trpzBasicSystemInfo": trpzBasicSystemInfo,
       "trpzSerialNumber": trpzSerialNumber,
       "trpzSwMajorVersionNumber": trpzSwMajorVersionNumber,
       "trpzSwMinorVersionNumber": trpzSwMinorVersionNumber,
       "trpzVersionString": trpzVersionString,
       "trpzMobilityDomainInfo": trpzMobilityDomainInfo,
       "trpzMobilityDomainName": trpzMobilityDomainName,
       "trpzMobilitySeedIp": trpzMobilitySeedIp,
       "trpzMobilityMemberTableSize": trpzMobilityMemberTableSize,
       "trpzMobilityMemberTable": trpzMobilityMemberTable,
       "trpzMobilityMemberEntry": trpzMobilityMemberEntry,
       "trpzMobilityMemberEntryAddr": trpzMobilityMemberEntryAddr,
       "trpzLicenseInfoGroup": trpzLicenseInfoGroup,
       "trpzLicenseInfoTableSize": trpzLicenseInfoTableSize,
       "trpzLicenseInfoTable": trpzLicenseInfoTable,
       "trpzLicenseInfoEntry": trpzLicenseInfoEntry,
       "trpzLicenseInfoEntryFeature": trpzLicenseInfoEntryFeature,
       "trpzLicenseInfoEntryValue": trpzLicenseInfoEntryValue,
       "trpzLicenseInfoEntryDescr": trpzLicenseInfoEntryDescr}
)
