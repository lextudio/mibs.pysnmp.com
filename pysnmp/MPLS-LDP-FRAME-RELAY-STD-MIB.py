# SNMP MIB module (MPLS-LDP-FRAME-RELAY-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MPLS-LDP-FRAME-RELAY-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:13 2024
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

(DLCI,) = mibBuilder.importSymbols(
    "FRAME-RELAY-DTE-MIB",
    "DLCI")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(mplsLdpEntityIndex,
 mplsLdpEntityLdpId,
 mplsLdpPeerLdpId) = mibBuilder.importSymbols(
    "MPLS-LDP-STD-MIB",
    "mplsLdpEntityIndex",
    "mplsLdpEntityLdpId",
    "mplsLdpPeerLdpId")

(mplsStdMIB,) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "mplsStdMIB")

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
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

mplsLdpFrameRelayStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 6)
)
mplsLdpFrameRelayStdMIB.setRevisions(
        ("2004-06-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MplsLdpFrameRelayObjects_ObjectIdentity = ObjectIdentity
mplsLdpFrameRelayObjects = _MplsLdpFrameRelayObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 6, 1)
)
_MplsLdpEntityFrameRelayObjects_ObjectIdentity = ObjectIdentity
mplsLdpEntityFrameRelayObjects = _MplsLdpEntityFrameRelayObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1)
)
_MplsLdpEntityFrameRelayTable_Object = MibTable
mplsLdpEntityFrameRelayTable = _MplsLdpEntityFrameRelayTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayTable.setStatus("current")
_MplsLdpEntityFrameRelayEntry_Object = MibTableRow
mplsLdpEntityFrameRelayEntry = _MplsLdpEntityFrameRelayEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 1, 1)
)
mplsLdpEntityFrameRelayEntry.setIndexNames(
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"),
)
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayEntry.setStatus("current")
_MplsLdpEntityFrameRelayIfIndexOrZero_Type = InterfaceIndexOrZero
_MplsLdpEntityFrameRelayIfIndexOrZero_Object = MibTableColumn
mplsLdpEntityFrameRelayIfIndexOrZero = _MplsLdpEntityFrameRelayIfIndexOrZero_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 1, 1, 1),
    _MplsLdpEntityFrameRelayIfIndexOrZero_Type()
)
mplsLdpEntityFrameRelayIfIndexOrZero.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayIfIndexOrZero.setStatus("current")


class _MplsLdpEntityFrameRelayMergeCap_Type(Integer32):
    """Custom type mplsLdpEntityFrameRelayMergeCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("supported", 1))
    )


_MplsLdpEntityFrameRelayMergeCap_Type.__name__ = "Integer32"
_MplsLdpEntityFrameRelayMergeCap_Object = MibTableColumn
mplsLdpEntityFrameRelayMergeCap = _MplsLdpEntityFrameRelayMergeCap_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 1, 1, 2),
    _MplsLdpEntityFrameRelayMergeCap_Type()
)
mplsLdpEntityFrameRelayMergeCap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayMergeCap.setStatus("current")


class _MplsLdpEntityFrameRelayLRComponents_Type(Unsigned32):
    """Custom type mplsLdpEntityFrameRelayLRComponents based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MplsLdpEntityFrameRelayLRComponents_Type.__name__ = "Unsigned32"
_MplsLdpEntityFrameRelayLRComponents_Object = MibTableColumn
mplsLdpEntityFrameRelayLRComponents = _MplsLdpEntityFrameRelayLRComponents_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 1, 1, 3),
    _MplsLdpEntityFrameRelayLRComponents_Type()
)
mplsLdpEntityFrameRelayLRComponents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayLRComponents.setStatus("current")


