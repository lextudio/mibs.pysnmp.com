# SNMP MIB module (IPAD-NAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPAD-NAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:43 2024
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

(ipad,) = mibBuilder.importSymbols(
    "IPADv2-MIB",
    "ipad")

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

ipadNat = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpadNatParms_ObjectIdentity = ObjectIdentity
ipadNatParms = _IpadNatParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 1)
)


class _IpadNatEnable_Type(Integer32):
    """Custom type ipadNatEnable based on Integer32"""
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
          ("other", 1))
    )


_IpadNatEnable_Type.__name__ = "Integer32"
_IpadNatEnable_Object = MibScalar
ipadNatEnable = _IpadNatEnable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 1, 1),
    _IpadNatEnable_Type()
)
ipadNatEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatEnable.setStatus("current")


class _IpadNatMode_Type(Integer32):
    """Custom type ipadNatMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("napt", 3),
          ("nat", 2),
          ("other", 1))
    )


_IpadNatMode_Type.__name__ = "Integer32"
_IpadNatMode_Object = MibScalar
ipadNatMode = _IpadNatMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 1, 2),
    _IpadNatMode_Type()
)
ipadNatMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatMode.setStatus("current")
_IpadNatGlobalAddress_Type = IpAddress
_IpadNatGlobalAddress_Object = MibScalar
ipadNatGlobalAddress = _IpadNatGlobalAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 1, 3),
    _IpadNatGlobalAddress_Type()
)
ipadNatGlobalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatGlobalAddress.setStatus("current")
_IpadNatGlobalMask_Type = IpAddress
_IpadNatGlobalMask_Object = MibScalar
ipadNatGlobalMask = _IpadNatGlobalMask_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 1, 4),
    _IpadNatGlobalMask_Type()
)
ipadNatGlobalMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatGlobalMask.setStatus("current")
_IpadNatICMPDefaultAddress_Type = IpAddress
_IpadNatICMPDefaultAddress_Object = MibScalar
ipadNatICMPDefaultAddress = _IpadNatICMPDefaultAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 1, 5),
    _IpadNatICMPDefaultAddress_Type()
)
ipadNatICMPDefaultAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatICMPDefaultAddress.setStatus("current")


class _IpadNatFilterNonLocalAddress_Type(Integer32):
    """Custom type ipadNatFilterNonLocalAddress based on Integer32"""
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
          ("other", 1))
    )


_IpadNatFilterNonLocalAddress_Type.__name__ = "Integer32"
_IpadNatFilterNonLocalAddress_Object = MibScalar
ipadNatFilterNonLocalAddress = _IpadNatFilterNonLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 1, 6),
    _IpadNatFilterNonLocalAddress_Type()
)
ipadNatFilterNonLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatFilterNonLocalAddress.setStatus("current")
_IpadNatIPEntryTimer_Type = Integer32
_IpadNatIPEntryTimer_Object = MibScalar
ipadNatIPEntryTimer = _IpadNatIPEntryTimer_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 1, 7),
    _IpadNatIPEntryTimer_Type()
)
ipadNatIPEntryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatIPEntryTimer.setStatus("current")
_IpadNatTCPConnectionTimer_Type = Integer32
_IpadNatTCPConnectionTimer_Object = MibScalar
ipadNatTCPConnectionTimer = _IpadNatTCPConnectionTimer_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 1, 8),
    _IpadNatTCPConnectionTimer_Type()
)
ipadNatTCPConnectionTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatTCPConnectionTimer.setStatus("current")
_IpadNatTCPClosingTimer_Type = Integer32
_IpadNatTCPClosingTimer_Object = MibScalar
ipadNatTCPClosingTimer = _IpadNatTCPClosingTimer_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 1, 9),
    _IpadNatTCPClosingTimer_Type()
)
ipadNatTCPClosingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatTCPClosingTimer.setStatus("current")
_IpadNatTCPDisconnectedTimer_Type = Integer32
_IpadNatTCPDisconnectedTimer_Object = MibScalar
ipadNatTCPDisconnectedTimer = _IpadNatTCPDisconnectedTimer_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 1, 10),
    _IpadNatTCPDisconnectedTimer_Type()
)
ipadNatTCPDisconnectedTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatTCPDisconnectedTimer.setStatus("current")
_IpadNatTCPSequenceDeltaTimer_Type = Integer32
_IpadNatTCPSequenceDeltaTimer_Object = MibScalar
ipadNatTCPSequenceDeltaTimer = _IpadNatTCPSequenceDeltaTimer_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 1, 11),
    _IpadNatTCPSequenceDeltaTimer_Type()
)
ipadNatTCPSequenceDeltaTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatTCPSequenceDeltaTimer.setStatus("current")
_IpadNatUDPTimer_Type = Integer32
_IpadNatUDPTimer_Object = MibScalar
ipadNatUDPTimer = _IpadNatUDPTimer_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 1, 12),
    _IpadNatUDPTimer_Type()
)
ipadNatUDPTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatUDPTimer.setStatus("current")
_IpadNatICMPTimer_Type = Integer32
_IpadNatICMPTimer_Object = MibScalar
ipadNatICMPTimer = _IpadNatICMPTimer_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 1, 13),
    _IpadNatICMPTimer_Type()
)
ipadNatICMPTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatICMPTimer.setStatus("current")
_IpadNatStaticTranslationParms_ObjectIdentity = ObjectIdentity
ipadNatStaticTranslationParms = _IpadNatStaticTranslationParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2)
)
_IpadNatStaticTranslationTable_Object = MibTable
ipadNatStaticTranslationTable = _IpadNatStaticTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 1)
)
if mibBuilder.loadTexts:
    ipadNatStaticTranslationTable.setStatus("current")
_IpadNatStaticTranslationTableEntry_Object = MibTableRow
ipadNatStaticTranslationTableEntry = _IpadNatStaticTranslationTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 1, 1)
)
ipadNatStaticTranslationTableEntry.setIndexNames(
    (0, "IPAD-NAT-MIB", "ipadNatStaticTranslationEntryIndex"),
)
if mibBuilder.loadTexts:
    ipadNatStaticTranslationTableEntry.setStatus("current")
_IpadNatStaticTranslationEntryIndex_Type = Integer32
_IpadNatStaticTranslationEntryIndex_Object = MibTableColumn
ipadNatStaticTranslationEntryIndex = _IpadNatStaticTranslationEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 1, 1, 1),
    _IpadNatStaticTranslationEntryIndex_Type()
)
ipadNatStaticTranslationEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadNatStaticTranslationEntryIndex.setStatus("current")


class _IpadNatStaticTranslationEnable_Type(Integer32):
    """Custom type ipadNatStaticTranslationEnable based on Integer32"""
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
          ("other", 1))
    )


_IpadNatStaticTranslationEnable_Type.__name__ = "Integer32"
_IpadNatStaticTranslationEnable_Object = MibTableColumn
ipadNatStaticTranslationEnable = _IpadNatStaticTranslationEnable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 1, 1, 2),
    _IpadNatStaticTranslationEnable_Type()
)
ipadNatStaticTranslationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatStaticTranslationEnable.setStatus("current")
_IpadNatStaticTranslationLocalAddress_Type = IpAddress
_IpadNatStaticTranslationLocalAddress_Object = MibTableColumn
ipadNatStaticTranslationLocalAddress = _IpadNatStaticTranslationLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 1, 1, 3),
    _IpadNatStaticTranslationLocalAddress_Type()
)
ipadNatStaticTranslationLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatStaticTranslationLocalAddress.setStatus("current")
_IpadNatStaticTranslationGlobalAddress_Type = IpAddress
_IpadNatStaticTranslationGlobalAddress_Object = MibTableColumn
ipadNatStaticTranslationGlobalAddress = _IpadNatStaticTranslationGlobalAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 1, 1, 4),
    _IpadNatStaticTranslationGlobalAddress_Type()
)
ipadNatStaticTranslationGlobalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatStaticTranslationGlobalAddress.setStatus("current")
_IpadNatStaticTCPTranslationTable_Object = MibTable
ipadNatStaticTCPTranslationTable = _IpadNatStaticTCPTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 2)
)
if mibBuilder.loadTexts:
    ipadNatStaticTCPTranslationTable.setStatus("current")
_IpadNatStaticTCPTranslationTableEntry_Object = MibTableRow
ipadNatStaticTCPTranslationTableEntry = _IpadNatStaticTCPTranslationTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 2, 1)
)
ipadNatStaticTCPTranslationTableEntry.setIndexNames(
    (0, "IPAD-NAT-MIB", "ipadNatStaticTCPTranslationEntryIndex"),
)
if mibBuilder.loadTexts:
    ipadNatStaticTCPTranslationTableEntry.setStatus("current")
_IpadNatStaticTCPTranslationEntryIndex_Type = Integer32
_IpadNatStaticTCPTranslationEntryIndex_Object = MibTableColumn
ipadNatStaticTCPTranslationEntryIndex = _IpadNatStaticTCPTranslationEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 2, 1, 1),
    _IpadNatStaticTCPTranslationEntryIndex_Type()
)
ipadNatStaticTCPTranslationEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadNatStaticTCPTranslationEntryIndex.setStatus("current")
_IpadNatStaticTCPTranslationGlobalPort_Type = Integer32
_IpadNatStaticTCPTranslationGlobalPort_Object = MibTableColumn
ipadNatStaticTCPTranslationGlobalPort = _IpadNatStaticTCPTranslationGlobalPort_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 2, 1, 2),
    _IpadNatStaticTCPTranslationGlobalPort_Type()
)
ipadNatStaticTCPTranslationGlobalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatStaticTCPTranslationGlobalPort.setStatus("current")
_IpadNatStaticTCPTranslationServerPort_Type = Integer32
_IpadNatStaticTCPTranslationServerPort_Object = MibTableColumn
ipadNatStaticTCPTranslationServerPort = _IpadNatStaticTCPTranslationServerPort_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 2, 1, 3),
    _IpadNatStaticTCPTranslationServerPort_Type()
)
ipadNatStaticTCPTranslationServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatStaticTCPTranslationServerPort.setStatus("current")
_IpadNatStaticTCPTranslationServerAddress_Type = IpAddress
_IpadNatStaticTCPTranslationServerAddress_Object = MibTableColumn
ipadNatStaticTCPTranslationServerAddress = _IpadNatStaticTCPTranslationServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 2, 1, 4),
    _IpadNatStaticTCPTranslationServerAddress_Type()
)
ipadNatStaticTCPTranslationServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatStaticTCPTranslationServerAddress.setStatus("current")
_IpadNatStaticUDPTranslationTable_Object = MibTable
ipadNatStaticUDPTranslationTable = _IpadNatStaticUDPTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 3)
)
if mibBuilder.loadTexts:
    ipadNatStaticUDPTranslationTable.setStatus("current")
_IpadNatStaticUDPTranslationTableEntry_Object = MibTableRow
ipadNatStaticUDPTranslationTableEntry = _IpadNatStaticUDPTranslationTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 3, 1)
)
ipadNatStaticUDPTranslationTableEntry.setIndexNames(
    (0, "IPAD-NAT-MIB", "ipadNatStaticUDPTranslationEntryIndex"),
)
if mibBuilder.loadTexts:
    ipadNatStaticUDPTranslationTableEntry.setStatus("current")
_IpadNatStaticUDPTranslationEntryIndex_Type = Integer32
_IpadNatStaticUDPTranslationEntryIndex_Object = MibTableColumn
ipadNatStaticUDPTranslationEntryIndex = _IpadNatStaticUDPTranslationEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 3, 1, 1),
    _IpadNatStaticUDPTranslationEntryIndex_Type()
)
ipadNatStaticUDPTranslationEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadNatStaticUDPTranslationEntryIndex.setStatus("current")
_IpadNatStaticUDPTranslationGlobalPort_Type = Integer32
_IpadNatStaticUDPTranslationGlobalPort_Object = MibTableColumn
ipadNatStaticUDPTranslationGlobalPort = _IpadNatStaticUDPTranslationGlobalPort_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 3, 1, 2),
    _IpadNatStaticUDPTranslationGlobalPort_Type()
)
ipadNatStaticUDPTranslationGlobalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatStaticUDPTranslationGlobalPort.setStatus("current")
_IpadNatStaticUDPTranslationServerPort_Type = Integer32
_IpadNatStaticUDPTranslationServerPort_Object = MibTableColumn
ipadNatStaticUDPTranslationServerPort = _IpadNatStaticUDPTranslationServerPort_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 3, 1, 3),
    _IpadNatStaticUDPTranslationServerPort_Type()
)
ipadNatStaticUDPTranslationServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatStaticUDPTranslationServerPort.setStatus("current")
_IpadNatStaticUDPTranslationServerAddress_Type = IpAddress
_IpadNatStaticUDPTranslationServerAddress_Object = MibTableColumn
ipadNatStaticUDPTranslationServerAddress = _IpadNatStaticUDPTranslationServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 3, 1, 4),
    _IpadNatStaticUDPTranslationServerAddress_Type()
)
ipadNatStaticUDPTranslationServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatStaticUDPTranslationServerAddress.setStatus("current")


class _IpadNatStaticTranslationAdd_Type(Integer32):
    """Custom type ipadNatStaticTranslationAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addnew", 2),
          ("other", 1))
    )


