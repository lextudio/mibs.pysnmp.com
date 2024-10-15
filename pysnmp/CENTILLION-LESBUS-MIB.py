# SNMP MIB module (CENTILLION-LESBUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CENTILLION-LESBUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:10 2024
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

(EnableIndicator,
 atmLane) = mibBuilder.importSymbols(
    "CENTILLION-ROOT-MIB",
    "EnableIndicator",
    "atmLane")

(AtmLaneAddress,
 lecIndex) = mibBuilder.importSymbols(
    "LAN-EMULATION-CLIENT-MIB",
    "AtmLaneAddress",
    "lecIndex")

(lecsConfIndex,) = mibBuilder.importSymbols(
    "LAN-EMULATION-ELAN-MIB",
    "lecsConfIndex")

(LesLocalIndex,) = mibBuilder.importSymbols(
    "LAN-EMULATION-LES-MIB",
    "LesLocalIndex")

(TimeIntervalSec,) = mibBuilder.importSymbols(
    "S5-TCS-MIB",
    "TimeIntervalSec")

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

_CnLesBusExtnGroup_ObjectIdentity = ObjectIdentity
cnLesBusExtnGroup = _CnLesBusExtnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 1)
)
_CnLesBusTable_Object = MibTable
cnLesBusTable = _CnLesBusTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cnLesBusTable.setStatus("mandatory")
_CnLesBusEntry_Object = MibTableRow
cnLesBusEntry = _CnLesBusEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 1, 1, 1)
)
cnLesBusEntry.setIndexNames(
    (0, "CENTILLION-LESBUS-MIB", "cnLesBusConfIndex"),
)
if mibBuilder.loadTexts:
    cnLesBusEntry.setStatus("mandatory")
_CnLesBusConfIndex_Type = LesLocalIndex
_CnLesBusConfIndex_Object = MibTableColumn
cnLesBusConfIndex = _CnLesBusConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 1, 1, 1, 1),
    _CnLesBusConfIndex_Type()
)
cnLesBusConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnLesBusConfIndex.setStatus("mandatory")