class _MplsLdpEntityFrameRelayVcDirectionality_Type(Integer32):
    """Custom type mplsLdpEntityFrameRelayVcDirectionality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 0),
          ("unidirection", 1))
    )


_MplsLdpEntityFrameRelayVcDirectionality_Type.__name__ = "Integer32"
_MplsLdpEntityFrameRelayVcDirectionality_Object = MibTableColumn
mplsLdpEntityFrameRelayVcDirectionality = _MplsLdpEntityFrameRelayVcDirectionality_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 1, 1, 4),
    _MplsLdpEntityFrameRelayVcDirectionality_Type()
)
mplsLdpEntityFrameRelayVcDirectionality.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayVcDirectionality.setStatus("current")


class _MplsLdpEntityFrameRelayStorageType_Type(StorageType):
    """Custom type mplsLdpEntityFrameRelayStorageType based on StorageType"""


_MplsLdpEntityFrameRelayStorageType_Object = MibTableColumn
mplsLdpEntityFrameRelayStorageType = _MplsLdpEntityFrameRelayStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 1, 1, 5),
    _MplsLdpEntityFrameRelayStorageType_Type()
)
mplsLdpEntityFrameRelayStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayStorageType.setStatus("current")
_MplsLdpEntityFrameRelayRowStatus_Type = RowStatus
_MplsLdpEntityFrameRelayRowStatus_Object = MibTableColumn
mplsLdpEntityFrameRelayRowStatus = _MplsLdpEntityFrameRelayRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 1, 1, 6),
    _MplsLdpEntityFrameRelayRowStatus_Type()
)
mplsLdpEntityFrameRelayRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayRowStatus.setStatus("current")
_MplsLdpEntityFrameRelayLRTable_Object = MibTable
mplsLdpEntityFrameRelayLRTable = _MplsLdpEntityFrameRelayLRTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayLRTable.setStatus("current")
_MplsLdpEntityFrameRelayLREntry_Object = MibTableRow
mplsLdpEntityFrameRelayLREntry = _MplsLdpEntityFrameRelayLREntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 2, 1)
)
mplsLdpEntityFrameRelayLREntry.setIndexNames(
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayLRMinDlci"),
)
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayLREntry.setStatus("current")
_MplsLdpEntityFrameRelayLRMinDlci_Type = DLCI
_MplsLdpEntityFrameRelayLRMinDlci_Object = MibTableColumn
mplsLdpEntityFrameRelayLRMinDlci = _MplsLdpEntityFrameRelayLRMinDlci_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 2, 1, 1),
    _MplsLdpEntityFrameRelayLRMinDlci_Type()
)
mplsLdpEntityFrameRelayLRMinDlci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayLRMinDlci.setStatus("current")
_MplsLdpEntityFrameRelayLRMaxDlci_Type = DLCI
_MplsLdpEntityFrameRelayLRMaxDlci_Object = MibTableColumn
mplsLdpEntityFrameRelayLRMaxDlci = _MplsLdpEntityFrameRelayLRMaxDlci_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 2, 1, 2),
    _MplsLdpEntityFrameRelayLRMaxDlci_Type()
)
mplsLdpEntityFrameRelayLRMaxDlci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayLRMaxDlci.setStatus("current")


class _MplsLdpEntityFrameRelayLRLen_Type(Integer32):
    """Custom type mplsLdpEntityFrameRelayLRLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tenDlciBits", 0),
          ("twentyThreeDlciBits", 2))
    )


_MplsLdpEntityFrameRelayLRLen_Type.__name__ = "Integer32"
_MplsLdpEntityFrameRelayLRLen_Object = MibTableColumn
mplsLdpEntityFrameRelayLRLen = _MplsLdpEntityFrameRelayLRLen_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 2, 1, 3),
    _MplsLdpEntityFrameRelayLRLen_Type()
)
mplsLdpEntityFrameRelayLRLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayLRLen.setStatus("current")


class _MplsLdpEntityFrameRelayLRStorageType_Type(StorageType):
    """Custom type mplsLdpEntityFrameRelayLRStorageType based on StorageType"""