_IpadNatStaticTranslationAdd_Type.__name__ = "Integer32"
_IpadNatStaticTranslationAdd_Object = MibScalar
ipadNatStaticTranslationAdd = _IpadNatStaticTranslationAdd_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 4),
    _IpadNatStaticTranslationAdd_Type()
)
ipadNatStaticTranslationAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatStaticTranslationAdd.setStatus("current")
_IpadNatStaticTranslationDelete_Type = Integer32
_IpadNatStaticTranslationDelete_Object = MibScalar
ipadNatStaticTranslationDelete = _IpadNatStaticTranslationDelete_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 5),
    _IpadNatStaticTranslationDelete_Type()
)
ipadNatStaticTranslationDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatStaticTranslationDelete.setStatus("current")


class _IpadNatStaticTCPTranslationAdd_Type(Integer32):
    """Custom type ipadNatStaticTCPTranslationAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addnew", 2),
          ("other", 1))
    )


_IpadNatStaticTCPTranslationAdd_Type.__name__ = "Integer32"
_IpadNatStaticTCPTranslationAdd_Object = MibScalar
ipadNatStaticTCPTranslationAdd = _IpadNatStaticTCPTranslationAdd_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 6),
    _IpadNatStaticTCPTranslationAdd_Type()
)
ipadNatStaticTCPTranslationAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatStaticTCPTranslationAdd.setStatus("current")
_IpadNatStaticTCPTranslationDelete_Type = Integer32
_IpadNatStaticTCPTranslationDelete_Object = MibScalar
ipadNatStaticTCPTranslationDelete = _IpadNatStaticTCPTranslationDelete_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 7),
    _IpadNatStaticTCPTranslationDelete_Type()
)
ipadNatStaticTCPTranslationDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatStaticTCPTranslationDelete.setStatus("current")


class _IpadNatStaticUDPTranslationAdd_Type(Integer32):
    """Custom type ipadNatStaticUDPTranslationAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addnew", 2),
          ("other", 1))
    )


