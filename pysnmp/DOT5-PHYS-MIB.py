# SNMP MIB module (DOT5-PHYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOT5-PHYS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:18 2024
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

(ctDot5PhysMgmt,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctDot5PhysMgmt")

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

_Dot5PhysMgmtRev1_ObjectIdentity = ObjectIdentity
dot5PhysMgmtRev1 = _Dot5PhysMgmtRev1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1)
)
_Dot5PhysMgmtDevice_ObjectIdentity = ObjectIdentity
dot5PhysMgmtDevice = _Dot5PhysMgmtDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 1)
)
_Dot5PhysMgmtDeviceRingCount_Type = Integer32
_Dot5PhysMgmtDeviceRingCount_Object = MibScalar
dot5PhysMgmtDeviceRingCount = _Dot5PhysMgmtDeviceRingCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 1, 1),
    _Dot5PhysMgmtDeviceRingCount_Type()
)
dot5PhysMgmtDeviceRingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtDeviceRingCount.setStatus("mandatory")
_Dot5PhysMgmtDevicePortCount_Type = Integer32
_Dot5PhysMgmtDevicePortCount_Object = MibScalar
dot5PhysMgmtDevicePortCount = _Dot5PhysMgmtDevicePortCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 1, 2),
    _Dot5PhysMgmtDevicePortCount_Type()
)
dot5PhysMgmtDevicePortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtDevicePortCount.setStatus("mandatory")


class _Dot5PhysMgmtDevicePortsEnable_Type(Integer32):
    """Custom type dot5PhysMgmtDevicePortsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("noEnable", 1))
    )


_Dot5PhysMgmtDevicePortsEnable_Type.__name__ = "Integer32"
_Dot5PhysMgmtDevicePortsEnable_Object = MibScalar
dot5PhysMgmtDevicePortsEnable = _Dot5PhysMgmtDevicePortsEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 1, 3),
    _Dot5PhysMgmtDevicePortsEnable_Type()
)
dot5PhysMgmtDevicePortsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot5PhysMgmtDevicePortsEnable.setStatus("mandatory")
_Dot5PhysMgmtDevicePortsOn_Type = Integer32
_Dot5PhysMgmtDevicePortsOn_Object = MibScalar
dot5PhysMgmtDevicePortsOn = _Dot5PhysMgmtDevicePortsOn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 1, 4),
    _Dot5PhysMgmtDevicePortsOn_Type()
)
dot5PhysMgmtDevicePortsOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtDevicePortsOn.setStatus("mandatory")
_Dot5PhysMgmtDevicePortsOper_Type = Integer32
_Dot5PhysMgmtDevicePortsOper_Object = MibScalar
dot5PhysMgmtDevicePortsOper = _Dot5PhysMgmtDevicePortsOper_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 1, 5),
    _Dot5PhysMgmtDevicePortsOper_Type()
)
dot5PhysMgmtDevicePortsOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtDevicePortsOper.setStatus("mandatory")
_Dot5PhysMgmtDeviceStnPortCount_Type = Integer32
_Dot5PhysMgmtDeviceStnPortCount_Object = MibScalar
dot5PhysMgmtDeviceStnPortCount = _Dot5PhysMgmtDeviceStnPortCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 1, 6),
    _Dot5PhysMgmtDeviceStnPortCount_Type()
)
dot5PhysMgmtDeviceStnPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtDeviceStnPortCount.setStatus("mandatory")


class _Dot5PhysMgmtDeviceStnPortsEnable_Type(Integer32):
    """Custom type dot5PhysMgmtDeviceStnPortsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("noEnable", 1))
    )


_Dot5PhysMgmtDeviceStnPortsEnable_Type.__name__ = "Integer32"
_Dot5PhysMgmtDeviceStnPortsEnable_Object = MibScalar
dot5PhysMgmtDeviceStnPortsEnable = _Dot5PhysMgmtDeviceStnPortsEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 1, 7),
    _Dot5PhysMgmtDeviceStnPortsEnable_Type()
)
dot5PhysMgmtDeviceStnPortsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot5PhysMgmtDeviceStnPortsEnable.setStatus("mandatory")
_Dot5PhysMgmtDeviceStnPortsOn_Type = Integer32
_Dot5PhysMgmtDeviceStnPortsOn_Object = MibScalar
dot5PhysMgmtDeviceStnPortsOn = _Dot5PhysMgmtDeviceStnPortsOn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 1, 8),
    _Dot5PhysMgmtDeviceStnPortsOn_Type()
)
dot5PhysMgmtDeviceStnPortsOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtDeviceStnPortsOn.setStatus("mandatory")
_Dot5PhysMgmtDeviceRingPortCount_Type = Integer32
_Dot5PhysMgmtDeviceRingPortCount_Object = MibScalar
dot5PhysMgmtDeviceRingPortCount = _Dot5PhysMgmtDeviceRingPortCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 1, 9),
    _Dot5PhysMgmtDeviceRingPortCount_Type()
)
dot5PhysMgmtDeviceRingPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtDeviceRingPortCount.setStatus("mandatory")


