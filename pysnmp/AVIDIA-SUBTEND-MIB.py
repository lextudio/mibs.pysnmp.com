# SNMP MIB module (AVIDIA-SUBTEND-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AVIDIA-SUBTEND-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:49 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(pgainDSLAM,) = mibBuilder.importSymbols(
    "PAIRGAIN-COMMON-HD-MIB",
    "pgainDSLAM")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

avSubtendMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 14)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AvSubtendInterfaces_ObjectIdentity = ObjectIdentity
avSubtendInterfaces = _AvSubtendInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1)
)
_AvSubtendIfTable_Object = MibTable
avSubtendIfTable = _AvSubtendIfTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1, 1)
)
if mibBuilder.loadTexts:
    avSubtendIfTable.setStatus("mandatory")
_AvSubtendIfEntry_Object = MibTableRow
avSubtendIfEntry = _AvSubtendIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1, 1, 1)
)
avSubtendIfEntry.setIndexNames(
    (0, "AVIDIA-SUBTEND-MIB", "avSubtendIndex"),
)
if mibBuilder.loadTexts:
    avSubtendIfEntry.setStatus("mandatory")
_AvSubtendIndex_Type = Integer32
_AvSubtendIndex_Object = MibTableColumn
avSubtendIndex = _AvSubtendIndex_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1, 1, 1, 1),
    _AvSubtendIndex_Type()
)
avSubtendIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avSubtendIndex.setStatus("mandatory")
_AvSubtendIfRowStatus_Type = RowStatus
_AvSubtendIfRowStatus_Object = MibTableColumn
avSubtendIfRowStatus = _AvSubtendIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1, 1, 1, 2),
    _AvSubtendIfRowStatus_Type()
)
avSubtendIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avSubtendIfRowStatus.setStatus("mandatory")
_AvSubtendIfIndex_Type = InterfaceIndex
_AvSubtendIfIndex_Object = MibTableColumn
avSubtendIfIndex = _AvSubtendIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1, 1, 1, 3),
    _AvSubtendIfIndex_Type()
)
avSubtendIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avSubtendIfIndex.setStatus("mandatory")
_AvSubtendIfVpi_Type = Integer32
_AvSubtendIfVpi_Object = MibTableColumn
avSubtendIfVpi = _AvSubtendIfVpi_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1, 1, 1, 4),
    _AvSubtendIfVpi_Type()
)
avSubtendIfVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avSubtendIfVpi.setStatus("mandatory")
_AvSubtendIfVci_Type = Integer32
_AvSubtendIfVci_Object = MibTableColumn
avSubtendIfVci = _AvSubtendIfVci_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1, 1, 1, 5),
    _AvSubtendIfVci_Type()
)
avSubtendIfVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avSubtendIfVci.setStatus("mandatory")
_AvSubtendIfSourceIpAddress_Type = IpAddress
_AvSubtendIfSourceIpAddress_Object = MibTableColumn
avSubtendIfSourceIpAddress = _AvSubtendIfSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1, 1, 1, 6),
    _AvSubtendIfSourceIpAddress_Type()
)
avSubtendIfSourceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avSubtendIfSourceIpAddress.setStatus("mandatory")
_AvSubtendIfDestinationIpAddress_Type = IpAddress
_AvSubtendIfDestinationIpAddress_Object = MibTableColumn
avSubtendIfDestinationIpAddress = _AvSubtendIfDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1, 1, 1, 7),
    _AvSubtendIfDestinationIpAddress_Type()
)
avSubtendIfDestinationIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avSubtendIfDestinationIpAddress.setStatus("mandatory")
_AvSubtendIfSubnetMask_Type = IpAddress
_AvSubtendIfSubnetMask_Object = MibTableColumn
avSubtendIfSubnetMask = _AvSubtendIfSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1, 1, 1, 8),
    _AvSubtendIfSubnetMask_Type()
)
avSubtendIfSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avSubtendIfSubnetMask.setStatus("mandatory")


class _AvSubtendIfParentIfIndex_Type(InterfaceIndex):
    """Custom type avSubtendIfParentIfIndex based on InterfaceIndex"""
    defaultValue = 0


_AvSubtendIfParentIfIndex_Object = MibTableColumn
avSubtendIfParentIfIndex = _AvSubtendIfParentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1, 1, 1, 9),
    _AvSubtendIfParentIfIndex_Type()
)
avSubtendIfParentIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avSubtendIfParentIfIndex.setStatus("mandatory")
_AvSubtendIfParentIpAddress_Type = IpAddress
_AvSubtendIfParentIpAddress_Object = MibTableColumn
avSubtendIfParentIpAddress = _AvSubtendIfParentIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1, 1, 1, 10),
    _AvSubtendIfParentIpAddress_Type()
)
avSubtendIfParentIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avSubtendIfParentIpAddress.setStatus("mandatory")


class _AvSubtendIfAdminStatus_Type(Integer32):
    """Custom type avSubtendIfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_AvSubtendIfAdminStatus_Type.__name__ = "Integer32"
_AvSubtendIfAdminStatus_Object = MibTableColumn
avSubtendIfAdminStatus = _AvSubtendIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1, 1, 1, 11),
    _AvSubtendIfAdminStatus_Type()
)
avSubtendIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avSubtendIfAdminStatus.setStatus("mandatory")


class _AvSubtendIfOperStatus_Type(Integer32):
    """Custom type avSubtendIfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 5),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_AvSubtendIfOperStatus_Type.__name__ = "Integer32"
_AvSubtendIfOperStatus_Object = MibTableColumn
avSubtendIfOperStatus = _AvSubtendIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1, 1, 1, 12),
    _AvSubtendIfOperStatus_Type()
)
avSubtendIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avSubtendIfOperStatus.setStatus("mandatory")


class _AvSubtendIndexNext_Type(Integer32):
    """Custom type avSubtendIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_AvSubtendIndexNext_Type.__name__ = "Integer32"
_AvSubtendIndexNext_Object = MibScalar
avSubtendIndexNext = _AvSubtendIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1, 2),
    _AvSubtendIndexNext_Type()
)
avSubtendIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avSubtendIndexNext.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVIDIA-SUBTEND-MIB",
    **{"avSubtendMIB": avSubtendMIB,
       "avSubtendInterfaces": avSubtendInterfaces,
       "avSubtendIfTable": avSubtendIfTable,
       "avSubtendIfEntry": avSubtendIfEntry,
       "avSubtendIndex": avSubtendIndex,
       "avSubtendIfRowStatus": avSubtendIfRowStatus,
       "avSubtendIfIndex": avSubtendIfIndex,
       "avSubtendIfVpi": avSubtendIfVpi,
       "avSubtendIfVci": avSubtendIfVci,
       "avSubtendIfSourceIpAddress": avSubtendIfSourceIpAddress,
       "avSubtendIfDestinationIpAddress": avSubtendIfDestinationIpAddress,
       "avSubtendIfSubnetMask": avSubtendIfSubnetMask,
       "avSubtendIfParentIfIndex": avSubtendIfParentIfIndex,
       "avSubtendIfParentIpAddress": avSubtendIfParentIpAddress,
       "avSubtendIfAdminStatus": avSubtendIfAdminStatus,
       "avSubtendIfOperStatus": avSubtendIfOperStatus,
       "avSubtendIndexNext": avSubtendIndexNext}
)