_IpadNatStaticUDPTranslationAdd_Type.__name__ = "Integer32"
_IpadNatStaticUDPTranslationAdd_Object = MibScalar
ipadNatStaticUDPTranslationAdd = _IpadNatStaticUDPTranslationAdd_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 8),
    _IpadNatStaticUDPTranslationAdd_Type()
)
ipadNatStaticUDPTranslationAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatStaticUDPTranslationAdd.setStatus("current")
_IpadNatStaticUDPTranslationDelete_Type = Integer32
_IpadNatStaticUDPTranslationDelete_Object = MibScalar
ipadNatStaticUDPTranslationDelete = _IpadNatStaticUDPTranslationDelete_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 9),
    _IpadNatStaticUDPTranslationDelete_Type()
)
ipadNatStaticUDPTranslationDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatStaticUDPTranslationDelete.setStatus("current")
_IpadNatPortParms_ObjectIdentity = ObjectIdentity
ipadNatPortParms = _IpadNatPortParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3)
)
_IpadNatPortConfigTable_Object = MibTable
ipadNatPortConfigTable = _IpadNatPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 1)
)
if mibBuilder.loadTexts:
    ipadNatPortConfigTable.setStatus("current")
_IpadNatPortConfigTableEntry_Object = MibTableRow
ipadNatPortConfigTableEntry = _IpadNatPortConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 1, 1)
)
ipadNatPortConfigTableEntry.setIndexNames(
    (0, "IPAD-NAT-MIB", "ipadNatPortConfigIndex"),
)
if mibBuilder.loadTexts:
    ipadNatPortConfigTableEntry.setStatus("current")
