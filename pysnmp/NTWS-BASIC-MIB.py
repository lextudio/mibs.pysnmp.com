# SNMP MIB module (NTWS-BASIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NTWS-BASIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:53 2024
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

(NtwsLicenseFeature,) = mibBuilder.importSymbols(
    "NTWS-LICENSE-FEATURE-TC-MIB",
    "NtwsLicenseFeature")

(ntwsMibs,) = mibBuilder.importSymbols(
    "NTWS-ROOT-MIB",
    "ntwsMibs")

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


# MODULE-IDENTITY

ntwsBasic = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2)
)
ntwsBasic.setRevisions(
        ("2009-11-16 00:10",
         "2007-08-16 00:09",
         "2006-07-10 00:08",
         "2006-04-14 00:07",
         "2005-01-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtwsBasicSystemInfo_ObjectIdentity = ObjectIdentity
ntwsBasicSystemInfo = _NtwsBasicSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 1)
)


class _NtwsSerialNumber_Type(DisplayString):
    """Custom type ntwsSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtwsSerialNumber_Type.__name__ = "DisplayString"
_NtwsSerialNumber_Object = MibScalar
ntwsSerialNumber = _NtwsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 1, 1),
    _NtwsSerialNumber_Type()
)
ntwsSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsSerialNumber.setStatus("current")


class _NtwsSwMajorVersionNumber_Type(Integer32):
    """Custom type ntwsSwMajorVersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_NtwsSwMajorVersionNumber_Type.__name__ = "Integer32"
_NtwsSwMajorVersionNumber_Object = MibScalar
ntwsSwMajorVersionNumber = _NtwsSwMajorVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 1, 2),
    _NtwsSwMajorVersionNumber_Type()
)
ntwsSwMajorVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsSwMajorVersionNumber.setStatus("current")


class _NtwsSwMinorVersionNumber_Type(Integer32):
    """Custom type ntwsSwMinorVersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_NtwsSwMinorVersionNumber_Type.__name__ = "Integer32"
_NtwsSwMinorVersionNumber_Object = MibScalar
ntwsSwMinorVersionNumber = _NtwsSwMinorVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 1, 3),
    _NtwsSwMinorVersionNumber_Type()
)
ntwsSwMinorVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsSwMinorVersionNumber.setStatus("current")


class _NtwsVersionString_Type(DisplayString):
    """Custom type ntwsVersionString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NtwsVersionString_Type.__name__ = "DisplayString"
_NtwsVersionString_Object = MibScalar
ntwsVersionString = _NtwsVersionString_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 1, 4),
    _NtwsVersionString_Type()
)
ntwsVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsVersionString.setStatus("current")
_NtwsMobilityDomainInfo_ObjectIdentity = ObjectIdentity
ntwsMobilityDomainInfo = _NtwsMobilityDomainInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 2)
)


class _NtwsMobilityDomainName_Type(DisplayString):
    """Custom type ntwsMobilityDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtwsMobilityDomainName_Type.__name__ = "DisplayString"
_NtwsMobilityDomainName_Object = MibScalar
ntwsMobilityDomainName = _NtwsMobilityDomainName_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 2, 1),
    _NtwsMobilityDomainName_Type()
)
ntwsMobilityDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsMobilityDomainName.setStatus("current")
_NtwsMobilitySeedIp_Type = IpAddress
_NtwsMobilitySeedIp_Object = MibScalar
ntwsMobilitySeedIp = _NtwsMobilitySeedIp_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 2, 2),
    _NtwsMobilitySeedIp_Type()
)
ntwsMobilitySeedIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsMobilitySeedIp.setStatus("current")


class _NtwsMobilityMemberTableSize_Type(Integer32):
    """Custom type ntwsMobilityMemberTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_NtwsMobilityMemberTableSize_Type.__name__ = "Integer32"
_NtwsMobilityMemberTableSize_Object = MibScalar
ntwsMobilityMemberTableSize = _NtwsMobilityMemberTableSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 2, 3),
    _NtwsMobilityMemberTableSize_Type()
)
ntwsMobilityMemberTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsMobilityMemberTableSize.setStatus("current")
_NtwsMobilityMemberTable_Object = MibTable
ntwsMobilityMemberTable = _NtwsMobilityMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 2, 4)
)
if mibBuilder.loadTexts:
    ntwsMobilityMemberTable.setStatus("current")
_NtwsMobilityMemberEntry_Object = MibTableRow
ntwsMobilityMemberEntry = _NtwsMobilityMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 2, 4, 1)
)
ntwsMobilityMemberEntry.setIndexNames(
    (0, "NTWS-BASIC-MIB", "ntwsMobilityMemberEntryAddr"),
)
if mibBuilder.loadTexts:
    ntwsMobilityMemberEntry.setStatus("current")