class _CnLesBusSmartLes_Type(Integer32):
    """Custom type cnLesBusSmartLes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CnLesBusSmartLes_Type.__name__ = "Integer32"
_CnLesBusSmartLes_Object = MibTableColumn
cnLesBusSmartLes = _CnLesBusSmartLes_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 1, 1, 1, 2),
    _CnLesBusSmartLes_Type()
)
cnLesBusSmartLes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLesBusSmartLes.setStatus("mandatory")
_CnLesBusServerId_Type = Integer32
_CnLesBusServerId_Object = MibTableColumn
cnLesBusServerId = _CnLesBusServerId_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 1, 1, 1, 3),
    _CnLesBusServerId_Type()
)
cnLesBusServerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLesBusServerId.setStatus("mandatory")
_CnLesBusBusAddrSpec_Type = AtmLaneAddress
_CnLesBusBusAddrSpec_Object = MibTableColumn
cnLesBusBusAddrSpec = _CnLesBusBusAddrSpec_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 1, 1, 1, 4),
    _CnLesBusBusAddrSpec_Type()
)
cnLesBusBusAddrSpec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLesBusBusAddrSpec.setStatus("mandatory")
_CnLesBusBusAddrActual_Type = AtmLaneAddress
_CnLesBusBusAddrActual_Object = MibTableColumn
cnLesBusBusAddrActual = _CnLesBusBusAddrActual_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 1, 1, 1, 5),
    _CnLesBusBusAddrActual_Type()
)
cnLesBusBusAddrActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnLesBusBusAddrActual.setStatus("mandatory")
_CnLesBusPeerTable_Object = MibTable
cnLesBusPeerTable = _CnLesBusPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cnLesBusPeerTable.setStatus("mandatory")
_CnLesBusPeerEntry_Object = MibTableRow
cnLesBusPeerEntry = _CnLesBusPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 1, 2, 1)
)
cnLesBusPeerEntry.setIndexNames(
    (0, "CENTILLION-LESBUS-MIB", "cnLesBusIndex"),
    (0, "CENTILLION-LESBUS-MIB", "cnLesBusPeerIndex"),
)
if mibBuilder.loadTexts:
    cnLesBusPeerEntry.setStatus("mandatory")
_CnLesBusIndex_Type = LesLocalIndex
_CnLesBusIndex_Object = MibTableColumn
cnLesBusIndex = _CnLesBusIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 1, 2, 1, 1),
    _CnLesBusIndex_Type()
)
cnLesBusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnLesBusIndex.setStatus("mandatory")
_CnLesBusPeerIndex_Type = Integer32
_CnLesBusPeerIndex_Object = MibTableColumn
cnLesBusPeerIndex = _CnLesBusPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 1, 2, 1, 2),
    _CnLesBusPeerIndex_Type()
)
cnLesBusPeerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnLesBusPeerIndex.setStatus("mandatory")
_CnLesBusPeerLesAddr_Type = AtmLaneAddress
_CnLesBusPeerLesAddr_Object = MibTableColumn
cnLesBusPeerLesAddr = _CnLesBusPeerLesAddr_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 1, 2, 1, 3),
    _CnLesBusPeerLesAddr_Type()
)
cnLesBusPeerLesAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLesBusPeerLesAddr.setStatus("mandatory")
_CnLesBusPeerBusAddr_Type = AtmLaneAddress
_CnLesBusPeerBusAddr_Object = MibTableColumn
cnLesBusPeerBusAddr = _CnLesBusPeerBusAddr_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 1, 2, 1, 4),
    _CnLesBusPeerBusAddr_Type()
)
cnLesBusPeerBusAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLesBusPeerBusAddr.setStatus("mandatory")


class _CnLesBusPeerStatus_Type(Integer32):
    """Custom type cnLesBusPeerStatus based on Integer32"""
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
        *(("active", 3),
          ("create", 1),
          ("delete", 2),
          ("inactive", 4))
    )


_CnLesBusPeerStatus_Type.__name__ = "Integer32"
_CnLesBusPeerStatus_Object = MibTableColumn
cnLesBusPeerStatus = _CnLesBusPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 1, 2, 1, 5),
    _CnLesBusPeerStatus_Type()
)
cnLesBusPeerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLesBusPeerStatus.setStatus("mandatory")
_CnLesBusPortTable_Object = MibTable
cnLesBusPortTable = _CnLesBusPortTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cnLesBusPortTable.setStatus("mandatory")
_CnLesBusPortEntry_Object = MibTableRow
cnLesBusPortEntry = _CnLesBusPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 1, 3, 1)
)
cnLesBusPortEntry.setIndexNames(
    (0, "CENTILLION-LESBUS-MIB", "cnLesBusPortElanIndex"),
    (0, "CENTILLION-LESBUS-MIB", "cnLesBusPortIndex"),
)
if mibBuilder.loadTexts:
    cnLesBusPortEntry.setStatus("mandatory")
_CnLesBusPortElanIndex_Type = Integer32
_CnLesBusPortElanIndex_Object = MibTableColumn
cnLesBusPortElanIndex = _CnLesBusPortElanIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 1, 3, 1, 1),
    _CnLesBusPortElanIndex_Type()
)
cnLesBusPortElanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnLesBusPortElanIndex.setStatus("mandatory")
_CnLesBusPortIndex_Type = Integer32
_CnLesBusPortIndex_Object = MibTableColumn
cnLesBusPortIndex = _CnLesBusPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 1, 3, 1, 2),
    _CnLesBusPortIndex_Type()
)
cnLesBusPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnLesBusPortIndex.setStatus("mandatory")
_CnLesBusCardId_Type = Integer32
_CnLesBusCardId_Object = MibTableColumn
cnLesBusCardId = _CnLesBusCardId_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 1, 3, 1, 3),
    _CnLesBusCardId_Type()
)
cnLesBusCardId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLesBusCardId.setStatus("mandatory")
_CnLesBusPortId_Type = Integer32
_CnLesBusPortId_Object = MibTableColumn
cnLesBusPortId = _CnLesBusPortId_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 1, 3, 1, 4),
    _CnLesBusPortId_Type()
)
cnLesBusPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLesBusPortId.setStatus("mandatory")


class _CnLesBusPortStatus_Type(Integer32):
    """Custom type cnLesBusPortStatus based on Integer32"""
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
        *(("active", 3),
          ("create", 1),
          ("delete", 2),
          ("inactive", 4))
    )


_CnLesBusPortStatus_Type.__name__ = "Integer32"
_CnLesBusPortStatus_Object = MibTableColumn
cnLesBusPortStatus = _CnLesBusPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 1, 3, 1, 5),
    _CnLesBusPortStatus_Type()
)
cnLesBusPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLesBusPortStatus.setStatus("mandatory")
_CnLecExtnGroup_ObjectIdentity = ObjectIdentity
cnLecExtnGroup = _CnLecExtnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 2)
)
_CnLecServerTable_Object = MibTable
cnLecServerTable = _CnLecServerTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cnLecServerTable.setStatus("mandatory")
_CnLecServerEntry_Object = MibTableRow
cnLecServerEntry = _CnLecServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 2, 1, 1)
)
cnLecServerEntry.setIndexNames(
    (0, "LAN-EMULATION-CLIENT-MIB", "lecIndex"),
    (0, "CENTILLION-LESBUS-MIB", "cnLecServerIndex"),
)
if mibBuilder.loadTexts:
    cnLecServerEntry.setStatus("mandatory")
_CnLecServerIndex_Type = Integer32
_CnLecServerIndex_Object = MibTableColumn
cnLecServerIndex = _CnLecServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 2, 1, 1, 1),
    _CnLecServerIndex_Type()
)
cnLecServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnLecServerIndex.setStatus("mandatory")


class _CnLecServerType_Type(Integer32):
    """Custom type cnLecServerType based on Integer32"""
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
        *(("directLecs", 3),
          ("directLes", 4),
          ("lecsAtmForum", 1),
          ("lecsFromIlmi", 2),
          ("lecsFromPvc", 5))
    )


_CnLecServerType_Type.__name__ = "Integer32"
_CnLecServerType_Object = MibTableColumn
cnLecServerType = _CnLecServerType_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 2, 1, 1, 2),
    _CnLecServerType_Type()
)
cnLecServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecServerType.setStatus("mandatory")
_CnLecServerAddress_Type = AtmLaneAddress
_CnLecServerAddress_Object = MibTableColumn
cnLecServerAddress = _CnLecServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 2, 1, 1, 3),
    _CnLecServerAddress_Type()
)
cnLecServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecServerAddress.setStatus("mandatory")


class _CnLecServerStatus_Type(Integer32):
    """Custom type cnLecServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("create", 1),
          ("delete", 2))
    )