_IpadNatPortConfigIndex_Type = Integer32
_IpadNatPortConfigIndex_Object = MibTableColumn
ipadNatPortConfigIndex = _IpadNatPortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 1, 1, 1),
    _IpadNatPortConfigIndex_Type()
)
ipadNatPortConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadNatPortConfigIndex.setStatus("current")


class _IpadNatPortConfigEnable_Type(Integer32):
    """Custom type ipadNatPortConfigEnable based on Integer32"""
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
          ("other", 1))
    )


_IpadNatPortConfigEnable_Type.__name__ = "Integer32"
_IpadNatPortConfigEnable_Object = MibTableColumn
ipadNatPortConfigEnable = _IpadNatPortConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 1, 1, 2),
    _IpadNatPortConfigEnable_Type()
)
ipadNatPortConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatPortConfigEnable.setStatus("current")


class _IpadNatPortConfigDefaultTranslation_Type(Integer32):
    """Custom type ipadNatPortConfigDefaultTranslation based on Integer32"""
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
          ("other", 1))
    )


_IpadNatPortConfigDefaultTranslation_Type.__name__ = "Integer32"
_IpadNatPortConfigDefaultTranslation_Object = MibTableColumn
ipadNatPortConfigDefaultTranslation = _IpadNatPortConfigDefaultTranslation_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 1, 1, 3),
    _IpadNatPortConfigDefaultTranslation_Type()
)
ipadNatPortConfigDefaultTranslation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatPortConfigDefaultTranslation.setStatus("current")


