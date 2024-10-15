# SNMP MIB module (CXUDRV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXUDRV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:55 2024
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

(cxUDrv,) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "cxUDrv")

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

_UdrvTable_Object = MibTable
udrvTable = _UdrvTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 41, 10)
)
if mibBuilder.loadTexts:
    udrvTable.setStatus("mandatory")
_UdrvEntry_Object = MibTableRow
udrvEntry = _UdrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 41, 10, 1)
)
udrvEntry.setIndexNames(
    (0, "CXUDRV-MIB", "udrvSlotNumberIndex"),
)
if mibBuilder.loadTexts:
    udrvEntry.setStatus("mandatory")


class _UdrvSlotNumberIndex_Type(Integer32):
    """Custom type udrvSlotNumberIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_UdrvSlotNumberIndex_Type.__name__ = "Integer32"
_UdrvSlotNumberIndex_Object = MibTableColumn
udrvSlotNumberIndex = _UdrvSlotNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 41, 10, 1, 1),
    _UdrvSlotNumberIndex_Type()
)
udrvSlotNumberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udrvSlotNumberIndex.setStatus("mandatory")
_UdrvClearStat_Type = Integer32
_UdrvClearStat_Object = MibTableColumn
udrvClearStat = _UdrvClearStat_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 41, 10, 1, 20),
    _UdrvClearStat_Type()
)
udrvClearStat.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    udrvClearStat.setStatus("mandatory")
_UdrvPortUp_Type = Integer32
_UdrvPortUp_Object = MibTableColumn
udrvPortUp = _UdrvPortUp_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 41, 10, 1, 21),
    _UdrvPortUp_Type()
)
udrvPortUp.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    udrvPortUp.setStatus("mandatory")
_UdrvPortReset_Type = Integer32
_UdrvPortReset_Object = MibTableColumn
udrvPortReset = _UdrvPortReset_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 41, 10, 1, 23),
    _UdrvPortReset_Type()
)
udrvPortReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    udrvPortReset.setStatus("mandatory")


class _UdrvPortStatus_Type(Integer32):
    """Custom type udrvPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portDown", 1),
          ("portUp", 2))
    )


_UdrvPortStatus_Type.__name__ = "Integer32"
_UdrvPortStatus_Object = MibTableColumn
udrvPortStatus = _UdrvPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 41, 10, 1, 30),
    _UdrvPortStatus_Type()
)
udrvPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udrvPortStatus.setStatus("mandatory")
_UdrvFebe_Type = Counter32
_UdrvFebe_Object = MibTableColumn
udrvFebe = _UdrvFebe_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 41, 10, 1, 40),
    _UdrvFebe_Type()
)
udrvFebe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udrvFebe.setStatus("mandatory")
_UdrvNebe_Type = Counter32
_UdrvNebe_Object = MibTableColumn
udrvNebe = _UdrvNebe_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 41, 10, 1, 41),
    _UdrvNebe_Type()
)
udrvNebe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udrvNebe.setStatus("mandatory")
_UdrvActivation_Type = Counter32
_UdrvActivation_Object = MibTableColumn
udrvActivation = _UdrvActivation_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 41, 10, 1, 42),
    _UdrvActivation_Type()
)
udrvActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udrvActivation.setStatus("mandatory")
_UdrvDeactivation_Type = Counter32
_UdrvDeactivation_Object = MibTableColumn
udrvDeactivation = _UdrvDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 41, 10, 1, 43),
    _UdrvDeactivation_Type()
)
udrvDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udrvDeactivation.setStatus("mandatory")
_UdrvTransition_Type = Counter32
_UdrvTransition_Object = MibTableColumn
udrvTransition = _UdrvTransition_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 41, 10, 1, 44),
    _UdrvTransition_Type()
)
udrvTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udrvTransition.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXUDRV-MIB",
    **{"udrvTable": udrvTable,
       "udrvEntry": udrvEntry,
       "udrvSlotNumberIndex": udrvSlotNumberIndex,
       "udrvClearStat": udrvClearStat,
       "udrvPortUp": udrvPortUp,
       "udrvPortReset": udrvPortReset,
       "udrvPortStatus": udrvPortStatus,
       "udrvFebe": udrvFebe,
       "udrvNebe": udrvNebe,
       "udrvActivation": udrvActivation,
       "udrvDeactivation": udrvDeactivation,
       "udrvTransition": udrvTransition}
)