_CnLecServerStatus_Type.__name__ = "Integer32"
_CnLecServerStatus_Object = MibTableColumn
cnLecServerStatus = _CnLecServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 2, 1, 1, 4),
    _CnLecServerStatus_Type()
)
cnLecServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecServerStatus.setStatus("mandatory")
_CnLecPortTable_Object = MibTable
cnLecPortTable = _CnLecPortTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 2, 2)
)
if mibBuilder.loadTexts:
    cnLecPortTable.setStatus("mandatory")
_CnLecPortEntry_Object = MibTableRow
cnLecPortEntry = _CnLecPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 2, 2, 1)
)
cnLecPortEntry.setIndexNames(
    (0, "CENTILLION-LESBUS-MIB", "cnLecPortlecIndex"),
    (0, "CENTILLION-LESBUS-MIB", "cnLecPortIndex"),
)
if mibBuilder.loadTexts:
    cnLecPortEntry.setStatus("mandatory")
_CnLecPortlecIndex_Type = Integer32
_CnLecPortlecIndex_Object = MibTableColumn
cnLecPortlecIndex = _CnLecPortlecIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 2, 2, 1, 1),
    _CnLecPortlecIndex_Type()
)
cnLecPortlecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnLecPortlecIndex.setStatus("mandatory")
_CnLecPortIndex_Type = Integer32
_CnLecPortIndex_Object = MibTableColumn
cnLecPortIndex = _CnLecPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 2, 2, 1, 2),
    _CnLecPortIndex_Type()
)
cnLecPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnLecPortIndex.setStatus("mandatory")
_CnLecCardId_Type = Integer32
_CnLecCardId_Object = MibTableColumn
cnLecCardId = _CnLecCardId_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 2, 2, 1, 3),
    _CnLecCardId_Type()
)
cnLecCardId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecCardId.setStatus("mandatory")
_CnLecPortId_Type = Integer32
_CnLecPortId_Object = MibTableColumn
cnLecPortId = _CnLecPortId_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 2, 2, 1, 4),
    _CnLecPortId_Type()
)
cnLecPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecPortId.setStatus("mandatory")


class _CnLecPortStatus_Type(Integer32):
    """Custom type cnLecPortStatus based on Integer32"""
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
        *(("active", 3),
          ("create", 1),
          ("delete", 2),
          ("inactive", 4))
    )


