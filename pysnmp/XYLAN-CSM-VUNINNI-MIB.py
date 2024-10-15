# SNMP MIB module (XYLAN-CSM-VUNINNI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-CSM-VUNINNI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:59 2024
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

(xylnatmInterfaceConfGroup,) = mibBuilder.importSymbols(
    "XYLAN-CSM-MIB",
    "xylnatmInterfaceConfGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XylnatmVUniConfGroup_ObjectIdentity = ObjectIdentity
xylnatmVUniConfGroup = _XylnatmVUniConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2)
)
_XylnatmVUniConfInstanceCount_Type = Counter32
_XylnatmVUniConfInstanceCount_Object = MibScalar
xylnatmVUniConfInstanceCount = _XylnatmVUniConfInstanceCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 1),
    _XylnatmVUniConfInstanceCount_Type()
)
xylnatmVUniConfInstanceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVUniConfInstanceCount.setStatus("mandatory")
_XylnatmVUniConfTable_Object = MibTable
xylnatmVUniConfTable = _XylnatmVUniConfTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    xylnatmVUniConfTable.setStatus("mandatory")
_XylnatmVUniConfEntry_Object = MibTableRow
xylnatmVUniConfEntry = _XylnatmVUniConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 2, 1)
)
xylnatmVUniConfEntry.setIndexNames(
    (0, "XYLAN-CSM-VUNINNI-MIB", "xylnatmVUniConfSlotIndex"),
    (0, "XYLAN-CSM-VUNINNI-MIB", "xylnatmVUniConfPortIndex"),
    (0, "XYLAN-CSM-VUNINNI-MIB", "xylnatmVUniConfInsIndex"),
)
if mibBuilder.loadTexts:
    xylnatmVUniConfEntry.setStatus("mandatory")
_XylnatmVUniConfSlotIndex_Type = Integer32
_XylnatmVUniConfSlotIndex_Object = MibTableColumn
xylnatmVUniConfSlotIndex = _XylnatmVUniConfSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 2, 1, 1),
    _XylnatmVUniConfSlotIndex_Type()
)
xylnatmVUniConfSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVUniConfSlotIndex.setStatus("mandatory")
_XylnatmVUniConfPortIndex_Type = Integer32
_XylnatmVUniConfPortIndex_Object = MibTableColumn
xylnatmVUniConfPortIndex = _XylnatmVUniConfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 2, 1, 2),
    _XylnatmVUniConfPortIndex_Type()
)
xylnatmVUniConfPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVUniConfPortIndex.setStatus("mandatory")


class _XylnatmVUniConfInsIndex_Type(Integer32):
    """Custom type xylnatmVUniConfInsIndex based on Integer32"""
    defaultValue = 0


_XylnatmVUniConfInsIndex_Object = MibTableColumn
xylnatmVUniConfInsIndex = _XylnatmVUniConfInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 2, 1, 3),
    _XylnatmVUniConfInsIndex_Type()
)
xylnatmVUniConfInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVUniConfInsIndex.setStatus("mandatory")
_XylnatmVUniConfIfIndex_Type = Integer32
_XylnatmVUniConfIfIndex_Object = MibTableColumn
xylnatmVUniConfIfIndex = _XylnatmVUniConfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 2, 1, 4),
    _XylnatmVUniConfIfIndex_Type()
)
xylnatmVUniConfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVUniConfIfIndex.setStatus("mandatory")


class _XylnatmVUniConfVPI_Type(Integer32):
    """Custom type xylnatmVUniConfVPI based on Integer32"""
    defaultValue = 1


_XylnatmVUniConfVPI_Object = MibTableColumn
xylnatmVUniConfVPI = _XylnatmVUniConfVPI_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 2, 1, 5),
    _XylnatmVUniConfVPI_Type()
)
xylnatmVUniConfVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVUniConfVPI.setStatus("mandatory")
_XylnatmVUniConfTunnelID_Type = Integer32
_XylnatmVUniConfTunnelID_Object = MibTableColumn
xylnatmVUniConfTunnelID = _XylnatmVUniConfTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 2, 1, 6),
    _XylnatmVUniConfTunnelID_Type()
)
xylnatmVUniConfTunnelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylnatmVUniConfTunnelID.setStatus("mandatory")