class _Dot5PhysMgmtDeviceRingPortsEnable_Type(Integer32):
    """Custom type dot5PhysMgmtDeviceRingPortsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("noEnable", 1))
    )


_Dot5PhysMgmtDeviceRingPortsEnable_Type.__name__ = "Integer32"
_Dot5PhysMgmtDeviceRingPortsEnable_Object = MibScalar
dot5PhysMgmtDeviceRingPortsEnable = _Dot5PhysMgmtDeviceRingPortsEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 1, 10),
    _Dot5PhysMgmtDeviceRingPortsEnable_Type()
)
dot5PhysMgmtDeviceRingPortsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot5PhysMgmtDeviceRingPortsEnable.setStatus("mandatory")
_Dot5PhysMgmtDeviceRingPortsOn_Type = Integer32
_Dot5PhysMgmtDeviceRingPortsOn_Object = MibScalar
dot5PhysMgmtDeviceRingPortsOn = _Dot5PhysMgmtDeviceRingPortsOn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 1, 11),
    _Dot5PhysMgmtDeviceRingPortsOn_Type()
)
dot5PhysMgmtDeviceRingPortsOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtDeviceRingPortsOn.setStatus("mandatory")
_Dot5PhysMgmtDevicePortAssociationChanges_Type = Counter32
_Dot5PhysMgmtDevicePortAssociationChanges_Object = MibScalar
dot5PhysMgmtDevicePortAssociationChanges = _Dot5PhysMgmtDevicePortAssociationChanges_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 1, 12),
    _Dot5PhysMgmtDevicePortAssociationChanges_Type()
)
dot5PhysMgmtDevicePortAssociationChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtDevicePortAssociationChanges.setStatus("mandatory")
_Dot5PhysMgmtBoard_ObjectIdentity = ObjectIdentity
dot5PhysMgmtBoard = _Dot5PhysMgmtBoard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 2)
)
_Dot5PhysMgmtBoardTable_Object = MibTable
dot5PhysMgmtBoardTable = _Dot5PhysMgmtBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dot5PhysMgmtBoardTable.setStatus("mandatory")
_Dot5PhysMgmtBoardEntry_Object = MibTableRow
dot5PhysMgmtBoardEntry = _Dot5PhysMgmtBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 2, 1, 1)
)
dot5PhysMgmtBoardEntry.setIndexNames(
    (0, "DOT5-PHYS-MIB", "dot5PhysMgmtBoardId"),
)
if mibBuilder.loadTexts:
    dot5PhysMgmtBoardEntry.setStatus("mandatory")
_Dot5PhysMgmtBoardId_Type = Integer32
_Dot5PhysMgmtBoardId_Object = MibTableColumn
dot5PhysMgmtBoardId = _Dot5PhysMgmtBoardId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 2, 1, 1, 1),
    _Dot5PhysMgmtBoardId_Type()
)
dot5PhysMgmtBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtBoardId.setStatus("mandatory")


class _Dot5PhysMgmtBoardDomain_Type(Integer32):
    """Custom type dot5PhysMgmtBoardDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("outsideDomain", 1),
          ("withinDomain", 2))
    )


_Dot5PhysMgmtBoardDomain_Type.__name__ = "Integer32"
_Dot5PhysMgmtBoardDomain_Object = MibTableColumn
dot5PhysMgmtBoardDomain = _Dot5PhysMgmtBoardDomain_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 2, 1, 1, 2),
    _Dot5PhysMgmtBoardDomain_Type()
)
dot5PhysMgmtBoardDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtBoardDomain.setStatus("mandatory")


class _Dot5PhysMgmtBoardName_Type(DisplayString):
    """Custom type dot5PhysMgmtBoardName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_Dot5PhysMgmtBoardName_Type.__name__ = "DisplayString"
_Dot5PhysMgmtBoardName_Object = MibTableColumn
dot5PhysMgmtBoardName = _Dot5PhysMgmtBoardName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 2, 1, 1, 3),
    _Dot5PhysMgmtBoardName_Type()
)
dot5PhysMgmtBoardName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot5PhysMgmtBoardName.setStatus("mandatory")


class _Dot5PhysMgmtBoardDesc_Type(DisplayString):
    """Custom type dot5PhysMgmtBoardDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Dot5PhysMgmtBoardDesc_Type.__name__ = "DisplayString"
_Dot5PhysMgmtBoardDesc_Object = MibTableColumn
dot5PhysMgmtBoardDesc = _Dot5PhysMgmtBoardDesc_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 2, 1, 1, 4),
    _Dot5PhysMgmtBoardDesc_Type()
)
dot5PhysMgmtBoardDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtBoardDesc.setStatus("mandatory")
_Dot5PhysMgmtBoardDot5PortCount_Type = Integer32
_Dot5PhysMgmtBoardDot5PortCount_Object = MibTableColumn
dot5PhysMgmtBoardDot5PortCount = _Dot5PhysMgmtBoardDot5PortCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 2, 1, 1, 5),
    _Dot5PhysMgmtBoardDot5PortCount_Type()
)
dot5PhysMgmtBoardDot5PortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtBoardDot5PortCount.setStatus("mandatory")


class _Dot5PhysMgmtBoardDot5PortsEnable_Type(Integer32):
    """Custom type dot5PhysMgmtBoardDot5PortsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("noEnable", 1))
    )


_Dot5PhysMgmtBoardDot5PortsEnable_Type.__name__ = "Integer32"
_Dot5PhysMgmtBoardDot5PortsEnable_Object = MibTableColumn
dot5PhysMgmtBoardDot5PortsEnable = _Dot5PhysMgmtBoardDot5PortsEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 2, 1, 1, 6),
    _Dot5PhysMgmtBoardDot5PortsEnable_Type()
)
dot5PhysMgmtBoardDot5PortsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot5PhysMgmtBoardDot5PortsEnable.setStatus("mandatory")
_Dot5PhysMgmtBoardDot5PortsOn_Type = Integer32
_Dot5PhysMgmtBoardDot5PortsOn_Object = MibTableColumn
dot5PhysMgmtBoardDot5PortsOn = _Dot5PhysMgmtBoardDot5PortsOn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 2, 1, 1, 7),
    _Dot5PhysMgmtBoardDot5PortsOn_Type()
)
dot5PhysMgmtBoardDot5PortsOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtBoardDot5PortsOn.setStatus("mandatory")
_Dot5PhysMgmtBoardDot5PortsOper_Type = Integer32
_Dot5PhysMgmtBoardDot5PortsOper_Object = MibTableColumn
dot5PhysMgmtBoardDot5PortsOper = _Dot5PhysMgmtBoardDot5PortsOper_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 2, 1, 1, 8),
    _Dot5PhysMgmtBoardDot5PortsOper_Type()
)
dot5PhysMgmtBoardDot5PortsOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtBoardDot5PortsOper.setStatus("mandatory")
_Dot5PhysMgmtBoardDot5StnPortCount_Type = Integer32
_Dot5PhysMgmtBoardDot5StnPortCount_Object = MibTableColumn
dot5PhysMgmtBoardDot5StnPortCount = _Dot5PhysMgmtBoardDot5StnPortCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 2, 1, 1, 9),
    _Dot5PhysMgmtBoardDot5StnPortCount_Type()
)
dot5PhysMgmtBoardDot5StnPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtBoardDot5StnPortCount.setStatus("mandatory")


class _Dot5PhysMgmtBoardDot5StnPortsEnable_Type(Integer32):
    """Custom type dot5PhysMgmtBoardDot5StnPortsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("noEnable", 1))
    )


