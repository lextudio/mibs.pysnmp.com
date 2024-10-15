# SNMP MIB module (ASCEND-MIBIKESPD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBIKESPD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:39 2024
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

_MibmibProfIkeSpd_ObjectIdentity = ObjectIdentity
mibmibProfIkeSpd = _MibmibProfIkeSpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 166)
)
_MibmibProfIkeSpdTable_Object = MibTable
mibmibProfIkeSpdTable = _MibmibProfIkeSpdTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 166, 1)
)
if mibBuilder.loadTexts:
    mibmibProfIkeSpdTable.setStatus("mandatory")
_MibmibProfIkeSpdEntry_Object = MibTableRow
mibmibProfIkeSpdEntry = _MibmibProfIkeSpdEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 166, 1, 1)
)
mibmibProfIkeSpdEntry.setIndexNames(
    (0, "ASCEND-MIBIKESPD-MIB", "mibProfIkeSpd-Index-o"),
)
if mibBuilder.loadTexts:
    mibmibProfIkeSpdEntry.setStatus("mandatory")
_MibProfIkeSpd_Index_o_Type = Integer32
_MibProfIkeSpd_Index_o_Object = MibScalar
mibProfIkeSpd_Index_o = _MibProfIkeSpd_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 166, 1, 1, 1),
    _MibProfIkeSpd_Index_o_Type()
)
mibProfIkeSpd_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfIkeSpd_Index_o.setStatus("mandatory")


class _MibProfIkeSpd_Action_o_Type(Integer32):
    """Custom type mibProfIkeSpd_Action_o based on Integer32"""
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


_MibProfIkeSpd_Action_o_Type.__name__ = "Integer32"
_MibProfIkeSpd_Action_o_Object = MibScalar
mibProfIkeSpd_Action_o = _MibProfIkeSpd_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 166, 1, 1, 2),
    _MibProfIkeSpd_Action_o_Type()
)
mibProfIkeSpd_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIkeSpd_Action_o.setStatus("mandatory")
_MibmibProfIkeSpd_IkePolicyTable_Object = MibTable
mibmibProfIkeSpd_IkePolicyTable = _MibmibProfIkeSpd_IkePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 166, 2)
)
if mibBuilder.loadTexts:
    mibmibProfIkeSpd_IkePolicyTable.setStatus("mandatory")
_MibmibProfIkeSpd_IkePolicyEntry_Object = MibTableRow
mibmibProfIkeSpd_IkePolicyEntry = _MibmibProfIkeSpd_IkePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 166, 2, 1)
)
mibmibProfIkeSpd_IkePolicyEntry.setIndexNames(
    (0, "ASCEND-MIBIKESPD-MIB", "mibProfIkeSpd-IkePolicy-Index-o"),
    (0, "ASCEND-MIBIKESPD-MIB", "mibProfIkeSpd-IkePolicy-Index1-o"),
)
if mibBuilder.loadTexts:
    mibmibProfIkeSpd_IkePolicyEntry.setStatus("mandatory")
_MibProfIkeSpd_IkePolicy_Index_o_Type = Integer32
_MibProfIkeSpd_IkePolicy_Index_o_Object = MibScalar
mibProfIkeSpd_IkePolicy_Index_o = _MibProfIkeSpd_IkePolicy_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 166, 2, 1, 1),
    _MibProfIkeSpd_IkePolicy_Index_o_Type()
)
mibProfIkeSpd_IkePolicy_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfIkeSpd_IkePolicy_Index_o.setStatus("mandatory")
_MibProfIkeSpd_IkePolicy_Index1_o_Type = Integer32
_MibProfIkeSpd_IkePolicy_Index1_o_Object = MibScalar
mibProfIkeSpd_IkePolicy_Index1_o = _MibProfIkeSpd_IkePolicy_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 166, 2, 1, 2),
    _MibProfIkeSpd_IkePolicy_Index1_o_Type()
)
mibProfIkeSpd_IkePolicy_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfIkeSpd_IkePolicy_Index1_o.setStatus("mandatory")


class _MibProfIkeSpd_IkePolicy_ValidEntry_Type(Integer32):
    """Custom type mibProfIkeSpd_IkePolicy_ValidEntry based on Integer32"""
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


