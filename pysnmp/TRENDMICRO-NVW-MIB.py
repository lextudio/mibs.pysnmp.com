# SNMP MIB module (TRENDMICRO-NVW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRENDMICRO-NVW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:42 2024
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

(tmNVW,) = mibBuilder.importSymbols(
    "TRENDMICRO-SMI",
    "tmNVW")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NvwScanCurrConn_Type = Integer32
_NvwScanCurrConn_Object = MibScalar
nvwScanCurrConn = _NvwScanCurrConn_Object(
    (1, 3, 6, 1, 4, 1, 6101, 2500, 1),
    _NvwScanCurrConn_Type()
)
nvwScanCurrConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvwScanCurrConn.setStatus("mandatory")
_NvwScanCurrMem_Type = Integer32
_NvwScanCurrMem_Object = MibScalar
nvwScanCurrMem = _NvwScanCurrMem_Object(
    (1, 3, 6, 1, 4, 1, 6101, 2500, 2),
    _NvwScanCurrMem_Type()
)
nvwScanCurrMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvwScanCurrMem.setStatus("mandatory")
_NvwPolicyCurrConn_Type = Integer32
_NvwPolicyCurrConn_Object = MibScalar
nvwPolicyCurrConn = _NvwPolicyCurrConn_Object(
    (1, 3, 6, 1, 4, 1, 6101, 2500, 3),
    _NvwPolicyCurrConn_Type()
)
nvwPolicyCurrConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvwPolicyCurrConn.setStatus("mandatory")
_NvwTraps_ObjectIdentity = ObjectIdentity
nvwTraps = _NvwTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6101, 2500, 251)
)

# Managed Objects groups


# Notification objects

oppOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6101, 2500, 251, 1)
)
if mibBuilder.loadTexts:
    oppOn.setStatus(
        "current"
    )

oppOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6101, 2500, 251, 2)
)
if mibBuilder.loadTexts:
    oppOff.setStatus(
        "current"
    )

bootFactory = NotificationType(
    (1, 3, 6, 1, 4, 1, 6101, 2500, 251, 3)
)
if mibBuilder.loadTexts:
    bootFactory.setStatus(
        "current"
    )

bootPrevious = NotificationType(
    (1, 3, 6, 1, 4, 1, 6101, 2500, 251, 4)
)
if mibBuilder.loadTexts:
    bootPrevious.setStatus(
        "current"
    )

haFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 6101, 2500, 251, 5)
)
if mibBuilder.loadTexts:
    haFailover.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRENDMICRO-NVW-MIB",
    **{"nvwScanCurrConn": nvwScanCurrConn,
       "nvwScanCurrMem": nvwScanCurrMem,
       "nvwPolicyCurrConn": nvwPolicyCurrConn,
       "nvwTraps": nvwTraps,
       "oppOn": oppOn,
       "oppOff": oppOff,
       "bootFactory": bootFactory,
       "bootPrevious": bootPrevious,
       "haFailover": haFailover}
)