_Dot5PhysMgmtBoardDot5StnPortsEnable_Type.__name__ = "Integer32"
_Dot5PhysMgmtBoardDot5StnPortsEnable_Object = MibTableColumn
dot5PhysMgmtBoardDot5StnPortsEnable = _Dot5PhysMgmtBoardDot5StnPortsEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 2, 1, 1, 10),
    _Dot5PhysMgmtBoardDot5StnPortsEnable_Type()
)
dot5PhysMgmtBoardDot5StnPortsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot5PhysMgmtBoardDot5StnPortsEnable.setStatus("mandatory")
_Dot5PhysMgmtBoardDot5StnPortsOn_Type = Integer32
_Dot5PhysMgmtBoardDot5StnPortsOn_Object = MibTableColumn
dot5PhysMgmtBoardDot5StnPortsOn = _Dot5PhysMgmtBoardDot5StnPortsOn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 2, 1, 1, 11),
    _Dot5PhysMgmtBoardDot5StnPortsOn_Type()
)
dot5PhysMgmtBoardDot5StnPortsOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtBoardDot5StnPortsOn.setStatus("mandatory")
_Dot5PhysMgmtBoardDot5RingPortCount_Type = Integer32
_Dot5PhysMgmtBoardDot5RingPortCount_Object = MibTableColumn
dot5PhysMgmtBoardDot5RingPortCount = _Dot5PhysMgmtBoardDot5RingPortCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 2, 1, 1, 12),
    _Dot5PhysMgmtBoardDot5RingPortCount_Type()
)
dot5PhysMgmtBoardDot5RingPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtBoardDot5RingPortCount.setStatus("mandatory")


class _Dot5PhysMgmtBoardDot5RingPortsEnable_Type(Integer32):
    """Custom type dot5PhysMgmtBoardDot5RingPortsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("noEnable", 1))
    )


_Dot5PhysMgmtBoardDot5RingPortsEnable_Type.__name__ = "Integer32"
_Dot5PhysMgmtBoardDot5RingPortsEnable_Object = MibTableColumn
dot5PhysMgmtBoardDot5RingPortsEnable = _Dot5PhysMgmtBoardDot5RingPortsEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 2, 1, 1, 13),
    _Dot5PhysMgmtBoardDot5RingPortsEnable_Type()
)
dot5PhysMgmtBoardDot5RingPortsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot5PhysMgmtBoardDot5RingPortsEnable.setStatus("mandatory")
_Dot5PhysMgmtBoardDot5RingPortsOn_Type = Integer32
_Dot5PhysMgmtBoardDot5RingPortsOn_Object = MibTableColumn
dot5PhysMgmtBoardDot5RingPortsOn = _Dot5PhysMgmtBoardDot5RingPortsOn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 2, 1, 1, 14),
    _Dot5PhysMgmtBoardDot5RingPortsOn_Type()
)
dot5PhysMgmtBoardDot5RingPortsOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtBoardDot5RingPortsOn.setStatus("mandatory")


class _Dot5PhysMgmtBoardMode_Type(Integer32):
    """Custom type dot5PhysMgmtBoardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoMode", 2),
          ("managementMode", 1),
          ("unknown", 3))
    )


_Dot5PhysMgmtBoardMode_Type.__name__ = "Integer32"
_Dot5PhysMgmtBoardMode_Object = MibTableColumn
dot5PhysMgmtBoardMode = _Dot5PhysMgmtBoardMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 2, 1, 1, 15),
    _Dot5PhysMgmtBoardMode_Type()
)
dot5PhysMgmtBoardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot5PhysMgmtBoardMode.setStatus("mandatory")


class _Dot5PhysMgmtBoardSpeed_Type(Integer32):
    """Custom type dot5PhysMgmtBoardSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              10,
              16,
              100)
        )
    )
    namedValues = NamedValues(
        *(("fourMegaBits", 4),
          ("hundredMegaBits", 100),
          ("sixteenMegaBits", 16),
          ("tenMegaBits", 10),
          ("unknown", 1))
    )


_Dot5PhysMgmtBoardSpeed_Type.__name__ = "Integer32"
_Dot5PhysMgmtBoardSpeed_Object = MibTableColumn
dot5PhysMgmtBoardSpeed = _Dot5PhysMgmtBoardSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 2, 1, 1, 16),
    _Dot5PhysMgmtBoardSpeed_Type()
)
dot5PhysMgmtBoardSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot5PhysMgmtBoardSpeed.setStatus("mandatory")


class _Dot5PhysMgmtBoardSpeedFault_Type(Integer32):
    """Custom type dot5PhysMgmtBoardSpeedFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("faultDetected", 2),
          ("noFaultDetected", 1),
          ("notSupported", 3))
    )


_Dot5PhysMgmtBoardSpeedFault_Type.__name__ = "Integer32"
_Dot5PhysMgmtBoardSpeedFault_Object = MibTableColumn
dot5PhysMgmtBoardSpeedFault = _Dot5PhysMgmtBoardSpeedFault_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 2, 1, 1, 17),
    _Dot5PhysMgmtBoardSpeedFault_Type()
)
dot5PhysMgmtBoardSpeedFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtBoardSpeedFault.setStatus("mandatory")


class _Dot5PhysMgmtBoardSpeedFaultLocation_Type(Integer32):
    """Custom type dot5PhysMgmtBoardSpeedFaultLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fnb", 2),
          ("notApplicable", 1),
          ("ringIn", 3),
          ("ringOut", 4))
    )


_Dot5PhysMgmtBoardSpeedFaultLocation_Type.__name__ = "Integer32"
_Dot5PhysMgmtBoardSpeedFaultLocation_Object = MibTableColumn
dot5PhysMgmtBoardSpeedFaultLocation = _Dot5PhysMgmtBoardSpeedFaultLocation_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 2, 1, 1, 18),
    _Dot5PhysMgmtBoardSpeedFaultLocation_Type()
)
dot5PhysMgmtBoardSpeedFaultLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtBoardSpeedFaultLocation.setStatus("mandatory")


class _Dot5PhysMgmtBoardPortAssociation_Type(Integer32):
    """Custom type dot5PhysMgmtBoardPortAssociation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Dot5PhysMgmtBoardPortAssociation_Type.__name__ = "Integer32"
