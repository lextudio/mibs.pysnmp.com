# SNMP MIB module (A3COM-MIP-R1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-MIP-R1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:37 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_BrouterMIB_ObjectIdentity = ObjectIdentity
brouterMIB = _BrouterMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2)
)
_A3ComMIP_ObjectIdentity = ObjectIdentity
a3ComMIP = _A3ComMIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 27)
)
_A3ComMipSConfig_ObjectIdentity = ObjectIdentity
a3ComMipSConfig = _A3ComMipSConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 27, 1)
)


class _A3ComMipControl_Type(Integer32):
    """Custom type a3ComMipControl based on Integer32"""
    defaultValue = 2

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


_A3ComMipControl_Type.__name__ = "Integer32"
_A3ComMipControl_Object = MibScalar
a3ComMipControl = _A3ComMipControl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 27, 1, 1),
    _A3ComMipControl_Type()
)
a3ComMipControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComMipControl.setStatus("mandatory")
_A3ComMipCConfig_ObjectIdentity = ObjectIdentity
a3ComMipCConfig = _A3ComMipCConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 27, 2)
)
_A3ComMipPortTable_Object = MibTable
a3ComMipPortTable = _A3ComMipPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 1)
)
if mibBuilder.loadTexts:
    a3ComMipPortTable.setStatus("mandatory")
_A3ComMipPortEntry_Object = MibTableRow
a3ComMipPortEntry = _A3ComMipPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 1, 1)
)
a3ComMipPortEntry.setIndexNames(
    (0, "A3COM-MIP-R1-MIB", "a3ComMipPortIndex"),
)
if mibBuilder.loadTexts:
    a3ComMipPortEntry.setStatus("mandatory")
_A3ComMipPortIndex_Type = Integer32
_A3ComMipPortIndex_Object = MibTableColumn
a3ComMipPortIndex = _A3ComMipPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 1, 1, 1),
    _A3ComMipPortIndex_Type()
)
a3ComMipPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComMipPortIndex.setStatus("mandatory")


class _A3ComMipPortQueryInterval_Type(Integer32):
    """Custom type a3ComMipPortQueryInterval based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5400),
    )


_A3ComMipPortQueryInterval_Type.__name__ = "Integer32"
_A3ComMipPortQueryInterval_Object = MibTableColumn
a3ComMipPortQueryInterval = _A3ComMipPortQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 1, 1, 2),
    _A3ComMipPortQueryInterval_Type()
)
a3ComMipPortQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComMipPortQueryInterval.setStatus("mandatory")


class _A3ComMipPortThreshold_Type(Integer32):
    """Custom type a3ComMipPortThreshold based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_A3ComMipPortThreshold_Type.__name__ = "Integer32"
_A3ComMipPortThreshold_Object = MibTableColumn
a3ComMipPortThreshold = _A3ComMipPortThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 1, 1, 3),
    _A3ComMipPortThreshold_Type()
)
a3ComMipPortThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComMipPortThreshold.setStatus("mandatory")


class _A3ComMipPortQuerier_Type(Integer32):
    """Custom type a3ComMipPortQuerier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_A3ComMipPortQuerier_Type.__name__ = "Integer32"
_A3ComMipPortQuerier_Object = MibTableColumn
a3ComMipPortQuerier = _A3ComMipPortQuerier_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 1, 1, 4),
    _A3ComMipPortQuerier_Type()
)
a3ComMipPortQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComMipPortQuerier.setStatus("mandatory")


class _A3ComMipPortPaceMode_Type(Integer32):
    """Custom type a3ComMipPortPaceMode based on Integer32"""
    defaultValue = 2

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


_A3ComMipPortPaceMode_Type.__name__ = "Integer32"
_A3ComMipPortPaceMode_Object = MibTableColumn
a3ComMipPortPaceMode = _A3ComMipPortPaceMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 1, 1, 5),
    _A3ComMipPortPaceMode_Type()
)
a3ComMipPortPaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComMipPortPaceMode.setStatus("mandatory")
_A3ComMipLocalGroupTable_Object = MibTable
a3ComMipLocalGroupTable = _A3ComMipLocalGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 2)
)
if mibBuilder.loadTexts:
    a3ComMipLocalGroupTable.setStatus("mandatory")
_A3ComMipLocalGroupEntry_Object = MibTableRow
a3ComMipLocalGroupEntry = _A3ComMipLocalGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 2, 1)
)
a3ComMipLocalGroupEntry.setIndexNames(
    (0, "A3COM-MIP-R1-MIB", "a3ComMipLocalGroupPort"),
    (0, "A3COM-MIP-R1-MIB", "a3ComMipLocalGroupIpAddr"),
)
if mibBuilder.loadTexts:
    a3ComMipLocalGroupEntry.setStatus("mandatory")
_A3ComMipLocalGroupPort_Type = Integer32
_A3ComMipLocalGroupPort_Object = MibTableColumn
a3ComMipLocalGroupPort = _A3ComMipLocalGroupPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 2, 1, 1),
    _A3ComMipLocalGroupPort_Type()
)
a3ComMipLocalGroupPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComMipLocalGroupPort.setStatus("mandatory")
_A3ComMipLocalGroupIpAddr_Type = IpAddress
_A3ComMipLocalGroupIpAddr_Object = MibTableColumn
a3ComMipLocalGroupIpAddr = _A3ComMipLocalGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 2, 1, 2),
    _A3ComMipLocalGroupIpAddr_Type()
)
a3ComMipLocalGroupIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComMipLocalGroupIpAddr.setStatus("mandatory")


class _A3ComMipLocalGroupType_Type(Integer32):
    """Custom type a3ComMipLocalGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("igmp", 2),
          ("static", 1))
    )