_NtwsMobilityMemberEntryAddr_Type = IpAddress
_NtwsMobilityMemberEntryAddr_Object = MibTableColumn
ntwsMobilityMemberEntryAddr = _NtwsMobilityMemberEntryAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 2, 4, 1, 1),
    _NtwsMobilityMemberEntryAddr_Type()
)
ntwsMobilityMemberEntryAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsMobilityMemberEntryAddr.setStatus("current")
_NtwsLicenseInfoGroup_ObjectIdentity = ObjectIdentity
ntwsLicenseInfoGroup = _NtwsLicenseInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 3)
)


class _NtwsLicenseInfoTableSize_Type(Integer32):
    """Custom type ntwsLicenseInfoTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_NtwsLicenseInfoTableSize_Type.__name__ = "Integer32"
_NtwsLicenseInfoTableSize_Object = MibScalar
ntwsLicenseInfoTableSize = _NtwsLicenseInfoTableSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 3, 1),
    _NtwsLicenseInfoTableSize_Type()
)
ntwsLicenseInfoTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsLicenseInfoTableSize.setStatus("current")
_NtwsLicenseInfoTable_Object = MibTable
ntwsLicenseInfoTable = _NtwsLicenseInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 3, 2)
)
if mibBuilder.loadTexts:
    ntwsLicenseInfoTable.setStatus("current")
_NtwsLicenseInfoEntry_Object = MibTableRow
ntwsLicenseInfoEntry = _NtwsLicenseInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 3, 2, 1)
)
ntwsLicenseInfoEntry.setIndexNames(
    (0, "NTWS-BASIC-MIB", "ntwsLicenseInfoEntryFeature"),
)
if mibBuilder.loadTexts:
    ntwsLicenseInfoEntry.setStatus("current")
_NtwsLicenseInfoEntryFeature_Type = NtwsLicenseFeature
_NtwsLicenseInfoEntryFeature_Object = MibTableColumn
ntwsLicenseInfoEntryFeature = _NtwsLicenseInfoEntryFeature_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 3, 2, 1, 1),
    _NtwsLicenseInfoEntryFeature_Type()
)
ntwsLicenseInfoEntryFeature.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsLicenseInfoEntryFeature.setStatus("current")


class _NtwsLicenseInfoEntryValue_Type(Integer32):
    """Custom type ntwsLicenseInfoEntryValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_NtwsLicenseInfoEntryValue_Type.__name__ = "Integer32"
_NtwsLicenseInfoEntryValue_Object = MibTableColumn
ntwsLicenseInfoEntryValue = _NtwsLicenseInfoEntryValue_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 3, 2, 1, 2),
    _NtwsLicenseInfoEntryValue_Type()
)
ntwsLicenseInfoEntryValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsLicenseInfoEntryValue.setStatus("current")


class _NtwsLicenseInfoEntryDescr_Type(DisplayString):
    """Custom type ntwsLicenseInfoEntryDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtwsLicenseInfoEntryDescr_Type.__name__ = "DisplayString"
_NtwsLicenseInfoEntryDescr_Object = MibTableColumn
ntwsLicenseInfoEntryDescr = _NtwsLicenseInfoEntryDescr_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 3, 2, 1, 3),
    _NtwsLicenseInfoEntryDescr_Type()
)
ntwsLicenseInfoEntryDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsLicenseInfoEntryDescr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NTWS-BASIC-MIB",
    **{"ntwsBasic": ntwsBasic,
       "ntwsBasicSystemInfo": ntwsBasicSystemInfo,
       "ntwsSerialNumber": ntwsSerialNumber,
       "ntwsSwMajorVersionNumber": ntwsSwMajorVersionNumber,
       "ntwsSwMinorVersionNumber": ntwsSwMinorVersionNumber,
       "ntwsVersionString": ntwsVersionString,
       "ntwsMobilityDomainInfo": ntwsMobilityDomainInfo,
       "ntwsMobilityDomainName": ntwsMobilityDomainName,
       "ntwsMobilitySeedIp": ntwsMobilitySeedIp,
       "ntwsMobilityMemberTableSize": ntwsMobilityMemberTableSize,
       "ntwsMobilityMemberTable": ntwsMobilityMemberTable,
       "ntwsMobilityMemberEntry": ntwsMobilityMemberEntry,
       "ntwsMobilityMemberEntryAddr": ntwsMobilityMemberEntryAddr,
       "ntwsLicenseInfoGroup": ntwsLicenseInfoGroup,
       "ntwsLicenseInfoTableSize": ntwsLicenseInfoTableSize,
       "ntwsLicenseInfoTable": ntwsLicenseInfoTable,
       "ntwsLicenseInfoEntry": ntwsLicenseInfoEntry,
       "ntwsLicenseInfoEntryFeature": ntwsLicenseInfoEntryFeature,
       "ntwsLicenseInfoEntryValue": ntwsLicenseInfoEntryValue,
       "ntwsLicenseInfoEntryDescr": ntwsLicenseInfoEntryDescr}
)