_Dot5PhysMgmtBoardPortAssociation_Object = MibTableColumn
dot5PhysMgmtBoardPortAssociation = _Dot5PhysMgmtBoardPortAssociation_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 2, 1, 1, 19),
    _Dot5PhysMgmtBoardPortAssociation_Type()
)
dot5PhysMgmtBoardPortAssociation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot5PhysMgmtBoardPortAssociation.setStatus("mandatory")
_Dot5PhysMgmtBoardPortAssociationChanges_Type = Counter32
_Dot5PhysMgmtBoardPortAssociationChanges_Object = MibTableColumn
dot5PhysMgmtBoardPortAssociationChanges = _Dot5PhysMgmtBoardPortAssociationChanges_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 2, 1, 1, 20),
    _Dot5PhysMgmtBoardPortAssociationChanges_Type()
)
dot5PhysMgmtBoardPortAssociationChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtBoardPortAssociationChanges.setStatus("mandatory")
_Dot5PhysMgmtPort_ObjectIdentity = ObjectIdentity
dot5PhysMgmtPort = _Dot5PhysMgmtPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3)
)
_Dot5PhysMgmtPortCommon_ObjectIdentity = ObjectIdentity
dot5PhysMgmtPortCommon = _Dot5PhysMgmtPortCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 1)
)
_Dot5PhysMgmtPortCommonTable_Object = MibTable
dot5PhysMgmtPortCommonTable = _Dot5PhysMgmtPortCommonTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    dot5PhysMgmtPortCommonTable.setStatus("mandatory")
_Dot5PhysMgmtPortCommonEntry_Object = MibTableRow
dot5PhysMgmtPortCommonEntry = _Dot5PhysMgmtPortCommonEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 1, 1, 1)
)
dot5PhysMgmtPortCommonEntry.setIndexNames(
    (0, "DOT5-PHYS-MIB", "dot5PhysMgmtPortCommonBoardId"),
    (0, "DOT5-PHYS-MIB", "dot5PhysMgmtPortCommonPortId"),
)
if mibBuilder.loadTexts:
    dot5PhysMgmtPortCommonEntry.setStatus("mandatory")
_Dot5PhysMgmtPortCommonPortId_Type = Integer32
_Dot5PhysMgmtPortCommonPortId_Object = MibTableColumn
dot5PhysMgmtPortCommonPortId = _Dot5PhysMgmtPortCommonPortId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 1, 1, 1, 1),
    _Dot5PhysMgmtPortCommonPortId_Type()
)
dot5PhysMgmtPortCommonPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtPortCommonPortId.setStatus("mandatory")
_Dot5PhysMgmtPortCommonBoardId_Type = Integer32
_Dot5PhysMgmtPortCommonBoardId_Object = MibTableColumn
dot5PhysMgmtPortCommonBoardId = _Dot5PhysMgmtPortCommonBoardId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 1, 1, 1, 2),
    _Dot5PhysMgmtPortCommonBoardId_Type()
)
dot5PhysMgmtPortCommonBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtPortCommonBoardId.setStatus("mandatory")


class _Dot5PhysMgmtPortCommonPortName_Type(DisplayString):
    """Custom type dot5PhysMgmtPortCommonPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_Dot5PhysMgmtPortCommonPortName_Type.__name__ = "DisplayString"
_Dot5PhysMgmtPortCommonPortName_Object = MibTableColumn
dot5PhysMgmtPortCommonPortName = _Dot5PhysMgmtPortCommonPortName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 1, 1, 1, 3),
    _Dot5PhysMgmtPortCommonPortName_Type()
)
dot5PhysMgmtPortCommonPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot5PhysMgmtPortCommonPortName.setStatus("mandatory")


class _Dot5PhysMgmtPortCommonPortAdminState_Type(Integer32):
    """Custom type dot5PhysMgmtPortCommonPortAdminState based on Integer32"""
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


_Dot5PhysMgmtPortCommonPortAdminState_Type.__name__ = "Integer32"
_Dot5PhysMgmtPortCommonPortAdminState_Object = MibTableColumn
dot5PhysMgmtPortCommonPortAdminState = _Dot5PhysMgmtPortCommonPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 1, 1, 1, 4),
    _Dot5PhysMgmtPortCommonPortAdminState_Type()
)
dot5PhysMgmtPortCommonPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot5PhysMgmtPortCommonPortAdminState.setStatus("mandatory")


class _Dot5PhysMgmtPortCommonPortOperState_Type(Integer32):
    """Custom type dot5PhysMgmtPortCommonPortOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notOperational", 1),
          ("operational", 2))
    )


_Dot5PhysMgmtPortCommonPortOperState_Type.__name__ = "Integer32"
_Dot5PhysMgmtPortCommonPortOperState_Object = MibTableColumn
dot5PhysMgmtPortCommonPortOperState = _Dot5PhysMgmtPortCommonPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 1, 1, 1, 5),
    _Dot5PhysMgmtPortCommonPortOperState_Type()
)
dot5PhysMgmtPortCommonPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtPortCommonPortOperState.setStatus("mandatory")
_Dot5PhysMgmtPortCommonPortType_Type = ObjectIdentifier
_Dot5PhysMgmtPortCommonPortType_Object = MibTableColumn
dot5PhysMgmtPortCommonPortType = _Dot5PhysMgmtPortCommonPortType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 1, 1, 1, 6),
    _Dot5PhysMgmtPortCommonPortType_Type()
)
dot5PhysMgmtPortCommonPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtPortCommonPortType.setStatus("mandatory")


class _Dot5PhysMgmtPortCommonSpeedFaultDetect_Type(Integer32):
    """Custom type dot5PhysMgmtPortCommonSpeedFaultDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("faultDetected", 3),
          ("noFaultDetected", 2),
          ("notDetectable", 1))
    )


_Dot5PhysMgmtPortCommonSpeedFaultDetect_Type.__name__ = "Integer32"
_Dot5PhysMgmtPortCommonSpeedFaultDetect_Object = MibTableColumn
dot5PhysMgmtPortCommonSpeedFaultDetect = _Dot5PhysMgmtPortCommonSpeedFaultDetect_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 1, 1, 1, 7),
    _Dot5PhysMgmtPortCommonSpeedFaultDetect_Type()
)
dot5PhysMgmtPortCommonSpeedFaultDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtPortCommonSpeedFaultDetect.setStatus("mandatory")


class _Dot5PhysMgmtPortCommonRingOutEnable_Type(Integer32):
    """Custom type dot5PhysMgmtPortCommonRingOutEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("notAvailable", 1))
    )


_Dot5PhysMgmtPortCommonRingOutEnable_Type.__name__ = "Integer32"
_Dot5PhysMgmtPortCommonRingOutEnable_Object = MibTableColumn
dot5PhysMgmtPortCommonRingOutEnable = _Dot5PhysMgmtPortCommonRingOutEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 1, 1, 1, 8),
    _Dot5PhysMgmtPortCommonRingOutEnable_Type()
)
dot5PhysMgmtPortCommonRingOutEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot5PhysMgmtPortCommonRingOutEnable.setStatus("mandatory")