class _IpadNatPortConfigType_Type(Integer32):
    """Custom type ipadNatPortConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("global", 2),
          ("local", 3),
          ("other", 1))
    )


_IpadNatPortConfigType_Type.__name__ = "Integer32"
_IpadNatPortConfigType_Object = MibTableColumn
ipadNatPortConfigType = _IpadNatPortConfigType_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 1, 1, 4),
    _IpadNatPortConfigType_Type()
)
ipadNatPortConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatPortConfigType.setStatus("current")
_IpadNatPortConfigIpAddress_Type = IpAddress
_IpadNatPortConfigIpAddress_Object = MibTableColumn
ipadNatPortConfigIpAddress = _IpadNatPortConfigIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 1, 1, 5),
    _IpadNatPortConfigIpAddress_Type()
)
ipadNatPortConfigIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatPortConfigIpAddress.setStatus("current")
_IpadNatPortConfigMask_Type = IpAddress
_IpadNatPortConfigMask_Object = MibTableColumn
ipadNatPortConfigMask = _IpadNatPortConfigMask_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 1, 1, 6),
    _IpadNatPortConfigMask_Type()
)
ipadNatPortConfigMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatPortConfigMask.setStatus("current")


class _IpadNatPortConfigEndpoint_Type(DisplayString):
    """Custom type ipadNatPortConfigEndpoint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_IpadNatPortConfigEndpoint_Type.__name__ = "DisplayString"
_IpadNatPortConfigEndpoint_Object = MibTableColumn
ipadNatPortConfigEndpoint = _IpadNatPortConfigEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 1, 1, 7),
    _IpadNatPortConfigEndpoint_Type()
)
ipadNatPortConfigEndpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatPortConfigEndpoint.setStatus("current")


class _IpadNatPortConfigClearStats_Type(Integer32):
    """Custom type ipadNatPortConfigClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("other", 1))
    )


_IpadNatPortConfigClearStats_Type.__name__ = "Integer32"
_IpadNatPortConfigClearStats_Object = MibTableColumn
ipadNatPortConfigClearStats = _IpadNatPortConfigClearStats_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 1, 1, 8),
    _IpadNatPortConfigClearStats_Type()
)
ipadNatPortConfigClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatPortConfigClearStats.setStatus("current")


class _IpadNatPortAdd_Type(Integer32):
    """Custom type ipadNatPortAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addnew", 2),
          ("other", 1))
    )


