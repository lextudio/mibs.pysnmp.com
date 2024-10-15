# SNMP MIB module (CXViewing-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXViewing-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:01 2024
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

(cxViewing,) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "cxViewing")

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

_CxViewTable_Object = MibTable
cxViewTable = _CxViewTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cxViewTable.setStatus("mandatory")
_CxViewEntry_Object = MibTableRow
cxViewEntry = _CxViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 3, 1, 1)
)
cxViewEntry.setIndexNames(
    (0, "CXViewing-MIB", "cxViewConsoleAddress"),
)
if mibBuilder.loadTexts:
    cxViewEntry.setStatus("mandatory")
_CxViewConsoleAddress_Type = IpAddress
_CxViewConsoleAddress_Object = MibTableColumn
cxViewConsoleAddress = _CxViewConsoleAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 3, 1, 1, 1),
    _CxViewConsoleAddress_Type()
)
cxViewConsoleAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxViewConsoleAddress.setStatus("mandatory")


class _CxViewCurrent_Type(Integer32):
    """Custom type cxViewCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CxViewCurrent_Type.__name__ = "Integer32"
_CxViewCurrent_Object = MibTableColumn
cxViewCurrent = _CxViewCurrent_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 3, 1, 1, 2),
    _CxViewCurrent_Type()
)
cxViewCurrent.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cxViewCurrent.setStatus("mandatory")


class _CxViewNMEStatus_Type(Integer32):
    """Custom type cxViewNMEStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CxViewNMEStatus_Type.__name__ = "Integer32"
_CxViewNMEStatus_Object = MibScalar
cxViewNMEStatus = _CxViewNMEStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 3, 2),
    _CxViewNMEStatus_Type()
)
cxViewNMEStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxViewNMEStatus.setStatus("mandatory")


class _CxViewNMEMode_Type(Integer32):
    """Custom type cxViewNMEMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 2),
          ("slave", 1))
    )


_CxViewNMEMode_Type.__name__ = "Integer32"
_CxViewNMEMode_Object = MibScalar
cxViewNMEMode = _CxViewNMEMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 3, 3),
    _CxViewNMEMode_Type()
)
cxViewNMEMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxViewNMEMode.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXViewing-MIB",
    **{"cxViewTable": cxViewTable,
       "cxViewEntry": cxViewEntry,
       "cxViewConsoleAddress": cxViewConsoleAddress,
       "cxViewCurrent": cxViewCurrent,
       "cxViewNMEStatus": cxViewNMEStatus,
       "cxViewNMEMode": cxViewNMEMode}
)