class _Dot5PhysMgmtPortCommonPortAssociation_Type(Integer32):
    """Custom type dot5PhysMgmtPortCommonPortAssociation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_Dot5PhysMgmtPortCommonPortAssociation_Type.__name__ = "Integer32"
_Dot5PhysMgmtPortCommonPortAssociation_Object = MibTableColumn
dot5PhysMgmtPortCommonPortAssociation = _Dot5PhysMgmtPortCommonPortAssociation_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 1, 1, 1, 9),
    _Dot5PhysMgmtPortCommonPortAssociation_Type()
)
dot5PhysMgmtPortCommonPortAssociation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot5PhysMgmtPortCommonPortAssociation.setStatus("mandatory")
_Dot5PhysMgmtPortCommonMauCompId_Type = Integer32
_Dot5PhysMgmtPortCommonMauCompId_Object = MibTableColumn
dot5PhysMgmtPortCommonMauCompId = _Dot5PhysMgmtPortCommonMauCompId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 1, 1, 1, 10),
    _Dot5PhysMgmtPortCommonMauCompId_Type()
)
dot5PhysMgmtPortCommonMauCompId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtPortCommonMauCompId.setStatus("mandatory")
_Dot5PhysMgmtPortStn_ObjectIdentity = ObjectIdentity
dot5PhysMgmtPortStn = _Dot5PhysMgmtPortStn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 2)
)
_Dot5PhysMgmtPortStnTable_Object = MibTable
dot5PhysMgmtPortStnTable = _Dot5PhysMgmtPortStnTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    dot5PhysMgmtPortStnTable.setStatus("mandatory")
_Dot5PhysMgmtPortStnEntry_Object = MibTableRow
dot5PhysMgmtPortStnEntry = _Dot5PhysMgmtPortStnEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 2, 1, 1)
)
dot5PhysMgmtPortStnEntry.setIndexNames(
    (0, "DOT5-PHYS-MIB", "dot5PhysMgmtPortStnBoardId"),
    (0, "DOT5-PHYS-MIB", "dot5PhysMgmtPortStnPortId"),
)
if mibBuilder.loadTexts:
    dot5PhysMgmtPortStnEntry.setStatus("mandatory")
_Dot5PhysMgmtPortStnPortId_Type = Integer32
_Dot5PhysMgmtPortStnPortId_Object = MibTableColumn
dot5PhysMgmtPortStnPortId = _Dot5PhysMgmtPortStnPortId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 2, 1, 1, 1),
    _Dot5PhysMgmtPortStnPortId_Type()
)
dot5PhysMgmtPortStnPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtPortStnPortId.setStatus("mandatory")
_Dot5PhysMgmtPortStnBoardId_Type = Integer32
_Dot5PhysMgmtPortStnBoardId_Object = MibTableColumn
dot5PhysMgmtPortStnBoardId = _Dot5PhysMgmtPortStnBoardId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 2, 1, 1, 2),
    _Dot5PhysMgmtPortStnBoardId_Type()
)
dot5PhysMgmtPortStnBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtPortStnBoardId.setStatus("mandatory")


class _Dot5PhysMgmtPortStnPortLinkState_Type(Integer32):
    """Custom type dot5PhysMgmtPortStnPortLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link", 2),
          ("noLink", 1))
    )


_Dot5PhysMgmtPortStnPortLinkState_Type.__name__ = "Integer32"
_Dot5PhysMgmtPortStnPortLinkState_Object = MibTableColumn
dot5PhysMgmtPortStnPortLinkState = _Dot5PhysMgmtPortStnPortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 2, 1, 1, 3),
    _Dot5PhysMgmtPortStnPortLinkState_Type()
)
dot5PhysMgmtPortStnPortLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtPortStnPortLinkState.setStatus("mandatory")
_Dot5PhysMgmtPortStnPortLinkStateTime_Type = TimeTicks
_Dot5PhysMgmtPortStnPortLinkStateTime_Object = MibTableColumn
dot5PhysMgmtPortStnPortLinkStateTime = _Dot5PhysMgmtPortStnPortLinkStateTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 2, 1, 1, 4),
    _Dot5PhysMgmtPortStnPortLinkStateTime_Type()
)
dot5PhysMgmtPortStnPortLinkStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtPortStnPortLinkStateTime.setStatus("mandatory")


class _Dot5PhysMgmtPortStnInsertionTrapEnable_Type(Integer32):
    """Custom type dot5PhysMgmtPortStnInsertionTrapEnable based on Integer32"""
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


_Dot5PhysMgmtPortStnInsertionTrapEnable_Type.__name__ = "Integer32"
_Dot5PhysMgmtPortStnInsertionTrapEnable_Object = MibTableColumn
dot5PhysMgmtPortStnInsertionTrapEnable = _Dot5PhysMgmtPortStnInsertionTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 2, 1, 1, 5),
    _Dot5PhysMgmtPortStnInsertionTrapEnable_Type()
)
dot5PhysMgmtPortStnInsertionTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot5PhysMgmtPortStnInsertionTrapEnable.setStatus("mandatory")
_Dot5PhysMgmtPortRing_ObjectIdentity = ObjectIdentity
dot5PhysMgmtPortRing = _Dot5PhysMgmtPortRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 3)
)
_Dot5PhysMgmtPortRingTable_Object = MibTable
dot5PhysMgmtPortRingTable = _Dot5PhysMgmtPortRingTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    dot5PhysMgmtPortRingTable.setStatus("mandatory")
_Dot5PhysMgmtPortRingEntry_Object = MibTableRow
dot5PhysMgmtPortRingEntry = _Dot5PhysMgmtPortRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 3, 1, 1)
)
dot5PhysMgmtPortRingEntry.setIndexNames(
    (0, "DOT5-PHYS-MIB", "dot5PhysMgmtPortRingBoardId"),
    (0, "DOT5-PHYS-MIB", "dot5PhysMgmtPortRingPortId"),
)
if mibBuilder.loadTexts:
    dot5PhysMgmtPortRingEntry.setStatus("mandatory")
_Dot5PhysMgmtPortRingPortId_Type = Integer32
_Dot5PhysMgmtPortRingPortId_Object = MibTableColumn
dot5PhysMgmtPortRingPortId = _Dot5PhysMgmtPortRingPortId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 3, 1, 1, 1),
    _Dot5PhysMgmtPortRingPortId_Type()
)
dot5PhysMgmtPortRingPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtPortRingPortId.setStatus("mandatory")
_Dot5PhysMgmtPortRingBoardId_Type = Integer32
_Dot5PhysMgmtPortRingBoardId_Object = MibTableColumn
dot5PhysMgmtPortRingBoardId = _Dot5PhysMgmtPortRingBoardId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 3, 1, 1, 2),
    _Dot5PhysMgmtPortRingBoardId_Type()
)
dot5PhysMgmtPortRingBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtPortRingBoardId.setStatus("mandatory")