_IpadNatPortAdd_Type.__name__ = "Integer32"
_IpadNatPortAdd_Object = MibScalar
ipadNatPortAdd = _IpadNatPortAdd_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 2),
    _IpadNatPortAdd_Type()
)
ipadNatPortAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatPortAdd.setStatus("current")
_IpadNatPortDelete_Type = Integer32
_IpadNatPortDelete_Object = MibScalar
ipadNatPortDelete = _IpadNatPortDelete_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 3),
    _IpadNatPortDelete_Type()
)
ipadNatPortDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadNatPortDelete.setStatus("current")
_IpadNatPortStatusTable_Object = MibTable
ipadNatPortStatusTable = _IpadNatPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 4)
)
if mibBuilder.loadTexts:
    ipadNatPortStatusTable.setStatus("current")
_IpadNatPortStatusTableEntry_Object = MibTableRow
ipadNatPortStatusTableEntry = _IpadNatPortStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 4, 1)
)
ipadNatPortStatusTableEntry.setIndexNames(
    (0, "IPAD-NAT-MIB", "ipadNatPortStatusIndex"),
    (0, "IPAD-NAT-MIB", "ipadNatPortStatusLocalIpAddress"),
)
if mibBuilder.loadTexts:
    ipadNatPortStatusTableEntry.setStatus("current")
