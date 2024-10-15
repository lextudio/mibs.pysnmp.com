# SNMP MIB module (GBNL2PppoePlus-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GBNL2PppoePlus-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:46 2024
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

(gbnL2,) = mibBuilder.importSymbols(
    "GREENTECH-MASTER-MIB",
    "gbnL2")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

gbnL2PppoePlus = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 6)
)
gbnL2PppoePlus.setRevisions(
        ("1907-11-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PppoeplusOnOff_Type = TruthValue
_PppoeplusOnOff_Object = MibScalar
pppoeplusOnOff = _PppoeplusOnOff_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 6, 1),
    _PppoeplusOnOff_Type()
)
pppoeplusOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeplusOnOff.setStatus("current")


class _PppoeplusType_Type(Integer32):
    """Custom type pppoeplusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("huawei", 1),
          ("standard", 0))
    )


_PppoeplusType_Type.__name__ = "Integer32"
_PppoeplusType_Object = MibScalar
pppoeplusType = _PppoeplusType_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 6, 2),
    _PppoeplusType_Type()
)
pppoeplusType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeplusType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GBNL2PppoePlus-MIB",
    **{"gbnL2PppoePlus": gbnL2PppoePlus,
       "pppoeplusOnOff": pppoeplusOnOff,
       "pppoeplusType": pppoeplusType}
)