class _Dot5PhysMgmtPortRingPortClass_Type(Integer32):
    """Custom type dot5PhysMgmtPortRingPortClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autowrap", 2),
          ("noAutowrap", 1),
          ("selectable", 3))
    )


_Dot5PhysMgmtPortRingPortClass_Type.__name__ = "Integer32"
_Dot5PhysMgmtPortRingPortClass_Object = MibTableColumn
dot5PhysMgmtPortRingPortClass = _Dot5PhysMgmtPortRingPortClass_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 3, 1, 1, 3),
    _Dot5PhysMgmtPortRingPortClass_Type()
)
dot5PhysMgmtPortRingPortClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtPortRingPortClass.setStatus("mandatory")


class _Dot5PhysMgmtPortRingPortMediaSelect_Type(Integer32):
    """Custom type dot5PhysMgmtPortRingPortMediaSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fiber", 3),
          ("noSelection", 1),
          ("stp", 2))
    )


_Dot5PhysMgmtPortRingPortMediaSelect_Type.__name__ = "Integer32"
_Dot5PhysMgmtPortRingPortMediaSelect_Object = MibTableColumn
dot5PhysMgmtPortRingPortMediaSelect = _Dot5PhysMgmtPortRingPortMediaSelect_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 3, 1, 1, 4),
    _Dot5PhysMgmtPortRingPortMediaSelect_Type()
)
dot5PhysMgmtPortRingPortMediaSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot5PhysMgmtPortRingPortMediaSelect.setStatus("mandatory")


class _Dot5PhysMgmtPortRingFaultStatus_Type(Integer32):
    """Custom type dot5PhysMgmtPortRingFaultStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("faultDetected", 3),
          ("noFaultDetected", 2),
          ("notSupported", 1))
    )


_Dot5PhysMgmtPortRingFaultStatus_Type.__name__ = "Integer32"
_Dot5PhysMgmtPortRingFaultStatus_Object = MibTableColumn
dot5PhysMgmtPortRingFaultStatus = _Dot5PhysMgmtPortRingFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 3, 1, 1, 5),
    _Dot5PhysMgmtPortRingFaultStatus_Type()
)
dot5PhysMgmtPortRingFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtPortRingFaultStatus.setStatus("mandatory")
_Dot5PhysMgmtPortRingFaultStateTime_Type = TimeTicks
_Dot5PhysMgmtPortRingFaultStateTime_Object = MibTableColumn
dot5PhysMgmtPortRingFaultStateTime = _Dot5PhysMgmtPortRingFaultStateTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 3, 1, 1, 6),
    _Dot5PhysMgmtPortRingFaultStateTime_Type()
)
dot5PhysMgmtPortRingFaultStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtPortRingFaultStateTime.setStatus("mandatory")


class _Dot5PhysMgmtPortRingPhantomCurrent_Type(Integer32):
    """Custom type dot5PhysMgmtPortRingPhantomCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activatePhantom", 2),
          ("deactivatePhantom", 3),
          ("noPhantomAvailable", 1))
    )


_Dot5PhysMgmtPortRingPhantomCurrent_Type.__name__ = "Integer32"
_Dot5PhysMgmtPortRingPhantomCurrent_Object = MibTableColumn
dot5PhysMgmtPortRingPhantomCurrent = _Dot5PhysMgmtPortRingPhantomCurrent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 3, 1, 1, 7),
    _Dot5PhysMgmtPortRingPhantomCurrent_Type()
)
dot5PhysMgmtPortRingPhantomCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot5PhysMgmtPortRingPhantomCurrent.setStatus("mandatory")


class _Dot5PhysMgmtPortRingPortType_Type(Integer32):
    """Custom type dot5PhysMgmtPortRingPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ringIn", 1),
          ("ringOut", 2))
    )


_Dot5PhysMgmtPortRingPortType_Type.__name__ = "Integer32"
_Dot5PhysMgmtPortRingPortType_Object = MibTableColumn
dot5PhysMgmtPortRingPortType = _Dot5PhysMgmtPortRingPortType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 3, 1, 1, 8),
    _Dot5PhysMgmtPortRingPortType_Type()
)
dot5PhysMgmtPortRingPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtPortRingPortType.setStatus("mandatory")
_Dot5PhysMgmtPortSwitch_ObjectIdentity = ObjectIdentity
dot5PhysMgmtPortSwitch = _Dot5PhysMgmtPortSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 3, 4)
)
_Dot5PhysMgmtRingSpeedTables_ObjectIdentity = ObjectIdentity
dot5PhysMgmtRingSpeedTables = _Dot5PhysMgmtRingSpeedTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 4)
)
_Dot5PhysMgmtDeviceRingSpeedTable_Object = MibTable
dot5PhysMgmtDeviceRingSpeedTable = _Dot5PhysMgmtDeviceRingSpeedTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dot5PhysMgmtDeviceRingSpeedTable.setStatus("mandatory")
_Dot5PhysMgmtDeviceRingSpeedEntry_Object = MibTableRow
dot5PhysMgmtDeviceRingSpeedEntry = _Dot5PhysMgmtDeviceRingSpeedEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 4, 1, 1)
)
dot5PhysMgmtDeviceRingSpeedEntry.setIndexNames(
    (0, "DOT5-PHYS-MIB", "dot5PhysMgmtDeviceRingSpeedRing"),
)
if mibBuilder.loadTexts:
    dot5PhysMgmtDeviceRingSpeedEntry.setStatus("mandatory")


class _Dot5PhysMgmtDeviceRingSpeedRing_Type(Integer32):
    """Custom type dot5PhysMgmtDeviceRingSpeedRing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_Dot5PhysMgmtDeviceRingSpeedRing_Type.__name__ = "Integer32"
_Dot5PhysMgmtDeviceRingSpeedRing_Object = MibTableColumn
dot5PhysMgmtDeviceRingSpeedRing = _Dot5PhysMgmtDeviceRingSpeedRing_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 4, 1, 1, 1),
    _Dot5PhysMgmtDeviceRingSpeedRing_Type()
)
dot5PhysMgmtDeviceRingSpeedRing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtDeviceRingSpeedRing.setStatus("mandatory")


