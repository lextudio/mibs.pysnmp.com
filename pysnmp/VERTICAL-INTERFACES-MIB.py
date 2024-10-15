# SNMP MIB module (VERTICAL-INTERFACES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VERTICAL-INTERFACES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:22 2024
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
 NotificationType,
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
    "NotificationType",
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Vertical_ObjectIdentity = ObjectIdentity
vertical = _Vertical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338)
)
_Vinterfaces_ObjectIdentity = ObjectIdentity
vinterfaces = _Vinterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338, 14)
)


class _VifNumber_Type(Integer32):
    """Custom type vifNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VifNumber_Type.__name__ = "Integer32"
_VifNumber_Object = MibScalar
vifNumber = _VifNumber_Object(
    (1, 3, 6, 1, 4, 1, 2338, 14, 1),
    _VifNumber_Type()
)
vifNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifNumber.setStatus("mandatory")
_VifTable_Object = MibTable
vifTable = _VifTable_Object(
    (1, 3, 6, 1, 4, 1, 2338, 14, 2)
)
if mibBuilder.loadTexts:
    vifTable.setStatus("mandatory")
_VifEntry_Object = MibTableRow
vifEntry = _VifEntry_Object(
    (1, 3, 6, 1, 4, 1, 2338, 14, 2, 1)
)
vifEntry.setIndexNames(
    (0, "VERTICAL-INTERFACES-MIB", "vifIndex"),
)
if mibBuilder.loadTexts:
    vifEntry.setStatus("mandatory")
_VifIndex_Type = Integer32
_VifIndex_Object = MibTableColumn
vifIndex = _VifIndex_Object(
    (1, 3, 6, 1, 4, 1, 2338, 14, 2, 1, 1),
    _VifIndex_Type()
)
vifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifIndex.setStatus("mandatory")


class _VifDescr_Type(DisplayString):
    """Custom type vifDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VifDescr_Type.__name__ = "DisplayString"
_VifDescr_Object = MibTableColumn
vifDescr = _VifDescr_Object(
    (1, 3, 6, 1, 4, 1, 2338, 14, 2, 1, 2),
    _VifDescr_Type()
)
vifDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifDescr.setStatus("mandatory")


class _VifType_Type(Integer32):
    """Custom type vifType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32)
        )
    )
    namedValues = NamedValues(
        *(("basicISDN", 20),
          ("ddn-x25", 4),
          ("ds1", 18),
          ("ds3", 30),
          ("e1", 19),
          ("eon", 25),
          ("ethernet-3Mbit", 26),
          ("ethernet-csmacd", 6),
          ("fddi", 15),
          ("frame-relay", 32),
          ("hdh1822", 3),
          ("hyperchannel", 14),
          ("iso88023-csmacd", 7),
          ("iso88024-tokenBus", 8),
          ("iso88025-tokenRing", 9),
          ("iso88026-man", 10),
          ("lapb", 16),
          ("nsip", 27),
          ("other", 1),
          ("ppp", 23),
          ("primaryISDN", 21),
          ("propPointToPointSerial", 22),
          ("proteon-10Mbit", 12),
          ("proteon-80Mbit", 13),
          ("regular1822", 2),
          ("rfc877-x25", 5),
          ("sdlc", 17),
          ("sip", 31),
          ("slip", 28),
          ("softwareLoopback", 24),
          ("starLan", 11),
          ("ultra", 29))
    )


_VifType_Type.__name__ = "Integer32"
_VifType_Object = MibTableColumn
vifType = _VifType_Object(
    (1, 3, 6, 1, 4, 1, 2338, 14, 2, 1, 3),
    _VifType_Type()
)
vifType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifType.setStatus("mandatory")


class _VifOperStatus_Type(Integer32):
    """Custom type vifOperStatus based on Integer32"""
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


_VifOperStatus_Type.__name__ = "Integer32"
_VifOperStatus_Object = MibTableColumn
vifOperStatus = _VifOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2338, 14, 2, 1, 4),
    _VifOperStatus_Type()
)
vifOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifOperStatus.setStatus("mandatory")
_VifSpecific_Type = ObjectIdentifier
_VifSpecific_Object = MibTableColumn
vifSpecific = _VifSpecific_Object(
    (1, 3, 6, 1, 4, 1, 2338, 14, 2, 1, 5),
    _VifSpecific_Type()
)
vifSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifSpecific.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VERTICAL-INTERFACES-MIB",
    **{"vertical": vertical,
       "vinterfaces": vinterfaces,
       "vifNumber": vifNumber,
       "vifTable": vifTable,
       "vifEntry": vifEntry,
       "vifIndex": vifIndex,
       "vifDescr": vifDescr,
       "vifType": vifType,
       "vifOperStatus": vifOperStatus,
       "vifSpecific": vifSpecific}
)