_CnLecPortStatus_Type.__name__ = "Integer32"
_CnLecPortStatus_Object = MibTableColumn
cnLecPortStatus = _CnLecPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 2, 2, 1, 5),
    _CnLecPortStatus_Type()
)
cnLecPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecPortStatus.setStatus("mandatory")
_CnLecConfigExtnTable_Object = MibTable
cnLecConfigExtnTable = _CnLecConfigExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 2, 3)
)
if mibBuilder.loadTexts:
    cnLecConfigExtnTable.setStatus("mandatory")
_CnLecConfigExtnEntry_Object = MibTableRow
cnLecConfigExtnEntry = _CnLecConfigExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 2, 3, 1)
)
cnLecConfigExtnEntry.setIndexNames(
    (0, "LAN-EMULATION-CLIENT-MIB", "lecIndex"),
)
if mibBuilder.loadTexts:
    cnLecConfigExtnEntry.setStatus("mandatory")


class _CnLecTargetlessArp_Type(EnableIndicator):
    """Custom type cnLecTargetlessArp based on EnableIndicator"""


_CnLecTargetlessArp_Object = MibTableColumn
cnLecTargetlessArp = _CnLecTargetlessArp_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 2, 3, 1, 1),
    _CnLecTargetlessArp_Type()
)
cnLecTargetlessArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecTargetlessArp.setStatus("mandatory")
_CnLecsExtnGroup_ObjectIdentity = ObjectIdentity
cnLecsExtnGroup = _CnLecsExtnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 3)
)
_CnLecsPortTable_Object = MibTable
cnLecsPortTable = _CnLecsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    cnLecsPortTable.setStatus("mandatory")
_CnLecsPortEntry_Object = MibTableRow
cnLecsPortEntry = _CnLecsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 3, 1, 1)
)
cnLecsPortEntry.setIndexNames(
    (0, "CENTILLION-LESBUS-MIB", "cnLecsIndex"),
    (0, "CENTILLION-LESBUS-MIB", "cnLecsPortIndex"),
)
if mibBuilder.loadTexts:
    cnLecsPortEntry.setStatus("mandatory")
_CnLecsIndex_Type = Integer32
_CnLecsIndex_Object = MibTableColumn
cnLecsIndex = _CnLecsIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 3, 1, 1, 1),
    _CnLecsIndex_Type()
)
cnLecsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnLecsIndex.setStatus("mandatory")
_CnLecsPortIndex_Type = Integer32
_CnLecsPortIndex_Object = MibTableColumn
cnLecsPortIndex = _CnLecsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 3, 1, 1, 2),
    _CnLecsPortIndex_Type()
)
cnLecsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnLecsPortIndex.setStatus("mandatory")
_CnLecsCardId_Type = Integer32
_CnLecsCardId_Object = MibTableColumn
cnLecsCardId = _CnLecsCardId_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 3, 1, 1, 3),
    _CnLecsCardId_Type()
)
cnLecsCardId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecsCardId.setStatus("mandatory")
_CnLecsPortId_Type = Integer32
_CnLecsPortId_Object = MibTableColumn
cnLecsPortId = _CnLecsPortId_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 3, 1, 1, 4),
    _CnLecsPortId_Type()
)
cnLecsPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecsPortId.setStatus("mandatory")


class _CnLecsPortStatus_Type(Integer32):
    """Custom type cnLecsPortStatus based on Integer32"""
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
        *(("active", 3),
          ("create", 1),
          ("delete", 2),
          ("inactive", 4))
    )


_CnLecsPortStatus_Type.__name__ = "Integer32"
_CnLecsPortStatus_Object = MibTableColumn
cnLecsPortStatus = _CnLecsPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 3, 1, 1, 5),
    _CnLecsPortStatus_Type()
)
cnLecsPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecsPortStatus.setStatus("mandatory")
_CnLecsExtnTable_Object = MibTable
cnLecsExtnTable = _CnLecsExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 3, 2)
)
if mibBuilder.loadTexts:
    cnLecsExtnTable.setStatus("mandatory")
_CnLecsExtnEntry_Object = MibTableRow
cnLecsExtnEntry = _CnLecsExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 3, 2, 1)
)
cnLecsExtnEntry.setIndexNames(
    (0, "LAN-EMULATION-ELAN-MIB", "lecsConfIndex"),
)
if mibBuilder.loadTexts:
    cnLecsExtnEntry.setStatus("mandatory")


