# SNMP MIB module (CXPortManager-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXPortManager-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:46 2024
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

(cxPortManager,) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "cxPortManager")

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

_CxPrtMPlannedCfgTable_Object = MibTable
cxPrtMPlannedCfgTable = _CxPrtMPlannedCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 16, 1)
)
if mibBuilder.loadTexts:
    cxPrtMPlannedCfgTable.setStatus("mandatory")
_CxPrtMPlannedCfgEntry_Object = MibTableRow
cxPrtMPlannedCfgEntry = _CxPrtMPlannedCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 16, 1, 1)
)
cxPrtMPlannedCfgEntry.setIndexNames(
    (0, "CXPortManager-MIB", "cxPrtMPrtNum"),
)
if mibBuilder.loadTexts:
    cxPrtMPlannedCfgEntry.setStatus("mandatory")
_CxPrtMPrtNum_Type = Integer32
_CxPrtMPrtNum_Object = MibTableColumn
cxPrtMPrtNum = _CxPrtMPrtNum_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 16, 1, 1, 1),
    _CxPrtMPrtNum_Type()
)
cxPrtMPrtNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxPrtMPrtNum.setStatus("mandatory")


class _CxPrtMPrtType_Type(Integer32):
    """Custom type cxPrtMPrtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CxPrtMPrtType_Type.__name__ = "Integer32"
_CxPrtMPrtType_Object = MibTableColumn
cxPrtMPrtType = _CxPrtMPrtType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 16, 1, 1, 2),
    _CxPrtMPrtType_Type()
)
cxPrtMPrtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxPrtMPrtType.setStatus("mandatory")
_CxPrtMAdminTable_Object = MibTable
cxPrtMAdminTable = _CxPrtMAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 16, 2)
)
if mibBuilder.loadTexts:
    cxPrtMAdminTable.setStatus("mandatory")
_CxPrtMAdminEntry_Object = MibTableRow
cxPrtMAdminEntry = _CxPrtMAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 16, 2, 1)
)
cxPrtMAdminEntry.setIndexNames(
    (0, "CXPortManager-MIB", "cxPrtMPrtNum"),
)
if mibBuilder.loadTexts:
    cxPrtMAdminEntry.setStatus("mandatory")


class _CxPrtMAdminPortControl_Type(Integer32):
    """Custom type cxPrtMAdminPortControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("deactivate", 2),
          ("reinitialize", 3))
    )


_CxPrtMAdminPortControl_Type.__name__ = "Integer32"
_CxPrtMAdminPortControl_Object = MibTableColumn
cxPrtMAdminPortControl = _CxPrtMAdminPortControl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 16, 2, 1, 1),
    _CxPrtMAdminPortControl_Type()
)
cxPrtMAdminPortControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cxPrtMAdminPortControl.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXPortManager-MIB",
    **{"cxPrtMPlannedCfgTable": cxPrtMPlannedCfgTable,
       "cxPrtMPlannedCfgEntry": cxPrtMPlannedCfgEntry,
       "cxPrtMPrtNum": cxPrtMPrtNum,
       "cxPrtMPrtType": cxPrtMPrtType,
       "cxPrtMAdminTable": cxPrtMAdminTable,
       "cxPrtMAdminEntry": cxPrtMAdminEntry,
       "cxPrtMAdminPortControl": cxPrtMAdminPortControl}
)