class _XylnatmVUniConfDescr_Type(DisplayString):
    """Custom type xylnatmVUniConfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_XylnatmVUniConfDescr_Type.__name__ = "DisplayString"
_XylnatmVUniConfDescr_Object = MibTableColumn
xylnatmVUniConfDescr = _XylnatmVUniConfDescr_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 2, 1, 7),
    _XylnatmVUniConfDescr_Type()
)
xylnatmVUniConfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVUniConfDescr.setStatus("mandatory")


class _XylnatmVUniConfIfType_Type(Integer32):
    """Custom type xylnatmVUniConfIfType based on Integer32"""
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
        *(("iisp-network", 4),
          ("iisp-user", 5),
          ("pnni", 3),
          ("pri-uni", 2),
          ("pub-uni", 1))
    )


_XylnatmVUniConfIfType_Type.__name__ = "Integer32"
_XylnatmVUniConfIfType_Object = MibTableColumn
xylnatmVUniConfIfType = _XylnatmVUniConfIfType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 2, 1, 8),
    _XylnatmVUniConfIfType_Type()
)
xylnatmVUniConfIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVUniConfIfType.setStatus("mandatory")


class _XylnatmVUniConfSigEnable_Type(Integer32):
    """Custom type xylnatmVUniConfSigEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_XylnatmVUniConfSigEnable_Type.__name__ = "Integer32"
_XylnatmVUniConfSigEnable_Object = MibTableColumn
xylnatmVUniConfSigEnable = _XylnatmVUniConfSigEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 2, 1, 9),
    _XylnatmVUniConfSigEnable_Type()
)
xylnatmVUniConfSigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVUniConfSigEnable.setStatus("mandatory")


class _XylnatmVUniConfSignalingVer_Type(Integer32):
    """Custom type xylnatmVUniConfSignalingVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ver30", 1),
          ("ver31", 2))
    )


_XylnatmVUniConfSignalingVer_Type.__name__ = "Integer32"
_XylnatmVUniConfSignalingVer_Object = MibTableColumn
xylnatmVUniConfSignalingVer = _XylnatmVUniConfSignalingVer_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 2, 1, 10),
    _XylnatmVUniConfSignalingVer_Type()
)
xylnatmVUniConfSignalingVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVUniConfSignalingVer.setStatus("mandatory")


class _XylnatmVUniConfILMIEnable_Type(Integer32):
    """Custom type xylnatmVUniConfILMIEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_XylnatmVUniConfILMIEnable_Type.__name__ = "Integer32"
_XylnatmVUniConfILMIEnable_Object = MibTableColumn
xylnatmVUniConfILMIEnable = _XylnatmVUniConfILMIEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 2, 1, 11),
    _XylnatmVUniConfILMIEnable_Type()
)
xylnatmVUniConfILMIEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVUniConfILMIEnable.setStatus("mandatory")


class _XylnatmVUniConfAdminStatus_Type(Integer32):
    """Custom type xylnatmVUniConfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_XylnatmVUniConfAdminStatus_Type.__name__ = "Integer32"
_XylnatmVUniConfAdminStatus_Object = MibTableColumn
xylnatmVUniConfAdminStatus = _XylnatmVUniConfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 2, 1, 12),
    _XylnatmVUniConfAdminStatus_Type()
)
xylnatmVUniConfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVUniConfAdminStatus.setStatus("mandatory")


class _XylnatmVUniConfRowStatus_Type(Integer32):
    """Custom type xylnatmVUniConfRowStatus based on Integer32"""
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
        *(("create", 1),
          ("delete", 3),
          ("inService", 4),
          ("modify", 2))
    )


_XylnatmVUniConfRowStatus_Type.__name__ = "Integer32"
_XylnatmVUniConfRowStatus_Object = MibTableColumn
xylnatmVUniConfRowStatus = _XylnatmVUniConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 2, 1, 13),
    _XylnatmVUniConfRowStatus_Type()
)
xylnatmVUniConfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylnatmVUniConfRowStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-CSM-VUNINNI-MIB",
    **{"xylnatmVUniConfGroup": xylnatmVUniConfGroup,
       "xylnatmVUniConfInstanceCount": xylnatmVUniConfInstanceCount,
       "xylnatmVUniConfTable": xylnatmVUniConfTable,
       "xylnatmVUniConfEntry": xylnatmVUniConfEntry,
       "xylnatmVUniConfSlotIndex": xylnatmVUniConfSlotIndex,
       "xylnatmVUniConfPortIndex": xylnatmVUniConfPortIndex,
       "xylnatmVUniConfInsIndex": xylnatmVUniConfInsIndex,
       "xylnatmVUniConfIfIndex": xylnatmVUniConfIfIndex,
       "xylnatmVUniConfVPI": xylnatmVUniConfVPI,
       "xylnatmVUniConfTunnelID": xylnatmVUniConfTunnelID,
       "xylnatmVUniConfDescr": xylnatmVUniConfDescr,
       "xylnatmVUniConfIfType": xylnatmVUniConfIfType,
       "xylnatmVUniConfSigEnable": xylnatmVUniConfSigEnable,
       "xylnatmVUniConfSignalingVer": xylnatmVUniConfSignalingVer,
       "xylnatmVUniConfILMIEnable": xylnatmVUniConfILMIEnable,
       "xylnatmVUniConfAdminStatus": xylnatmVUniConfAdminStatus,
       "xylnatmVUniConfRowStatus": xylnatmVUniConfRowStatus}
)