class _CnLecsExtnAtmAddressSelect_Type(Integer32):
    """Custom type cnLecsExtnAtmAddressSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atmForum", 1),
          ("userDefined", 2))
    )


_CnLecsExtnAtmAddressSelect_Type.__name__ = "Integer32"
_CnLecsExtnAtmAddressSelect_Object = MibTableColumn
cnLecsExtnAtmAddressSelect = _CnLecsExtnAtmAddressSelect_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 3, 2, 1, 1),
    _CnLecsExtnAtmAddressSelect_Type()
)
cnLecsExtnAtmAddressSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecsExtnAtmAddressSelect.setStatus("mandatory")
_AtmCallRoutingConfig_ObjectIdentity = ObjectIdentity
atmCallRoutingConfig = _AtmCallRoutingConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 4)
)
_AtmCallRoutingConfigTable_Object = MibTable
atmCallRoutingConfigTable = _AtmCallRoutingConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 4, 1)
)
if mibBuilder.loadTexts:
    atmCallRoutingConfigTable.setStatus("mandatory")
_AtmCallRoutingConfigEntry_Object = MibTableRow
atmCallRoutingConfigEntry = _AtmCallRoutingConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 4, 1, 1)
)
atmCallRoutingConfigEntry.setIndexNames(
    (0, "CENTILLION-LESBUS-MIB", "atmCallRoutingId"),
)
if mibBuilder.loadTexts:
    atmCallRoutingConfigEntry.setStatus("mandatory")
_AtmCallRoutingId_Type = Integer32
_AtmCallRoutingId_Object = MibTableColumn
atmCallRoutingId = _AtmCallRoutingId_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 4, 1, 1, 1),
    _AtmCallRoutingId_Type()
)
atmCallRoutingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCallRoutingId.setStatus("mandatory")
_AtmCallRoutingAtmAddress_Type = AtmLaneAddress
_AtmCallRoutingAtmAddress_Object = MibTableColumn
atmCallRoutingAtmAddress = _AtmCallRoutingAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 4, 1, 1, 2),
    _AtmCallRoutingAtmAddress_Type()
)
atmCallRoutingAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmCallRoutingAtmAddress.setStatus("mandatory")


class _AtmCallRoutingType_Type(Integer32):
    """Custom type atmCallRoutingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("linkGroup", 3),
          ("network", 2))
    )


_AtmCallRoutingType_Type.__name__ = "Integer32"
_AtmCallRoutingType_Object = MibTableColumn
atmCallRoutingType = _AtmCallRoutingType_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 4, 1, 1, 3),
    _AtmCallRoutingType_Type()
)
atmCallRoutingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmCallRoutingType.setStatus("mandatory")


class _AtmCallRoutingCard_Type(Integer32):
    """Custom type atmCallRoutingCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AtmCallRoutingCard_Type.__name__ = "Integer32"
_AtmCallRoutingCard_Object = MibTableColumn
atmCallRoutingCard = _AtmCallRoutingCard_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 4, 1, 1, 4),
    _AtmCallRoutingCard_Type()
)
atmCallRoutingCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmCallRoutingCard.setStatus("mandatory")


class _AtmCallRoutingPort_Type(Integer32):
    """Custom type atmCallRoutingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AtmCallRoutingPort_Type.__name__ = "Integer32"
_AtmCallRoutingPort_Object = MibTableColumn
atmCallRoutingPort = _AtmCallRoutingPort_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 4, 1, 1, 5),
    _AtmCallRoutingPort_Type()
)
atmCallRoutingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmCallRoutingPort.setStatus("mandatory")


class _AtmCallRoutingCost_Type(Integer32):
    """Custom type atmCallRoutingCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmCallRoutingCost_Type.__name__ = "Integer32"
_AtmCallRoutingCost_Object = MibTableColumn
atmCallRoutingCost = _AtmCallRoutingCost_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 4, 1, 1, 6),
    _AtmCallRoutingCost_Type()
)
atmCallRoutingCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmCallRoutingCost.setStatus("mandatory")


class _AtmCallRoutingEnable_Type(Integer32):
    """Custom type atmCallRoutingEnable based on Integer32"""
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


_AtmCallRoutingEnable_Type.__name__ = "Integer32"
_AtmCallRoutingEnable_Object = MibTableColumn
atmCallRoutingEnable = _AtmCallRoutingEnable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 4, 1, 1, 7),
    _AtmCallRoutingEnable_Type()
)
atmCallRoutingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmCallRoutingEnable.setStatus("mandatory")


class _AtmCallRoutingRowStatus_Type(Integer32):
    """Custom type atmCallRoutingRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2))
    )


