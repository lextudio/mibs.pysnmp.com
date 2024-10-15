# SNMP MIB module (CTRON-SFPS-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SFPS-CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:18 2024
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

(sfpsChassisRipAPI,
 sfpsChassisRipTable) = mibBuilder.importSymbols(
    "CTRON-SFPS-INCLUDE-MIB",
    "sfpsChassisRipAPI",
    "sfpsChassisRipTable")

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



class SfpsAddress(OctetString):
    """Custom type SfpsAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SfpsChassisRipChassisMac_Type = OctetString
_SfpsChassisRipChassisMac_Object = MibScalar
sfpsChassisRipChassisMac = _SfpsChassisRipChassisMac_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1, 1),
    _SfpsChassisRipChassisMac_Type()
)
sfpsChassisRipChassisMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsChassisRipChassisMac.setStatus("mandatory")
_SfpsChassisRipFPPortMask_Type = OctetString
_SfpsChassisRipFPPortMask_Object = MibScalar
sfpsChassisRipFPPortMask = _SfpsChassisRipFPPortMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1, 2),
    _SfpsChassisRipFPPortMask_Type()
)
sfpsChassisRipFPPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsChassisRipFPPortMask.setStatus("mandatory")
_SfpsChassisRipINBPortMask_Type = OctetString
_SfpsChassisRipINBPortMask_Object = MibScalar
sfpsChassisRipINBPortMask = _SfpsChassisRipINBPortMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1, 3),
    _SfpsChassisRipINBPortMask_Type()
)
sfpsChassisRipINBPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsChassisRipINBPortMask.setStatus("mandatory")
_SfpsChassisRipModifiedTime_Type = TimeTicks
_SfpsChassisRipModifiedTime_Object = MibScalar
sfpsChassisRipModifiedTime = _SfpsChassisRipModifiedTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1, 4),
    _SfpsChassisRipModifiedTime_Type()
)
sfpsChassisRipModifiedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsChassisRipModifiedTime.setStatus("mandatory")


class _SfpsChassisRipStatus_Type(Integer32):
    """Custom type sfpsChassisRipStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("dead", 3),
          ("other", 1))
    )


_SfpsChassisRipStatus_Type.__name__ = "Integer32"
_SfpsChassisRipStatus_Object = MibScalar
sfpsChassisRipStatus = _SfpsChassisRipStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1, 5),
    _SfpsChassisRipStatus_Type()
)
sfpsChassisRipStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsChassisRipStatus.setStatus("mandatory")


class _SfpsChassisRipAPIVerb_Type(Integer32):
    """Custom type sfpsChassisRipAPIVerb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("clearTable", 6),
          ("delete", 3),
          ("other", 1),
          ("purgePort", 4),
          ("sendUpdate", 5),
          ("setTimer", 7))
    )


_SfpsChassisRipAPIVerb_Type.__name__ = "Integer32"
_SfpsChassisRipAPIVerb_Object = MibScalar
sfpsChassisRipAPIVerb = _SfpsChassisRipAPIVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2, 1),
    _SfpsChassisRipAPIVerb_Type()
)
sfpsChassisRipAPIVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsChassisRipAPIVerb.setStatus("mandatory")
_SfpsChassisRipAPIChassisMac_Type = SfpsAddress
_SfpsChassisRipAPIChassisMac_Object = MibScalar
sfpsChassisRipAPIChassisMac = _SfpsChassisRipAPIChassisMac_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2, 2),
    _SfpsChassisRipAPIChassisMac_Type()
)
sfpsChassisRipAPIChassisMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsChassisRipAPIChassisMac.setStatus("mandatory")
_SfpsChassisRipAPIPort_Type = Integer32
_SfpsChassisRipAPIPort_Object = MibScalar
sfpsChassisRipAPIPort = _SfpsChassisRipAPIPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2, 3),
    _SfpsChassisRipAPIPort_Type()
)
sfpsChassisRipAPIPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsChassisRipAPIPort.setStatus("mandatory")
_SfpsChassisRipAPITimer_Type = Integer32
_SfpsChassisRipAPITimer_Object = MibScalar
sfpsChassisRipAPITimer = _SfpsChassisRipAPITimer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2, 4),
    _SfpsChassisRipAPITimer_Type()
)
sfpsChassisRipAPITimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsChassisRipAPITimer.setStatus("mandatory")
_SfpsChassisRipAPINumInTable_Type = Integer32
_SfpsChassisRipAPINumInTable_Object = MibScalar
sfpsChassisRipAPINumInTable = _SfpsChassisRipAPINumInTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2, 5),
    _SfpsChassisRipAPINumInTable_Type()
)
sfpsChassisRipAPINumInTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsChassisRipAPINumInTable.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SFPS-CHASSIS-MIB",
    **{"SfpsAddress": SfpsAddress,
       "sfpsChassisRipChassisMac": sfpsChassisRipChassisMac,
       "sfpsChassisRipFPPortMask": sfpsChassisRipFPPortMask,
       "sfpsChassisRipINBPortMask": sfpsChassisRipINBPortMask,
       "sfpsChassisRipModifiedTime": sfpsChassisRipModifiedTime,
       "sfpsChassisRipStatus": sfpsChassisRipStatus,
       "sfpsChassisRipAPIVerb": sfpsChassisRipAPIVerb,
       "sfpsChassisRipAPIChassisMac": sfpsChassisRipAPIChassisMac,
       "sfpsChassisRipAPIPort": sfpsChassisRipAPIPort,
       "sfpsChassisRipAPITimer": sfpsChassisRipAPITimer,
       "sfpsChassisRipAPINumInTable": sfpsChassisRipAPINumInTable}
)
