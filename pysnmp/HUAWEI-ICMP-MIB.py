# SNMP MIB module (HUAWEI-ICMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-ICMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:59 2024
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

(huawei,
 hwInternetProtocol,
 hwLocal) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "huawei",
    "hwInternetProtocol",
    "hwLocal")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RIcmp_ObjectIdentity = ObjectIdentity
rIcmp = _RIcmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 2)
)
_IcmpInBadCode_Type = Counter32
_IcmpInBadCode_Object = MibScalar
icmpInBadCode = _IcmpInBadCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 2, 1),
    _IcmpInBadCode_Type()
)
icmpInBadCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInBadCode.setStatus("mandatory")
_IcmpInBadLen_Type = Counter32
_IcmpInBadLen_Object = MibScalar
icmpInBadLen = _IcmpInBadLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 2, 2),
    _IcmpInBadLen_Type()
)
icmpInBadLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInBadLen.setStatus("mandatory")
_IcmpInChecksum_Type = Counter32
_IcmpInChecksum_Object = MibScalar
icmpInChecksum = _IcmpInChecksum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 2, 3),
    _IcmpInChecksum_Type()
)
icmpInChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInChecksum.setStatus("mandatory")
_IcmpInTooShort_Type = Counter32
_IcmpInTooShort_Object = MibScalar
icmpInTooShort = _IcmpInTooShort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 2, 4),
    _IcmpInTooShort_Type()
)
icmpInTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInTooShort.setStatus("mandatory")
_IcmpOutOldIcmp_Type = Counter32
_IcmpOutOldIcmp_Object = MibScalar
icmpOutOldIcmp = _IcmpOutOldIcmp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 2, 5),
    _IcmpOutOldIcmp_Type()
)
icmpOutOldIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpOutOldIcmp.setStatus("mandatory")
_IcmpOutShort_Type = Counter32
_IcmpOutShort_Object = MibScalar
icmpOutShort = _IcmpOutShort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 2, 6),
    _IcmpOutShort_Type()
)
icmpOutShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpOutShort.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-ICMP-MIB",
    **{"rIcmp": rIcmp,
       "icmpInBadCode": icmpInBadCode,
       "icmpInBadLen": icmpInBadLen,
       "icmpInChecksum": icmpInChecksum,
       "icmpInTooShort": icmpInTooShort,
       "icmpOutOldIcmp": icmpOutOldIcmp,
       "icmpOutShort": icmpOutShort}
)