_AtmCallRoutingRowStatus_Type.__name__ = "Integer32"
_AtmCallRoutingRowStatus_Object = MibTableColumn
atmCallRoutingRowStatus = _AtmCallRoutingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 4, 1, 1, 8),
    _AtmCallRoutingRowStatus_Type()
)
atmCallRoutingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmCallRoutingRowStatus.setStatus("mandatory")


class _AtmCallRoutingScope_Type(Integer32):
    """Custom type atmCallRoutingScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 104),
    )


_AtmCallRoutingScope_Type.__name__ = "Integer32"
_AtmCallRoutingScope_Object = MibTableColumn
atmCallRoutingScope = _AtmCallRoutingScope_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 4, 1, 1, 9),
    _AtmCallRoutingScope_Type()
)
atmCallRoutingScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmCallRoutingScope.setStatus("mandatory")


class _AtmCallRoutingVpi_Type(Integer32):
    """Custom type atmCallRoutingVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AtmCallRoutingVpi_Type.__name__ = "Integer32"
_AtmCallRoutingVpi_Object = MibTableColumn
atmCallRoutingVpi = _AtmCallRoutingVpi_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 4, 1, 1, 10),
    _AtmCallRoutingVpi_Type()
)
atmCallRoutingVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmCallRoutingVpi.setStatus("mandatory")
_CnLaneGlobalConf_ObjectIdentity = ObjectIdentity
cnLaneGlobalConf = _CnLaneGlobalConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 5)
)


class _CnLaneSig_Type(Integer32):
    """Custom type cnLaneSig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CnLaneSig_Type.__name__ = "Integer32"
_CnLaneSig_Object = MibScalar
cnLaneSig = _CnLaneSig_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 5, 1),
    _CnLaneSig_Type()
)
cnLaneSig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLaneSig.setStatus("mandatory")


class _CnLaneEdge_Type(Integer32):
    """Custom type cnLaneEdge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("edgeAndSwitch", 2),
          ("edgeOnly", 1),
          ("switchOnly", 3))
    )


_CnLaneEdge_Type.__name__ = "Integer32"
_CnLaneEdge_Object = MibScalar
cnLaneEdge = _CnLaneEdge_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 5, 2),
    _CnLaneEdge_Type()
)
cnLaneEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLaneEdge.setStatus("mandatory")