_A3ComMipLocalGroupType_Type.__name__ = "Integer32"
_A3ComMipLocalGroupType_Object = MibTableColumn
a3ComMipLocalGroupType = _A3ComMipLocalGroupType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 2, 1, 3),
    _A3ComMipLocalGroupType_Type()
)
a3ComMipLocalGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComMipLocalGroupType.setStatus("mandatory")
_A3ComMipLocalGroupStatus_Type = RowStatus
_A3ComMipLocalGroupStatus_Object = MibTableColumn
a3ComMipLocalGroupStatus = _A3ComMipLocalGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 2, 1, 4),
    _A3ComMipLocalGroupStatus_Type()
)
a3ComMipLocalGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComMipLocalGroupStatus.setStatus("mandatory")
_A3ComMipSmdsGroupTable_Object = MibTable
a3ComMipSmdsGroupTable = _A3ComMipSmdsGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 3)
)
if mibBuilder.loadTexts:
    a3ComMipSmdsGroupTable.setStatus("mandatory")
_A3ComMipSmdsGroupEntry_Object = MibTableRow
a3ComMipSmdsGroupEntry = _A3ComMipSmdsGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 3, 1)
)
a3ComMipSmdsGroupEntry.setIndexNames(
    (0, "A3COM-MIP-R1-MIB", "a3ComMipSmdsGroupIpAddr"),
)
if mibBuilder.loadTexts:
    a3ComMipSmdsGroupEntry.setStatus("mandatory")
_A3ComMipSmdsGroupIpAddr_Type = IpAddress
_A3ComMipSmdsGroupIpAddr_Object = MibTableColumn
a3ComMipSmdsGroupIpAddr = _A3ComMipSmdsGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 3, 1, 1),
    _A3ComMipSmdsGroupIpAddr_Type()
)
a3ComMipSmdsGroupIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComMipSmdsGroupIpAddr.setStatus("mandatory")


class _A3ComMipSmdsGroupMediaAddr_Type(OctetString):
    """Custom type a3ComMipSmdsGroupMediaAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_A3ComMipSmdsGroupMediaAddr_Type.__name__ = "OctetString"
_A3ComMipSmdsGroupMediaAddr_Object = MibTableColumn
a3ComMipSmdsGroupMediaAddr = _A3ComMipSmdsGroupMediaAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 3, 1, 2),
    _A3ComMipSmdsGroupMediaAddr_Type()
)
a3ComMipSmdsGroupMediaAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComMipSmdsGroupMediaAddr.setStatus("mandatory")
_A3ComMipSmdsGroupStatus_Type = RowStatus
_A3ComMipSmdsGroupStatus_Object = MibTableColumn
a3ComMipSmdsGroupStatus = _A3ComMipSmdsGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 3, 1, 3),
    _A3ComMipSmdsGroupStatus_Type()
)
a3ComMipSmdsGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComMipSmdsGroupStatus.setStatus("mandatory")
_A3ComMipData_ObjectIdentity = ObjectIdentity
a3ComMipData = _A3ComMipData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 27, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-MIP-R1-MIB",
    **{"RowStatus": RowStatus,
       "a3Com": a3Com,
       "brouterMIB": brouterMIB,
       "a3ComMIP": a3ComMIP,
       "a3ComMipSConfig": a3ComMipSConfig,
       "a3ComMipControl": a3ComMipControl,
       "a3ComMipCConfig": a3ComMipCConfig,
       "a3ComMipPortTable": a3ComMipPortTable,
       "a3ComMipPortEntry": a3ComMipPortEntry,
       "a3ComMipPortIndex": a3ComMipPortIndex,
       "a3ComMipPortQueryInterval": a3ComMipPortQueryInterval,
       "a3ComMipPortThreshold": a3ComMipPortThreshold,
       "a3ComMipPortQuerier": a3ComMipPortQuerier,
       "a3ComMipPortPaceMode": a3ComMipPortPaceMode,
       "a3ComMipLocalGroupTable": a3ComMipLocalGroupTable,
       "a3ComMipLocalGroupEntry": a3ComMipLocalGroupEntry,
       "a3ComMipLocalGroupPort": a3ComMipLocalGroupPort,
       "a3ComMipLocalGroupIpAddr": a3ComMipLocalGroupIpAddr,
       "a3ComMipLocalGroupType": a3ComMipLocalGroupType,
       "a3ComMipLocalGroupStatus": a3ComMipLocalGroupStatus,
       "a3ComMipSmdsGroupTable": a3ComMipSmdsGroupTable,
       "a3ComMipSmdsGroupEntry": a3ComMipSmdsGroupEntry,
       "a3ComMipSmdsGroupIpAddr": a3ComMipSmdsGroupIpAddr,
       "a3ComMipSmdsGroupMediaAddr": a3ComMipSmdsGroupMediaAddr,
       "a3ComMipSmdsGroupStatus": a3ComMipSmdsGroupStatus,
       "a3ComMipData": a3ComMipData}
)
