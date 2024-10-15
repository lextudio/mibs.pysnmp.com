# SNMP MIB module (CISCO-DMN-DSG-FPUI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-FPUI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:25 2024
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

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

ciscoDSGFPUI = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 24)
)
ciscoDSGFPUI.setRevisions(
        ("2010-08-30 11:00",
         "2010-03-22 05:00",
         "2009-12-20 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _FpuiKBLock_Type(Integer32):
    """Custom type fpuiKBLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_FpuiKBLock_Type.__name__ = "Integer32"
_FpuiKBLock_Object = MibScalar
fpuiKBLock = _FpuiKBLock_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 24, 1),
    _FpuiKBLock_Type()
)
fpuiKBLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpuiKBLock.setStatus("current")


class _FpuiKBLockTimeout_Type(Integer32):
    """Custom type fpuiKBLockTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_FpuiKBLockTimeout_Type.__name__ = "Integer32"
_FpuiKBLockTimeout_Object = MibScalar
fpuiKBLockTimeout = _FpuiKBLockTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 24, 2),
    _FpuiKBLockTimeout_Type()
)
fpuiKBLockTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpuiKBLockTimeout.setStatus("current")


class _FpuiLCDContrast_Type(Integer32):
    """Custom type fpuiLCDContrast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_FpuiLCDContrast_Type.__name__ = "Integer32"
_FpuiLCDContrast_Object = MibScalar
fpuiLCDContrast = _FpuiLCDContrast_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 24, 3),
    _FpuiLCDContrast_Type()
)
fpuiLCDContrast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpuiLCDContrast.setStatus("current")


class _FpuiAWReminder_Type(Integer32):
    """Custom type fpuiAWReminder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FpuiAWReminder_Type.__name__ = "Integer32"
_FpuiAWReminder_Object = MibScalar
fpuiAWReminder = _FpuiAWReminder_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 24, 4),
    _FpuiAWReminder_Type()
)
fpuiAWReminder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpuiAWReminder.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-FPUI-MIB",
    **{"ciscoDSGFPUI": ciscoDSGFPUI,
       "fpuiKBLock": fpuiKBLock,
       "fpuiKBLockTimeout": fpuiKBLockTimeout,
       "fpuiLCDContrast": fpuiLCDContrast,
       "fpuiAWReminder": fpuiAWReminder}
)
