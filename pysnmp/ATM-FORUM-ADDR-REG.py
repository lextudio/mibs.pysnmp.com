# SNMP MIB module (ATM-FORUM-ADDR-REG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATM-FORUM-ADDR-REG
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:50 2024
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

(AtmAddress,
 NetPrefix,
 atmfAddressGroup,
 atmfAddressRegistrationAdminGroup,
 atmfNetPrefixGroup) = mibBuilder.importSymbols(
    "ATM-FORUM-TC-MIB",
    "AtmAddress",
    "NetPrefix",
    "atmfAddressGroup",
    "atmfAddressRegistrationAdminGroup",
    "atmfNetPrefixGroup")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtmfAddressTable_Object = MibTable
atmfAddressTable = _AtmfAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 6, 1)
)
if mibBuilder.loadTexts:
    atmfAddressTable.setStatus("mandatory")
_AtmfAddressEntry_Object = MibTableRow
atmfAddressEntry = _AtmfAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 6, 1, 1)
)
atmfAddressEntry.setIndexNames(
    (0, "ATM-FORUM-ADDR-REG", "atmfAddressPort"),
    (0, "ATM-FORUM-ADDR-REG", "atmfAddressAtmAddress"),
)
if mibBuilder.loadTexts:
    atmfAddressEntry.setStatus("mandatory")


class _AtmfAddressPort_Type(Integer32):
    """Custom type atmfAddressPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfAddressPort_Type.__name__ = "Integer32"
_AtmfAddressPort_Object = MibTableColumn
atmfAddressPort = _AtmfAddressPort_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 6, 1, 1, 1),
    _AtmfAddressPort_Type()
)
atmfAddressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAddressPort.setStatus("mandatory")
_AtmfAddressAtmAddress_Type = AtmAddress
_AtmfAddressAtmAddress_Object = MibTableColumn
atmfAddressAtmAddress = _AtmfAddressAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 6, 1, 1, 2),
    _AtmfAddressAtmAddress_Type()
)
atmfAddressAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAddressAtmAddress.setStatus("mandatory")


class _AtmfAddressStatus_Type(Integer32):
    """Custom type atmfAddressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AtmfAddressStatus_Type.__name__ = "Integer32"
_AtmfAddressStatus_Object = MibTableColumn
atmfAddressStatus = _AtmfAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 6, 1, 1, 3),
    _AtmfAddressStatus_Type()
)
atmfAddressStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfAddressStatus.setStatus("mandatory")


class _AtmfAddressOrgScope_Type(Integer32):
    """Custom type atmfAddressOrgScope based on Integer32"""
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
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("communityMinusOne", 10),
          ("communityPlusOne", 12),
          ("global", 15),
          ("interRegional", 14),
          ("intraCommunity", 11),
          ("intraOrganization", 8),
          ("intraSite", 5),
          ("localNetwork", 1),
          ("localNetworkPlusOne", 2),
          ("localNetworkPlusTwo", 3),
          ("organizationMinusOne", 7),
          ("organizationPlusOne", 9),
          ("regional", 13),
          ("siteMinusOne", 4),
          ("sitePlusOne", 6))
    )


_AtmfAddressOrgScope_Type.__name__ = "Integer32"
_AtmfAddressOrgScope_Object = MibTableColumn
atmfAddressOrgScope = _AtmfAddressOrgScope_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 6, 1, 1, 4),
    _AtmfAddressOrgScope_Type()
)
atmfAddressOrgScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfAddressOrgScope.setStatus("mandatory")
_AtmfNetPrefixTable_Object = MibTable
atmfNetPrefixTable = _AtmfNetPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 7, 1)
)
if mibBuilder.loadTexts:
    atmfNetPrefixTable.setStatus("mandatory")
_AtmfNetPrefixEntry_Object = MibTableRow
atmfNetPrefixEntry = _AtmfNetPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 7, 1, 1)
)
atmfNetPrefixEntry.setIndexNames(
    (0, "ATM-FORUM-ADDR-REG", "atmfNetPrefixPort"),
    (0, "ATM-FORUM-ADDR-REG", "atmfNetPrefixPrefix"),
)
if mibBuilder.loadTexts:
    atmfNetPrefixEntry.setStatus("mandatory")


