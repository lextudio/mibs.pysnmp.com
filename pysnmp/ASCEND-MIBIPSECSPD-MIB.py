# SNMP MIB module (ASCEND-MIBIPSECSPD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBIPSECSPD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:46 2024
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

_MibmibProfIpsecSpd_ObjectIdentity = ObjectIdentity
mibmibProfIpsecSpd = _MibmibProfIpsecSpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 168)
)
_MibmibProfIpsecSpdTable_Object = MibTable
mibmibProfIpsecSpdTable = _MibmibProfIpsecSpdTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 168, 1)
)
if mibBuilder.loadTexts:
    mibmibProfIpsecSpdTable.setStatus("mandatory")
_MibmibProfIpsecSpdEntry_Object = MibTableRow
mibmibProfIpsecSpdEntry = _MibmibProfIpsecSpdEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 168, 1, 1)
)
mibmibProfIpsecSpdEntry.setIndexNames(
    (0, "ASCEND-MIBIPSECSPD-MIB", "mibProfIpsecSpd-SpdName"),
)
if mibBuilder.loadTexts:
    mibmibProfIpsecSpdEntry.setStatus("mandatory")
_MibProfIpsecSpd_SpdName_Type = DisplayString
_MibProfIpsecSpd_SpdName_Object = MibScalar
mibProfIpsecSpd_SpdName = _MibProfIpsecSpd_SpdName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 168, 1, 1, 1),
    _MibProfIpsecSpd_SpdName_Type()
)
mibProfIpsecSpd_SpdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfIpsecSpd_SpdName.setStatus("mandatory")
_MibProfIpsecSpd_DefaultFilter_Type = DisplayString
_MibProfIpsecSpd_DefaultFilter_Object = MibScalar
mibProfIpsecSpd_DefaultFilter = _MibProfIpsecSpd_DefaultFilter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 168, 1, 1, 2),
    _MibProfIpsecSpd_DefaultFilter_Type()
)
mibProfIpsecSpd_DefaultFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsecSpd_DefaultFilter.setStatus("mandatory")


class _MibProfIpsecSpd_Action_o_Type(Integer32):
    """Custom type mibProfIpsecSpd_Action_o based on Integer32"""
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


_MibProfIpsecSpd_Action_o_Type.__name__ = "Integer32"
_MibProfIpsecSpd_Action_o_Object = MibScalar
mibProfIpsecSpd_Action_o = _MibProfIpsecSpd_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 168, 1, 1, 3),
    _MibProfIpsecSpd_Action_o_Type()
)
mibProfIpsecSpd_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsecSpd_Action_o.setStatus("mandatory")
_MibmibProfIpsecSpd_PolicyTable_Object = MibTable
mibmibProfIpsecSpd_PolicyTable = _MibmibProfIpsecSpd_PolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 168, 2)
)
if mibBuilder.loadTexts:
    mibmibProfIpsecSpd_PolicyTable.setStatus("mandatory")
_MibmibProfIpsecSpd_PolicyEntry_Object = MibTableRow
mibmibProfIpsecSpd_PolicyEntry = _MibmibProfIpsecSpd_PolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 168, 2, 1)
)
mibmibProfIpsecSpd_PolicyEntry.setIndexNames(
    (0, "ASCEND-MIBIPSECSPD-MIB", "mibProfIpsecSpd-Policy-SpdName"),
    (0, "ASCEND-MIBIPSECSPD-MIB", "mibProfIpsecSpd-Policy-Index-o"),
)
if mibBuilder.loadTexts:
    mibmibProfIpsecSpd_PolicyEntry.setStatus("mandatory")
_MibProfIpsecSpd_Policy_SpdName_Type = DisplayString
_MibProfIpsecSpd_Policy_SpdName_Object = MibScalar
mibProfIpsecSpd_Policy_SpdName = _MibProfIpsecSpd_Policy_SpdName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 168, 2, 1, 1),
    _MibProfIpsecSpd_Policy_SpdName_Type()
)
mibProfIpsecSpd_Policy_SpdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfIpsecSpd_Policy_SpdName.setStatus("mandatory")
_MibProfIpsecSpd_Policy_Index_o_Type = Integer32
_MibProfIpsecSpd_Policy_Index_o_Object = MibScalar
mibProfIpsecSpd_Policy_Index_o = _MibProfIpsecSpd_Policy_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 168, 2, 1, 2),
    _MibProfIpsecSpd_Policy_Index_o_Type()
)
mibProfIpsecSpd_Policy_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfIpsecSpd_Policy_Index_o.setStatus("mandatory")
_MibProfIpsecSpd_Policy_Type = DisplayString
_MibProfIpsecSpd_Policy_Object = MibScalar
mibProfIpsecSpd_Policy = _MibProfIpsecSpd_Policy_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 168, 2, 1, 3),
    _MibProfIpsecSpd_Policy_Type()
)
mibProfIpsecSpd_Policy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIpsecSpd_Policy.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBIPSECSPD-MIB",
    **{"DisplayString": DisplayString,
       "mibmibProfIpsecSpd": mibmibProfIpsecSpd,
       "mibmibProfIpsecSpdTable": mibmibProfIpsecSpdTable,
       "mibmibProfIpsecSpdEntry": mibmibProfIpsecSpdEntry,
       "mibProfIpsecSpd-SpdName": mibProfIpsecSpd_SpdName,
       "mibProfIpsecSpd-DefaultFilter": mibProfIpsecSpd_DefaultFilter,
       "mibProfIpsecSpd-Action-o": mibProfIpsecSpd_Action_o,
       "mibmibProfIpsecSpd-PolicyTable": mibmibProfIpsecSpd_PolicyTable,
       "mibmibProfIpsecSpd-PolicyEntry": mibmibProfIpsecSpd_PolicyEntry,
       "mibProfIpsecSpd-Policy-SpdName": mibProfIpsecSpd_Policy_SpdName,
       "mibProfIpsecSpd-Policy-Index-o": mibProfIpsecSpd_Policy_Index_o,
       "mibProfIpsecSpd-Policy": mibProfIpsecSpd_Policy}
)
