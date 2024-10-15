# SNMP MIB module (WEBMGMTEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WEBMGMTEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:42 2024
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

(webMgmtExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "webMgmtExt")

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

apWebMgmtExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 37, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ApWebMgmtStatus_Type(Integer32):
    """Custom type apWebMgmtStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ApWebMgmtStatus_Type.__name__ = "Integer32"
_ApWebMgmtStatus_Object = MibScalar
apWebMgmtStatus = _ApWebMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 37, 2),
    _ApWebMgmtStatus_Type()
)
apWebMgmtStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWebMgmtStatus.setStatus("current")


class _ApWebMgmtAccess_Type(Integer32):
    """Custom type apWebMgmtAccess based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("limited", 2))
    )


_ApWebMgmtAccess_Type.__name__ = "Integer32"
_ApWebMgmtAccess_Object = MibScalar
apWebMgmtAccess = _ApWebMgmtAccess_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 37, 3),
    _ApWebMgmtAccess_Type()
)
apWebMgmtAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWebMgmtAccess.setStatus("current")
_ApWebMgmtIpAddr1_Type = IpAddress
_ApWebMgmtIpAddr1_Object = MibScalar
apWebMgmtIpAddr1 = _ApWebMgmtIpAddr1_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 37, 4),
    _ApWebMgmtIpAddr1_Type()
)
apWebMgmtIpAddr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWebMgmtIpAddr1.setStatus("current")
_ApWebMgmtIpAddr2_Type = IpAddress
_ApWebMgmtIpAddr2_Object = MibScalar
apWebMgmtIpAddr2 = _ApWebMgmtIpAddr2_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 37, 5),
    _ApWebMgmtIpAddr2_Type()
)
apWebMgmtIpAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWebMgmtIpAddr2.setStatus("current")
_ApWebMgmtIpAddr3_Type = IpAddress
_ApWebMgmtIpAddr3_Object = MibScalar
apWebMgmtIpAddr3 = _ApWebMgmtIpAddr3_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 37, 6),
    _ApWebMgmtIpAddr3_Type()
)
apWebMgmtIpAddr3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWebMgmtIpAddr3.setStatus("current")
_ApWebMgmtIpAddr4_Type = IpAddress
_ApWebMgmtIpAddr4_Object = MibScalar
apWebMgmtIpAddr4 = _ApWebMgmtIpAddr4_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 37, 7),
    _ApWebMgmtIpAddr4_Type()
)
apWebMgmtIpAddr4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWebMgmtIpAddr4.setStatus("current")
_ApWebMgmtIpAddr5_Type = IpAddress
_ApWebMgmtIpAddr5_Object = MibScalar
apWebMgmtIpAddr5 = _ApWebMgmtIpAddr5_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 37, 8),
    _ApWebMgmtIpAddr5_Type()
)
apWebMgmtIpAddr5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWebMgmtIpAddr5.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WEBMGMTEXT-MIB",
    **{"apWebMgmtExtMib": apWebMgmtExtMib,
       "apWebMgmtStatus": apWebMgmtStatus,
       "apWebMgmtAccess": apWebMgmtAccess,
       "apWebMgmtIpAddr1": apWebMgmtIpAddr1,
       "apWebMgmtIpAddr2": apWebMgmtIpAddr2,
       "apWebMgmtIpAddr3": apWebMgmtIpAddr3,
       "apWebMgmtIpAddr4": apWebMgmtIpAddr4,
       "apWebMgmtIpAddr5": apWebMgmtIpAddr5}
)