class _AtmfNetPrefixPort_Type(Integer32):
    """Custom type atmfNetPrefixPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfNetPrefixPort_Type.__name__ = "Integer32"
_AtmfNetPrefixPort_Object = MibTableColumn
atmfNetPrefixPort = _AtmfNetPrefixPort_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 7, 1, 1, 1),
    _AtmfNetPrefixPort_Type()
)
atmfNetPrefixPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfNetPrefixPort.setStatus("mandatory")
_AtmfNetPrefixPrefix_Type = NetPrefix
_AtmfNetPrefixPrefix_Object = MibTableColumn
atmfNetPrefixPrefix = _AtmfNetPrefixPrefix_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 7, 1, 1, 2),
    _AtmfNetPrefixPrefix_Type()
)
atmfNetPrefixPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfNetPrefixPrefix.setStatus("mandatory")


class _AtmfNetPrefixStatus_Type(Integer32):
    """Custom type atmfNetPrefixStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AtmfNetPrefixStatus_Type.__name__ = "Integer32"
_AtmfNetPrefixStatus_Object = MibTableColumn
atmfNetPrefixStatus = _AtmfNetPrefixStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 7, 1, 1, 3),
    _AtmfNetPrefixStatus_Type()
)
atmfNetPrefixStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfNetPrefixStatus.setStatus("mandatory")
_AtmfAddressRegistrationAdminTable_Object = MibTable
atmfAddressRegistrationAdminTable = _AtmfAddressRegistrationAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 11, 1)
)
if mibBuilder.loadTexts:
    atmfAddressRegistrationAdminTable.setStatus("mandatory")
_AtmfAddressRegistrationAdminEntry_Object = MibTableRow
atmfAddressRegistrationAdminEntry = _AtmfAddressRegistrationAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 11, 1, 1)
)
atmfAddressRegistrationAdminEntry.setIndexNames(
    (0, "ATM-FORUM-ADDR-REG", "atmfAddressRegistrationAdminIndex"),
)
if mibBuilder.loadTexts:
    atmfAddressRegistrationAdminEntry.setStatus("mandatory")


class _AtmfAddressRegistrationAdminIndex_Type(Integer32):
    """Custom type atmfAddressRegistrationAdminIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfAddressRegistrationAdminIndex_Type.__name__ = "Integer32"
_AtmfAddressRegistrationAdminIndex_Object = MibTableColumn
atmfAddressRegistrationAdminIndex = _AtmfAddressRegistrationAdminIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 11, 1, 1, 1),
    _AtmfAddressRegistrationAdminIndex_Type()
)
atmfAddressRegistrationAdminIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAddressRegistrationAdminIndex.setStatus("mandatory")


class _AtmfAddressRegistrationAdminStatus_Type(Integer32):
    """Custom type atmfAddressRegistrationAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_AtmfAddressRegistrationAdminStatus_Type.__name__ = "Integer32"
_AtmfAddressRegistrationAdminStatus_Object = MibTableColumn
atmfAddressRegistrationAdminStatus = _AtmfAddressRegistrationAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 11, 1, 1, 2),
    _AtmfAddressRegistrationAdminStatus_Type()
)
atmfAddressRegistrationAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAddressRegistrationAdminStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATM-FORUM-ADDR-REG",
    **{"atmfAddressTable": atmfAddressTable,
       "atmfAddressEntry": atmfAddressEntry,
       "atmfAddressPort": atmfAddressPort,
       "atmfAddressAtmAddress": atmfAddressAtmAddress,
       "atmfAddressStatus": atmfAddressStatus,
       "atmfAddressOrgScope": atmfAddressOrgScope,
       "atmfNetPrefixTable": atmfNetPrefixTable,
       "atmfNetPrefixEntry": atmfNetPrefixEntry,
       "atmfNetPrefixPort": atmfNetPrefixPort,
       "atmfNetPrefixPrefix": atmfNetPrefixPrefix,
       "atmfNetPrefixStatus": atmfNetPrefixStatus,
       "atmfAddressRegistrationAdminTable": atmfAddressRegistrationAdminTable,
       "atmfAddressRegistrationAdminEntry": atmfAddressRegistrationAdminEntry,
       "atmfAddressRegistrationAdminIndex": atmfAddressRegistrationAdminIndex,
       "atmfAddressRegistrationAdminStatus": atmfAddressRegistrationAdminStatus}
)