class _Dot5PhysMgmtDeviceRingSpeed_Type(Integer32):
    """Custom type dot5PhysMgmtDeviceRingSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              10,
              16,
              100)
        )
    )
    namedValues = NamedValues(
        *(("fourMegaBits", 4),
          ("hundredMegaBits", 100),
          ("sixteenMegaBits", 16),
          ("tenMegaBits", 10),
          ("unknown", 1))
    )


_Dot5PhysMgmtDeviceRingSpeed_Type.__name__ = "Integer32"
_Dot5PhysMgmtDeviceRingSpeed_Object = MibTableColumn
dot5PhysMgmtDeviceRingSpeed = _Dot5PhysMgmtDeviceRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 4, 1, 1, 2),
    _Dot5PhysMgmtDeviceRingSpeed_Type()
)
dot5PhysMgmtDeviceRingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot5PhysMgmtDeviceRingSpeed.setStatus("mandatory")
_Dot5PhysMgmtBoardAuxRingSpeedTable_Object = MibTable
dot5PhysMgmtBoardAuxRingSpeedTable = _Dot5PhysMgmtBoardAuxRingSpeedTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 4, 2)
)
if mibBuilder.loadTexts:
    dot5PhysMgmtBoardAuxRingSpeedTable.setStatus("mandatory")
_Dot5PhysMgmtBoardAuxRingSpeedEntry_Object = MibTableRow
dot5PhysMgmtBoardAuxRingSpeedEntry = _Dot5PhysMgmtBoardAuxRingSpeedEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 4, 2, 1)
)
dot5PhysMgmtBoardAuxRingSpeedEntry.setIndexNames(
    (0, "DOT5-PHYS-MIB", "dot5PhysMgmtBoardAuxRingSpeedBoardId"),
    (0, "DOT5-PHYS-MIB", "dot5PhysMgmtBoardAuxRingSpeedAuxRing"),
)
if mibBuilder.loadTexts:
    dot5PhysMgmtBoardAuxRingSpeedEntry.setStatus("mandatory")
_Dot5PhysMgmtBoardAuxRingSpeedBoardId_Type = Integer32
_Dot5PhysMgmtBoardAuxRingSpeedBoardId_Object = MibTableColumn
dot5PhysMgmtBoardAuxRingSpeedBoardId = _Dot5PhysMgmtBoardAuxRingSpeedBoardId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 4, 2, 1, 1),
    _Dot5PhysMgmtBoardAuxRingSpeedBoardId_Type()
)
dot5PhysMgmtBoardAuxRingSpeedBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtBoardAuxRingSpeedBoardId.setStatus("mandatory")


class _Dot5PhysMgmtBoardAuxRingSpeedAuxRing_Type(Integer32):
    """Custom type dot5PhysMgmtBoardAuxRingSpeedAuxRing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(201, 254),
    )


_Dot5PhysMgmtBoardAuxRingSpeedAuxRing_Type.__name__ = "Integer32"
_Dot5PhysMgmtBoardAuxRingSpeedAuxRing_Object = MibTableColumn
dot5PhysMgmtBoardAuxRingSpeedAuxRing = _Dot5PhysMgmtBoardAuxRingSpeedAuxRing_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 4, 2, 1, 2),
    _Dot5PhysMgmtBoardAuxRingSpeedAuxRing_Type()
)
dot5PhysMgmtBoardAuxRingSpeedAuxRing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5PhysMgmtBoardAuxRingSpeedAuxRing.setStatus("mandatory")