_MplsLdpEntityFrameRelayLRStorageType_Object = MibTableColumn
mplsLdpEntityFrameRelayLRStorageType = _MplsLdpEntityFrameRelayLRStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 2, 1, 4),
    _MplsLdpEntityFrameRelayLRStorageType_Type()
)
mplsLdpEntityFrameRelayLRStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayLRStorageType.setStatus("current")
_MplsLdpEntityFrameRelayLRRowStatus_Type = RowStatus
_MplsLdpEntityFrameRelayLRRowStatus_Object = MibTableColumn
mplsLdpEntityFrameRelayLRRowStatus = _MplsLdpEntityFrameRelayLRRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 2, 1, 5),
    _MplsLdpEntityFrameRelayLRRowStatus_Type()
)
mplsLdpEntityFrameRelayLRRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayLRRowStatus.setStatus("current")
_MplsLdpFrameRelaySessionObjects_ObjectIdentity = ObjectIdentity
mplsLdpFrameRelaySessionObjects = _MplsLdpFrameRelaySessionObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 2)
)
_MplsLdpFrameRelaySessionTable_Object = MibTable
mplsLdpFrameRelaySessionTable = _MplsLdpFrameRelaySessionTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mplsLdpFrameRelaySessionTable.setStatus("current")
_MplsLdpFrameRelaySessionEntry_Object = MibTableRow
mplsLdpFrameRelaySessionEntry = _MplsLdpFrameRelaySessionEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 2, 1, 1)
)
mplsLdpFrameRelaySessionEntry.setIndexNames(
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpPeerLdpId"),
    (0, "MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpFrameRelaySessionMinDlci"),
)
if mibBuilder.loadTexts:
    mplsLdpFrameRelaySessionEntry.setStatus("current")
_MplsLdpFrameRelaySessionMinDlci_Type = DLCI
_MplsLdpFrameRelaySessionMinDlci_Object = MibTableColumn
mplsLdpFrameRelaySessionMinDlci = _MplsLdpFrameRelaySessionMinDlci_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 2, 1, 1, 1),
    _MplsLdpFrameRelaySessionMinDlci_Type()
)
mplsLdpFrameRelaySessionMinDlci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpFrameRelaySessionMinDlci.setStatus("current")
_MplsLdpFrameRelaySessionMaxDlci_Type = DLCI
_MplsLdpFrameRelaySessionMaxDlci_Object = MibTableColumn
mplsLdpFrameRelaySessionMaxDlci = _MplsLdpFrameRelaySessionMaxDlci_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 2, 1, 1, 2),
    _MplsLdpFrameRelaySessionMaxDlci_Type()
)
mplsLdpFrameRelaySessionMaxDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpFrameRelaySessionMaxDlci.setStatus("current")


