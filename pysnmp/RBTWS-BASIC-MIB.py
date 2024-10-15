# SNMP MIB module (RBTWS-BASIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBTWS-BASIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:32 2024
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

(rbtwsMibs,) = mibBuilder.importSymbols(
    "RBTWS-ROOT-MIB",
    "rbtwsMibs")

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

rbtwsBasic = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 2)
)
rbtwsBasic.setRevisions(
        ("2006-07-10 00:08",
         "2006-04-14 00:07",
         "2005-01-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RbtwsLicenseFeature(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("maxSupportedAPsOrDAPs", 2),
          ("none", 1))
    )



# MIB Managed Objects in the order of their OIDs

_RbtwsBasicSystemInfo_ObjectIdentity = ObjectIdentity
rbtwsBasicSystemInfo = _RbtwsBasicSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 2, 1)
)


class _RbtwsSerialNumber_Type(DisplayString):
    """Custom type rbtwsSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbtwsSerialNumber_Type.__name__ = "DisplayString"
_RbtwsSerialNumber_Object = MibScalar
rbtwsSerialNumber = _RbtwsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 2, 1, 1),
    _RbtwsSerialNumber_Type()
)
rbtwsSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsSerialNumber.setStatus("current")


class _RbtwsSwMajorVersionNumber_Type(Integer32):
    """Custom type rbtwsSwMajorVersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_RbtwsSwMajorVersionNumber_Type.__name__ = "Integer32"
_RbtwsSwMajorVersionNumber_Object = MibScalar
rbtwsSwMajorVersionNumber = _RbtwsSwMajorVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 2, 1, 2),
    _RbtwsSwMajorVersionNumber_Type()
)
rbtwsSwMajorVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsSwMajorVersionNumber.setStatus("current")


class _RbtwsSwMinorVersionNumber_Type(Integer32):
    """Custom type rbtwsSwMinorVersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_RbtwsSwMinorVersionNumber_Type.__name__ = "Integer32"
_RbtwsSwMinorVersionNumber_Object = MibScalar
rbtwsSwMinorVersionNumber = _RbtwsSwMinorVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 2, 1, 3),
    _RbtwsSwMinorVersionNumber_Type()
)
rbtwsSwMinorVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsSwMinorVersionNumber.setStatus("current")


class _RbtwsVersionString_Type(DisplayString):
    """Custom type rbtwsVersionString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RbtwsVersionString_Type.__name__ = "DisplayString"
_RbtwsVersionString_Object = MibScalar
rbtwsVersionString = _RbtwsVersionString_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 2, 1, 4),
    _RbtwsVersionString_Type()
)
rbtwsVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsVersionString.setStatus("current")
_RbtwsMobilityDomainInfo_ObjectIdentity = ObjectIdentity
rbtwsMobilityDomainInfo = _RbtwsMobilityDomainInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 2, 2)
)


class _RbtwsMobilityDomainName_Type(DisplayString):
    """Custom type rbtwsMobilityDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbtwsMobilityDomainName_Type.__name__ = "DisplayString"
_RbtwsMobilityDomainName_Object = MibScalar
rbtwsMobilityDomainName = _RbtwsMobilityDomainName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 2, 2, 1),
    _RbtwsMobilityDomainName_Type()
)
rbtwsMobilityDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsMobilityDomainName.setStatus("current")
_RbtwsMobilitySeedIp_Type = IpAddress
_RbtwsMobilitySeedIp_Object = MibScalar
rbtwsMobilitySeedIp = _RbtwsMobilitySeedIp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 2, 2, 2),
    _RbtwsMobilitySeedIp_Type()
)
rbtwsMobilitySeedIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsMobilitySeedIp.setStatus("current")


class _RbtwsMobilityMemberTableSize_Type(Integer32):
    """Custom type rbtwsMobilityMemberTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_RbtwsMobilityMemberTableSize_Type.__name__ = "Integer32"
_RbtwsMobilityMemberTableSize_Object = MibScalar
rbtwsMobilityMemberTableSize = _RbtwsMobilityMemberTableSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 2, 2, 3),
    _RbtwsMobilityMemberTableSize_Type()
)
rbtwsMobilityMemberTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsMobilityMemberTableSize.setStatus("current")
_RbtwsMobilityMemberTable_Object = MibTable
rbtwsMobilityMemberTable = _RbtwsMobilityMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 2, 2, 4)
)
if mibBuilder.loadTexts:
    rbtwsMobilityMemberTable.setStatus("current")
_RbtwsMobilityMemberEntry_Object = MibTableRow
rbtwsMobilityMemberEntry = _RbtwsMobilityMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 2, 2, 4, 1)
)
rbtwsMobilityMemberEntry.setIndexNames(
    (0, "RBTWS-BASIC-MIB", "rbtwsMobilityMemberEntryAddr"),
)
if mibBuilder.loadTexts:
    rbtwsMobilityMemberEntry.setStatus("current")