class _CnLaneNetPrefix_Type(OctetString):
    """Custom type cnLaneNetPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_CnLaneNetPrefix_Type.__name__ = "OctetString"
_CnLaneNetPrefix_Object = MibScalar
cnLaneNetPrefix = _CnLaneNetPrefix_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 5, 3),
    _CnLaneNetPrefix_Type()
)
cnLaneNetPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLaneNetPrefix.setStatus("mandatory")


class _CnLaneStatusEnquiryEnable_Type(EnableIndicator):
    """Custom type cnLaneStatusEnquiryEnable based on EnableIndicator"""


_CnLaneStatusEnquiryEnable_Object = MibScalar
cnLaneStatusEnquiryEnable = _CnLaneStatusEnquiryEnable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 5, 4),
    _CnLaneStatusEnquiryEnable_Type()
)
cnLaneStatusEnquiryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLaneStatusEnquiryEnable.setStatus("mandatory")


class _CnLaneStatusEnquiryInterval_Type(TimeIntervalSec):
    """Custom type cnLaneStatusEnquiryInterval based on TimeIntervalSec"""
    defaultValue = 600

    subtypeSpec = TimeIntervalSec.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 9999),
    )


_CnLaneStatusEnquiryInterval_Type.__name__ = "TimeIntervalSec"
_CnLaneStatusEnquiryInterval_Object = MibScalar
cnLaneStatusEnquiryInterval = _CnLaneStatusEnquiryInterval_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 5, 5),
    _CnLaneStatusEnquiryInterval_Type()
)
cnLaneStatusEnquiryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLaneStatusEnquiryInterval.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CENTILLION-LESBUS-MIB",
    **{"cnLesBusExtnGroup": cnLesBusExtnGroup,
       "cnLesBusTable": cnLesBusTable,
       "cnLesBusEntry": cnLesBusEntry,
       "cnLesBusConfIndex": cnLesBusConfIndex,
       "cnLesBusSmartLes": cnLesBusSmartLes,
       "cnLesBusServerId": cnLesBusServerId,
       "cnLesBusBusAddrSpec": cnLesBusBusAddrSpec,
       "cnLesBusBusAddrActual": cnLesBusBusAddrActual,
       "cnLesBusPeerTable": cnLesBusPeerTable,
       "cnLesBusPeerEntry": cnLesBusPeerEntry,
       "cnLesBusIndex": cnLesBusIndex,
       "cnLesBusPeerIndex": cnLesBusPeerIndex,
       "cnLesBusPeerLesAddr": cnLesBusPeerLesAddr,
       "cnLesBusPeerBusAddr": cnLesBusPeerBusAddr,
       "cnLesBusPeerStatus": cnLesBusPeerStatus,
       "cnLesBusPortTable": cnLesBusPortTable,
       "cnLesBusPortEntry": cnLesBusPortEntry,
       "cnLesBusPortElanIndex": cnLesBusPortElanIndex,
       "cnLesBusPortIndex": cnLesBusPortIndex,
       "cnLesBusCardId": cnLesBusCardId,
       "cnLesBusPortId": cnLesBusPortId,
       "cnLesBusPortStatus": cnLesBusPortStatus,
       "cnLecExtnGroup": cnLecExtnGroup,
       "cnLecServerTable": cnLecServerTable,
       "cnLecServerEntry": cnLecServerEntry,
       "cnLecServerIndex": cnLecServerIndex,
       "cnLecServerType": cnLecServerType,
       "cnLecServerAddress": cnLecServerAddress,
       "cnLecServerStatus": cnLecServerStatus,
       "cnLecPortTable": cnLecPortTable,
       "cnLecPortEntry": cnLecPortEntry,
       "cnLecPortlecIndex": cnLecPortlecIndex,
       "cnLecPortIndex": cnLecPortIndex,
       "cnLecCardId": cnLecCardId,
       "cnLecPortId": cnLecPortId,
       "cnLecPortStatus": cnLecPortStatus,
       "cnLecConfigExtnTable": cnLecConfigExtnTable,
       "cnLecConfigExtnEntry": cnLecConfigExtnEntry,
       "cnLecTargetlessArp": cnLecTargetlessArp,
       "cnLecsExtnGroup": cnLecsExtnGroup,
       "cnLecsPortTable": cnLecsPortTable,
       "cnLecsPortEntry": cnLecsPortEntry,
       "cnLecsIndex": cnLecsIndex,
       "cnLecsPortIndex": cnLecsPortIndex,
       "cnLecsCardId": cnLecsCardId,
       "cnLecsPortId": cnLecsPortId,
       "cnLecsPortStatus": cnLecsPortStatus,
       "cnLecsExtnTable": cnLecsExtnTable,
       "cnLecsExtnEntry": cnLecsExtnEntry,
       "cnLecsExtnAtmAddressSelect": cnLecsExtnAtmAddressSelect,
       "atmCallRoutingConfig": atmCallRoutingConfig,
       "atmCallRoutingConfigTable": atmCallRoutingConfigTable,
       "atmCallRoutingConfigEntry": atmCallRoutingConfigEntry,
       "atmCallRoutingId": atmCallRoutingId,
       "atmCallRoutingAtmAddress": atmCallRoutingAtmAddress,
       "atmCallRoutingType": atmCallRoutingType,
       "atmCallRoutingCard": atmCallRoutingCard,
       "atmCallRoutingPort": atmCallRoutingPort,
       "atmCallRoutingCost": atmCallRoutingCost,
       "atmCallRoutingEnable": atmCallRoutingEnable,
       "atmCallRoutingRowStatus": atmCallRoutingRowStatus,
       "atmCallRoutingScope": atmCallRoutingScope,
       "atmCallRoutingVpi": atmCallRoutingVpi,
       "cnLaneGlobalConf": cnLaneGlobalConf,
       "cnLaneSig": cnLaneSig,
       "cnLaneEdge": cnLaneEdge,
       "cnLaneNetPrefix": cnLaneNetPrefix,
       "cnLaneStatusEnquiryEnable": cnLaneStatusEnquiryEnable,
       "cnLaneStatusEnquiryInterval": cnLaneStatusEnquiryInterval}
)