_IpadNatPortStatusIndex_Type = Integer32
_IpadNatPortStatusIndex_Object = MibTableColumn
ipadNatPortStatusIndex = _IpadNatPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 4, 1, 1),
    _IpadNatPortStatusIndex_Type()
)
ipadNatPortStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadNatPortStatusIndex.setStatus("current")
_IpadNatPortStatusLocalIpAddress_Type = IpAddress
_IpadNatPortStatusLocalIpAddress_Object = MibTableColumn
ipadNatPortStatusLocalIpAddress = _IpadNatPortStatusLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 4, 1, 2),
    _IpadNatPortStatusLocalIpAddress_Type()
)
ipadNatPortStatusLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadNatPortStatusLocalIpAddress.setStatus("current")
_IpadNatPortStatusNatIpAddress_Type = IpAddress
_IpadNatPortStatusNatIpAddress_Object = MibTableColumn
ipadNatPortStatusNatIpAddress = _IpadNatPortStatusNatIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 4, 1, 3),
    _IpadNatPortStatusNatIpAddress_Type()
)
ipadNatPortStatusNatIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadNatPortStatusNatIpAddress.setStatus("current")
_IpadNatPortStatusTxPackets_Type = Integer32
_IpadNatPortStatusTxPackets_Object = MibTableColumn
ipadNatPortStatusTxPackets = _IpadNatPortStatusTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 4, 1, 4),
    _IpadNatPortStatusTxPackets_Type()
)
ipadNatPortStatusTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadNatPortStatusTxPackets.setStatus("current")
_IpadNatPortStatusRxPackets_Type = Integer32
_IpadNatPortStatusRxPackets_Object = MibTableColumn
ipadNatPortStatusRxPackets = _IpadNatPortStatusRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 4, 1, 5),
    _IpadNatPortStatusRxPackets_Type()
)
ipadNatPortStatusRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadNatPortStatusRxPackets.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPAD-NAT-MIB",
    **{"ipadNat": ipadNat,
       "ipadNatParms": ipadNatParms,
       "ipadNatEnable": ipadNatEnable,
       "ipadNatMode": ipadNatMode,
       "ipadNatGlobalAddress": ipadNatGlobalAddress,
       "ipadNatGlobalMask": ipadNatGlobalMask,
       "ipadNatICMPDefaultAddress": ipadNatICMPDefaultAddress,
       "ipadNatFilterNonLocalAddress": ipadNatFilterNonLocalAddress,
       "ipadNatIPEntryTimer": ipadNatIPEntryTimer,
       "ipadNatTCPConnectionTimer": ipadNatTCPConnectionTimer,
       "ipadNatTCPClosingTimer": ipadNatTCPClosingTimer,
       "ipadNatTCPDisconnectedTimer": ipadNatTCPDisconnectedTimer,
       "ipadNatTCPSequenceDeltaTimer": ipadNatTCPSequenceDeltaTimer,
       "ipadNatUDPTimer": ipadNatUDPTimer,
       "ipadNatICMPTimer": ipadNatICMPTimer,
       "ipadNatStaticTranslationParms": ipadNatStaticTranslationParms,
       "ipadNatStaticTranslationTable": ipadNatStaticTranslationTable,
       "ipadNatStaticTranslationTableEntry": ipadNatStaticTranslationTableEntry,
       "ipadNatStaticTranslationEntryIndex": ipadNatStaticTranslationEntryIndex,
       "ipadNatStaticTranslationEnable": ipadNatStaticTranslationEnable,
       "ipadNatStaticTranslationLocalAddress": ipadNatStaticTranslationLocalAddress,
       "ipadNatStaticTranslationGlobalAddress": ipadNatStaticTranslationGlobalAddress,
       "ipadNatStaticTCPTranslationTable": ipadNatStaticTCPTranslationTable,
       "ipadNatStaticTCPTranslationTableEntry": ipadNatStaticTCPTranslationTableEntry,
       "ipadNatStaticTCPTranslationEntryIndex": ipadNatStaticTCPTranslationEntryIndex,
       "ipadNatStaticTCPTranslationGlobalPort": ipadNatStaticTCPTranslationGlobalPort,
       "ipadNatStaticTCPTranslationServerPort": ipadNatStaticTCPTranslationServerPort,
       "ipadNatStaticTCPTranslationServerAddress": ipadNatStaticTCPTranslationServerAddress,
       "ipadNatStaticUDPTranslationTable": ipadNatStaticUDPTranslationTable,
       "ipadNatStaticUDPTranslationTableEntry": ipadNatStaticUDPTranslationTableEntry,
       "ipadNatStaticUDPTranslationEntryIndex": ipadNatStaticUDPTranslationEntryIndex,
       "ipadNatStaticUDPTranslationGlobalPort": ipadNatStaticUDPTranslationGlobalPort,
       "ipadNatStaticUDPTranslationServerPort": ipadNatStaticUDPTranslationServerPort,
       "ipadNatStaticUDPTranslationServerAddress": ipadNatStaticUDPTranslationServerAddress,
       "ipadNatStaticTranslationAdd": ipadNatStaticTranslationAdd,
       "ipadNatStaticTranslationDelete": ipadNatStaticTranslationDelete,
       "ipadNatStaticTCPTranslationAdd": ipadNatStaticTCPTranslationAdd,
       "ipadNatStaticTCPTranslationDelete": ipadNatStaticTCPTranslationDelete,
       "ipadNatStaticUDPTranslationAdd": ipadNatStaticUDPTranslationAdd,
       "ipadNatStaticUDPTranslationDelete": ipadNatStaticUDPTranslationDelete,
       "ipadNatPortParms": ipadNatPortParms,
       "ipadNatPortConfigTable": ipadNatPortConfigTable,
       "ipadNatPortConfigTableEntry": ipadNatPortConfigTableEntry,
       "ipadNatPortConfigIndex": ipadNatPortConfigIndex,
       "ipadNatPortConfigEnable": ipadNatPortConfigEnable,
       "ipadNatPortConfigDefaultTranslation": ipadNatPortConfigDefaultTranslation,
       "ipadNatPortConfigType": ipadNatPortConfigType,
       "ipadNatPortConfigIpAddress": ipadNatPortConfigIpAddress,
       "ipadNatPortConfigMask": ipadNatPortConfigMask,
       "ipadNatPortConfigEndpoint": ipadNatPortConfigEndpoint,
       "ipadNatPortConfigClearStats": ipadNatPortConfigClearStats,
       "ipadNatPortAdd": ipadNatPortAdd,
       "ipadNatPortDelete": ipadNatPortDelete,
       "ipadNatPortStatusTable": ipadNatPortStatusTable,
       "ipadNatPortStatusTableEntry": ipadNatPortStatusTableEntry,
       "ipadNatPortStatusIndex": ipadNatPortStatusIndex,
       "ipadNatPortStatusLocalIpAddress": ipadNatPortStatusLocalIpAddress,
       "ipadNatPortStatusNatIpAddress": ipadNatPortStatusNatIpAddress,
       "ipadNatPortStatusTxPackets": ipadNatPortStatusTxPackets,
       "ipadNatPortStatusRxPackets": ipadNatPortStatusRxPackets}
)