_RbtwsMobilityMemberEntryAddr_Type = IpAddress
_RbtwsMobilityMemberEntryAddr_Object = MibTableColumn
rbtwsMobilityMemberEntryAddr = _RbtwsMobilityMemberEntryAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 2, 2, 4, 1, 1),
    _RbtwsMobilityMemberEntryAddr_Type()
)
rbtwsMobilityMemberEntryAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsMobilityMemberEntryAddr.setStatus("current")
_RbtwsLicenseInfoGroup_ObjectIdentity = ObjectIdentity
rbtwsLicenseInfoGroup = _RbtwsLicenseInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 2, 3)
)


class _RbtwsLicenseInfoTableSize_Type(Integer32):
    """Custom type rbtwsLicenseInfoTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_RbtwsLicenseInfoTableSize_Type.__name__ = "Integer32"
_RbtwsLicenseInfoTableSize_Object = MibScalar
rbtwsLicenseInfoTableSize = _RbtwsLicenseInfoTableSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 2, 3, 1),
    _RbtwsLicenseInfoTableSize_Type()
)
rbtwsLicenseInfoTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsLicenseInfoTableSize.setStatus("current")
_RbtwsLicenseInfoTable_Object = MibTable
rbtwsLicenseInfoTable = _RbtwsLicenseInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 2, 3, 2)
)
if mibBuilder.loadTexts:
    rbtwsLicenseInfoTable.setStatus("current")
_RbtwsLicenseInfoEntry_Object = MibTableRow
rbtwsLicenseInfoEntry = _RbtwsLicenseInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 2, 3, 2, 1)
)
rbtwsLicenseInfoEntry.setIndexNames(
    (0, "RBTWS-BASIC-MIB", "rbtwsLicenseInfoEntryFeature"),
)
if mibBuilder.loadTexts:
    rbtwsLicenseInfoEntry.setStatus("current")
_RbtwsLicenseInfoEntryFeature_Type = RbtwsLicenseFeature
_RbtwsLicenseInfoEntryFeature_Object = MibTableColumn
rbtwsLicenseInfoEntryFeature = _RbtwsLicenseInfoEntryFeature_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 2, 3, 2, 1, 1),
    _RbtwsLicenseInfoEntryFeature_Type()
)
rbtwsLicenseInfoEntryFeature.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsLicenseInfoEntryFeature.setStatus("current")


class _RbtwsLicenseInfoEntryValue_Type(Integer32):
    """Custom type rbtwsLicenseInfoEntryValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_RbtwsLicenseInfoEntryValue_Type.__name__ = "Integer32"
_RbtwsLicenseInfoEntryValue_Object = MibTableColumn
rbtwsLicenseInfoEntryValue = _RbtwsLicenseInfoEntryValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 2, 3, 2, 1, 2),
    _RbtwsLicenseInfoEntryValue_Type()
)
rbtwsLicenseInfoEntryValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsLicenseInfoEntryValue.setStatus("current")


class _RbtwsLicenseInfoEntryDescr_Type(DisplayString):
    """Custom type rbtwsLicenseInfoEntryDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RbtwsLicenseInfoEntryDescr_Type.__name__ = "DisplayString"
_RbtwsLicenseInfoEntryDescr_Object = MibTableColumn
rbtwsLicenseInfoEntryDescr = _RbtwsLicenseInfoEntryDescr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 2, 3, 2, 1, 3),
    _RbtwsLicenseInfoEntryDescr_Type()
)
rbtwsLicenseInfoEntryDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsLicenseInfoEntryDescr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBTWS-BASIC-MIB",
    **{"RbtwsLicenseFeature": RbtwsLicenseFeature,
       "rbtwsBasic": rbtwsBasic,
       "rbtwsBasicSystemInfo": rbtwsBasicSystemInfo,
       "rbtwsSerialNumber": rbtwsSerialNumber,
       "rbtwsSwMajorVersionNumber": rbtwsSwMajorVersionNumber,
       "rbtwsSwMinorVersionNumber": rbtwsSwMinorVersionNumber,
       "rbtwsVersionString": rbtwsVersionString,
       "rbtwsMobilityDomainInfo": rbtwsMobilityDomainInfo,
       "rbtwsMobilityDomainName": rbtwsMobilityDomainName,
       "rbtwsMobilitySeedIp": rbtwsMobilitySeedIp,
       "rbtwsMobilityMemberTableSize": rbtwsMobilityMemberTableSize,
       "rbtwsMobilityMemberTable": rbtwsMobilityMemberTable,
       "rbtwsMobilityMemberEntry": rbtwsMobilityMemberEntry,
       "rbtwsMobilityMemberEntryAddr": rbtwsMobilityMemberEntryAddr,
       "rbtwsLicenseInfoGroup": rbtwsLicenseInfoGroup,
       "rbtwsLicenseInfoTableSize": rbtwsLicenseInfoTableSize,
       "rbtwsLicenseInfoTable": rbtwsLicenseInfoTable,
       "rbtwsLicenseInfoEntry": rbtwsLicenseInfoEntry,
       "rbtwsLicenseInfoEntryFeature": rbtwsLicenseInfoEntryFeature,
       "rbtwsLicenseInfoEntryValue": rbtwsLicenseInfoEntryValue,
       "rbtwsLicenseInfoEntryDescr": rbtwsLicenseInfoEntryDescr}
)