class _MplsLdpFrameRelaySessionLen_Type(Integer32):
    """Custom type mplsLdpFrameRelaySessionLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tenDlciBits", 0),
          ("twentyThreeDlciBits", 2))
    )


_MplsLdpFrameRelaySessionLen_Type.__name__ = "Integer32"
_MplsLdpFrameRelaySessionLen_Object = MibTableColumn
mplsLdpFrameRelaySessionLen = _MplsLdpFrameRelaySessionLen_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 2, 1, 1, 3),
    _MplsLdpFrameRelaySessionLen_Type()
)
mplsLdpFrameRelaySessionLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpFrameRelaySessionLen.setStatus("current")
_MplsLdpFrameRelayConformance_ObjectIdentity = ObjectIdentity
mplsLdpFrameRelayConformance = _MplsLdpFrameRelayConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 6, 2)
)
_MplsLdpFrameRelayGroups_ObjectIdentity = ObjectIdentity
mplsLdpFrameRelayGroups = _MplsLdpFrameRelayGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 6, 2, 1)
)
_MplsLdpFrameRelayCompliances_ObjectIdentity = ObjectIdentity
mplsLdpFrameRelayCompliances = _MplsLdpFrameRelayCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 6, 2, 2)
)

# Managed Objects groups

mplsLdpFrameRelayGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 6, 2, 1, 1)
)
mplsLdpFrameRelayGroup.setObjects(
      *(("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayIfIndexOrZero"),
        ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayMergeCap"),
        ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayLRComponents"),
        ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayVcDirectionality"),
        ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayStorageType"),
        ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayRowStatus"),
        ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayLRMaxDlci"),
        ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayLRLen"),
        ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayLRStorageType"),
        ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayLRRowStatus"),
        ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpFrameRelaySessionMaxDlci"),
        ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpFrameRelaySessionLen"))
)
if mibBuilder.loadTexts:
    mplsLdpFrameRelayGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mplsLdpFrameRelayModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 6, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mplsLdpFrameRelayModuleFullCompliance.setStatus(
        "current"
    )

mplsLdpFrameRelayModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 6, 2, 2, 2)
)
if mibBuilder.loadTexts:
    mplsLdpFrameRelayModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPLS-LDP-FRAME-RELAY-STD-MIB",
    **{"mplsLdpFrameRelayStdMIB": mplsLdpFrameRelayStdMIB,
       "mplsLdpFrameRelayObjects": mplsLdpFrameRelayObjects,
       "mplsLdpEntityFrameRelayObjects": mplsLdpEntityFrameRelayObjects,
       "mplsLdpEntityFrameRelayTable": mplsLdpEntityFrameRelayTable,
       "mplsLdpEntityFrameRelayEntry": mplsLdpEntityFrameRelayEntry,
       "mplsLdpEntityFrameRelayIfIndexOrZero": mplsLdpEntityFrameRelayIfIndexOrZero,
       "mplsLdpEntityFrameRelayMergeCap": mplsLdpEntityFrameRelayMergeCap,
       "mplsLdpEntityFrameRelayLRComponents": mplsLdpEntityFrameRelayLRComponents,
       "mplsLdpEntityFrameRelayVcDirectionality": mplsLdpEntityFrameRelayVcDirectionality,
       "mplsLdpEntityFrameRelayStorageType": mplsLdpEntityFrameRelayStorageType,
       "mplsLdpEntityFrameRelayRowStatus": mplsLdpEntityFrameRelayRowStatus,
       "mplsLdpEntityFrameRelayLRTable": mplsLdpEntityFrameRelayLRTable,
       "mplsLdpEntityFrameRelayLREntry": mplsLdpEntityFrameRelayLREntry,
       "mplsLdpEntityFrameRelayLRMinDlci": mplsLdpEntityFrameRelayLRMinDlci,
       "mplsLdpEntityFrameRelayLRMaxDlci": mplsLdpEntityFrameRelayLRMaxDlci,
       "mplsLdpEntityFrameRelayLRLen": mplsLdpEntityFrameRelayLRLen,
       "mplsLdpEntityFrameRelayLRStorageType": mplsLdpEntityFrameRelayLRStorageType,
       "mplsLdpEntityFrameRelayLRRowStatus": mplsLdpEntityFrameRelayLRRowStatus,
       "mplsLdpFrameRelaySessionObjects": mplsLdpFrameRelaySessionObjects,
       "mplsLdpFrameRelaySessionTable": mplsLdpFrameRelaySessionTable,
       "mplsLdpFrameRelaySessionEntry": mplsLdpFrameRelaySessionEntry,
       "mplsLdpFrameRelaySessionMinDlci": mplsLdpFrameRelaySessionMinDlci,
       "mplsLdpFrameRelaySessionMaxDlci": mplsLdpFrameRelaySessionMaxDlci,
       "mplsLdpFrameRelaySessionLen": mplsLdpFrameRelaySessionLen,
       "mplsLdpFrameRelayConformance": mplsLdpFrameRelayConformance,
       "mplsLdpFrameRelayGroups": mplsLdpFrameRelayGroups,
       "mplsLdpFrameRelayGroup": mplsLdpFrameRelayGroup,
       "mplsLdpFrameRelayCompliances": mplsLdpFrameRelayCompliances,
       "mplsLdpFrameRelayModuleFullCompliance": mplsLdpFrameRelayModuleFullCompliance,
       "mplsLdpFrameRelayModuleReadOnlyCompliance": mplsLdpFrameRelayModuleReadOnlyCompliance}
)