class _Dot5PhysMgmtBoardAuxRingSpeed_Type(Integer32):
    """Custom type dot5PhysMgmtBoardAuxRingSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              10,
              16,
              100)
        )
    )
    namedValues = NamedValues(
        *(("fourMegaBits", 4),
          ("hundredMegaBits", 100),
          ("sixteenMegaBits", 16),
          ("tenMegaBits", 10),
          ("unknown", 1))
    )


_Dot5PhysMgmtBoardAuxRingSpeed_Type.__name__ = "Integer32"
_Dot5PhysMgmtBoardAuxRingSpeed_Object = MibTableColumn
dot5PhysMgmtBoardAuxRingSpeed = _Dot5PhysMgmtBoardAuxRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6, 1, 4, 2, 1, 3),
    _Dot5PhysMgmtBoardAuxRingSpeed_Type()
)
dot5PhysMgmtBoardAuxRingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot5PhysMgmtBoardAuxRingSpeed.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOT5-PHYS-MIB",
    **{"dot5PhysMgmtRev1": dot5PhysMgmtRev1,
       "dot5PhysMgmtDevice": dot5PhysMgmtDevice,
       "dot5PhysMgmtDeviceRingCount": dot5PhysMgmtDeviceRingCount,
       "dot5PhysMgmtDevicePortCount": dot5PhysMgmtDevicePortCount,
       "dot5PhysMgmtDevicePortsEnable": dot5PhysMgmtDevicePortsEnable,
       "dot5PhysMgmtDevicePortsOn": dot5PhysMgmtDevicePortsOn,
       "dot5PhysMgmtDevicePortsOper": dot5PhysMgmtDevicePortsOper,
       "dot5PhysMgmtDeviceStnPortCount": dot5PhysMgmtDeviceStnPortCount,
       "dot5PhysMgmtDeviceStnPortsEnable": dot5PhysMgmtDeviceStnPortsEnable,
       "dot5PhysMgmtDeviceStnPortsOn": dot5PhysMgmtDeviceStnPortsOn,
       "dot5PhysMgmtDeviceRingPortCount": dot5PhysMgmtDeviceRingPortCount,
       "dot5PhysMgmtDeviceRingPortsEnable": dot5PhysMgmtDeviceRingPortsEnable,
       "dot5PhysMgmtDeviceRingPortsOn": dot5PhysMgmtDeviceRingPortsOn,
       "dot5PhysMgmtDevicePortAssociationChanges": dot5PhysMgmtDevicePortAssociationChanges,
       "dot5PhysMgmtBoard": dot5PhysMgmtBoard,
       "dot5PhysMgmtBoardTable": dot5PhysMgmtBoardTable,
       "dot5PhysMgmtBoardEntry": dot5PhysMgmtBoardEntry,
       "dot5PhysMgmtBoardId": dot5PhysMgmtBoardId,
       "dot5PhysMgmtBoardDomain": dot5PhysMgmtBoardDomain,
       "dot5PhysMgmtBoardName": dot5PhysMgmtBoardName,
       "dot5PhysMgmtBoardDesc": dot5PhysMgmtBoardDesc,
       "dot5PhysMgmtBoardDot5PortCount": dot5PhysMgmtBoardDot5PortCount,
       "dot5PhysMgmtBoardDot5PortsEnable": dot5PhysMgmtBoardDot5PortsEnable,
       "dot5PhysMgmtBoardDot5PortsOn": dot5PhysMgmtBoardDot5PortsOn,
       "dot5PhysMgmtBoardDot5PortsOper": dot5PhysMgmtBoardDot5PortsOper,
       "dot5PhysMgmtBoardDot5StnPortCount": dot5PhysMgmtBoardDot5StnPortCount,
       "dot5PhysMgmtBoardDot5StnPortsEnable": dot5PhysMgmtBoardDot5StnPortsEnable,
       "dot5PhysMgmtBoardDot5StnPortsOn": dot5PhysMgmtBoardDot5StnPortsOn,
       "dot5PhysMgmtBoardDot5RingPortCount": dot5PhysMgmtBoardDot5RingPortCount,
       "dot5PhysMgmtBoardDot5RingPortsEnable": dot5PhysMgmtBoardDot5RingPortsEnable,
       "dot5PhysMgmtBoardDot5RingPortsOn": dot5PhysMgmtBoardDot5RingPortsOn,
       "dot5PhysMgmtBoardMode": dot5PhysMgmtBoardMode,
       "dot5PhysMgmtBoardSpeed": dot5PhysMgmtBoardSpeed,
       "dot5PhysMgmtBoardSpeedFault": dot5PhysMgmtBoardSpeedFault,
       "dot5PhysMgmtBoardSpeedFaultLocation": dot5PhysMgmtBoardSpeedFaultLocation,
       "dot5PhysMgmtBoardPortAssociation": dot5PhysMgmtBoardPortAssociation,
       "dot5PhysMgmtBoardPortAssociationChanges": dot5PhysMgmtBoardPortAssociationChanges,
       "dot5PhysMgmtPort": dot5PhysMgmtPort,
       "dot5PhysMgmtPortCommon": dot5PhysMgmtPortCommon,
       "dot5PhysMgmtPortCommonTable": dot5PhysMgmtPortCommonTable,
       "dot5PhysMgmtPortCommonEntry": dot5PhysMgmtPortCommonEntry,
       "dot5PhysMgmtPortCommonPortId": dot5PhysMgmtPortCommonPortId,
       "dot5PhysMgmtPortCommonBoardId": dot5PhysMgmtPortCommonBoardId,
       "dot5PhysMgmtPortCommonPortName": dot5PhysMgmtPortCommonPortName,
       "dot5PhysMgmtPortCommonPortAdminState": dot5PhysMgmtPortCommonPortAdminState,
       "dot5PhysMgmtPortCommonPortOperState": dot5PhysMgmtPortCommonPortOperState,
       "dot5PhysMgmtPortCommonPortType": dot5PhysMgmtPortCommonPortType,
       "dot5PhysMgmtPortCommonSpeedFaultDetect": dot5PhysMgmtPortCommonSpeedFaultDetect,
       "dot5PhysMgmtPortCommonRingOutEnable": dot5PhysMgmtPortCommonRingOutEnable,
       "dot5PhysMgmtPortCommonPortAssociation": dot5PhysMgmtPortCommonPortAssociation,
       "dot5PhysMgmtPortCommonMauCompId": dot5PhysMgmtPortCommonMauCompId,
       "dot5PhysMgmtPortStn": dot5PhysMgmtPortStn,
       "dot5PhysMgmtPortStnTable": dot5PhysMgmtPortStnTable,
       "dot5PhysMgmtPortStnEntry": dot5PhysMgmtPortStnEntry,
       "dot5PhysMgmtPortStnPortId": dot5PhysMgmtPortStnPortId,
       "dot5PhysMgmtPortStnBoardId": dot5PhysMgmtPortStnBoardId,
       "dot5PhysMgmtPortStnPortLinkState": dot5PhysMgmtPortStnPortLinkState,
       "dot5PhysMgmtPortStnPortLinkStateTime": dot5PhysMgmtPortStnPortLinkStateTime,
       "dot5PhysMgmtPortStnInsertionTrapEnable": dot5PhysMgmtPortStnInsertionTrapEnable,
       "dot5PhysMgmtPortRing": dot5PhysMgmtPortRing,
       "dot5PhysMgmtPortRingTable": dot5PhysMgmtPortRingTable,
       "dot5PhysMgmtPortRingEntry": dot5PhysMgmtPortRingEntry,
       "dot5PhysMgmtPortRingPortId": dot5PhysMgmtPortRingPortId,
       "dot5PhysMgmtPortRingBoardId": dot5PhysMgmtPortRingBoardId,
       "dot5PhysMgmtPortRingPortClass": dot5PhysMgmtPortRingPortClass,
       "dot5PhysMgmtPortRingPortMediaSelect": dot5PhysMgmtPortRingPortMediaSelect,
       "dot5PhysMgmtPortRingFaultStatus": dot5PhysMgmtPortRingFaultStatus,
       "dot5PhysMgmtPortRingFaultStateTime": dot5PhysMgmtPortRingFaultStateTime,
       "dot5PhysMgmtPortRingPhantomCurrent": dot5PhysMgmtPortRingPhantomCurrent,
       "dot5PhysMgmtPortRingPortType": dot5PhysMgmtPortRingPortType,
       "dot5PhysMgmtPortSwitch": dot5PhysMgmtPortSwitch,
       "dot5PhysMgmtRingSpeedTables": dot5PhysMgmtRingSpeedTables,
       "dot5PhysMgmtDeviceRingSpeedTable": dot5PhysMgmtDeviceRingSpeedTable,
       "dot5PhysMgmtDeviceRingSpeedEntry": dot5PhysMgmtDeviceRingSpeedEntry,
       "dot5PhysMgmtDeviceRingSpeedRing": dot5PhysMgmtDeviceRingSpeedRing,
       "dot5PhysMgmtDeviceRingSpeed": dot5PhysMgmtDeviceRingSpeed,
       "dot5PhysMgmtBoardAuxRingSpeedTable": dot5PhysMgmtBoardAuxRingSpeedTable,
       "dot5PhysMgmtBoardAuxRingSpeedEntry": dot5PhysMgmtBoardAuxRingSpeedEntry,
       "dot5PhysMgmtBoardAuxRingSpeedBoardId": dot5PhysMgmtBoardAuxRingSpeedBoardId,
       "dot5PhysMgmtBoardAuxRingSpeedAuxRing": dot5PhysMgmtBoardAuxRingSpeedAuxRing,
       "dot5PhysMgmtBoardAuxRingSpeed": dot5PhysMgmtBoardAuxRingSpeed}
)
