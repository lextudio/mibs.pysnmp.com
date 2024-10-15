# SNMP MIB module (ASCEND-MIBDS1CLKERR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBDS1CLKERR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:30 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mibds1ClockErrorProfile_ObjectIdentity = ObjectIdentity
mibds1ClockErrorProfile = _Mibds1ClockErrorProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 164)
)
_Mibds1ClockErrorProfileTable_Object = MibTable
mibds1ClockErrorProfileTable = _Mibds1ClockErrorProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 164, 1)
)
if mibBuilder.loadTexts:
    mibds1ClockErrorProfileTable.setStatus("mandatory")
_Mibds1ClockErrorProfileEntry_Object = MibTableRow
mibds1ClockErrorProfileEntry = _Mibds1ClockErrorProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 164, 1, 1)
)
mibds1ClockErrorProfileEntry.setIndexNames(
    (0, "ASCEND-MIBDS1CLKERR-MIB", "ds1ClockErrorProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibds1ClockErrorProfileEntry.setStatus("mandatory")
_Ds1ClockErrorProfile_Index_o_Type = Integer32
_Ds1ClockErrorProfile_Index_o_Object = MibScalar
ds1ClockErrorProfile_Index_o = _Ds1ClockErrorProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 164, 1, 1, 1),
    _Ds1ClockErrorProfile_Index_o_Type()
)
ds1ClockErrorProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1ClockErrorProfile_Index_o.setStatus("mandatory")


class _Ds1ClockErrorProfile_Enabled_Type(Integer32):
    """Custom type ds1ClockErrorProfile_Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_Ds1ClockErrorProfile_Enabled_Type.__name__ = "Integer32"
_Ds1ClockErrorProfile_Enabled_Object = MibScalar
ds1ClockErrorProfile_Enabled = _Ds1ClockErrorProfile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 164, 1, 1, 2),
    _Ds1ClockErrorProfile_Enabled_Type()
)
ds1ClockErrorProfile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1ClockErrorProfile_Enabled.setStatus("mandatory")
_Ds1ClockErrorProfile_CrcThreshold_Type = Integer32
_Ds1ClockErrorProfile_CrcThreshold_Object = MibScalar
ds1ClockErrorProfile_CrcThreshold = _Ds1ClockErrorProfile_CrcThreshold_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 164, 1, 1, 3),
    _Ds1ClockErrorProfile_CrcThreshold_Type()
)
ds1ClockErrorProfile_CrcThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1ClockErrorProfile_CrcThreshold.setStatus("mandatory")
_Ds1ClockErrorProfile_FrameSlipsThreshold_Type = Integer32
_Ds1ClockErrorProfile_FrameSlipsThreshold_Object = MibScalar
ds1ClockErrorProfile_FrameSlipsThreshold = _Ds1ClockErrorProfile_FrameSlipsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 164, 1, 1, 4),
    _Ds1ClockErrorProfile_FrameSlipsThreshold_Type()
)
ds1ClockErrorProfile_FrameSlipsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1ClockErrorProfile_FrameSlipsThreshold.setStatus("mandatory")
_Ds1ClockErrorProfile_FerThreshold_Type = Integer32
_Ds1ClockErrorProfile_FerThreshold_Object = MibScalar
ds1ClockErrorProfile_FerThreshold = _Ds1ClockErrorProfile_FerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 164, 1, 1, 5),
    _Ds1ClockErrorProfile_FerThreshold_Type()
)
ds1ClockErrorProfile_FerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1ClockErrorProfile_FerThreshold.setStatus("mandatory")
_Ds1ClockErrorProfile_OofThreshold_Type = Integer32
_Ds1ClockErrorProfile_OofThreshold_Object = MibScalar
ds1ClockErrorProfile_OofThreshold = _Ds1ClockErrorProfile_OofThreshold_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 164, 1, 1, 6),
    _Ds1ClockErrorProfile_OofThreshold_Type()
)
ds1ClockErrorProfile_OofThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1ClockErrorProfile_OofThreshold.setStatus("mandatory")
_Ds1ClockErrorProfile_FebeThreshold_Type = Integer32
_Ds1ClockErrorProfile_FebeThreshold_Object = MibScalar
ds1ClockErrorProfile_FebeThreshold = _Ds1ClockErrorProfile_FebeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 164, 1, 1, 7),
    _Ds1ClockErrorProfile_FebeThreshold_Type()
)
ds1ClockErrorProfile_FebeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1ClockErrorProfile_FebeThreshold.setStatus("mandatory")
_Ds1ClockErrorProfile_LcvThreshold_Type = Integer32
_Ds1ClockErrorProfile_LcvThreshold_Object = MibScalar
ds1ClockErrorProfile_LcvThreshold = _Ds1ClockErrorProfile_LcvThreshold_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 164, 1, 1, 8),
    _Ds1ClockErrorProfile_LcvThreshold_Type()
)
ds1ClockErrorProfile_LcvThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1ClockErrorProfile_LcvThreshold.setStatus("mandatory")


class _Ds1ClockErrorProfile_Action_o_Type(Integer32):
    """Custom type ds1ClockErrorProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_Ds1ClockErrorProfile_Action_o_Type.__name__ = "Integer32"
_Ds1ClockErrorProfile_Action_o_Object = MibScalar
ds1ClockErrorProfile_Action_o = _Ds1ClockErrorProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 164, 1, 1, 9),
    _Ds1ClockErrorProfile_Action_o_Type()
)
ds1ClockErrorProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1ClockErrorProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBDS1CLKERR-MIB",
    **{"DisplayString": DisplayString,
       "mibds1ClockErrorProfile": mibds1ClockErrorProfile,
       "mibds1ClockErrorProfileTable": mibds1ClockErrorProfileTable,
       "mibds1ClockErrorProfileEntry": mibds1ClockErrorProfileEntry,
       "ds1ClockErrorProfile-Index-o": ds1ClockErrorProfile_Index_o,
       "ds1ClockErrorProfile-Enabled": ds1ClockErrorProfile_Enabled,
       "ds1ClockErrorProfile-CrcThreshold": ds1ClockErrorProfile_CrcThreshold,
       "ds1ClockErrorProfile-FrameSlipsThreshold": ds1ClockErrorProfile_FrameSlipsThreshold,
       "ds1ClockErrorProfile-FerThreshold": ds1ClockErrorProfile_FerThreshold,
       "ds1ClockErrorProfile-OofThreshold": ds1ClockErrorProfile_OofThreshold,
       "ds1ClockErrorProfile-FebeThreshold": ds1ClockErrorProfile_FebeThreshold,
       "ds1ClockErrorProfile-LcvThreshold": ds1ClockErrorProfile_LcvThreshold,
       "ds1ClockErrorProfile-Action-o": ds1ClockErrorProfile_Action_o}
)