_MibProfIkeSpd_IkePolicy_ValidEntry_Type.__name__ = "Integer32"
_MibProfIkeSpd_IkePolicy_ValidEntry_Object = MibScalar
mibProfIkeSpd_IkePolicy_ValidEntry = _MibProfIkeSpd_IkePolicy_ValidEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 166, 2, 1, 3),
    _MibProfIkeSpd_IkePolicy_ValidEntry_Type()
)
mibProfIkeSpd_IkePolicy_ValidEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIkeSpd_IkePolicy_ValidEntry.setStatus("mandatory")
_MibProfIkeSpd_IkePolicy_Address_IpAddress_Type = IpAddress
_MibProfIkeSpd_IkePolicy_Address_IpAddress_Object = MibScalar
mibProfIkeSpd_IkePolicy_Address_IpAddress = _MibProfIkeSpd_IkePolicy_Address_IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 166, 2, 1, 4),
    _MibProfIkeSpd_IkePolicy_Address_IpAddress_Type()
)
mibProfIkeSpd_IkePolicy_Address_IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIkeSpd_IkePolicy_Address_IpAddress.setStatus("mandatory")
_MibProfIkeSpd_IkePolicy_Address_Netmask_Type = IpAddress
_MibProfIkeSpd_IkePolicy_Address_Netmask_Object = MibScalar
mibProfIkeSpd_IkePolicy_Address_Netmask = _MibProfIkeSpd_IkePolicy_Address_Netmask_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 166, 2, 1, 5),
    _MibProfIkeSpd_IkePolicy_Address_Netmask_Type()
)
mibProfIkeSpd_IkePolicy_Address_Netmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIkeSpd_IkePolicy_Address_Netmask.setStatus("mandatory")
_MibProfIkeSpd_IkePolicy_IkeProposals_Type = DisplayString
_MibProfIkeSpd_IkePolicy_IkeProposals_Object = MibScalar
mibProfIkeSpd_IkePolicy_IkeProposals = _MibProfIkeSpd_IkePolicy_IkeProposals_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 166, 2, 1, 6),
    _MibProfIkeSpd_IkePolicy_IkeProposals_Type()
)
mibProfIkeSpd_IkePolicy_IkeProposals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIkeSpd_IkePolicy_IkeProposals.setStatus("mandatory")
_MibProfIkeSpd_IkePolicy_PresharedKey_Type = DisplayString
_MibProfIkeSpd_IkePolicy_PresharedKey_Object = MibScalar
mibProfIkeSpd_IkePolicy_PresharedKey = _MibProfIkeSpd_IkePolicy_PresharedKey_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 166, 2, 1, 7),
    _MibProfIkeSpd_IkePolicy_PresharedKey_Type()
)
mibProfIkeSpd_IkePolicy_PresharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIkeSpd_IkePolicy_PresharedKey.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBIKESPD-MIB",
    **{"DisplayString": DisplayString,
       "mibmibProfIkeSpd": mibmibProfIkeSpd,
       "mibmibProfIkeSpdTable": mibmibProfIkeSpdTable,
       "mibmibProfIkeSpdEntry": mibmibProfIkeSpdEntry,
       "mibProfIkeSpd-Index-o": mibProfIkeSpd_Index_o,
       "mibProfIkeSpd-Action-o": mibProfIkeSpd_Action_o,
       "mibmibProfIkeSpd-IkePolicyTable": mibmibProfIkeSpd_IkePolicyTable,
       "mibmibProfIkeSpd-IkePolicyEntry": mibmibProfIkeSpd_IkePolicyEntry,
       "mibProfIkeSpd-IkePolicy-Index-o": mibProfIkeSpd_IkePolicy_Index_o,
       "mibProfIkeSpd-IkePolicy-Index1-o": mibProfIkeSpd_IkePolicy_Index1_o,
       "mibProfIkeSpd-IkePolicy-ValidEntry": mibProfIkeSpd_IkePolicy_ValidEntry,
       "mibProfIkeSpd-IkePolicy-Address-IpAddress": mibProfIkeSpd_IkePolicy_Address_IpAddress,
       "mibProfIkeSpd-IkePolicy-Address-Netmask": mibProfIkeSpd_IkePolicy_Address_Netmask,
       "mibProfIkeSpd-IkePolicy-IkeProposals": mibProfIkeSpd_IkePolicy_IkeProposals,
       "mibProfIkeSpd-IkePolicy-PresharedKey": mibProfIkeSpd_IkePolicy_PresharedKey}
)
